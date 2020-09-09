import codecs

import requests
import threading
import queue
from lxml import etree
import time
Q = queue.Queue()

class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.url = 'https://gw-cn.jiaoliuqu.com/mall/v3/PortalV2/getTabList?distinctRequestId=7cd32f41a839f27cd5da71dab3a26278'

    def run(self):
        resp = requests.get(self.url)
        html = resp.content.decode('utf-8')
        text = etree.HTML(html)
        print(text)
        dds = text.xpath('//div[@id="list"]/dl/dd/a/@href')
        # print(type(dds))
        for url in dds[4:-1]:
            url = 'https://www.xbiquge6.com' + url
            # print(url)
            Q.put(url)

class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            url = Q.get()
            resp = requests.get(url)
            html = resp.content.decode('utf-8')
            text = etree.HTML(html)
            fo = codecs.open('元尊.txt', 'a+', 'utf-8')
            name = text.xpath('//div[@class="bookname"]/h1/text()')[0].strip()  # 章节的名字
            print(name)
            fo.write("\r\n"+name+"\r\n")

            contents = text.xpath('//div[@id="content"]/text()')
            # print(contents)
            # f = open('./%s.txt' % name, 'w')
            # print('正在保存%s' % name)
            for content in contents:
                fo.write(content)  # content是一段一段的文字，不是一个整体的，若是使用with open只能保存第一句
                fo.write('\n')
            fo.close()

if __name__ == '__main__':
    start = time.time()
    s = A()
    q = B()
    s.start()
    q.start()
    s.join()
    q.join()
    print(time.time()-start)