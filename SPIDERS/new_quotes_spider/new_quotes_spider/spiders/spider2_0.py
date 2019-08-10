# -*- coding: utf-8 -*-
import scrapy


class Spider20Spider(scrapy.Spider):
    name = 'spider2.0'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quote_container = response.xpath("//*[@class = 'quote']")
        for quote in quote_container:
            quotes = quote.xpath(".//*[@class = 'text']/text()").extract_first()
            author = quote.xpath(".//*[@class = 'author']/text()").extract_first()
            tags   = quote.xpath(".//*[@class = 'keywords']/@content").extract_first()  

            
            yield{'Quotes' : quotes,
                  'Author' : author,
                  'Tags'   : tags}
            
            
            next_page = response.xpath("//*[@class = 'next']//@href").extract_first()
            absolute_page = response.urljoin(next_page)
            yield scrapy.Request(absolute_page)
        

