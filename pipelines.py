# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import  MongoClient

# class MongoPipeline(object):
class SportspiderPipeline(object):
    def __init__(self, databaseIp = '127.0.0.1', databasePort = 27017, mongodbName = 'sports'):
        client = MongoClient(databaseIp, databasePort)
        self.db = client[mongodbName]

    def process_item(self, item, spider):
        postItem = dict(item)
        self.db.scrapy.insert(postItem)
        return item

