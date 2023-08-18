from demo.utils import timefn
from demo.primes import primes


@timefn
def main():
    for i in range(1000):
        primes(i)
