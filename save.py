import bs4 as bs
from selenium import webdriver 
import pandas as pd

with open('456.txt', 'w') as f:
 #with open('sitebunker.txt', 'w') as b:

  
  browser = webdriver.Firefox()
  url = ("https://directories.lloydslist.com/services-browse/sscompid//country//ss/5693/oas/bunkering")
  browser.get(url)
  for page in range (279):
     s1="https://directories.lloydslist.com/var/recordset/66893/pos/"
     s2="1"
     browser.get(s1+str(page)+s2)
     html_source = browser.page_source
  
     soup = bs.BeautifulSoup(html_source, "html.parser")
  
     
     for tr in soup.find_all('tr'):
       #country = soup.findAll('p', attrs={'class' : 'ss_country sectionhead'})
       #f.write("\n")
       #f.write("^^")
       #f.write(country[0].text)
       #f.write("^^")
       #f.write("\n")
       comp = tr.findAll('p', attrs={'class' : 'ss_cname'})
       f.write("\n")
       f.write("#")
       f.write(comp[0].text)
       texts = tr.findAll('p', attrs={'class' : 'ss_text'})
       f.write("#")
       f.write(texts[0])
       site = tr.findAll('p', attrs={'class' : 'ss_url'})
       f.write("#")
       f.write(site[0].text)

##mails = [mail.get_text(strip=True) for mail in soup.select('a[href^=mailto]')]
##     f.write("#")
##     f.write(mail[0])
##texta = soup.findAll('p', attrs={'class' : 'ss_text'})
##textq = [textq.get_text(strip=True) for textq in soup.select(".ss_text")]
        #f.write("")
        #tds = tr.find_all('td')
        #f.write(tds[0].text)
        #f.write("\n\n")
        

     


        #f.write("")
        #tds = tr.find_all('td')
        #f.write(tds[0].text)
        #f.write("\n\n")

 ##for link in soup.select(): 
          #                      
           #b.write(str(link.get('a'))) 
            #b.write(",")
 #for td in soup.find_all('td'):
  

 #if tds.text in c.read():
  #          f.write("\n")
 #print('Classes of each table:')
 #for table in soup.find_all('table'):
     #print(table.get('class'))
