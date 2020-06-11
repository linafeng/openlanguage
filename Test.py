# -*- coding: utf-8 -*-
import numpy as np

# 0
a, b = 1, 2
a, b = b, a
print(a, b)
# 1
print(max(1024, 256))
# 2
X = [[1, 2], [3, 4], [5, 6]]
print([i for l in X for i in l])

# 3
a3 = '123,456,789'
a4 = a3.split(',')
print(type(a4))

# 4
a4 = [1, 2, 3, 4, 5]
list(map(str, [1, 2, 3, 4, 5]))
# 5
print(np.array([[1, 2], [3, 4], [5, 6]]).T)
# 6
Y = [[[1, 2], [3, 4]]]
print([x for z in Y for y in z for x in y])
# 7
print(min(1, 2, 3))
# 8
print([i for i in range(1, 11) if i % 2 == 0])
# 9
print([i for i in range(1, 11) if i % 2 == 1])




