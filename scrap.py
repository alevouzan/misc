import bs4 as bs
from selenium import webdriver 
import pandas as pd

with open('456.txt', 'w') as f:
 #with open('sitebunker.txt', 'w') as b:

  #a="ss_country_s sectionhead"
  #b="ss_country sectionhead"
  #c="ss_cname"
  #e="ss_text"
  #d="ss_cname_s"
  #f="ss_text_s"
  #h="ss_url_s"
  #i="ss_url"
  browser = webdriver.Firefox()
  url = ("https://directories.lloydslist.com/services-browse/sscompid//country//ss/5693/oas/bunkering")
  browser.get(url)
  for page in range (279):
     s1="https://directories.lloydslist.com/var/recordset/66893/pos/"
     s2="1"
     browser.get(s1+str(page)+s2)
     html_source = browser.page_source
  
     soup = bs.BeautifulSoup(html_source, "html.parser")
     f.write("\n")
     for tr in soup.find_all('tr'):
        #if a | b in tr:
        print(len(soup.find_all('tr')))
        #tds = tr.find_all('td')
        #f.write(tds[0].text)
        #f.write("#")

     


     

