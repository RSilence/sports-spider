# -*- coding: utf-8 -*-

import scrapy
from sportspider.items import SportspiderItem
import json
import time
from selenium import webdriver


class MySpider(scrapy.Spider):
    # 设置name
    name = "spiderJD"
    # 设定域名
    allowed_domains = ["tmall.com"]
    # 填写爬取地址
    start_urls = [
        #天猫篮球运动搜索结果
        'https://list.tmall.com//search_product.htm?spm=a221t.1710954.8404982328.34.5d33287aN6woWs&acm=lb-zebra-7771-282648.1003.8.421246&q=%C0%BA%C7%F2%D4%CB%B6%AF&tab=mall&type=p&scm=1003.8.lb-zebra-7771-282648.ITEM_14413206744903_421246'
    ]

    # 编写爬取方法
    def parse(self, response):
        搜索结果页

        nameList = response.css(".productTitle>a::attr(title)").getall()
        priceList = response.css(".productPrice>em::attr(title)").getall()
        dealSumList = response.css(".productStatus>span:first-child>em::text").getall()
        # imgList = response.css(".productImg>img::attr(src)").getall()

        list3 = []
        for name, price, dealSum in zip(nameList, priceList, dealSumList):
            #price
            price = float(price)
            #dealSum
            dealSum = dealSum[0:-1]
            if '万' in  dealSum:
                dealSum = int(float(dealSum[0:-1])*10000)
            else:
                dealSum = int(dealSum)
            dict = SportspiderItem()
            dict['name']=name
            dict['price']=price
            dict['dealSum']=dealSum
            dict['type']=''
            yield dict

        # print(nameList)
        # print(priceList)
        # print(dealSumList)
        # print(list3)
        # with open('basketball.json','w') as f:
        #     json.dump(list3, f, ensure_ascii=False)