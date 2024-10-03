import requests
from bs4 import BeautifulSoup

# URL de la página que quieres scrapear
url = 'https://dudjob.com'

# Hacemos la petición a la página
response = requests.get(url)

# Verificamos que la petición sea exitosa
if response.status_code == 200:
    # Parseamos el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Buscamos la etiqueta <title> y obtenemos su texto
    title = soup.find('title').text
    
    # Mostramos el título en la consola
    print('Título de la página:', title)
else:
    print('Error al hacer la petición, código de estado:', response.status_code)
