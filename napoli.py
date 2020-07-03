import requests
from bs4 import BeautifulSoup
import csv
import time

store_name = []
store_address = []

token_url ="https://www.0800076666.com.tw/Stores/StoresLocation"

rs = requests.session()

res = rs.get(token_url)

token_html = res.text

#print(token_html)

soup = BeautifulSoup(token_html, "html.parser")
token =  soup.select('input')[0].get('value')

areas =["N", "M", "S", "E"]

for area in areas:

	form_data = {
		'__RequestVerificationToken':token,
	'country': '',
	'town': '',
	'Info.StoreArea': area,
	'Info.StoreCity': '',
	'Info.StoreTown': '',
	'page': '1',
	'sortCol': '',
	'sortDesc': 'false',
	}

	url = "https://www.0800076666.com.tw/Stores/StoresLocation"

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

with open('shop_list_0800076666.csv', 'w', newline='',  encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    newrow = ['門市名稱', '門市地址']
    csvwriter.writerow(newrow)
    for n in range(0, len(store_name)):
        newrow.clear()
        newrow.append(store_name[n])
        newrow.append(store_address[n])
        csvwriter.writerow(newrow)