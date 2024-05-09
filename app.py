from flask import Flask, render_template, url_for, redirect
from funciones import carga_csv, crea_diccionario_revistas_por_cada_titulo, Diccionario_Revistas_Por_Cada_Palabra, crea_diccionario_alfabetico, find_keys_containing_substring, explorar_abcedario
from config import Config
from forms import SearchForm


archivo = 'revistas.csv'
app = Flask(__name__)
app.config.from_object(Config)

catalogo = carga_csv(archivo)
diccionario_revistas_titulo = crea_diccionario_revistas_por_cada_titulo(catalogo)
diccionario_revistas = Diccionario_Revistas_Por_Cada_Palabra(catalogo) # ahi vemos cual usar
abcdario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
dicc_letras = explorar_abcedario(diccionario_revistas)



@app.route("/")
def index():
    return render_template("index.html")

#pasar el form al template base.html
@app.context_processor
def base():
    form = SearchForm()
    return dict(form = form,lista_abcdario = abcdario)

@app.route("/search", methods= ['GET', 'POST'])
def search():
    form = SearchForm()
    key = form.search.data
    key = key.lower().strip()
    lista_revistas = find_keys_containing_substring(diccionario_revistas, key)
    if lista_revistas is not None:
        if form.validate_on_submit():
            return render_template('search.html', form = form, lista_revistas = lista_revistas, key = key)
    return redirect(url_for('index'))


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/explorar")
def explorar():
    return render_template("explorar.html")

@app.route("/explorar/<letra>")
def explorar_letra(letra:str):
    if letra in dicc_letras:
        revistas = dicc_letras[letra]
        return render_template("explorar_letra.html", letra=letra, dic_revistas=revistas)
    return render_template("explorar_letra.html", letra=letra)

@app.route("/explorar/<letra>/<palabra>")
def explorar_palabra(letra:str,palabra:str):
    for dic in dicc_letras[letra]:
        if palabra in dic:
            revistas = dic[palabra]
            return render_template("explorar_palabras.html", palabra = palabra, list_revistas=revistas)
    return render_template("error.html", palabra = palabra)

@app.route("/revista/<id>")
def revista(id):
    if id in diccionario_revistas_titulo:
        revista = diccionario_revistas_titulo[id]
        area_dict=eval(revista['area'])
        bandera=revista['pais'].split(",")[1]
        bandera=f"https://www.scimagojr.com/{bandera}"
        
        return render_template("revista.html", revista=revista, area_dict=area_dict, bandera = bandera)

    return render_template("revista.html", id=id)

if __name__ == '__main__':
    app.run(debug=True)
