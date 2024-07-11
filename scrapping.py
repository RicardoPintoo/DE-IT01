import requests
from bs4 import BeautifulSoup

url = 'https://www.domusbasto.com' 

page = 1

params = {
    'bus': 1,  #'Venda'
    'gnt': 3,  #'Terrenos'
    'defaulttxt': 'Localidade',
    'pss': 'BasicPropertySearchFormU0X',
    'pag': page
}

# GET request
response = requests.get(url + '/imoveis/', params=params)

soup = BeautifulSoup(response.content, 'html.parser')
properties = soup.find(id='PROPERTIES_LIST')

pagination =  soup.find(class_ = 'pagination')

while pagination:

    # Update the page number in params
    params['pag'] = page

    #print(params)

    # GET request
    response = requests.get(url + '/imoveis/', params=params)

    soup = BeautifulSoup(response.content, 'html.parser')
    properties = soup.find(id='PROPERTIES_LIST')

    details_list = properties.find_all('span', id='details')

    for details in details_list:
        terreno_response = requests.get(url + details.a['href'])
        soup_terreno = BeautifulSoup(terreno_response.content, 'html.parser')
        price = soup_terreno.find('span', class_='value notranslate')
        print(price.text)

        detailRow_district = soup_terreno.find(class_='detailRow distrito')
        district = detailRow_district.find(class_='value').text
        print(district)

        detailRow_freguesia = soup_terreno.find(class_='detailRow freguesia')
        freguesia = detailRow_freguesia.find(class_='value').text
        print(freguesia)

        detailRow_referencia = soup_terreno.find(class_='detailRow referencia')
        referencia = detailRow_referencia.find(class_='value').text
        print(referencia)

        if soup_terreno.find(class_='detailRow areadoterreno'):
            detailRow_area = soup_terreno.find(class_='detailRow areadoterreno')
            area = detailRow_area.find(class_='value').text
            if "ha" in area:
                area = area.replace("ha", "").replace(",", ".")
                area = float(area)
                area = area * 10000
                print(str(area) + ' m²')
                continue
            print(area)
        else :
            print('None')
        
        print( " *********** ******* ********** ")

    # Next page
    page += 1
    pagination =  soup.find(class_ = 'pagination')
    

