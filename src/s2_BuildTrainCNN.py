import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore")

import tensorflow as tf 
from keras.models import Sequential
from keras.layers import Conv1D, Flatten, MaxPooling1D, Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
import numpy as np
print("TensorFlow", tf.__version__)

data_dir = 'ue_rff_data'
rffs = []
macs = []

print('Build lists of RFFs, their MAC IDs from dataset')
dir_list = os.listdir(data_dir)
for mac_id in dir_list:
  mac_dir = os.path.join(data_dir, mac_id)
  file_list = os.listdir(mac_dir)
  for rff_file in file_list:
    rff = []
    with open(os.path.join(data_dir, mac_id, rff_file)) as file:
      for line in file:
        rff.append(float(line.rstrip()))
    rffs.append(rff)
    macs.append(mac_id)
# print(f"{macs} {len(macs)}\n")

print('Convert lists to NumPy arrays')
RFFs = np.array(rffs) / 1.1555
MACs = np.array(macs)
# print(f'{RFFs} {len(MACs)}\n')

print('Label encoding')
le = LabelEncoder()
MACs = le.fit_transform(MACs)
# print(f'{MACs} {len(MACs)}\n')

print('Shuffle arrays')
RFFsh, MACsh = shuffle(RFFs, MACs, random_state=42)
# print(f'{MACsh} {len(MACsh)}\n')

print('Build CNN model')
model = Sequential()
model.add(Conv1D(filters=16, kernel_size=3, activation='relu', input_shape=(5000,1)))
model.add(MaxPooling1D())
model.add(Conv1D(filters=32, kernel_size=3, activation='relu'))
model.add(MaxPooling1D())
model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
model.add(MaxPooling1D())
model.add(Conv1D(filters=128, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=54, activation='softmax'))
#print(f'{model.get_config()}\n')

print('Compile, train, save')
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics = ['accuracy'])
history = model.fit(RFFsh, MACsh, validation_split=0.2, batch_size=16, epochs=10)
model.save('rff_cnn.keras')

print('Done')
