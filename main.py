import requests
import datetime
import csv
from bs4 import BeautifulSoup
proxies = {
    'http://114.121.248.251:8080',
    'http://222.85.190.32:8090',
    'http://47.107.128.69:888',
    'http://41.65.146.38:8080',
    'http://190.63.184.11:8080',
    'http://45.7.135.34:999',
    'http://141.94.104.25:8080',
    'http://222.74.202.229:8080',
    'http://141.94.106.43:8080',
    'http://191.101.39.96:80'
}
url = 'https://ipecho.net/plain'
for proxy in proxies:
    try:

        # https://ipecho.net/plain returns the ip address
        # of the current session if a GET request is sent.
        page = requests.get(
          url, proxies={"http": proxy, "https": proxy})

        # Prints Proxy server IP address if proxy is alive.
        print("Status OK, Output:", page.text)

    except OSError as e:

        # Proxy returns Connection error
        print(e)
product_url = input("Enter the url")
#product_url = "https://www.snapdeal.com/product/asian-white-mesh-textile-sport/662912850947"
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

