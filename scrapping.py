import requests
from bs4 import BeautifulSoup

url = 'https://www.domusbasto.com' 

params = {
    'bus': 1,  #'Venda'
    'gnt': 3,  #'Terrenos'
    'defaulttxt': 'Localidade',
    'pss': 'BasicPropertySearchFormU0X',
    'pag': 1
}

# GET request
response = requests.get(url + '/imoveis/', params=params)

soup = BeautifulSoup(response.content, 'html.parser')
properties = soup.find(id='PROPERTIES_LIST')
#print(properties.find_all(class_="fieldValue"))

details_list = properties.find_all('span', id='details')
# terreno = requests.get(url + details.a['href'])

for details in details_list:
    terreno_response = requests.get(url + details.a['href'])
    soup_terreno = BeautifulSoup(terreno_response.content, 'html.parser')
    price = soup_terreno.find('span', class_='value notranslate')
    print(price.text)
    detailRow = soup_terreno.find(class_='detailRow distrito')
    district = detailRow.find(class_='value').text
    print(district)
    

