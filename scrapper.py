from Revista import Revista, lee_archivo
from bs4 import BeautifulSoup
import argparse
import requests
import csv

b_url = 'https://www.scimagojr.com/'
base_url_1902 = 'https://www.scimagojr.com/journalrank.php?category=1902'
base_url_1706 = 'https://www.scimagojr.com/journalrank.php?category=1706'
def scrap(URL:str):
    page=requests.get(URL)
    source = BeautifulSoup(page.content,'html.parser')
    return source

def get_urls(dom,url_list:list)->list:
    i = 0
    url = dom.find('div',class_='pagination_buttons')
    for anchor in url.find_all('a'):
        if i == 1:
            next = anchor['href']
        i+=1
    if next != '#':
        next = f"{b_url}{next}"
        print(next)
        url_list.append(next)
        soup = scrap(next)
        return get_urls(soup, url_list)
    return url_list

#Nota mental, si falla en busqueda agregar un strip
def main2():
    lista = [base_url_1902]
    soup = scrap(base_url_1902)
    urls = get_urls(soup,lista)
    lista_total = []
    print(urls)
    for url in urls:
        soup = scrap(url)
        result = soup.find('tbody')
        lista_revistas = []
        for row in result.find_all('tr'):
            i = 0
            for col in row.find_all('td'):
                if i == 1:
                    url_revista = col.a['href']
                    url_revista = f"{b_url}{url_revista}"
                    titulo = col.text.strip()
                if i == 2:
                    catalogo = col.text
                if i == 3:
                    splitted=col.text.split(" ")
                    if len(splitted)>1:
                        sjr = col.text.split(" ")[0]
                        q = col.text.split(" ")[1]
                    else:
                        sjr = col.text.strip()
                        q = None
                if i == 4:
                    h_index = col.text
                if i == 8:
                    total_citas = col.text
                if i == 12:
                    pais = col.img['title']
                i += 1
            r = Revista(titulo,catalogo,sjr,q,h_index,total_citas,url_revista,pais)
            lista_revistas.append(r)
            break
        lista_total.extend(lista_revistas)
    return lista_total

def scrap_revista(lista: list[Revista],url_base:str):
    for revista in lista:
        url = f"{revista.url_revista}"
        soup = scrap(url)
        result = soup.find('div',class_='journalgrid')
        i = 0
        result=result.find_all('div')
        for div in result:
            if i == 1:
              revista.area = area_and_categories_magazine(div)
            if i == 2:
                revista.publisher = div.p.a.text.strip()
            if i == 5:
                revista.ISSN = div.p.text.strip()
            i+=1
        widget = soup.find('input',id='embed_code')
        revista.widget = widget['value']


#TODO Hacer que devuelva un dict donde key=area y value=categories
def area_and_categories_magazine(div)->str:
    dicc={}
    for ul in div.find_all('ul', style='padding-left:0px'):
        area = ul.li.a.text
        for li in ul.find_all('ul',class_='treecategory'):
            for categoria in li:
                category = categoria.a.text.strip()
                if area in dicc:
                    dicc[area].append(category)
                else:
                    dicc[area]=[category]
    texto = ''
    for area in dicc:
        texto += f"{area}:"
        for category in dicc[area]:
           texto+= f"{category};"
        texto += '+'
         # split en + para separar las areas y luego split en : para separar las areas de las categorias y split en ; para separar las categorias en sí

    print(texto)
    return texto



def hindex_menor(lista: list, index: int):
    return [revista for revista in lista if revista.h_index < index]

def guardar_JSON(lista: list, nombre_archivo: str):
    with open(nombre_archivo, 'w') as file:
        for revista in lista:
            file.write(revista.__str__() + '\n')
def guardar_csv(lista:list[Revista]):
    print('Se esta generando el archivo')
    fields = ['titulo','catalogo','sjr','q','h_index','total_citas','url_revista','pais','area','publisher','issn','widget']
    with open('revistas.csv', 'w', newline='') as archivo:
        csv_writer = csv.DictWriter(archivo,fieldnames=fields)
        csv_writer.writeheader()
        for revista in lista:
            csv_writer.writerow(revista.__dict__())
        print('Successfully wrote :D')



if __name__ == '__main__':
    lista_rev = main2()
    scrap_revista(lista_rev,b_url)

