from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

from selenium.webdriver.ie.webdriver import DEFAULT_HOST

options = Options()
options.add_argument("--disable.infobars")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.chileautos.cl/vehiculos/autos-veh%C3%ADculo/')

time.sleep(3)

# Buscar datos 

lista_precios = driver.find_elements_by_tag_name('ul li a div div')

print("Listaokk")

time.sleep(2)

autos_lista = []

for auto in lista_precios:
    autos_lista.append(auto.text)
    # autos_lista.append()

driver.quit()

# Pandas (Crear data frame, guardar lista en archivo csv)
df = pd.DataFrame({'Autos usados - Oxl':autos_lista})
print(df)
df.to_csv('Autos usados Oxl.csv', index=False)
