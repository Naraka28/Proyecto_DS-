from flask import Flask, render_template, url_for
from funciones import carga_csv, crea_diccionario_revistas_por_cada_titulo, Diccionario_Revistas_Por_Cada_Palabra, crea_diccionario_alfabetico


archivo = 'revistas.csv'
app = Flask(__name__)
catalogo = carga_csv(archivo)
diccionario_revistas_titulo = crea_diccionario_revistas_por_cada_titulo(catalogo)
diccionario_revistas = Diccionario_Revistas_Por_Cada_Palabra(catalogo) # ahi vemos cual usar
abcdario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
dicc_letras = crea_diccionario_alfabetico(catalogo)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/explorar")
def explorar():
    return render_template("explorar.html", lista_abcdario=abcdario)

@app.route("/explorar/<letra>")
def explorar_letra(letra:str):
    if letra in dicc_letras:
        revistas = dicc_letras[letra]
        return render_template("explorar_letra.html", letra=letra, list_revistas=revistas)
    return render_template("explorar_letra.html", letra=letra)


@app.route("/revista/<id>")
def revista(id):
    if id in diccionario_revistas_titulo:
        revista = diccionario_revistas_titulo[id]
        return render_template("revista.html", revista=revista)

    return render_template("revista.html", id=id)

if __name__ == '__main__':
    app.run(debug=True)
