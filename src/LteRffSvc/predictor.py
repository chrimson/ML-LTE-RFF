from logger import log

import re
import numpy as np

def predict(model, le, stage, mac):
    log('Import target RWF from stage')
    rwf_l = []
    mag = 1e-10
    with open(f'{stage}/{mac}', 'r') as file:
        for line in file:
            cpx = re.sub('[+ij]', '', line).split()
            real = float(cpx[0])
            imag = float(cpx[1])
            mag = max(abs(real), abs(imag), mag)
            rwf_l.append([real, imag])
    
    # log('Convert list of one target RWF to NumPy array')
    norm = 0.5 / mag
    rwf = np.array([rwf_l]) * norm + 0.5
    
    # log('Predict target')
    predicted = model.predict(rwf, verbose=2)
    pred = np.argmax(predicted, axis=1)
    predicted_label = le.inverse_transform(pred)[0]
    prob = predicted[0][pred[0]]
    log(f'Guess   {predicted_label} {prob}')

    if mac in le.classes_:
        prob_mac = predicted[0][le.transform([mac])[0]]
        log(f'Claim   {mac} {prob_mac}')
    else:
        log(f'New MAC {mac}')
