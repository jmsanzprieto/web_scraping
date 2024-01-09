# Importamos las librerias necesarias
import requests
from bs4 import BeautifulSoup
import csv

# URL objetivo
url = 'https://www.josemanuelsanz.es'

# Realizar la solicitud HTTP
response = requests.get(url)

# Verificar si la solicitud fue OK (código 200)
if response.status_code == 200:
    # Obtener el contenido HTML 
    html_content = response.text

    # Crear un objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # En este caso, recogemos todos los links <a> de la página objetivo
    links = soup.find_all('a')

    # Crear un archivo CSV para escribir los resultados
    with open('resultados.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Escribir encabezado
        csv_writer.writerow(['Enlace'])  

        # Escribir los enlaces en el archivo CSV
        for link in links:
            csv_writer.writerow([link.get('href')])

    # Mensaje si OK
    print('Análisis completado. Resultados guardados en resultados.csv')
else:

    # Mensaje si KO
    print(f'Error al hacer la solicitud. Código de estado: {response.status_code}')
