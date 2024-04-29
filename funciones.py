import csv
from datetime import datetime
from Revista import Revista
import re

def carga_csv(nombre_archivo:str)->list:
    '''
    Carga archivo csv y regresa una lista 
    '''
    lista = []
    with open(nombre_archivo,'r',encoding="utf-8") as archivo:
        lista = list(csv.DictReader(archivo))
    return lista

def crea_diccionario_revistas_por_cada_titulo(lista_revistas:list)->dict:
    ''' Crea diccionario de revistas a partir de 
        la lista de revistas
        {"id_revista" ={dict_revista}}
    '''
    d = {}
    for revista in lista_revistas:
        key = revista["titulo"]
        d[key] = revista # key,value
    return d

def crea_diccionario_alfabetico(lista_revistas:list)->dict:
    d = {}
    for revista in lista_revistas:
        letra = revista["titulo"][0].upper()
        if letra in d:
            d[letra].append(revista)
        else:
            d[letra] = [revista]
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
    return d

def Diccionario_Revistas_Por_Cada_Palabra(lista_Revista:list[Revista])->dict:
    diccionario={}
    for revista in lista_Revista:
        revista=dict(revista)
        titulo=revista["titulo"]
        splitteado=titulo.split()
        for palabra in splitteado: 
            palabra_limpia = re.sub(r'[^a-zA-Z0-9]', '', palabra).lower()
            if palabra_limpia != "":
                if palabra_limpia in diccionario:
                    diccionario[palabra_limpia].append(revista)
                else:
                    diccionario[palabra_limpia]=[revista]
    return diccionario

def crear_diccionario_por_pais(lista_Revista)->dict:
    d={}
    for revista in lista_Revista:
        pais=revista["pais"]
        if pais in d:
            d[pais].append(revista)
        else:
            d[pais]=[revista]
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
    return d


def Buscar_Revista(diccionario:dict, palabra:str)->list:
    lista=[]
    if palabra in diccionario:
       print("\n Revistas encontradas: ")
       for revista in diccionario[palabra]:
            print(f"{revista}")
            lista.append(revista)
    return lista

def unir_diccionarios(dict_letras:dict, dict_palabras:dict)->dict:
    # buscamos que los diccionarios de palabras esten dentro de las keys de cada letra
    d={}	
    for k,v in dict_palabras.items():
        letra=k[0].upper()
        if letra in dict_letras:
            if letra not in d:
                d[letra]=[v]
            else:
                d[letra].append(v)
    d={k: v for k, v in sorted(d.items(), key=lambda item: item[0])}
    return d #nos devuelve un diccionario de listas de diccionarios :P


if __name__ == '__main__':
    archivo = 'revistas.csv'
    catalogo = carga_csv(archivo)
    diccionario_revistas=Diccionario_Revistas_Por_Cada_Palabra(catalogo)
    for k,v in diccionario_revistas.items():
        print(f"{k}\n:{v}\n")
       
    diccionario_revistas_titulos=crea_diccionario_revistas_por_cada_titulo(catalogo)
    diccionario_pais=crear_diccionario_por_pais(catalogo)
    diccionario_alfabetico=crea_diccionario_alfabetico(catalogo) #los values del diccionario son listas de revistas
    for k,v in diccionario_alfabetico.items():
        print(f"{k}\n:{v}\n")
    dict_unido=unir_diccionarios(diccionario_alfabetico,diccionario_revistas)
