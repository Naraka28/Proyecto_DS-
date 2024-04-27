import csv
from datetime import datetime
from Revista import Revista


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

def Diccionario_Revistas_Por_Cada_Palabra(lista_Revista:list[Revista])->dict:
    diccionario={}
    for revista in lista_Revista:
        revista=dict(revista)
        titulo=revista["titulo"]
        splitteado=titulo.split()
        for i in range(len(splitteado)):
            if splitteado[i] in diccionario:
                diccionario[splitteado[i]].append(revista)
            else:
                diccionario[splitteado[i]]=[revista]
    return diccionario


def Buscar_Revista(diccionario:dict, palabra:str)->list:
    if palabra in diccionario:
       print("\n Revistas encontradas: ")
       for revista in diccionario[palabra]:
           print(f"{revista}")
   #no esta terminada


if __name__ == '__main__':
    archivo = 'revistas.csv'
    catalogo = carga_csv(archivo)
    diccionario_revistas=Diccionario_Revistas_Por_Cada_Palabra(catalogo)
    diccionario_revistas_titulos=crea_diccionario_revistas_por_cada_titulo(catalogo)

    for k,v in diccionario_revistas.items():
        print(f"{k} : {v}")
        print("\n")