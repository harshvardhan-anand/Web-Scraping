# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com//']

    def parse(self, response):
        quote= response.xpath("//*[@class='quote']/*[@class='text']/text()").extract()
        written_by=response.xpath("//*[@class='quote']//*[@class='author']/text()").extract()
        tags= response.xpath("//*[@class='quote']//a/text()").extract()[1:]
        k=0
        for i in range(len(quote)):
            with open("scraped_page_1.txt", 'a+') as file:
                file.write(str(i+1)+' '+quote[i]+'\n'+written_by[i]+'\n'+'tags: ')
                for i in range(k, len(tags)):
                    if tags[i] != '(about)':
                        file.write(tags[i]+ '   ')
                    else:
                        k+=1
                        break
                file.write('\n\n')

                    

            
            