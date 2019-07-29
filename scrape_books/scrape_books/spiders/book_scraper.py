# -*- coding: utf-8 -*-
import scrapy


class BookScraperSpider(scrapy.Spider):
    name = 'book_scraper'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        
        book_name_in_page_1 =  response.xpath('//h3/a/@title').extract()

        price_of_books_on_first_page = response.xpath("//*[@class='price_color']/text()").extract()

        rating_in_first_page =  response.xpath('//*[@class = "product_pod"]/p/@class').extract()

        stock_raw = response.xpath('//*[@class = "instock availability"]/text()').extract()