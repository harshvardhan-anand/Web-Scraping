# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
import numpy as np
import pickle as pk

class TgrptSpider(scrapy.Spider):
    name = 'tgrpt' 
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
       a = [201900442, 201900443, 201900319, 201900389, 201900379, 201900369, 201900329, 201900349, 201900419, 201900273, 201900359, 201900399, 201800343]
#       a = [201921419, 201921422]
       regno = a
       details_url = 'http://10.51.0.9/ecm/Students/profile2.aspx?reg='
       
       def extractor():
           '''
           attandance = response.xpath('//*[@id="ctl00_ContentPlaceHolder1_gvRecord"]/*[@class = "padLeft"][SELECTROW]/td[ATTANDorSUBJECT]/text()').extract_first()
           row: from 3 to end
           '''
#           
#           attend = []
#           subj = []
#           all_data = None
#           for row in range(3, total_subject+1):
#               xp = '//*[@id="ctl00_ContentPlaceHolder1_gvRecord"]/*[@class = "padLeft"]['+str(row)+']/td[4]/text()'
#               attandance = int(response.xpath('//*[@id="ctl00_ContentPlaceHolder1_gvRecord"]/*[@class = "padLeft"]["'+str(row)+'"]/td[4]/text()').extract_first())
#               print((response.xpath(xp)))
#               attandance = (response.xpath(xp).extract_first())
#               print('\n\n', attandance,'\t',row,'\t',xp,  '\n\n')
#               attend.append(attandance)
#               subject = response.xpath('//*[@id="ctl00_ContentPlaceHolder1_gvRecord"]/*[@class = "padLeft"]["'+str(row)+'"]/td[1]/text()').extract_first()[4:10]
           name = response.xpath('//*[@id="ctl00_ContentPlaceHolder1_txtSName"]/@value').extract_first()
           all_data = response.xpath('//*[@id="ctl00_ContentPlaceHolder1_gvRecord"]/*[@class = "padLeft"]/td/text()').extract() 
           all_data.append(name)
           return all_data
#               all_sub_len = len(response.xpath('//*[@id="ctl00_ContentPlaceHolder1_gvRecord"]/*[@class = "padLeft"]/td[1]/text()').extract()[2:])
#               for i in range(all_sub_len):
#                   subject = response.xpath('//*[@id="ctl00_ContentPlaceHolder1_gvRecord"]/*[@class = "padLeft"]/td[1]/text()').extract()[2:][i][4:]
#                   subj.append(subject)
               # m means masked
        
#           print(all_data)
#           print('\n\n', attend, '\n\n')
#           attandance =  np.array(attend)
#           m_attandence = attandance[attandance>=75]
#           m_subject = []
#           try:
#               for i in m_attandence:
#                   m_subject.append(subject[np.where(attandance == i)[0][0]])
#           except:
#              return 'check this'
#           else:
#               return list(zip(m_subject, m_attandence))
        

           
           
       sublst = {}
       for reg in regno: 
           srno = 1
           abs_url = details_url+str(reg)
#           total_subject = len(response.xpath('//*[@id="ctl00_ContentPlaceHolder1_gvRecord"]/*[@class = "padLeft"]'))
             
           sublst[str(reg)] = extractor()
           
           
#           if type(sublst) == None:
#               sublst = 'Nil '
                      
#           yield{'Sr.No.':srno,
#                 'Name of ward present': name,
#                 'Registration Number': reg,
#                 'Subject list in which % Attandance is less than 75%': sublst,
#                 'Remarks':'No issues'
#                   }
#           print('\n\n\n')
#           print({'Sr.No.':srno,
#                 'Name of ward present': name,
#                 'Registration Number': reg,
#                 'Subject list in which % Attandance is less than 75%': sublst,
#                 'Remarks':'No issues'
#                   })
#           print('\n\n\n')
           #print(sublst)
           srno += 1
           abs_url = details_url+str(reg)
           yield scrapy.Request(abs_url)
       print(sublst)
       with open('row_data.txt', 'w') as f:
               pk.dump(sublst, f)
    
