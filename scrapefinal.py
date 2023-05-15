import bs4 as bs
from selenium import webdriver 
import pandas as pd


with open('Shipbuilders_Repairers.txt', 'w') as f:

    browser = webdriver.Firefox()
    url = ("https://directories.lloydslist.com/services-browse/sscompid//country//ss/5692/oas/ship_builders/repairers")
    browser.get(url)
    for page in range (1154):
        
        s1="https://directories.lloydslist.com/var/recordset/66893/pos/"
        s2="1"
        browser.get(s1+str(page)+s2)
        html_source = browser.page_source
    
        soup = bs.BeautifulSoup(html_source, "html.parser")
        
        rows = soup.findAll('table', {'class':'tf-66903'})[1].find('tbody').findAll('tr')
        
        
        for row in rows:
            
            if row.find_all('p' , {'class':'ss_cname'}):
                cname = row.find_all('p', {'class' : 'ss_cname'})
                for cname1 in cname:
                    f.write(cname1.get_text())
                    f.write("#!#")      
            if row.find_all('p', {'class' : 'ss_text'}):
                sstext=row.find_all('p', {'class' : 'ss_text'})
                for text1 in sstext:
                    f.write(text1.get_text())
                    f.write("#!#")
            if row.find_all('p', {'class' : 'ss_url'}):
                ssurl=row.find_all('p', {'class' : 'ss_url'})
                for curl in ssurl:    
                    f.write(curl.get_text())
                    f.write("#!#")
                f.write("\n")
            
      


         #working  # sstext=row.findAll('p', {'class' : 'ss_text'})
        #working   # ssurl=row.find('p', {'class' : 'ss_url'})
        #working   # f.write(str(company_list))
        #working   # f.write(str(texts_list))
        #working   # f.write(str(website_list))
       #working    # f.write("\n")
    #df=pd.DataFrame(lldata)
    #df.to_excel('lldata.xlsx', index=False)
                           

        #dic = {}
        #    #dic['Country']= row.find_all('p', attrs={'class' : 'ss_country sectionhead'})
        #    dic['Company']=row.find_all('p', attrs={'class' : 'ss_cname'})
        #    dic['texts']=row.find_all('p', attrs={'class' : 'ss_text'})
        #    dic['website']=row.find_all('p', attrs={'class' : 'ss_url'})
        #    lldata.append(dic)

        #for tr in soup.find_all('td'):
        #    country = tr.find('p', attrs={'class' : 'ss_country sectionhead'})
        #    country = tr.find('p', attrs={'class' : 'ss_country sectionhead'})
        #    f.write("#")
        #    f.write(str(country))
        #    comp= td.findAll('p', attrs={'class' : 'ss_cname'})
        #    f.write("#")
        #    f.write(str(comp))
        #    texts = tr.find_all('p', attrs={'class' : 'ss_text'})
        #    f.write("#")
        #    f.write(str(texts))
        #    site = tr.find_all('p', attrs={'class' : 'ss_url'})
        #    f.write("#")
        #    f.write(str(site))
        #    f.write("\n")
