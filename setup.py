from setuptools import setup, Extension, find_packages
from Cython.Distutils import build_ext
from Cython.Build import cythonize


ext_modules = cythonize([
    Extension("demo.primes", ["./demo/cython_demo/primes.py"]), 
    Extension("demo.calulate_z", ["./demo/cython_demo/calculate_z_serial.py"])],annotate=True)

setup(
    name="my_package",
    ext_modules=ext_modules,
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "c_primes=demo.c_primes:main",
            "python_primes=demo.python_primes:main",
            "julia=demo.julia:calc_pure_python_main",
            "julia_cython=demo.julia:calc_cython_main",
        ]
    },
    cmdclass={"build_ext": build_ext},
)
