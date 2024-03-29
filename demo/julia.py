"""Julia set generator without optional PIL-based image drawing"""
# import time
# import cProfile
# import subprocess
# import pysnooper
import numpy as np
from demo.utils import timefn
from demo.calulate_z import (
    calculate_z_serial_cython,
    calculate_z_numpy,
    calculate_z_parallel,
)

# area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -0.42193


@timefn
# @pysnooper.snoop()
def calculate_z_serial_purepython(maxiter, zs, cs):
    """Calculate output list using Julia update rule"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while n < maxiter and abs(z) < 2:
            z = z * z + c
            n += 1
        output[i] = n
    return output


@timefn
def calc_pure_python(desired_width, max_iterations):
    """Create a list of complex coordinates (zs) and complex parameters (cs), build Julia set, and display"""
    x_step = float(x2 - x1) / float(desired_width)
    y_step = float(y1 - y2) / float(desired_width)
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    # Build a list of coordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed;
    # we use it to simulate a real-world scenario with several inputs to # our function.
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    print("Length of x:", len(x))
    print("Total elements:", len(zs))
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    # This sum is expected for a 1000^2 grid with 300 iterations.
    # It catches minor errors we might introduce when we're
    # working on a fixed set of inputs.
    assert sum(output) == 33219980


@timefn
# @profile
def calc_cython(desired_width, max_iterations):
    """Create a list of complex coordinates (zs) and complex parameters (cs), build Julia set, and display"""
    x_step = float(x2 - x1) / float(desired_width)
    y_step = float(y1 - y2) / float(desired_width)
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    # Build a list of coordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed;
    # we use it to simulate a real-world scenario with several inputs to # our function.
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    print("Length of x:", len(x))
    print("Total elements:", len(zs))
    output = calculate_z_serial_cython(max_iterations, zs, cs)
    # This sum is expected for a 1000^2 grid with 300 iterations.
    # It catches minor errors we might introduce when we're
    # working on a fixed set of inputs.
    assert sum(output) == 33219980


@timefn
# @profile
def calc_cython_numpy(desired_width, max_iterations):
    """Create a list of complex coordinates (zs) and complex parameters (cs), build Julia set, and display"""
    x_step = float(x2 - x1) / float(desired_width)
    y_step = float(y1 - y2) / float(desired_width)
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    # Build a list of coordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed;
    # we use it to simulate a real-world scenario with several inputs to # our function.
    x, y = np.meshgrid(x, y)
    zs = (x + y * 1j).ravel()
    cs = np.full(zs.shape, complex(c_real, c_imag))
    print("Length of x:", len(x))
    print("Total elements:", len(zs))
    output = calculate_z_parallel(max_iterations, zs, cs)
    # This sum is expected for a 1000^2 grid with 300 iterations.
    # It catches minor errors we might introduce when we're
    # working on a fixed set of inputs.
    assert sum(output) == 33219980


def calc_pure_python_main():
    # Calculate the Julia set using a pure Python solution with
    # reasonable defaults for a laptop
    calc_pure_python(desired_width=1000, max_iterations=300)
    # cProfile.run('calc_pure_python(desired_width=1000, max_iterations=300)',sort="cumtime", filename="test.prof")
    # subprocess.run(["snakeviz", "test.prof"])


def calc_cython_main():
    # Calculate the Julia set using a pure Python solution with
    # reasonable defaults for a laptop
    calc_cython(desired_width=1000, max_iterations=300)
    calc_cython_numpy(desired_width=1000, max_iterations=300)
    # cProfile.run('calc_pure_python(desired_width=1000, max_iterations=300)',sort="cumtime", filename="test.prof")
    # subprocess.run(["snakeviz", "test.prof"])


if __name__ == "__main__":
    calc_cython_main()
