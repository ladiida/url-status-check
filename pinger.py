# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 13:41:39 2019

@author: TXJ
"""


import requests
import csv
import time
#import urllib3
#http = urllib3.PoolManager()	

f = open("urls.txt", "r")

with open('urlstats.csv', mode='w', newline='') as urlstats:
    url_writer = csv.writer(urlstats, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    url_writer.writerow(['URL', 'HTTP Status'])


for url in f:
    url = url.replace("\n","")
    print(url)
   # resp = http.request('GET', url)
    
    try:
        r = requests.head(url)
        print(r.status_code)
    except requests.ConnectionError:
        print("failed to connect")
   
   
    with open('urlstats.csv', mode='a', newline='') as urlstats:
        url_writer = csv.writer(urlstats, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        url_writer.writerow([url, r.status_code])
    time.sleep(.1)
    


