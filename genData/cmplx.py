import numpy as np
import random as r

wf_r = []

with open('wf_r.txt', 'w') as f:
  for i in range(0, 5000):
    real = round(r.random() * 2 - 1, 4)
    imag = round(r.random() * 2 - 1, 4)
    wf_r.append(complex(real, imag))

    f.write(f'{real:.4f} + {imag:.4f}j\n')

print(wf_r)

wf = np.array(wf_r) 

print(wf)
wf.tofile('wf.cpx')
