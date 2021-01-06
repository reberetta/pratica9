import sys  
sys.path.append('back')


from flask import Flask, render_template, request, redirect, url_for
from marketplace import add_new_marketplace, list_marketplaces
from produto.produto import Produto



app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

titulo_app = 'Pratica 9'

@app.route('/')
def index():
    marketplaces = {'nome': 'Cadastrar novo marketplace', 'rota': '/addmkp'}
    produtos = {'nome': 'Cadastrar novo produto', 'rota': '/produto'}
    listar_marketplaces = {'nome': 'Listar marketplaces', 'rota': '/marketplaces'}
    lista = [marketplaces, listar_marketplaces, produtos]
    return render_template('index.html', nome=titulo_app, lista=lista)

@app.route('/addmkp')
def addmkp():  

    mkp = request.args.get('mkp')
    mkp_desc = request.args.get('mkp_desc')
    if mkp != None:
        add_new_marketplace(mkp, mkp_desc)
        return redirect(url_for('sucesso'), code=302)

    return render_template('addmkp.html', nome=titulo_app)

@app.route('/marketplaces')
def marketplaces():  
    result = list_marketplaces()
    return render_template('marketplaces.html', nome=titulo_app, lista = result)

@app.route('/produto')
def cadastrar_produto():
    p = Produto()
    nome = request.args.get('nome')
    desc = request.args.get('descricao')
    preco = request.args.get('preco')
    if nome != None:
        p.cadastrar_produto(nome, desc, preco)
        return redirect(url_for('sucesso'), code=302)
        
    return render_template('produto.html')

@app.route('/sucesso')
def sucesso():

    return render_template('sucesso.html')


app.run(debug=True)
