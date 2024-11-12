from logger import log
import numpy as np
import os
import re

def read(dataset):
    log('Read RWFs and MACs from dataset')
    if not os.path.isdir(dataset):
        os.mkdir(dataset)

    rwfs_l= []
    macs_l= []
    mag = 1e-10
    dir_list = os.listdir(dataset)
    for mac_id in dir_list:
        log(f'Read    {mac_id}')
        mac_dir = os.path.join(dataset, mac_id)
        file_list = os.listdir(mac_dir)
        for rwf_file in file_list:
            print(rwf_file, end=' ')
            rwf = []
            with open(os.path.join(dataset, mac_id, rwf_file)) as file:
               for line in file:
                   cpx = re.sub('[+ij]', '', line).split()
                   real = float(cpx[0])
                   imag = float(cpx[1])
                   mag = max(abs(real), abs(imag), mag)
                   rwf.append([real, imag])
            rwfs_l.append(rwf)
            macs_l.append(mac_id)
        print()

    # log('Convert lists to NumPy arrays, normalizing RWFs')
    norm = 0.5 / mag 
    rwfs = np.array(rwfs_l) * norm + 0.5 
    macs = np.array(macs_l)

    # log('Done reading to arrays in memory')
    return rwfs, macs
