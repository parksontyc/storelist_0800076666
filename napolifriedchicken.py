import requests
from bs4 import BeautifulSoup
import csv
import time

store_name = []
store_address = []

areas =["N", "M", "S"]

for area in areas:

	form_data = {
		'country':'' ,
		'town':'' ,
		'Info.StoreArea': area,
		'Info.StoreCity':'', 
		'Info.StoreTown':'', 
		'page': '1',
		'sortCol':'', 
		'sortDesc': 'false'
		}

	url = "https://www.0800076666.com.tw/Chicken/ChickenStoresLocation"

	res = requests.post(url, data=form_data)

	data_html = res.text

	soup = BeautifulSoup(data_html.replace('\n', '').strip(), 'html.parser')

	items = soup.find_all('table', class_='table bable-stores')

	for item in items:
		name = item.find('td')
		store_name.append(name.text)
		address = item.find('td').find_next_sibling('td')
		store_address.append(address.text)
		print(store_name)
		print(store_address)

with open('shop_list_napalifredchicken.py.csv', 'w', newline='',  encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    newrow = ['門市名稱', '門市地址']
    csvwriter.writerow(newrow)
    for n in range(0, len(store_name)):
        newrow.clear()
        newrow.append(store_name[n])
        newrow.append(store_address[n])
        csvwriter.writerow(newrow)