from setuptools import setup, Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = cythonize([Extension("primes", ["primes.py"])],annotate=True)

setup(
    name="my_package",
    ext_modules=ext_modules,
    py_modules=["c_primes", "python_primes"],
    entry_points={
        "console_scripts": [
            "c_primes=c_primes:main",
            "python_primes=python_primes:main",
        ]
    },
    cmdclass={"build_ext": build_ext},
)
