# -*- coding: utf-8 -*-
# 网易云音乐 通过歌手ID，生成该歌手的词云
import os
import pandas as pd
from pandas import Series, DataFrame
import requests
import sys
import re
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np
from lxml import etree


# 去掉停用词
def remove_stop_words(f):
    stop_words = ['作词', '作曲', '编曲', 'Arranger', '录音', '混音', '人声', 'Vocal', '弦乐', 'Keyboard', '键盘', '编辑', '助理',
                  'Assistants', 'Mixing', 'Editing', 'Recording', '音乐', '制作', 'Producer', '发行', 'produced', 'and',
                  'distributed', '吉他', 'guitar', '毛不易']
    for stop_word in stop_words:
        f = f.replace(stop_word, '')
    return f


# 生成词云
def create_word_cloud(f):
    print('根据词频，开始生成词云!')
    # f = remove_stop_words(f)
    cut_text = " ".join(jieba.cut(f, cut_all=False, HMM=True))
    wc = WordCloud(
        font_path="./msyhbd.ttf",
        max_words=100,
        width=2000,
        height=1200,
    )
    print(cut_text.replace(u'\xae', u' '))
    wordcloud = wc.generate(cut_text)
    # 写词云图片
    wordcloud.to_file("wordcloud.jpg")
    # 显示词云文件
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


all_word = ''
# 查找文件
path = "D:\\lina\document\\baiduyundownload\\开言英语\\"
paths = ['A1', 'A2', 'B1']

for p in paths:
    files = os.listdir(path + p)
    for f in files:
        all_word += f

# 根据词频 生成词云
create_word_cloud(all_word)
