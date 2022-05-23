from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import datetime
import re

browser = webdriver.Firefox()
browser.get('https://www.chileautos.cl/vehiculos/')

hora = '{:%Y_%b_%d_%H_%M_%S}'.format(datetime.datetime.now())

#Crear dataframe vacío con índice
df = pd.DataFrame(columns = ['Año', 'Marca', 'Modelo', 'Precio', 'Kms', 'Transmision', 't_combustible', 'Rendimiento', 'Href'])

#Numerador
num = 1

#Ciclo debe tener 84 ciclos, ya que el sitio web no soporta más
for i in range(84):

    print('Ciclo numero: ' + str(i))

    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, 'body > div.listing > div.container.listing-container > div.row.flex-nowrap.no-gutters > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > nav > ul > li:nth-child(7) > a')))

    elem_list = browser.find_elements(By.CSS_SELECTOR, "div.card-body")

    for auto in elem_list:

        years = int((auto.find_element(By.TAG_NAME, 'h3 > a').text[0:4]))
        print('Año de vehiculo' + str(years))
        #marca = (auto.find_element(By.TAG_NAME, 'h3 > a').split(' ')[1])
        #print(marca)
        #modelo = (auto.find_element(By.TAG_NAME, 'h3 > a').split()[1]).text
        modelo = (auto.find_element(By.TAG_NAME, 'h3 > a').text[5:])
        marca = modelo.split()[0]
        modelo = modelo.split()[1]
        print('Marca de auto: ' + marca)
        print('Modelo de auto: ' + modelo)
        #version = (auto.find_element(By.TAG_NAME, 'h3 > a')).text
        precio = (auto.find_element(By.CLASS_NAME, 'price > a').text)
        precio = precio.replace('.', '')
        precio = precio.replace('$', '')
        precio = int(precio.replace(' CLP', ''))
        print('Precio encontrado: ' + str(precio))
        href = (auto.find_element(By.CLASS_NAME, 'price > a').get_attribute('href'))

        #Iniciar con variables de lista vacias
        kms = ''
        rendimiento = ''
        transmision = ''
        t_combustible = ''
        
        for a in range(4):
            print('Numero de ciclo li: ' + str(num))
            try:

                aux = auto.find_element(By.TAG_NAME, 'div.col > ul > li:nth-child(' + str(num) + ')').text

                print('Probando formatos: ')
                print(aux)
                print(aux[-2:])
                print(aux[-6:])

                if aux[-2:] == "km":
                    kms = int(aux.replace('.', '').split()[0])
                    print('Kilometraje encontrado: ' + str(kms))

                print('Imprimiendo: ' + aux)

                if aux[-6:] == "Kms/Lt":
                    rendimiento = int(aux.split(' ')[0].replace(',', ''))
                    print('Rendimiento encontrado: ' + str(rendimiento))

                print('Imprimiendo: ' + aux)

                if aux == "Automática" or aux == "Manual":
                    transmision = aux
                    print('Transmision encontrada: ' + transmision)

                print('Imprimiendo: ' + aux)

                if aux == "Bencina" or aux == "Diesel" or aux == "Híbrido":
                    t_combustible = aux
                    print('Tipo de combustible encontrado: ' + t_combustible)

                print('Imprimiendo: ' + aux)
            
            except:
                print("Campo no encontrado.")
            
            num = num + 1

        num = 1    

        print('______________Separador_____________')

        df = df.append({ 'Año': years,
            'Modelo': modelo,
            'Marca': marca,
            'Precio': precio,
            'Kms': kms,
            'Transmision': transmision,
            't_combustible': t_combustible,
            'Rendimiento': rendimiento,
            'Href': href
        }, ignore_index=True )

browser.find_element(By.CSS_SELECTOR, 'body > div.listing > div.container.listing-container > div.row.flex-nowrap.no-gutters > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > nav > ul > li:nth-child(7) > a').click()

browser.quit()

df.to_csv(f'ChileAutos-{hora}.csv')

print('\nFinalizado.')
