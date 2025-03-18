import time
import math
import numpy as np

# 测试单个数值的计算
def test_math():
    start = time.time()
    for _ in range(1000000):
        math.sin(0.5)
    end = time.time()
    return end - start

def test_numpy():
    start = time.time()
    for _ in range(1000000):
        np.sin(0.5)
    end = time.time()
    return end - start

# 测试大规模数据的计算
def test_numpy_array():
    arr = np.random.rand(1000000)
    start = time.time()
    np.sin(arr)
    end = time.time()
    return end - start

# 输出结果
print("math.sin (单个数值):", test_math())
print("numpy.sin (单个数值):", test_numpy())
print("numpy.sin (大规模数据):", test_numpy_array())