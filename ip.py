import json
import urllib.request

import ipinfo
from selenium import webdriver

import time


def location():
    timer = 10000
    driver = webdriver.Chrome()
    for i in range(20):
        with urllib.request.urlopen("https://geolocation-db.com/json") as url:
            data = json.loads(url.read().decode())
            print(data)
            IPv4 = data['IPv4']
            details = ipinfo.handler.Details(IPv4)
            print(details.loc)
        time.sleep(timer)
        driver.refresh()
        print(i)
    driver.close()
