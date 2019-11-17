import os
import numpy as np
import re

def _load_data(dir):
    # loay x
    files = os.listdir(dir)

    idFiles = [(int(re.match('x_(.*?).npy', fn).group(1)), fn) for fn in files]
    idFiles.sort(key=lambda x: x[0])

    arrayFns = [os.path.join(dir, fn) for _, fn in idFiles]
    arrays = [np.load(fn) for fn in arrayFns]
    x = np.concatenate(arrays, axis=0)

    # load y
    y = np.load('y.npy')
    return x, y


def load_robust_dataset():
    return _load_data('robust')


def load_nonrobust_dataset():
    return _load_data('nonrobust')

