import time
from selenium import webdriver


def bot():
    timer = 30
    link = "https://www.tiktok.com/@saifgati/video/6893121535469440262"
    views = 25
    driver = webdriver.Chrome()
    driver.get(link)
    driver1 = webdriver.Chrome()
    driver1.get(link)
    for i in range(views):
        time.sleep(timer)
        driver.refresh()
        driver1.refresh()
        print(i)
    driver1.close()
    driver.close()


def alsoc():
    print("bot implanted")
