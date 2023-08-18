import random
import numpy as np
from multiprocessing import Pool
from ..utils import timefn


def estimate_nbr_points_in_circle(nbr_samples):
    nbr_points_in_circle = 0
    for i in range(nbr_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x * x + y * y <= 1:
            nbr_points_in_circle += 1
    return nbr_points_in_circle


def estimate_nbr_points_in_circle_numpy(nbr_samples):
    np.random.seed()
    x = np.random.uniform(-1, 1, nbr_samples)
    y = np.random.uniform(-1, 1, nbr_samples)
    return np.sum(x * x + y * y <= 1)


@timefn
def main():
    nbr_samples = 10000000
    nbr_processes = 8
    pool = Pool(nbr_processes)
    nbr_points_in_circle = sum(
        pool.map(
            estimate_nbr_points_in_circle_numpy,
            [nbr_samples // nbr_processes] * nbr_processes,
        )
    )
    print(4 * nbr_points_in_circle / nbr_samples)


if __name__ == "__main__":
    main()
