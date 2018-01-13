# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json

class BookinfoPipeline(object):

    def __init__(self):
        self.file = codecs.open('./bookdata/data.txt','w',encoding='utf-8')
        # 创建一个json list
        self.file.writelines("[")
        # 统计爬去图书总数 最后写入文档尾部
        self.book_counter = 0

    def process_item(self, item, spider):
        json.dump({
            'coverImage':item['coverImage'],
            'classify':item['classify'],
            'index':item['index'],
            'pageNo':item['pageNo'],
            'content':item['content'],
            }, self.file, indent=4)
        self.file.writelines(",\n")
        self.book_counter += 1
        return item

    def close_spider(self, spider):
        self.file.writelines(str(self.book_counter)+"]")
        self.file.close()