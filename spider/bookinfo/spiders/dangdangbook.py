# -*- coding: utf-8 -*-

import scrapy
from bookinfo.items import BookinfoItem

class DangdangbookSpider(scrapy.Spider):
    name = 'dangdangbook'
    
    def start_requests(self):
        # 爬去计算机和网络图书列表的前4页
        for page in range(1,5):
            yield scrapy.Request(url='http://category.dangdang.com/pg'+str(page)+'-cp01.54.00.00.00.00-srsort_score_desc.html', meta={'current_page':page}, callback=self.parse)

    def parse(self, response):
        page_bool_urls = response.xpath('//div[@dd_name="普通商品区域"]/ul/li/a/@href').extract()
        for u in page_bool_urls:
            meta_data = {
                'current_page':response.meta['current_page'],
                'index':page_bool_urls.index(u),
            }
            yield scrapy.Request(url=u, meta=meta_data, callback=self.parse_book_detail)

    def parse_book_detail(self, response):
        book_title = response.xpath('//h1[@title]/@title').extract()
        print(book_title)

        item = BookinfoItem()
        item['coverImage']=response.xpath('//img[@dd_name="大图"]/@src').extract()[0]
        item['classify']=str(response.xpath('//div[@dd_name="顶部面包屑导航"]/a[@href]/text()').extract())
        item['index']=response.meta['index']
        item['pageNo']=response.meta['current_page']
        item['content']= str(response.body_as_unicode())

        yield item
