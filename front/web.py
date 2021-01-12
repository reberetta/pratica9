import sys  
sys.path.append('.')

from flask import Flask, render_template, request, redirect, url_for
from back.controllers.marketplace_controller import create_marketplace, list_marketplaces
from back.controllers.seller_controller import create_seller, list_sellers
from back.controllers.product_controller import create_product, list_products
from back.controllers.category_controller import create_category, list_categories
from back.controllers.log_controller import create_log, list_log


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

titulo_app = 'Pratica 9'

@app.route('/')
def index():
    marketplaces = {'nome': 'Cadastrar novo marketplace', 'rota': '/addmkp'}
    produtos = {'nome': 'Cadastrar novo produto', 'rota': '/produto'}
    listar_marketplaces = {'nome': 'Listar marketplaces', 'rota': '/marketplaces'}
    products = {'nome': 'Listar produtos', 'rota': '/products'}
    create_seller = {'nome': 'Cadastrar novo seller', 'rota': '/new_seller'}
    list_sellers = {'nome': 'Listar sellers', 'rota': '/sellers'}
    categorias = {'nome': 'Cadastrar nova categoria', 'rota': '/cadastro_categoria'}
    listar_categorias = {'nome': 'Listar categorias', 'rota': '/categories'}
    listar_logs = {'nome': 'Listar logs', 'rota': '/logs'}

    lista = [
        marketplaces, 
        listar_marketplaces, 
        produtos, products, 
        create_seller, 
        list_sellers,
        categorias, 
        listar_categorias,
        listar_logs
        ]

    return render_template('index.html', nome=titulo_app, lista=lista)

@app.route('/addmkp')
def addmkp():  

    mkp = request.args.get('mkp')
    mkp_desc = request.args.get('mkp_desc')
    if mkp != None:
        create_marketplace(mkp, mkp_desc)
        return redirect(url_for('sucesso'), code=302)

    return render_template('addmkp.html', nome=titulo_app)

@app.route('/marketplaces')
def marketplaces():  
    result = list_marketplaces()
    return render_template('marketplaces.html', lista = result)


@app.route('/produto')
def cadastro_produto():
    nome = request.args.get('nome')
    desc = request.args.get('descricao')
    preco = request.args.get('preco')
    if nome != None:
        create_product(nome, desc, preco)
        return redirect(url_for('sucesso'), code=302)
        
    return render_template('produto.html')

@app.route('/products')
def products():
    products = list_products()
    return render_template('show_products.html', products = products)

@app.route('/new_seller')
def cadastro_seller():
    name = request.args.get('name')
    email = request.args.get('email')
    telephone = request.args.get('telephone')
    if name != None:
        create_seller(name, email, telephone)
        return redirect(url_for('sucesso'), code=302)
        
    return render_template('add_seller.html')

@app.route('/sellers')
def sellers():
    sellers = list_sellers()
    return render_template('show_sellers.html', sellers = sellers)

@app.route('/cadastro_categoria')
def cadastro_categoria():
    name = request.args.get('name')
    description = request.args.get('description')
    if name != None:
        create_category(name, description)
        return redirect(url_for('sucesso'), code=302)
        
    return render_template('category.html')

@app.route('/categories')
def categories():  
    result = list_categories()
    return render_template('categories.html', lista = result)

@app.route('/logs')
def logs():  
    result = list_log()
    return render_template('logs.html', lista = result)

@app.route('/sucesso')
def sucesso():

    return render_template('sucesso.html')


app.run(debug=True)
