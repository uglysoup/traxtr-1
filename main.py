import requests
import datetime
import csv
import random
from login import *
from bs4 import BeautifulSoup
from proxyreq import *

user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64; rv:     99.0) Gecko/20100101 Firefox/99.0',
]
for i in range(1,4):
    user_agent = random.choice(user_agent_list)
proxy = choice(get_working_proxies())
product_url = input("Enter the url")
headers = {"user agent":user_agent}
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

