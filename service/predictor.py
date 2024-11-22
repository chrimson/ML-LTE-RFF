import re
import numpy as np

def predict(svc, model, le, stage, claim_mac):
    svc.logger.info('Import target RWF from stage')
    rwf_l = []
    mag = 1e-10
    with open(f'{stage}/{claim_mac}', 'r') as file:
        for line in file:
            cpx = re.sub('[+ij]', '', line).split()
            real = float(cpx[0])
            imag = float(cpx[1])
            mag = max(abs(real), abs(imag), mag)
            rwf_l.append([real, imag])
    
    # svc.logger.info('Convert list of one target RWF to NumPy array')
    norm = 0.5 / mag
    rwf = np.array([rwf_l]) * norm + 0.5
    
    # svc.logger.info('Predict target')
    predicted = model(rwf)
    pred = np.argmax(predicted, axis=1)
    pred_mac = le.inverse_transform(pred)[0]
    pred_prob = predicted[0][pred[0]]
    svc.logger.info(f'  Guess {pred_mac} Probability {pred_prob:.2%}')

    if claim_mac in le.classes_:
        claim_prob = predicted[0][le.transform([claim_mac])[0]]
        svc.logger.info(f'  Claim {claim_mac} Probability {claim_prob:.2%}')
    else:
        svc.logger.info(f'  Claim {claim_mac} Probability N/A')
        claim_prob = 0

    return pred_mac, pred_prob, claim_prob, rwf
