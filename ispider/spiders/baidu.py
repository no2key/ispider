# -*- coding: utf-8 -*-

import scrapy
from bs4 import BeautifulSoup
from ..items import IspiderItem


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://www.baidu.com/',
    )

    def parse(self, response):
        items = []
        item = IspiderItem()
        item['title'] = unicode(response.xpath('/html/head/title/text()').extract()[0])
        item['url'] = response.url
        items.append(item)

        soup = BeautifulSoup(response.body)
        urls = soup.find_all('a')
        for url in urls:
            next_link = url.get('href', '')
            if next_link.startswith('h'):
                items.append(self.make_requests_from_url(next_link))

        return items