from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

drive = webdriver.Chrome()
drive.get('https://www.gogocloset.com.br/masculino-plus')
time.sleep(5)

nome_produtos = drive.find_elements(By.XPATH, "//h3[@class='product-name text-black font-semibold text-[0.938em] -tracking-[0.4px] uppercase text-center leading-[1.2em] min-h-[30px] max-md:text-[0.8125em]'] ")

valor_produtos = drive.find_elements(By.XPATH, "//span[@class='text-[1.125em] font-semibold price-pix text-[#2DBDAF]']")

for nome_produtos, valor_produtos in zip(nome_produtos, valor_produtos):
    with open('precos.csv', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{nome_produtos.text},{valor_produtos.text}{os.linesep}")


input('')







