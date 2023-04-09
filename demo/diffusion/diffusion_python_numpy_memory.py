import numpy as np
from demo.utils import timefn

grid_shape = (1024, 1024)


# @profile
def laplacian(grid, out):
    np.copyto(out, grid)
    out *= -4
    out += np.roll(grid, +1, 0)
    out += np.roll(grid, -1, 0)
    out += np.roll(grid, +1, 1)
    out += np.roll(grid, -1, 1)


# @profile
def evolve(grid, dt, out, D=1.0):
    laplacian(grid, out)
    out *= D * dt
    out += grid


@timefn
def run_experiment(num_iterations=10):
    grid = np.zeros(grid_shape)
    out = np.zeros(grid_shape)
    block_low = int(grid_shape[0] * 0.4)
    block_high = int(grid_shape[0] * 0.5)
    grid[block_low:block_high, block_low:block_high] = 0.005
    for i in range(num_iterations):
        evolve(grid, 0.1, out)
        grid, out = out, grid


if __name__ == "__main__":
    run_experiment(10)
