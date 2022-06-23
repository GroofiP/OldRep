import undetected_chromedriver as uc
import time

from pymongo import MongoClient
from selenium.webdriver.common.by import By

URL = "https://onlyfinder.com/new-free/profiles/"

driver = uc.Chrome()

driver.get(URL)
time.sleep(10)

client = MongoClient("127.0.0.1", 27017)["girls"]

girls = client.girls


while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    if driver.current_url == "https://onlyfinder.com/new-free/profiles/960/":
        break
time.sleep(10)
items = driver.find_elements(By.XPATH, "//div[@class='result']")

with open("text.txt", "w", encoding="utf-8") as string:
    for i in items:
        url = i.find_element(By.XPATH, ".//a").get_attribute("href")
        _id = url.split("/")[-1]
        string.writelines(f"\n{url}")

time.sleep(5)
