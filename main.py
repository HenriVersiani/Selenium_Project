import pandas as pd
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://books.toscrape.com/'

driver.get(url)

elementsA = driver.find_elements(By.TAG_NAME, 'a')[0]

print("elementsA: ",elementsA)