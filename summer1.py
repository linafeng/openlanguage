# -*- coding: utf-8 -*-
n = 6
for x in range(1, n + 1):
    z = n - x
    for i in range(0, z):
        print(' ', end='')
    for i in range(0, x):
        if (i < x - 1 and x != 1):
            print('**', end='')
        else:
            print('* ', end='')
    print('')
