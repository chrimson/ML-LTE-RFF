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
print("TensorFlow", tf.__version__)

norm = 40
rff_file = 'target_rff.asc'
le = joblib.load("mac_label_enc.pkl")

print('Load RFF CNN')
model = load_model('rff_cnn.keras')

print('Build one target RFF from file')
rff = []
with open(rff_file) as file:
  for line in file:
    cpx = re.sub('[+ij]', '', line).split()
    rff.append([float(cpx[0]), float(cpx[1])])
# print(f"{rff} {len(rff)}\n")

print('Convert list of target RFF to NumPy array')
# Move zero-centric to [0,1] normalization
RFF = np.array([rff]) * norm + 0.5
# print(f'{RFF} {len(RFF)}\n')

print('Predict target')
predicted = model.predict(RFF)
pred = np.argmax(predicted, axis=1)
predicted_label = le.inverse_transform(pred)[0]
prob = predicted[0][pred[0]]
print(f'{predicted_label} {prob}\n')
