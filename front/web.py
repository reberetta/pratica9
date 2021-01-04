import sys  
sys.path.append('back')


from flask import Flask, render_template, request

from marketplace import add_new_marketplace
from produto.produto import Produto



app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

titulo_app = 'Pratica 9'

@app.route('/')
def index():
    marketplaces = {'nome': 'Cadastrar novo marketplace', 'rota': '/addmkp'}
    produtos = {'nome': 'Cadastrar novo produto', 'rota': '/produto'}
    lista = [marketplaces, produtos]
    return render_template('index.html', nome=titulo_app, lista=lista)

@app.route('/addmkp')
def addmkp():  

    return render_template('addmkp.html', nome=titulo_app)

@app.route('/sucesso')
def sucesso():  

    mkp = request.args.get('mkp')
    mkp_desc = request.args.get('mkp_desc')
    add_new_marketplace(mkp, mkp_desc)


    return f'Sucesso' 

@app.route('/produto')
def cadastrar_produto():
    p = Produto()
    nome = request.args.get('nome')
    desc = request.args.get('descricao')
    preco = request.args.get('preco')
    if nome != None:
        p.cadastrar_produto(nome, desc, preco)
    return render_template('produto.html')


app.run(debug=True)
