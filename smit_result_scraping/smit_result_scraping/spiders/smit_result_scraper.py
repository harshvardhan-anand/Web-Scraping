# -*- coding: utf-8 -*-
import scrapy


class SmitResultScraperSpider(scrapy.Spider):
    name = 'smit_result_scraper'
    allowed_domains = ['results.smu.edu.in/smit/results_grade_view.php?exam=44']
    start_urls = ['http://results.smu.edu.in/smit/results_grade_view.php?exam=44/']

    def parse(self, response):
        
        # Arpil / May 2019

        marks_container =  response.xpath('//*[@id = "accordion"]')         #selector
        name_of_subject = marks_container.xpath('.//p/a/text()').extract() #list
        links_with_subject_name = marks_container.xpath('.//p/a')

        counter =  0
        subject_to_be_scraped = ['CHEMISTRY', 'SCIENCE', 'PROGRAMMING', 'ELECTRICAL', 'GRAPHICS', 'PRACTICE', 'PHYSICS']
        for i in subject_to_be_scraped:
            for j in name_of_subject:
                if (i in j) and ('BACK' not in j):
                    print(j)    #testing
                    break
                counter += 1
            print(counter)  #testing
            marks_page_link = links_with_subject_name[counter].xpath('./@href').extract_first()  #list
            print(marks_page_link)  #testing

            marks_page_redirect = response.urljoin(marks_page_link)
            yield scrapy.Request(marks_page_redirect)


            marks = response.xpath('//*[@style = "font-family:courier"]/text()').extract()  #selected where marks are written
            #ELEMINATING BAKWAS THINGS FROM MARKS SHEET
            k = 0
            to_be_deleted = 'SIKKIM SHEET Subject REGNO Mean cut Step Absentees Malpractices Detentions Malpractices Detentions students Abbreviations'
            to_be_deleted = to_be_deleted.split()
            while k<3:
                for i in to_be_deleted:
                    for j in marks:
                        if i.lower() in j.lower():
                            print(j)                  #testing
                            marks.remove(j)
                k += 1

            with open('marks_file.txt', 'w') as file:
                file.write(f'{i}\n{marks}\n')

            






