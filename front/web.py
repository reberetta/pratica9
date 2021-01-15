import sys  
sys.path.append('.')

from flask import Flask, render_template, request, redirect, url_for
from back.controllers.category_controller import CategoryController
from back.controllers.log_controller import LogController
from back.controllers.marketplace_controller import MarketplaceController
from back.controllers.seller_controller import SellerController
from back.controllers.product_controller import ProductController

from back.models.category import Category
from back.models.log import Log
from back.models.marketplace import Marketplace
from back.models.product import Product
from back.models.seller import Seller


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

titulo_app = 'Prática 9'


@app.route('/')
def index():
    marketplaces = {'nome': 'Cadastrar novo marketplace', 'rota': '/marketplace/create'}
    produtos = {'nome': 'Cadastrar novo produto', 'rota': '/product/create'}
    listar_marketplaces = {'nome': 'Listar marketplaces', 'rota': '/marketplace/read'}
    products = {'nome': 'Listar produtos', 'rota': '/product/read'}
    create_seller = {'nome': 'Cadastrar novo seller', 'rota': '/seller/create'}
    list_sellers = {'nome': 'Listar sellers', 'rota': '/seller/read'}
    categorias = {'nome': 'Cadastrar nova categoria', 'rota': '/category/create'}
    listar_categorias = {'nome': 'Listar categorias', 'rota': '/category/read'}
    listar_logs = {'nome': 'Listar logs', 'rota': '/log/read'}

    lista = [
        marketplaces, 
        listar_marketplaces, 
        produtos, products, 
        create_seller, 
        list_sellers,
        categorias, 
        listar_categorias,
        listar_logs]
    return render_template('index.html', nome=titulo_app, lista=lista)


@app.route('/category/create')
def create_category():
    name = request.args.get('name')
    description = request.args.get('description')
    if name != None:
        category = Category(name, description)
        CategoryController().create(category)
        return redirect(url_for('sucesso'), code=302)
    return render_template('create_category.html')

@app.route('/category/read')
def read_categories():  
    result = CategoryController().read_all()
    return render_template('read_categories.html', lista = result)

@app.route("/category/<id_>/update")
def update_category(id_):
    if request.args:
        name = request.args.get('name')
        description = request.args.get('description')
  
        category = Category(nome=name, descricao=description, id_=id_)
        print(category.id_)
        CategoryController().update(category)
    
        return redirect("/")
    else:
        category = CategoryController().read_by_id(id_)
        return render_template("edit_category.html", category = category)
        print(category.id_)
        
@app.route("/category/<id_>/delete")
def delete_category(id_):
    CategoryController().delete(id_)
    return redirect("/")
    

@app.route('/log/read')
def read_logs():  
    result = LogController().read_all()
    return render_template('read_logs.html', lista = result)


@app.route('/marketplace/create')
def create_marketplace():  
    name = request.args.get('name')
    description = request.args.get('description')
    if name != None:
        marketplace = Marketplace(nome=name, descricao=description)
        MarketplaceController().create(marketplace)
        return redirect(url_for('sucesso'), code=302)
    return render_template('create_marketplace.html')

@app.route('/marketplace/read')
def read_marketplaces():  
    result = MarketplaceController().read_all()
    return render_template('read_marketplaces.html', lista = result)


@app.route("/marketplace/<id_>/update")
def update_marketplace(id_):
    if request.args:
        name = request.args.get('name')
        description = request.args.get('description')
        marketplace = Marketplace(nome=name, descricao=description, id_=id_)
        
        MarketplaceController().update(marketplace)
        return redirect("/")
    else:
        marketplace = MarketplaceController().read_by_id(id_)
        return render_template("edit_marketplace.html", marketplace=marketplace)
        
@app.route("/marketplace/<id_>/delete")
def delete_marketplace(id_):
    MarketplaceController().delete(id_)
    return redirect("/")


@app.route('/product/create')
def create_product():
    nome = request.args.get('nome')
    desc = request.args.get('descricao')
    preco = request.args.get('preco')
    if nome != None:
        product = Product(nome=nome, descricao=desc, preco=preco)
        ProductController().create(product)
        return redirect(url_for('sucesso'), code=302)
    return render_template('create_product.html')

@app.route('/product/read')
def read_products():
    products = ProductController().read_all()
    return render_template('read_products.html', products = products)

@app.route("/product/<id_>/update")
def update_product(id_):
    if request.args:
        name = request.args.get('name')
        description = request.args.get('description')
        preco = requests.args.get('preco')
        product = Product(nome=name, descricao=description, preco=preco, id_=id_)
        ProductController().update(product)
        return redirect("/")
    else:
        product = ProductController().read_by_id(id_)
        return render_template("edit_product.html", product=product)

@app.route("/product/<id_>/delete")
def delete_product(id_):
    ProductController().delete(id_)
    return redirect("/")


@app.route('/seller/create')
def create_seller():
    name = request.args.get('name')
    email = request.args.get('email')
    telephone = request.args.get('telephone')
    seller = Seller(nome=name, email=email, telefone=telephone)
    if name != None:
        SellerController().create(seller)
        return redirect(url_for('sucesso'), code=302)
    
    return render_template('create_seller.html')


@app.route('/seller/read')
def read_sellers():
    sellers = SellerController().read_all()
    return render_template('read_sellers.html', sellers = sellers)


@app.route("/seller/<id_>/delete")
def delete_seller(id_):
    SellerController().delete(id_)
    return redirect("/")

@app.route("/seller/<id_>/update")
def update_seller(id_):
    if request.args:
        name = request.args.get('name')
        email = request.args.get('email')
        telefone = request.args.get('telefone')
        seller = Seller(nome=name, email=email, telefone=telefone, id_=id_)
        
        SellerController().update(seller)
        return redirect("/")
    else:
        seller = SellerController().read_by_id(id_)
        print(seller.telefone)
        return render_template("edit_seller.html", seller=seller)


@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')


app.run(debug=True)
