import pandas as pd

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

url = 'https://books.toscrape.com/'

driver.get(url)

listagemStock = []

paginaAtual = 0 # logicazinha pra poder escolher a quantidade de paginas q a gnt quer passar
numeroPaginas = 5

def pegarDataLivro():
   
   titulo = WebDriverWait(driver, 10).until(
   EC.presence_of_element_located((By.TAG_NAME, 'h1'))
    ).text 

   preco = WebDriverWait(driver, 10).until(
   EC.presence_of_element_located((By.CLASS_NAME, 'price_color'))
    ).text # melhor ultilizar um regex

   return {"nome": titulo, "preco": preco}

while numeroPaginas > paginaAtual:

   livros = driver.find_elements(By.TAG_NAME, 'a')[54:94:2] #pega 20 elementos de livro, que sao aqueles na minha pagina;

   for livro in livros:

      livro.click() 
      response = pegarDataLivro()

      listagemStock.append(response)
      driver.back()

   paginaAtual += 1

   try:
      botaoProximaPg = driver.find_element(By.CSS_SELECTOR, 'li.next a') #pega o botao para pular a pagina
      botaoProximaPg.click()

      WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
               (By.CSS_SELECTOR, 'article.product_pod')
            )
      )
      
   except NoSuchElementException:
      break

df = pd.DataFrame(listagemStock)
df.to_csv("livros.csv", index=False, sep=';', encoding="utf-8")
print(listagemStock)