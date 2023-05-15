import bs4 as bs
from selenium import webdriver 
import pandas as pd
from csv import reader
import re
import requests

browser = webdriver.Firefox()

with open('Activejobs.txt', 'w') as f:
	with open('Ship Agents.csv', 'r') as client:
		with open('Services.csv', 'r') as service:
			service_reader = reader(service)
			client_reader = reader(client)
			for rows in client_reader:
				url = (rows[4])
				response = requests.get('http://'+url)
				if response.status_code == 200:
					print( 'http://',url)
					browser.get('http://'+url)
					html_source = browser.page_source
					soup = bs.BeautifulSoup(html_source, "html.parser")
					#found= None
					for row in service_reader:
						count=0
						for col in row:
							my_regex =re.compile('^'+row[count]+'$')
							count += 1
							print(my_regex)
							found = soup.body.findAll(text=re.compile(my_regex))
							for found in found:
								f.write(rows[0])
								f.write(','.join(row))
								#f.write(',')
								f.write('\n')
				else:
					print("doesnt exist")				


