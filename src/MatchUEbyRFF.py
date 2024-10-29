import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore")

import tensorflow as tf 
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import numpy as np
print("TensorFlow", tf.__version__)

data_dir = 'ue_rff_data'
rff_file = 'target'
macs = []

print('Build list of MAC IDs from dataset')
dir_list = os.listdir(data_dir)
for mac_id in dir_list:
  macs.append(mac_id)
# print(f"{macs} {len(macs)}\n")

print('Convert list of MAC IDs to NumPy array')
MACs = np.array(macs)
# print(f'{MACs} {len(MACs)}\n')

print('Label encoding')
le = LabelEncoder()
MACs = le.fit_transform(MACs)
#print(f'{MACs} {len(MACs)}\n')

print('Load RFF CNN')
model = load_model('rff.keras')

print('Build one target RFF from file')
rff = []
with open(rff_file) as file:
  for line in file:
    rff.append(float(line.rstrip()))
# print(f"{rff} {len(rff)}\n")

print('Convert list of target RFF to NumPy array')
RFF = np.array([rff]) / 1.1555
# print(f'{RFF} {len(RFF)}\n')

print('Predict target')
predicted = model.predict(RFF)
predicted_label = le.inverse_transform(np.argmax(predicted, axis=1))
print(f'{predicted_label}\n')
