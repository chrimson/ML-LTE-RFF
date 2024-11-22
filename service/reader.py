import numpy as np
import os

def read(svc, dataset):
    if not os.path.isdir(dataset):
        os.mkdir(dataset)

    rwfs_l= []
    macs_l= []
    mag = 1e-10
    dir_list = os.listdir(dataset)
    svc.logger.info(f'Read {len(dir_list)} MACs and their variant RWFs from dataset')
    for mac_id in dir_list:
        mac_dir = os.path.join(dataset, mac_id)
        file_list = os.listdir(mac_dir)
        for rwf_file in file_list:
            rwf_cmplx = np.load(os.path.join(dataset, mac_id, rwf_file))
            rwf = []
            for num_cmplx in rwf_cmplx:
               real = num_cmplx.real
               imag = num_cmplx.imag
               mag = max(abs(real), abs(imag), mag)
               rwf.append([real, imag])
            rwfs_l.append(rwf)
            macs_l.append(mac_id)
        svc.logger.info(f'  Read {mac_id} {len(file_list)} Variants')

    # svc.logger.info('Convert lists to NumPy arrays, normalizing RWFs')
    norm = 0.5 / mag 
    rwfs = np.array(rwfs_l) * norm + 0.5 
    macs = np.array(macs_l)

    # svc.logger.info('Done reading to arrays in memory')
    return rwfs, macs
