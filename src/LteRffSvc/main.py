import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
warnings.filterwarnings("ignore")

from keras.models import load_model

import time

from logger import log
import reader
import builder
import predictor

MODEL               = './rwf_cnn.keras'
DATASET             = './dataset'
STAGE               = './stage'
CHECK_STAGE_SECONDS = 10

def main():
    # Read dataset
    rwfs, macs = reader.read()

    if os.path.exists(MODEL):
        model = load_model(MODEL)
    else:
        model, le = builder.build(rwfs, macs)

    log('Monitoring stage')
    if not os.path.isdir(STAGE):
        os.mkdir(STAGE)
    # Daemon loop
    while True:
        macs = os.listdir(STAGE)
        if len(macs) != 0:
            predictor.predict(model, le, STAGE, macs[0])

            # Predictor
#            if predicted_label == mac:
#            
#              if prob > 0.50:
#                print('MACs match. High enough', flush=True)
#            
#              if prob < 0.50:
#                print('Strengthen', flush=True)
#            
#            if predicted_label != mac:
#            
#              if prob < 0.20:
#                print('Learning new MAC\'s RWF', flush=True)
#            
#              elif prob > 0.80:
#                print('FLAG', flush=True)
#            
#              else:
#                print('Inconclusive. Not updating', flush=True)



        time.sleep(CHECK_STAGE_SECONDS)

if __name__ == "__main__":
    main()
