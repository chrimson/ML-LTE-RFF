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

print("TensorFlow", tf.__version__, flush=True)

rep = sys.argv[1]
stg = sys.argv[2]
mac = sys.argv[3]

norm_file = f'{rep}x{stg}_rwf_cnn_norm.asc'
cnn_file = f'{rep}x{stg}_rwf_cnn.keras'
rwf_file = f'{rep}x{stg}_target_rwf.asc'
le = joblib.load(f'{rep}x{stg}_mac_label_enc.pkl')

print('Load RWF CNN', flush=True)
model = load_model(cnn_file)

print('Build one target RWF from file', flush=True)
rwf = []
with open(rwf_file) as file:
  for line in file:
    cpx = re.sub('[+ij]', '', line).split()
    rwf.append([float(cpx[0]), float(cpx[1])])

print('Convert lists of one target to NumPy arrays', flush=True)
# Move zero-centric to [0,1] normalization
with open(norm_file) as file:
  norm = float(file.read())
RWF = np.array([rwf]) * norm + 0.5

print('Label encoding', flush=True)
#le = LabelEncoder()
#le.classes_ = np.append(le.classes_, mac)
#joblib.dump(le, f'{rep}x{stg}_mac_label_enc.pkl')
#MAC = np.array([le.fit_transform(le.classes_)[-1]])
MAC = le.transform([mac])

print('Retraining, save', flush=True)
#model.fit(RWF, MAC, validation_split=0.2, batch_size=16, epochs=10)
model.fit(RWF, MAC, batch_size=16, epochs=1)
model.save(cnn_file)

print('Done', flush=True)
