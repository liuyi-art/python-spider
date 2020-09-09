# _*_ coding:utf-8 _*_
import requests
from lxml import etree


class NovelSpider():
    def __init__(self):
        # self.base_url = "https://xs.sogou.com/29_2_0_0_heat/?pageNo={}"
        self.base_url = "https://xiaoshuo.sogou.com/list/5728502428"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.data_list = []

    def send_request(self,params):
        response = requests.get(self.base_url, headers=self.headers, params=params)
        data = response.content.decode()
        # print(response.url)
        return data
        pass

    def analysis_data(self,data):
        html_data = etree.HTML(data)
        tr_list = html_data.xpath('//li[@class="c3"]/a/@href')
        # print(tr_list)
        for tr in tr_list:
            url="https://xiaoshuo.sogou.com"+tr
            return url
    def save_data(self,url):
        html_data1 = etree.HTML(url)
        # print(html_data1)
        pass

    def run(self):
        # for i in range(1,275):
        #     url=self.base_url.format(i)
        #     data=self.send_request(url)
        #     print(data)
        #     self.analysis_data(data)
        data = self.send_request(self.base_url)
        # print(data)
        url=self.analysis_data(data)
        self.save_data(url)
        pass


if __name__ == '__main__':
    NovelSpider().run()