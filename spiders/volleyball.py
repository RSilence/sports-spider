# -*- coding: utf-8 -*-

import scrapy
from sportspider.items import SportspiderItem
import json
import time
from selenium import webdriver

class AttrSpider(scrapy.Spider):
    name = 'volleyball'
    allowed_domains = ['tmall.com']
    start_urls = [
        'https://list.tmall.com//search_product.htm?spm=a221t.1710954.8404982328.41.5d33287aCWPzBj&acm=lb-zebra-7771-283076.1003.8.421307&q=%C5%C5%C7%F2&tab=mall&type=p&scm=1003.8.lb-zebra-7771-283076.ITEM_14413211929647_421307']

    def parse(self, response):

        global dr
        dr = webdriver.Chrome('D:\lectures\Python\pycharm\scrapy\chromedriver_win32\chromedriver.exe')
        url = 'https://list.tmall.com//search_product.htm?spm=a221t.1710954.8404982328.41.5d33287aCWPzBj&acm=lb-zebra-7771-283076.1003.8.421307&q=%C5%C5%C7%F2&tab=mall&type=p&scm=1003.8.lb-zebra-7771-283076.ITEM_14413211929647_421307'
        page = dr.get(url)

        for x in range(1, 9, 1):
            j = x / 10
            js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
            dr.execute_script(js)
            time.sleep(2)


        #搜索结果页
        nameList = response.css(".productTitle>a::attr(title)").getall()
        priceList = response.css(".productPrice>em::attr(title)").getall()
        dealSumList = response.css(".productStatus>span:first-child>em::text").getall()
        # imgList = response.css(".productImg>img::attr(src)").getall()

        no = 1
        for name, price, dealSum in zip(nameList, priceList, dealSumList):
            # img
            xpathItem = '//*[@id="J_ItemList"]/div['+ str(no)+']/div/div[1]/a/img'
            img = dr.find_element_by_xpath(xpathItem).get_attribute('src')

            price = float(price)
            dealSum = dealSum[0:-1]
            if '万' in  dealSum:
                dealSum = int(float(dealSum[0:-1])*10000)
            else:
                dealSum = int(dealSum)
            dict = SportspiderItem()
            dict['name']=name
            dict['price']=price
            dict['dealSum']=dealSum
            dict['type']='volleyball'
            dict['img']=img
            # yield dict

            #detail

            xpathItem = './/*[@id="J_ItemList"]/div['+ str(no)+']'
            dr.find_element_by_xpath(xpathItem).click()
            windows=dr.window_handles
            dr.switch_to.window(windows[1])
            dict["brand"] = dr.find_element_by_id('J_attrBrandName').get_attribute('title')
            session = dr.find_elements_by_xpath('.//*[@id="J_AttrUL"]/li')
            for i in session:
                # print (i.get_attribute('title'))
                title = i.get_attribute('title')
                if len(title)>20:
                    continue
                if "号" in title:
                    dict["size"] = title

            dr.close()
            windows=dr.window_handles
            dr.switch_to.window(windows[0])

            print(no, dict)
            no = no+1

            yield dict

        pass
