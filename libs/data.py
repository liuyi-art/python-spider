#!/usr/bin/env python
# coding=utf-8
import os
from urllib.request import urlretrieve


def cbk(a, b, c):
    '''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    print(per)
    if per > 100:
        per = 100
    print("%.2f%%" % per)



# url = 'http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
# dir = os.path.abspath(".")
# print(dir)
# work_path = os.path.join(dir, 'Python-2.7.5.tar.bz2')
# print(work_path)
#
# urlretrieve(url, work_path, cbk)




url='http://www.baidu.com'
dir=os.path.abspath('.')
work_path=os.path.join(dir,'baidu.html')
urlretrieve(url,work_path,cbk)
