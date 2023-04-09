from demo.utils import timefn

grid_shape = [1024, 1024]


def evolve(grid, dt, D=1.0):
    xmax, ymax = grid_shape
    new_grid = [[0.0] * ymax for i in range(xmax)]
    for x in range(xmax):
        for y in range(ymax):
            grid_xx = (
                grid[(x + 1) % xmax][y] + grid[(x - 1) % xmax][y] - 2.0 * grid[x][y]
            )
            grid_yy = (
                grid[x][(y + 1) % ymax] + grid[x][(y - 1) % ymax] - 2.0 * grid[x][y]
            )
            new_grid[x][y] = grid[x][y] + D * dt * (grid_xx + grid_yy)
    return new_grid


@timefn
def run_experiment(num_iterations=10):
    xmax, ymax = grid_shape
    grid = [[0.0] * ymax for i in range(xmax)]
    block_low = int(grid_shape[0] * 0.4)
    block_high = int(grid_shape[0] * 0.5)
    for x in range(block_low, block_high):
        for y in range(block_low, block_high):
            grid[x][y] = 0.005
    for i in range(num_iterations):
        grid = evolve(grid, 0.1)


if __name__ == "__main__":
    run_experiment(10)
