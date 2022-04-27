from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import datetime

browser = webdriver.Firefox()
browser.get('https://www.chileautos.cl/vehiculos/')

stamp = '{:%Y_%b_%d_%H_%M_%S}'.format(datetime.datetime.now())

years = []
modelos = []
precios = []
kms = []
transmision = []
t_combustible = []
href = []

for i in range(20):

    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'body > div.listing > div.container.listing-container > div.row.flex-nowrap.no-gutters > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > nav > ul > li:nth-child(7) > a')))
    print("Pagina " +str(i))

    elem_list = browser.find_elements(By.CSS_SELECTOR, "div.card-body")

    for auto in elem_list:

        try:
            t_combustible.append(auto.find_element(By.TAG_NAME, 'div.col > ul > li:nth-child(3)').text)
            years.append(auto.find_element(By.TAG_NAME, 'h3 > a').text[0:4])
            modelos.append(auto.find_element(By.TAG_NAME, 'h3 > a').text[5:])
            precios.append(auto.find_element(By.CLASS_NAME, 'price > a').text)
            kms.append(auto.find_element(By.TAG_NAME, 'div.col > ul > li:nth-child(1)').text)
            transmision.append(auto.find_element(By.TAG_NAME, 'div.col > ul > li:nth-child(2)').text) 
            href.append(auto.find_element(By.CLASS_NAME, 'price > a').get_attribute('href'))

            # print("Año: " +title[0:4])
            # print("Modelo: " +title[5:])
            # print("Precio: " +precio)
            # print("Kilometraje: " +kms)
            # print("Transmisión: " +transmision)
            # print("Tipo Combustible: " +t_combustible)
            # print("Link: " +href)

        except:
            print("\n_____________________________\n")
            print("Auto no cumple con todos los datos.")
    

    browser.find_element(By.CSS_SELECTOR, 'body > div.listing > div.container.listing-container > div.row.flex-nowrap.no-gutters > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > nav > ul > li:nth-child(7) > a').click()

browser.quit()

df = pd.DataFrame()
df['Año'] = years
print(df)
df['Marca'] = modelos
print(df)
df['Precios'] = precios
print(df)
df['Kilometraje'] = kms
print(df)
df['Transmisión'] = transmision
print(df)
df['Tipo_combustible'] = t_combustible
print(df)
df['Link'] = href
print(df)

df.to_csv(f'ChileAutos-{stamp}.csv')

# df = pd.DataFrame({'Autos en ChileAutos':autos_lista})
# df.to_csv('ChileAutos.csv', index=False) 

# print(df)
