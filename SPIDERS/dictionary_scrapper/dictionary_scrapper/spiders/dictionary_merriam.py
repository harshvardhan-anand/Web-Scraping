# -*- coding: utf-8 -*-
import scrapy


class DictionaryMerriamSpider(scrapy.Spider):
    name = 'dictionary_merriam'
    allowed_domains = ['www.merriam-webster.com']
    start_urls = ['http://www.merriam-webster.com/']


    def parser(self, response):

        #scraping dictionary datas in index page i.e page 0 
        data_points = response.xpath('//*[@class = "entries"]/ul/li/a/text()').extract()
        yield {'Datas' : data_points}
        
        pages = response.xpath('//*[@class = "pagination"]/li/@class').extract()  
        
        if ('next' in pages) :
                #getting the next page url relative
                next_sub_pages = response.xpath('//*[@class = "next"]/a/@href').extract_first()
                #absolute uls to next pages eg=>1,2,3...
                abs_next_url = response.urljoin(next_sub_pages)
                #print(next_sub_pages)
                yield scrapy.Request(abs_next_url, callback=self.parser)

    
    def parse(self, response):
        #get in main page i.e www.merriam-webster.com
        #sub pages from main page
        res = response.xpath('//*[@class = "footer-menu browse-dictionary"]/li/a/@href')[1:].extract()
        
        for index in res:
            abs_index_url = response.urljoin(index)
            yield scrapy.Request(abs_index_url, callback = self.parser)   #now we are in index pages i.e a,b,c,d,e....
  
            
        
            
                


    
            
            
            
            
   
            
            
   
        
        
        
