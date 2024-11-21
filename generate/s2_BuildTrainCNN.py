import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore")

import tensorflow as tf 
from keras.models import Sequential
from keras.layers import Conv2D, Flatten, MaxPooling2D, Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
import joblib
import numpy as np
import re
import sys

print("TensorFlow", tf.__version__, flush=True)

rep = sys.argv[1]
stg = sys.argv[2]

norm_file = f'{rep}x{stg}_rwf_cnn_norm.asc'
cnn_file = f'{rep}x{stg}_rwf_cnn.keras'
data_dir = f'{rep}x{stg}_ue_rwf_data'
data_dir_cmplx = f'{rep}x{stg}_ue_rwf_data_cmplx'
trunc = 5000
rwfs = []
macs = []

print('Build lists of RWFs and their MAC IDs from dataset', flush=True)
dir_list = os.listdir(data_dir)
if not os.path.isdir(data_dir_cmplx):
  os.mkdir(data_dir_cmplx)
# Keep largest magnitude for normalization
mag = 0
for mac_id in dir_list:
  print(f'{mac_id}', flush=True)
  mac_dir = os.path.join(data_dir, mac_id)
  file_list = os.listdir(mac_dir)
  for rwf_file in file_list:
    print(rwf_file, end=' ', flush=True)
    rwf = []
    cmplx = []
    with open(os.path.join(data_dir, mac_id, rwf_file)) as file:
      for line in file:
        cpx = re.sub('[+ij]', '', line).split()
        real = float(cpx[0])
        imag = float(cpx[1])
        mag = max(abs(real), abs(imag), mag)
        rwf.append([real, imag])
        cmplx.append(complex(real, imag))
      cmplx_np = np.array(cmplx)
      if not os.path.isdir(os.path.join(data_dir_cmplx, mac_id)):
        os.mkdir(os.path.join(data_dir_cmplx, mac_id))
      cmplx_np.tofile(os.path.join(data_dir_cmplx, mac_id, rwf_file))
    rwfs.append(rwf)
    macs.append(mac_id)
  print(flush=True)
# print(f"{macs} {len(macs)}\n")

print('Convert lists to NumPy arrays', flush=True)
# Move zero-centric to [0,1] normalization
norm = 0.5 / mag
with open(norm_file, 'w') as file:
  file.write(str(norm))
RWFs = np.array(rwfs) * norm + 0.5
MACs = np.array(macs)
# print(f'{RWFs} {len(RWFs)}\n')

print('Label encoding', flush=True)
le = LabelEncoder()
MACs = le.fit_transform(MACs)
joblib.dump(le, f'{rep}x{stg}_mac_label_enc.pkl')
# print(f'{MACs} {len(MACs)}\n')

print('Shuffle arrays', flush=True)
RWFsh, MACsh = shuffle(RWFs, MACs, random_state=42)
# print(f'{MACsh} {len(MACsh)}\n')

print('Build CNN model', flush=True)
model = Sequential()
model.add(Conv2D(filters=64, kernel_size=1, activation='relu', input_shape=(trunc,2,1)))
model.add(MaxPooling2D())
model.add(Conv2D(filters=128, kernel_size=1, activation='relu'))
model.add(Flatten())
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=54, activation='softmax'))
#print(f'{model.get_config()}\n')

print('Compile, train, save', flush=True)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics = ['accuracy'])
history = model.fit(RWFsh, MACsh, validation_split=0.2, batch_size=16, epochs=12)
model.save(cnn_file)

print('Done', flush=True)
