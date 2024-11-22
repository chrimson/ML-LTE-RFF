import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
warnings.filterwarnings("ignore")

import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

from keras.models import load_model
import joblib
import numpy as np
import shutil
import time

from logger import log
import reader
import builder
import predictor

import logging
from flask import Flask, request

MODEL               = './rwf.keras'
LABELS              = './rwf.pkl'
DATASET             = './dataset'
STAGE               = './stage'
FLAG                = './flag'
CHECK_STAGE_SECONDS = 5
SAME_MACS_CMPR_RWF  = 0.50
DIFF_MACS_CMPR_RWF  = 0.80
EPOCHS              = 12

svc = Flask(__name__)
svc.logger.setLevel(logging.INFO)

#  curl -H "Content-Type: multipart/form-data" -F "rwf=@dataset/33-04-E7-92-52-BD/0000" http://52.20.245.57:64024
@svc.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        rwf_file = request.files['rwf']
        claim_mac = rwf_file.filename

        rwf_file.save(os.path.join(STAGE, claim_mac))
        svc.logger.info(f'Uploaded {claim_mac}')

        pred_mac, pred_prob, claim_prob, rwf = predictor.predict(svc.config['Model'], svc.config['Le'], STAGE, claim_mac)

        # Predictor
        if pred_mac == claim_mac:

            if pred_prob < SAME_MACS_CMPR_RWF:
                resp = f'  Same MACs, RWF < {SAME_MACS_CMPR_RWF:.0%} Strengthen'
                index = len(os.listdir(f'{DATASET}/{claim_mac}'))
                svc.config['Model'], svc.config['Le'] = update(rwf, claim_mac, svc.config['Rwfs'], svc.config['Macs'])

            else:
                resp = f'  Same MACs, RWF >= {SAME_MACS_CMPR_RWF:.0%} Checks out'
                os.remove(f'{STAGE}/{claim_mac}')

        else: # predicted != claim

            if pred_prob < DIFF_MACS_CMPR_RWF:
                resp = f'  Diff MACs, RWF < {DIFF_MACS_CMPR_RWF:.0%} Learn claimed MAC'
                if not os.path.exists(f'{DATASET}/{claim_mac}'):
                    os.mkdir(f'{DATASET}/{claim_mac}')
                svc.config['Model'], svc.config['Le'] = update(rwf, claim_mac, svc.config['Rwfs'], svc.config['Macs'])

            else:
                resp = f'  Diff MACs, RWF > {DIFF_MACS_CMPR_RWF:.0%} Flag for examination'
                if not os.path.exists(f'{FLAG}/{claim_mac}_{pred_mac}'):
                    os.mkdir(f'{FLAG}/{claim_mac}_{pred_mac}')
                index = len(os.listdir(f'{FLAG}/{claim_mac}_{pred_mac}'))
                shutil.move(f'{STAGE}/{claim_mac}', f'{FLAG}/{claim_mac}_{pred_mac}/{index:04d}')

        return resp


def update(rwf, claim_mac, rwfs, macs):
    index = len(os.listdir(f'{DATASET}/{claim_mac}'))
    shutil.move(f'{STAGE}/{claim_mac}', f'{DATASET}/{claim_mac}/{index:04d}')

    # Add to rwfs and macs np arrays
    svc.config['Rwfs'] = np.append(rwfs, rwf, axis=0)
    svc.config['Macs'] = np.append(macs, claim_mac)

    # Rebuild
    model, le = builder.build(svc.config['Rwfs'], svc.config['Macs'])
    return model, le


def setup():
    svc.config['Rwfs'], svc.config['Macs'] = reader.read(DATASET)

    if os.path.exists(MODEL) and os.path.exists(LABELS):
        svc.config['Model'] = load_model(MODEL)
        svc.config['Le'] = joblib.load(LABELS)
    else:
        svc.config['Model'], svc.config['Le'] = builder.build(svc.config['Rwfs'], svc.config['Macs'])

    if not os.path.isdir(FLAG):
        os.mkdir(FLAG)

    if not os.path.isdir(STAGE):
        os.mkdir(STAGE)


if __name__ == "__main__":
    setup()
    svc.run(host='0.0.0.0', port=64024)
