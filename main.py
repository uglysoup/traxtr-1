import requests
import datetime
import csv
from bs4 import BeautifulSoup
from proxyreq import *

proxy = choice(get_working_proxies())
product_url = input("Enter the url")
headers = {"user agent":"Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"}
page = requests.get(url=product_url, headers=headers)
soup = BeautifulSoup(page.content,'lxml')
#print(soup.prettify())
title = soup.find(class_ = 'pdp-e-i-head')
text = title.get_text()
title = text.strip()
#print(title )
price = soup.find(class_ = 'payBlkBig')
price = price.get_text()
price = price.strip() 
#print(price )
current_time = datetime.datetime.now()
#price_timestamp = price + current_time
#with open("output.txt", "a") as f:
#    print(price_timestamp, file=f)
filename = "data_chart.csv"
fields = ['title','price','timeStamp', 'link' ]
rows = [title,price, current_time,product_url]
with open(filename, 'a') as csvfile:
    csvwrite = csv.writer(csvfile)
    #csvwrite.writerow(fields)
    csvwrite.writerow(rows)

