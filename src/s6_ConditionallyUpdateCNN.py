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
import sys

#print("TensorFlow", tf.__version__, flush=True)

rep = sys.argv[1]
stg = sys.argv[2]
mac = sys.argv[3]

norm_file = f'{rep}x{stg}_rwf_cnn_norm.asc'
cnn_file = f'{rep}x{stg}_rwf_cnn.keras'
rwf_file = f'{rep}x{stg}_target_rwf.asc'
le = joblib.load(f'{rep}x{stg}_mac_label_enc.pkl')

model = load_model(cnn_file)

rwf = []
with open(rwf_file) as file:
  for line in file:
    cpx = re.sub('[+ij]', '', line).split()
    rwf.append([float(cpx[0]), float(cpx[1])])

with open(norm_file) as file:
  norm = float(file.read())
RWF = np.array([rwf]) * norm + 0.5

predicted = model.predict(RWF)
pred = np.argmax(predicted, axis=1)
predicted_label = le.inverse_transform(pred)[0]
prob = predicted[0][pred[0]]
print(f'{predicted_label} {prob}', flush=True)

if predicted_label == mac:

  if prob > 0.50:
    print('MACs match. Strengthening', flush=True)
#    MAC = le.transform([mac])
#    model.fit(RWF, MAC, batch_size=16, epochs=1)
#    model.save(cnn_file)

  if prob < 0.50:
    print('Lucky guess. Not updating', flush=True)

if predicted_label != mac:

  if prob < 0.20:
    print('Learning new MAC\'s RWF', flush=True)

  elif prob > 0.80:
    print('FLAG', flush=True)

  else:
    print('Inconclusive. Not updating', flush=True)
