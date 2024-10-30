import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore")

import tensorflow as tf 
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import joblib
import numpy as np
print("TensorFlow", tf.__version__)

rff_file = 'target_rff.asc'
le = joblib.load("mac_label_enc.pkl")

print('Load RFF CNN')
model = load_model('rff_cnn.keras')

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
