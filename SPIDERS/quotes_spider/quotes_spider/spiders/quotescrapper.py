#-*- coding: utf-8 -*-
import scrapy


class QuotescrapperSpider(scrapy.Spider):
    name = 'quotescrapper'                      #name of spider
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        headings=response.xpath("//h1/a/text()").extract()[0]
        tags= response.xpath("//*[@class='tag-item']/a/text()").extract()

        #x=('heading':headings, 'Tags':tags)
        #print(f'==================================\n{x}\n===========================')
        with open('scraped.txt', 'w') as file:
            file.write(headings+'\n')
            for i in tags:
                file.write(i+'\n')
        


