import numpy as np

def predict(svc, model, le, stage, claim_mac):
    svc.logger.info('Import target RWF from stage')
    rwf_l = []
    mag = 1e-10
    rwf_cmplx = np.load(f'{stage}/{claim_mac}')
    for num_cmplx in rwf_cmplx:
       real = num_cmplx.real
       imag = num_cmplx.imag
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
