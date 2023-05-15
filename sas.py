import bs4 as bs
from selenium import webdriver 
import csv
from urllib.request import urlopen

 

browser = webdriver.Firefox()
url = ("https://directories.lloydslist.com/services-browse/sscompid//country//ss/5693/oas/bunkering")
browser.get(url)
for page in range(5):
     s1="https://directories.lloydslist.com/var/recordset/66893/pos/"
     s2="1"
     html = browser.get(s1+str(page)+s2)
     html_source = browser.page_source
    
     soup = bs.BeautifulSoup(html_source, "html.parser")
     f = open('dataa.csv','w',newline = '')
     dataa = csv.writer(f)
     html = urlopen(s1+str(page)+s2)
     bsobj = bs.BeautifulSoup(html.read())
     tbody = bsobj('table',{'class':'tf-66903'})[0].findAll('tr')
     xl = []
     for row in tbody:
      cols = row.findChildren(recursive = False)
      cols = [element.text.strip() for element in cols]
      dataa.writerow(cols) 
      xl.append(cols)
import pandas as pd
df = pd.DataFrame(data = xl[1:],columns = xl[0])
df.to_excel('dataa.xlsx', index=False,header = False)#Writing to Excel file

