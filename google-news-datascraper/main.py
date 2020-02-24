import requests
from bs4 import BeautifulSoup as bs
import unittest, time, re


r = requests.get('https://www.bettingexpert.com/football/aris-limassol-vs-ayia-napa')
  
html = bs(r.content,'html.parser')  
cnt_over = 0
cnt_under = 0 
over_list = [] 
under_list = []
# 
for el in  html.select('.be-tiplist-item__tip__content span'):
    over_t = '' 
    under_t = ''
    
    if 'Over' in el.text :
        cnt_over += 1
        over_t = el.text  
        over_list.append(over_t)
        

    if 'Under' in el.text :
        cnt_under += 1
        under_t = el.text 
        under_list.append(under_t)

        
print (cnt_over,": ",over_list)
print(cnt_under,': ',under_list)
 
#  cover letter

# Dear hiring manager
# I am expert in web research,web scraping, data mining, 

# I can assure you that I will be able to submit your task in time with quality work .

# I am waiting to be hired in this project to show my skills.
# Regards,
# Vladimir.