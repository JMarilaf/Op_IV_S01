from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import datetime

browser = webdriver.Firefox()
browser.get('https://www.chileautos.cl/vehiculos/')

hora = '{:%Y_%b_%d_%H_%M_%S}'.format(datetime.datetime.now())

#Crear dataframe vacío con índice
df = pd.DataFrame(columns = ['Año', 'Modelo', 'Precio', 'Kms', 'Transmision', 't_combustible', 'Href'])
i = 0

for i in range(84):

    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'body > div.listing > div.container.listing-container > div.row.flex-nowrap.no-gutters > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > nav > ul > li:nth-child(7) > a')))

    elem_list = browser.find_elements(By.CSS_SELECTOR, "div.card-body")

    for auto in elem_list:

        try:
            t_combustible = (auto.find_element(By.TAG_NAME, 'div.col > ul > li:nth-child(3)').text)
            years = (auto.find_element(By.TAG_NAME, 'h3 > a').text[0:4])
            modelos = (auto.find_element(By.TAG_NAME, 'h3 > a').text[5:])
            precios = (auto.find_element(By.CLASS_NAME, 'price > a').text)
            kms = (auto.find_element(By.TAG_NAME, 'div.col > ul > li:nth-child(1)').text)
            transmision = (auto.find_element(By.TAG_NAME, 'div.col > ul > li:nth-child(2)').text) 
            href = (auto.find_element(By.CLASS_NAME, 'price > a').get_attribute('href'))

            df = df.append({ 'Año': years,
                'Modelo': modelos,
                'Precio': precios,
                'Kms': kms,
                'Transmision': transmision,
                't_combustible': t_combustible,
                'Href': href
              }, ignore_index=True )

        except:
            i = i + 1
    

    browser.find_element(By.CSS_SELECTOR, 'body > div.listing > div.container.listing-container > div.row.flex-nowrap.no-gutters > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > nav > ul > li:nth-child(7) > a').click()

browser.quit()

df.to_csv(f'ChileAutos-{hora}.csv')

print('Autos que no cumple con datos mínimos: ' + str(i) )

print('\nFinalizado.')
