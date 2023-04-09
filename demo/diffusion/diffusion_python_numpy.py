import numpy as np
from demo.utils import timefn

grid_shape = (1024, 1024)


def laplacian(grid):
    return (
        np.roll(grid, 1, 0)
        + np.roll(grid, -1, 0)
        + np.roll(grid, 1, 1)
        + np.roll(grid, -1, 1)
        - 4 * grid
    )


def evolve(grid, dt, D=1.0):
    return grid + D * dt * laplacian(grid)


@timefn
def run_experiment(num_iterations=10):
    grid = np.zeros(grid_shape)
    block_low = int(grid_shape[0] * 0.4)
    block_high = int(grid_shape[0] * 0.5)
    grid[block_low:block_high, block_low:block_high] = 0.005
    for i in range(num_iterations):
        grid = evolve(grid, 0.1)


if __name__ == "__main__":
    run_experiment(10)
