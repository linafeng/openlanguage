# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv(filepath_or_buffer='dump.csv', encoding='gb18030')
print(data)
