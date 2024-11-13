import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
warnings.filterwarnings("ignore")

from keras.models import load_model
import joblib
import numpy as np
import shutil
import time

from logger import log
import reader
import builder
import predictor

MODEL               = './rwf.keras'
LABELS              = './rwf.pkl'
DATASET             = './dataset'
STAGE               = './stage'
FLAG                = './flag'
CHECK_STAGE_SECONDS = 5
SAME_MACS_CMPR_RWF  = 0.50
DIFF_MACS_CMPR_RWF  = 0.80

def service():
    # Read dataset
    rwfs, macs = reader.read(DATASET)

    if os.path.exists(MODEL) and os.path.exists(LABELS):
        model = load_model(MODEL)
        le = joblib.load(LABELS)
    else:
        model, le = builder.build(rwfs, macs)

    if not os.path.isdir(FLAG):
        os.mkdir(FLAG)

    log(f'Monitoring {STAGE}/')
    if not os.path.isdir(STAGE):
        os.mkdir(STAGE)
    # Daemon loop
    while True:
        staged_macs = os.listdir(STAGE)
        if len(staged_macs) != 0:
            claim_mac = staged_macs[0]
            pred_mac, pred_prob, claim_prob, rwf = predictor.predict(model, le, STAGE, claim_mac)

            # Predictor
            if pred_mac == claim_mac:

                if pred_prob < SAME_MACS_CMPR_RWF:
                    log(f'Same MACs, RWF  < {SAME_MACS_CMPR_RWF} strengthen')
                    index = len(os.listdir(f'{DATASET}/{claim_mac}'))
                    model, le = update(rwf, claim_mac, rwfs, macs)

                else:
                    log(f'Same MACs, RWF >= {SAME_MACS_CMPR_RWF} checks out')
                    os.remove(f'{STAGE}/{claim_mac}')

            else:
            
                if pred_prob < DIFF_MACS_CMPR_RWF:
                    log(f'Diff MACs, RWF  < {DIFF_MACS_CMPR_RWF} learn claimed MAC')
                    if not os.path.exists(f'{DATASET}/{claim_mac}'):
                        os.mkdir(f'{DATASET}/{claim_mac}')
                    model, le = update(rwf, claim_mac, rwfs, macs)

                else:
                    log(f'Diff MACs, RWF  > {DIFF_MACS_CMPR_RWF} flag for examination')
                    if not os.path.exists(f'{FLAG}/{claim_mac}_{pred_mac}'):
                        os.mkdir(f'{FLAG}/{claim_mac}_{pred_mac}')
                    index = len(os.listdir(f'{FLAG}/{claim_mac}_{pred_mac}'))
                    shutil.move(f'{STAGE}/{claim_mac}', f'{FLAG}/{claim_mac}_{pred_mac}/{index:04d}')

        time.sleep(CHECK_STAGE_SECONDS)


def update(rwf, claim_mac, rwfs, macs):
    index = len(os.listdir(f'{DATASET}/{claim_mac}'))
    shutil.move(f'{STAGE}/{claim_mac}', f'{DATASET}/{claim_mac}/{index:04d}')

    # Add to rwfs and macs np arrays
    rwfs = np.append(rwfs, rwf)
    macs = np.append(macs, claim_mac)

    # Rebuild
    model, le = builder.build(rwfs, macs)
    return model, le


if __name__ == "__main__":
    service()
