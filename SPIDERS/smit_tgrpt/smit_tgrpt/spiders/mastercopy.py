# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class TgrptSpider(scrapy.Spider):
    name = 'tgrpt_master' 
    start_urls = ['http://10.51.0.9/ecm/']

    def parse(self, response):
        VIEWSTATE =  response.xpath("//*[@id = '__VIEWSTATE']/@value").extract_first()
        EVENTARGUMENT = response.xpath("//*[@id = '__EVENTARGUMENT']/@value").extract_first()
        EVENTTARGET = response.xpath("//*[@id = '__EVENTTARGET']/@value").extract_first()
        LASTFOCUS =  response.xpath("//*[@id = '__LASTFOCUS']/@value").extract_first()
        VIEWSTATEGENERATOR = response.xpath("//*[@id = '__VIEWSTATEGENERATOR']/@value").extract_first()
        EVENTVALIDATION = response.xpath("//*[@id = '__EVENTVALIDATION']/@value").extract_first()
        tbEmail = response.xpath("//*[@id = 'tbEmail']/@value").extract_first()
        btnLogin = response.xpath("//*[@id = 'btnLogin']/@value").extract_first()
       
        print('\n')
#        userid = input("Give your userID: ")
#        password = input("Give your password: ")
        userid = '4581'
        password = 'ginverse'
        print('\n')
        print('\n+++++++++++++++++++++++ENTERED IN SCRAPER++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
        return FormRequest.from_response(response, 
                                         formdata= {'__LASTFOCUS':LASTFOCUS ,
                                                    '__EVENTTARGET':EVENTTARGET,
                                                    '__EVENTARGUMENT':EVENTARGUMENT,
                                                    '__VIEWSTATE':VIEWSTATE,
                                                    '__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
                                                    '__EVENTVALIDATION':EVENTVALIDATION, 
                                                    'tbEmail':tbEmail,
                                                    'TxtUserName':userid,
                                                    'TxtPassword':password,
                                                    'btnLogin':btnLogin},
                                         callback = self.scraper)
    def scraper(self, response):
#       open_in_browser(response)
#       regno = response.xpath('//*[@id="ctl00_ContentPlaceHolder1_gv1_ctl02_lblReg"]/text()').extract_first()
#       course = response.xpath('//*[@id="ctl00_ContentPlaceHolder1_gv1_ctl02_lblCourse"]/text()').extract_first()
#       regno = input("Give registration number of students in comma seperated format: ").split(',')
       print('\n+++++++++++++++++++++++ENTERED IN SCRAPER++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
       a = [0, 201921419, 201921422, 201921417, 201921409, 201921411, 201921404, 201921412, 201921418, 201921420, 201900442, 201900443, 201900319, 201900389, 201900379, 201900369, 201900329, 201900349, 201900419, 201900273, 201900359, 201900399, 201800343]
       regno = a
       details_url = 'http://10.51.0.9/ecm/Students/profile2.aspx?reg='
       abs_url = details_url+str(regno)
       def extractor(row):
           '''
           attandance = response.xpath('//*[@id="ctl00_ContentPlaceHolder1_gvRecord"]/*[@class = "padLeft"][SELECTROW]/td[ATTANDorSUBJECT]/text()').extract_first()
           row: from 3 to end
           '''
           attandance = int(response.xpath('//*[@id="ctl00_ContentPlaceHolder1_gvRecord"]/*[@class = "padLeft"]["'+str(row)+'"]/td[4]/text()').extract_first())
           if (attandance<75):
               subject = response.xpath('//*[@id="ctl00_ContentPlaceHolder1_gvRecord"]/*[@class = "padLeft"]["'+str(row)+'"]/td[1]/text()').extract_first()[4:10]
               return attandance, subject
           else:
               return None
           
       for reg in regno[1:]: 
           srno = 1
           abs_url = details_url+str(reg)
           total_subject = len(response.xpath('//*[@id="ctl00_ContentPlaceHolder1_gvRecord"]/*[@class = "padLeft"]'))
           name = response.xpath('//*[@id="ctl00_ContentPlaceHolder1_txtSName"]/@value').extract_first()  
           sublst = []
           
           for i in range(3, total_subject+1):
               if ((extractor(i)) != None):
                   att, sub = extractor(i)
                   sublst.append(list(zip(sub, att)))

           if not(any(sublst)):
               sublst = 'Nil '
                      
           yield{'Sr.No.':srno,
                 'Name of ward present': name,
                 'Registration Number': reg,
                 'Subject list in which % Attandance is less than 75%': sublst,
                 'Remarks':'No issues'
                   }
           print('\n\n\n')
           print({'Sr.No.':srno,
                 'Name of ward present': name,
                 'Registration Number': reg,
                 'Subject list in which % Attandance is less than 75%': sublst,
                 'Remarks':'No issues'
                   })
           print('\n\n\n')
           srno += 1
           yield scrapy.Request(abs_url)
           
    
