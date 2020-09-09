# 爬取百度贴吧一些小图片
# urllib.urlretriev---将远程数据下载到本地
import urllib.request
# from urllib.request import urlretrieve
import re
from bs4 import BeautifulSoup

# http://tieba.baidu.com/p/3868127254
# a = input('inpt url:')
url="http://tieba.baidu.com/p/6189691275"
s = urllib.request.urlopen(url)
print(s)
s1 = s.read().decode("utf-8")
print(s1)


def getimg(aaa):
    reg = re.compile(r'img.src="(.*?)"')
    print(reg)
    # reg = re.compile(r'<title>')
    l = re.findall(reg, aaa)
    tmp = 0
    for x in l:
        tmp += 1
        urllib.request.urlretrieve(x, '%s.jpg' % tmp)

        # print s1


getimg(s1)