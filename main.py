import numpy as np
a = np.arange(15).reshape(3, 5)
a
a.shape
print(a)
a.ndim
print(a.ndim)
a.dtype.name
print(a.dtype.name)
a.itemsize
print(f'{a.itemsize} is the item size of a')
a.size
print(f'{a.size} is the size of a')
type(a)
print(type(a))
b = np.array([6, 7, 8])
b
print(b)
type(b)