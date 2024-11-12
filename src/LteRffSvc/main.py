import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
warnings.filterwarnings("ignore")

from keras.models import load_model
import joblib
import time

from logger import log
import reader
import builder
import predictor

MODEL               = './rwf_cnn.keras'
LABELS              = './rwf_cnn.pkl'
DATASET             = './dataset'
STAGE               = './stage'
CHECK_STAGE_SECONDS = 10
MATCHING_MACS_CONF  = 0.50
DIFF_MACS_NEW_RWF   = 0.20
DIFF_MACS_SAME_RWF  = 0.80

def main():
    # Read dataset
    rwfs, macs = reader.read(DATASET)

    if os.path.exists(MODEL) and os.path.exists(LABELS):
        model = load_model(MODEL)
        le = joblib.load(LABELS)
    else:
        model, le = builder.build(rwfs, macs)
        model.save(MODEL)
        joblib.dump(le, STAGE)

    log(f'Monitoring {STAGE}/')
    if not os.path.isdir(STAGE):
        os.mkdir(STAGE)
    # Daemon loop
    while True:
        staged_macs = os.listdir(STAGE)
        if len(staged_macs) != 0:
            claim_mac = staged_macs[0]
            pred_mac, pred_prob, claim_prob = predictor.predict(model, le, STAGE, claim_mac)

            # Predictor
            if pred_mac == claim_mac:

                if pred_prob >= MATCHING_MACS_CONF:
                    log(f'MACs match >= {MATCHING_MACS_CONF}, fair enough')

                else:
                    log(f'MACs match < {MATCHING_MACS_CONF}, strengthen')
                    # Move to approprate MAC and sequence number in dataset
                    # Add to rwfs and macs np arrays
                    # Rebuild, save, dump

            else:
            
                 if pred_prob < DIFF_MACS_NEW_RWF:
                     log(f'Different MACs match RWF < {DIFF_MACS_NEW_RWF}, learn claimed MAC\'s RWF')

                 elif pred_prob > DIFF_MACS_SAME_RWF:
                     log(f'Different MACs match RWF > {DIFF_MACS_SAME_RWF}, flag for inconsistency')

                 else:
                     log(f'Inconclusive, not updating')

            # For now
            os.remove(f'{STAGE}/{claim_mac}')

        time.sleep(CHECK_STAGE_SECONDS)

if __name__ == "__main__":
    main()
