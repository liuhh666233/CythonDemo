from demo.cython_dict import IntDict
from demo.cython_vector import IntVector
from demo.utils import timefn
import numpy as np

stock_ids = np.random.randint(0, 600000, 1000000, dtype=np.int32)
stock_nums = np.random.randint(0, 500, 1000000, dtype=np.int32)
stock_prices = np.random.randint(0, 10, 1000000, dtype=np.int32)



@timefn
# @profile
def test_python_dict():
    data = {}
    length = len(stock_ids)
    for i in range(length):
        data[i] = stock_nums[i]
    result = 0
    for i in range(length):
        result += data[i] * stock_prices[i]
    print(result)



@timefn
@profile
def test_int_dict():
    length = len(stock_ids)
    data = IntDict(length)
    data.update(length, stock_nums)
    # result = data.calc(length, stock_prices)
    # print(result)


@timefn
@profile
def test_int_vector():
    length = len(stock_ids)
    data = IntVector()
    for i in range(length):
        data[i] = stock_ids[i]
    
@timefn
@profile
def test_list():
    length = len(stock_ids)
    data = []
    for i in range(length):
        data.append(stock_ids[i])


if __name__ == "__main__":
    test_int_vector()
    test_list()