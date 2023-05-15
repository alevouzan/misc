import bs4 as bs
from selenium import webdriver 
#import pandas as pd
import requests



with open('ServProv2.txt', 'w', encoding="utf-8") as f:

	#browser = webdriver.Firefox()
	
	for page in range (1,447):
		s1="https://www.infomarine.gr/world-directory/search-in-directory/all/page"
		s2=".html"
		response = requests.get(s1+str(page)+s2)
		html_source=response.text
		soup = bs.BeautifulSoup(html_source, "html.parser")
		rows = soup.findAll('div', {'class':'listing-summary'})
		for row in rows:
			if row.find_all('div' , {'class':'header'}):
				provname = row.find_all('span', {'itemprop' : 'name'})
				for p in provname:
					f.write(p.get_text())

				f.write("#!#")

			if row.find_all('p', {'class' : 'address'}):
				address=row.find_all('p', {'class' : 'address'})
				if address:
					for a in address:
						f.write(a.get_text())
			else:
				f.write('No Address')		
				
				f.write("#!#")

			if row.find_all('div', {'class' : 'category'}):
				category=row.find_all('div', {'class' : 'category'})
				if category:
					for c in category:
						children = c.findChildren("a" , recursive=False)
						if children:
							for ca in children:
								f.write(c.get_text())
			else:
				f.write('No category')

			f.write("#!#")        

			f.write("\n")





					#browser.get(s1+str(page)+s2)
		#html_source = browser.page_source