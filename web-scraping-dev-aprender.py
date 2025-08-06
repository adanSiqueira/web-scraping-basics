from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

try:
    driver = webdriver.Chrome()
    driver.get('https://devaprender-play.netlify.app/')
    sleep(5)

    # alternativa para sleep(5):
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//h3[@class='text-lg font-semibold text-gray-900 group-hover:text-indigo-600']"))
        # )

    produtos = driver.find_elements(By.XPATH, "//h3[@class='text-lg font-semibold text-gray-900 group-hover:text-indigo-600']")
    precos = driver.find_elements(By.XPATH, "//p[@class='text-2xl font-bold text-indigo-600']")

    for produto, preco in zip(produtos, precos):
        with open('precos.csv', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{produto.text}, {preco.text}{os.linesep}')
    # alternativa com csv
    # import csv

    # with open('precos.csv', 'a', newline='', encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([produto.text, preco.text])
    pass

finally:
    driver.quit()