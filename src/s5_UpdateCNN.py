import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore")

import tensorflow as tf 
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import joblib
import numpy as np
import random
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
#print(rwf)

rwfs = []
macs = []
for i in range(0, 100):
  rwfs.append(rwf)
  macs.append(mac)

RWF = np.array(rwfs)
for i in range(0, 100):
  RWF[i] = RWF[i] * (0.975 + 0.05 * random.random())
  RWF[i] = np.roll(RWF[i], 50 - int(100*random.random()))

with open(norm_file) as file:
  norm = float(file.read())
RWF = RWF * norm + 0.5
#print(RWF)

le.classes_ = np.append(le.classes_, mac)
joblib.dump(le, f'{rep}x{stg}_mac_label_enc.pkl')
#MAC = np.array([le.fit_transform(le.classes_)[-1]])
MAC = le.transform(macs)

#for layer in model.layers:
#for layer in model.layers[:-1]:
#  layer.trainable = False

print('Retraining', flush=True)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics = ['accuracy'])
history = model.fit(RWF, MAC, validation_split=0.2, batch_size=16, epochs=10)
model.save(cnn_file)
