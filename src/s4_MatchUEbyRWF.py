import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore")

import tensorflow as tf 
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import joblib
import numpy as np
import re
print("TensorFlow", tf.__version__, flush=True)

norm_file = 'rwf_cnn_norm.asc'
cnn_file = 'rwf_cnn.keras'
rwf_file = 'target_rwf.asc'
le = joblib.load("mac_label_enc.pkl")

print('Load RWF CNN', flush=True)
model = load_model(cnn_file)

print('Build one target RWF from file', flush=True)
rwf = []
with open(rwf_file) as file:
  for line in file:
    cpx = re.sub('[+ij]', '', line).split()
    rwf.append([float(cpx[0]), float(cpx[1])])
# print(f"{rwf} {len(rwf)}\n")

print('Convert list of target RWF to NumPy array', flush=True)
# Move zero-centric to [0,1] normalization
with open(norm_file) as file:
  norm = float(file.read())
RWF = np.array([rwf]) * norm + 0.5
# print(f'{RWF} {len(RWF)}\n')

print('Predict target', flush=True)
predicted = model.predict(RWF)
pred = np.argmax(predicted, axis=1)
predicted_label = le.inverse_transform(pred)[0]
prob = predicted[0][pred[0]]
print(f'{predicted_label} {prob}\n', flush=True)
