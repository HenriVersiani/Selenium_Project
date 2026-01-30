import pandas as pd
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

url = 'https://books.toscrape.com/'

driver.get(url)

livros = driver.find_elements(By.TAG_NAME, 'a')[54:94:2] #pega 20 elementos de livro, que sao aqueles na minha pagina;
listagemStock = []

def pegarDataLivro():
   
   titulo = WebDriverWait(driver, 10).until(
   EC.presence_of_element_located((By.TAG_NAME, 'h1'))
    ).text 

   preco = WebDriverWait(driver, 10).until(
   EC.presence_of_element_located((By.CLASS_NAME, 'price_color'))
    ).text # melhor ultilizar um regex

   return {"nome": titulo, "preco": preco}


for livro in livros:
   
   livro.click() 
   response = pegarDataLivro()

   listagemStock.append(response)
   
   driver.back()

print(listagemStock)