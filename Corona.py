# importing modules
import requests
import pandas as pd 
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import csv

# requesting data from website
url = 'https://www.worldometers.info/coronavirus/'
r = requests.get(url)

# parsing it to beautiful soup
data = r.text
soup = BeautifulSoup(data,'html.parser')

live_data1 = soup.find('div',id='maincounter-wrap')
live_data2 = soup.find_all('div',id='maincounter-wrap')[1]
live_data3 = soup.find_all('div',id='maincounter-wrap')[2]
print(live_data1.text)
print(live_data2.text)
print(live_data3.text)

# Extracting table data
table_body = soup.find('tbody')
table_rows = table_body.find_all('tr')

countries = []
cases = []
todays = []
deaths = []

for tr in table_rows:
	td = tr.find_all('td')
	countries.append(td[0].text)
	cases.append(td[1].text)
	todays.append(td[2].text.strip())
	deaths.append(td[3].text.strip())
   
indice = [i for i in range(1,len(countries)+1)]
headers = ['Countries','Total Cases','Todays Cases','Total Deaths']
df = pd.DataFrame(list(zip(countries,cases,todays,deaths)),index=indice,columns=headers)

# Save csv file
df.to_csv('cases.csv')

