from logger import log
import service as s

import joblib
from keras.models import Sequential
from keras.layers import Conv2D, Flatten, MaxPooling2D, Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle

def build(rwfs, macs):
    log('Build and train')

    # log('Label encoding')
    le = LabelEncoder()
    macs = le.fit_transform(macs)
   
    # log('Shuffle arrays')
    rwfsh, macsh = shuffle(rwfs, macs, random_state=42)

    # log('Build CNN model')
    trunc = int(rwfs[0].size / 2)
    model = Sequential()
    model.add(Conv2D(filters=64, kernel_size=1, activation='relu', input_shape=(trunc,2,1)))
    model.add(MaxPooling2D())
    model.add(Conv2D(filters=128, kernel_size=1, activation='relu'))
    model.add(Flatten())
    model.add(Dense(units=128, activation='relu'))
    model.add(Dense(units=64, activation='relu'))
    model.add(Dense(units=54, activation='softmax'))

    # log('Train, save')
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics = ['accuracy'])
    model.fit(rwfsh, macsh, validation_split=0.2, batch_size=16, epochs=10, verbose=2)
    model.save(s.MODEL)
    joblib.dump(le, s.LABELS)

    return model, le
