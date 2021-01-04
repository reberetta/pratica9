from flask import Flask, render_template, request

import sys
sys.path.append('pratica9')

app = Flask(__name__)

titulo_app = 'Marketplaces e Produtos'

@app.route('/')
def index():
    marketplaces = {'nome': 'Cadastrar marketplaces', 'rota': '/marketplaces'}
    produtos = {'nome': 'produtos', 'rota': '/produtos'}
    lista = [marketplaces, produtos]
    return render_template('index.html', nome=titulo_app, lista=lista)

app.run()