# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    coverImage = scrapy.Field() #"cover.jpg",
    classify   = scrapy.Field() #"分类",
    index      = scrapy.Field() #"列表页中的排名",
    pageNo     = scrapy.Field() #"列表中的第几页",
    content    = scrapy.Field() #"html内容"
