import numpy as np
import numexpr as ne
from demo.utils import timefn

grid_shape = (1024, 1024)


def roll_add(rollee, shift, axis, out):
    if shift == 1 and axis == 0:
        out[1:, :] += rollee[:-1, :]
        out[0, :] += rollee[-1, :]
    elif shift == -1 and axis == 0:
        out[:-1, :] += rollee[1:, :]
        out[-1, :] += rollee[0, :]
    elif shift == 1 and axis == 1:
        out[:, 1:] += rollee[:, :-1]
        out[:, 0] += rollee[:, -1]
    elif shift == -1 and axis == 1:
        out[:, :-1] += rollee[:, 1:]
        out[:, -1] += rollee[:, 0]


# @profile
def laplacian(grid, out):
    np.copyto(out, grid)
    out *= -4
    roll_add(grid, +1, 0, out)
    roll_add(grid, -1, 0, out)
    roll_add(grid, +1, 1, out)
    roll_add(grid, -1, 1, out)


# @profile
def evolve(grid, dt, out, D=1.0):
    laplacian(grid, out)
    ne.evaluate("grid + (D * out * dt)", out=out)


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
