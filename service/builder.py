import ml_lte_rff_svc as s

from datetime import datetime
import joblib
from keras.callbacks import Callback
from keras.models import Sequential
from keras.layers import Conv2D, Flatten, MaxPooling2D, Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle

class CustomBuild(Callback):
    def on_epoch_begin(self, epoch, logs=None):
        timestamp = f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:23]}]'
        print(f'{timestamp} INFO in builder:   Epoch {epoch + 1}/{s.EPOCHS}',  end=' ', flush=True)

    def on_epoch_end(self, epoch, logs=None):
        accuracy = logs.get('accuracy')
        print(f"Accuracy {accuracy:.2%}", flush=True)

def build(svc, rwfs, macs):
    svc.logger.info('Build and train')

    # svc.logger.info('Label encoding')
    le = LabelEncoder()
    macs_e = le.fit_transform(macs)
   
    # svc.logger.info('Shuffle arrays')
    rwfsh, macsh = shuffle(rwfs, macs_e, random_state=42)

    # svc.logger.info('Build CNN model')
    trunc = int(rwfs[0].size / 2)
    model = Sequential()
    model.add(Conv2D(filters=64, kernel_size=1, activation='relu', input_shape=(trunc,2,1)))
    model.add(MaxPooling2D())
    model.add(Conv2D(filters=128, kernel_size=1, activation='relu'))
    model.add(Flatten())
    model.add(Dense(units=128, activation='relu'))
    model.add(Dense(units=64, activation='relu'))
    model.add(Dense(units=54, activation='softmax'))

    # svc.logger.info('Train, save')
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics = ['accuracy'])
    model.fit(
        rwfsh,
        macsh,
        validation_split=0.2,
        batch_size=16,
        epochs=s.EPOCHS,
        verbose=0,
        callbacks=[CustomBuild()])
    model.save(s.MODEL)
    joblib.dump(le, s.LABELS)

    return model, le
