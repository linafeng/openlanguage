# -*- coding: utf-8 -*-
import os
import pandas as pd
from pandas import Series, DataFrame

# 查找文件
path = "D:\\lina\document\\baiduyundownload\\开言英语\\"
paths = ['A1', 'A2', 'B1']

data = {}

for p in paths:
    data[p] = []
    files = os.listdir(path + p)
    for f in files:
        data[p].append(f)

print(data)
df = pd.DataFrame.from_dict(data, orient='index')
df = df.T
print(df)
df.to_excel('dump.xlsx')
