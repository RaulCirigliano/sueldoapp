import os
from flask import Flask, render_template

# Configuración de Flask
# Es una buena práctica definir explícitamente las carpetas de plantillas y archivos estáticos,
# aunque Flask las busca por defecto si usas la estructura estándar.
app = Flask(__name__, template_folder='.', static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def index():
    """Sirve la página principal de la aplicación."""
    # Como todo el procesamiento ocurre en el navegador, solo necesitamos servir el HTML.
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
