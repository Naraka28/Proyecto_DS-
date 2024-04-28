from flask import Flask, render_template, url_for
from funciones import carga_csv, crea_diccionario_revistas_por_cada_titulo, Diccionario_Revistas_Por_Cada_Palabra


archivo = 'revistas.csv'
app = Flask(__name__)
catalogo = carga_csv(archivo)
diccionario_revistas = crea_diccionario_revistas_por_cada_titulo(catalogo)
diccionario_revistas = Diccionario_Revistas_Por_Cada_Palabra(catalogo) # ahi vemos cual usar


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/explorar")
def explorar():
    return render_template("explorar.html")


@app.route("/revista/<id>")
def revista(id):
    if id in diccionario_revistas:
        revista=diccionario_revistas[id]
        return render_template("revista.html", revista=revista)

    return render_template("revista.html", id=id)

if __name__ == '__main__':
    app.run(debug=True)
