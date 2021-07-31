from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/Users/bernardolorenzini/Documents/Python_Projects/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://lorenzinibernardo.wixsite.com/bezini")
print(driver.title)

search_portifolio = driver.find_element_by_id("DrpDwnMn02label")
search_portifolio.click()

try:
    poa_cena = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "iawexb4a"))
    )
    poa_cena.click()
    try:
        poa_cenaTrabalhos = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "PAGES_CONTAINER"))
        )
        try:
            main = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "Containerez0sx"))
            )
            titulos = main.find_elements_by_tag_name("span")
            for titulo in titulos:
                print(titulo.text)
        finally:
            time.sleep(5)
    finally:
        time.sleep(5)
finally:
    time.sleep(5)
    driver.quit()



'''
search_contato = driver.find_element_by_id("DrpDwnMn03label")
search_contato.click()

search_nome = driver.find_element_by_id("input_comp-kemp07a71")
search_email = driver.find_element_by_id("input_comp-kemp07af2")
search_tel = driver.find_element_by_id("input_comp-kemp07ah1")
search_msg = driver.find_element_by_id("textarea_comp-kemp07aj")

search_nome.send_keys("Alberto Lorenzini")
search_email.send_keys("alberto.lorenzini@gmail.com")
search_tel.send_keys("55984455207")
search_msg.send_keys("ESSE e UM TESTEEEEEEEEEE")

search_botao = driver.find_element_by_id("comp-kemp07ap4")
search_botao.click()
'''


time.sleep(5)
driver.quit()