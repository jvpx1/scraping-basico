from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import os

drive = webdriver.Chrome()

try:

    drive.get('https://www.gogocloset.com.br/masculino-plus')



    wait = WebDriverWait(drive, 15)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h3[contains(@class, 'product-name')]")))


    nome_produtos = drive.find_elements(By.XPATH, "//h3[contains(@class, 'product-name')]")

    valor_produtos = drive.find_elements(By.XPATH, "//span[contains(@class, 'price-pix')]")

    for nome_produtos, valor_produtos in zip(nome_produtos, valor_produtos):
        with open('precos.csv', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"{nome_produtos.text},{valor_produtos.text}{os.linesep}")
            
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    # Fecha o navegador no final, independente de erro ou sucesso
    drive.quit()








