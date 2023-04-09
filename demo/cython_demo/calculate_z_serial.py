#cython: boundscheck=False
import cython
from cython.parallel import prange
import numpy as np

def calculate_z_parallel(maxiter: cython.int, zs: cython.complex[:], cs: cython.complex[:]): 
    """Calculate output list using Julia update rule""" 
    length: cython.int = len(zs)
    output: cython.int[:] = np.empty(length, dtype=np.int32)
    i : cython.int = 0
    z : cython.complex = 0.0
    c : cython.complex = 0.0
    #with cython.nogil:
    for i in prange(length, nogil=True, schedule="guided"): 
        z = zs[i] 
        c = cs[i]
        output[i] = 0
        while output[i] < maxiter and abs(z) < 2: 
            z = z * z + c 
            output[i] += 1
    return output


def calculate_z_numpy(maxiter: cython.int, zs: cython.complex[:], cs: cython.complex[:]): 
    """Calculate output list using Julia update rule""" 
    length: cython.int = len(zs)
    output: cython.int[:] = np.zeros(length, dtype=np.int32)
    n : cython.int = 0
    i : cython.int = 0
    z : cython.complex = 0.0
    c : cython.complex = 0.0
    for i in range(length): 
        n = 0
        z = zs[i] 
        c = cs[i]
        while n < maxiter and abs(z) < 2: 
            z = z * z + c 
            n += 1
        output[i] = n
    return output


def calculate_z_serial_cython(maxiter: cython.int, zs, cs): 
    """Calculate output list using Julia update rule""" 
    length: cython.int = len(zs)
    output = [0] * length 
    n : cython.int = 0
    i : cython.int = 0
    z : cython.complex = 0.0
    c : cython.complex = 0.0
    for i in range(length): 
        n = 0
        z = zs[i] 
        c = cs[i]
        while n < maxiter and abs(z) < 2: 
            z = z * z + c 
            n += 1
        output[i] = n
    return output