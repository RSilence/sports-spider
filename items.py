# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SportspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    dealSum = scrapy.Field()
    type = scrapy.Field()
    size = scrapy.Field() #型号 如篮球5号幼儿 6号中小学生 7号成人
    brand = scrapy.Field()
    img = scrapy.Field()
    pass
