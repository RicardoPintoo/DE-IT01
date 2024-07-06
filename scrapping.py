import requests
from bs4 import BeautifulSoup

url = 'https://www.domusbasto.com/imoveis/'  # Replace with the URL you want to scrape

params = {
    'bus': 1,  #'Venda'
    'gnt': 3,  #'Terrenos'
    'defaulttxt': 'Localidade',
    'pss': 'BasicPropertySearchFormU0X',
    'pag': 1
}

# GET request
response = requests.get(url, params=params)

soup = BeautifulSoup(response.content, 'html.parser')
properties = soup.find(id='PROPERTIES_LIST')
print(properties.find_all(class_="fieldValue"))

