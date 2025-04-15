""""
Scraping a una Pagina web con Python & beautifulsoup
"""""

import requests
from bs4 import BeautifulSoup
#import pandas as pd 
from urllib.parse import urljoin


url = ("https://medias.do/")


# Hacer la solicitud GET a la URL
soli = requests.get(url)
# Verificar el estado de la solicitud
soup = BeautifulSoup(soli.text, 'html.parser')

#print(soup.prettify())

#extraer el titulo de la pagina 
titulo = soup.title.string
print("el titulo de la pagina es:", titulo)
    


# Buscar productos y precios

productos = soup.find_all('h2', class_='woocommerce-loop-product__title')
precios = soup.find_all('span',class_='price')
imagenes = soup.find_all('img' , class_='attachment-woocommerce_thumbnail')
link=soup.find_all('a' , class_='woocommerce-LoopProduct-link')

print("\nPRODUCTOS Y PRECIOS ENCONTRADOS CON SUS LINK:")

# para interactuar con los productos y precios

#zip sirve para recorer varias listas al  mismo tiempo
for producto, precio, imagenes, link in zip(productos, precios, imagenes,link):
    producto_texto = producto.text.strip()
    precio_texto = precio.text.strip()
    img_url=imagenes.get('src')
    link_url=link.get('href')
   
   # F la utilizamos para poner variables dentro del teto
    print(f"\n producto: {producto_texto}")
    print(f"precio: {precio_texto}")
    print(f"imagen: {img_url}")
    print(f"link directo: {link_url}")
    print( )

#For el for se utiliza para recorer varias listas un por uno
#find all se utiliza para obtener el contenido de una pagina
link=soup.find_all('a' , class_='link')
for link in link:
    print(link.get('href'))
   