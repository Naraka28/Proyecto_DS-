import os
class Revista:
    def __init__(self,titulo:str,catalogo:str,sjr:float,
                 q:str,h_index:str,total_citas:str,url_revista:str,pais:str,area={},publisher="",ISSN="",widget=""):
        self.titulo = titulo
        self.catalogos = catalogo
        #self.catalogos.add(catalogo)
        self.sjr = sjr
        self.q = q
        self.h_index = int(h_index)
        self.total_citas = int(total_citas)
        self.url_revista = url_revista
        self.pais = pais
        self.area=area
        self.publisher=publisher
        self.ISSN=ISSN
        self.widget=widget

    def __str__(self):
        return f'{self.titulo}|{self.catalogos}|{self.sjr}|{self.q}|{self.total_citas}'
    
    def __repr__(self):
        return f'{self.titulo} |{self.catalogos} |{self.sjr}| {self.q} |{self.h_index} |{self.total_citas}|{self.url_revista} | {self.pais} | {self.area} | {self.publisher} | {self.ISSN} | {self.widget}'
    
    def __dict__(self):
        return {'titulo':self.titulo,'catalogo':self.catalogos,'sjr':self.sjr,'q':self.q,'h_index':self.h_index,'total_citas':self.total_citas,'url_revista':self.url_revista,'pais':self.pais,'area':self.area,'publisher':self.publisher,'issn':self.ISSN,'widget':self.widget}

def lee_archivo(archivo:str):
    palabras = []
    with open(archivo,"r",encoding="utf-8") as a:
        data = a.readlines()
    for palabra in data:
        palabra = palabra.strip("\n")
        palabras.append(palabra)
    return palabras

def main():
    urls = lee_archivo('urls.txt')
    print(urls)

if __name__ == '__main__':
    main()

