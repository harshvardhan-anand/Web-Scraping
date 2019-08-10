 #-*- coding: utf-8 -*-
import scrapy


class BookScraperSpider(scrapy.Spider):
    name = 'book_scraper'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def rating_convert(self, rating):
             rating = rating[12:]
             if rating == 'One':
                return 1
             if rating == 'Two':
                return 2
             if rating == 'Three':
                return 3
             if rating == 'Four':
                return 4
             if rating == 'Five':
                return 5
             if rating == 'Zero':
                return 0

    def parse(self, response):
        
        #we can also use custom selector to make it more easy
        book_name =  response.xpath('//h3/a/@title').extract()
        price_of_books = response.xpath("//*[@class='price_color']/text()").extract()
        rating =  response.xpath('//*[@class = "product_pod"]/p/@class').extract()
        
        #getting raw stock data
        stock_raw = response.xpath('//*[@class = "instock availability"]/text()').extract()
        for i in stock_raw:
         if i == '\n    ':
             stock_raw.remove('\n    ')
        #getting processed stock data
        stock = []
        for i in stock_raw:
            stock.append(' '.join(i.split()))


        for i in range(len(book_name)):

            #getting numbers for rating instead of string  
            rating_num = self.rating_convert(rating[i])

            yield{'Book Name' : book_name[i],
                  'Price' : price_of_books[i],
                  'Rating' :rating_num,    #use this to get strings, rating = rating[i][12:]
                  'stock' : stock[i]}

            print('\n\n\n')#for cmd just to prettify


        #next page
        next_page_url = response.xpath('//*[@class = "next"]/a/@href').extract_first()
        absolute_url = response.urljoin(next_page_url)

        yield scrapy.Request(absolute_url)