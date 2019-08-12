# -*- coding: utf-8 -*-

import scrapy


class DictScrapSpider(scrapy.Spider):
    name = 'dict_scrap'
    allowed_domains = ['www.dictionary.com']
    start_urls = ['http://www.dictionary.com/']

    def parse(self, response):
        q = response.xpath('//*[@data-linkid = "74qg7q"]')  # custom selector
        index_links = q.xpath('./*[@class = "dcom css-ulvvm0 ex77a8l1"]/a/@href').extract()  # list of all main links 
        
        
        for i in index_links:
            # getting into index links
            abs_index_url = response.urljoin(i)
            yield scrapy.Request(abs_index_url)


             # while all the sub-pages are not scraped
            while True:
                
                 dict_data = response.xpath('//*[@class = "css-ytumd6 e1j8zk4s1"]/text()').extract() #dictionary data
                 
             
                 # go to next page of current index
                 current_index_nxt_page = response.xpath("//*[@class = 'css-w3ynk9-NavNextItem e1wvt9ur5']/a/@href").extract()
                 #print(current_index_nxt_page[0])
                 
                 #for saving file in csv format
                 #print(dict_data)
                 
 
                 #using to break from the loop if there is no element present in the list
                 if (current_index_nxt_page) == []:
                     break
                 else:
                     abs_sub_link = response.urljoin(current_index_nxt_page[0])
                     yield scrapy.Request(abs_sub_link)
 
             
            print("\n\n\nSCRAPPING DONE OF SUB-PAGES\n\n\n")
         
        print("\n\n\nALL SCRAPPING DONE\n\n\n")
             
 
 #=============================================================================
