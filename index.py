from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def principal():
    #return 'hola al aprimera sfthsfhgpagina'
    return render_template('/principal.html')

@app.route('/otrapagina')
def otrapagina():
    #return 'hola soy la segunda pagina'
    return render_template('/otrapagina.html')

@app.route('/terceraPag')
def terceraPag():
    #return 'hola soy la tercera pagina'
    return render_template('/tercerPag.html')

@app.route('/layout')
def layout():
    #return 'hola soy la tercera pagina'
    return render_template('/layout.html')


if __name__ == "__main__":
    app.run(port=5000, debug=True)