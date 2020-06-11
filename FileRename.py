# -*- coding: utf-8 -*-
import os

# 查找文件
path = "D:\\lina\document\\baiduyundownload\\开言英语\\B1"


# os.listdir()方法，列出来所有文件
# 返回path指定的文件夹包含的文件或文件夹的名字的列表
# files = os.listdir(path)


def deal_files(path):
    files = os.listdir(path)
    for f in files:
        # 调试代码的方法：关键地方打上print语句，判断这一步是不是执行成功
        if os.path.isdir(path + "\\" + f):
            print("dir-" + f)
            deal_files(path + "\\" + f)
        elif f.find('讲义_') > 0:
            print(f)
            # 找到老的文件所在的位置
            old_file = os.path.join(path, f)
            print("old_file is {}".format(old_file))
            # 指定新文件的位置，如果没有使用这个方法，则新文件名生成在本项目的目录中
            new_file = os.path.join(path, f[f.find('讲义_') + 3:].replace('_', ''))
            print("File will be renamed as:{}".format(new_file))
            os.rename(old_file, new_file)


if __name__ == '__main__':
    deal_files(path)
