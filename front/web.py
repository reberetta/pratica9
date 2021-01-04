import sys  
sys.path.append('pratica9/')


from flask import Flask, render_template, request

from back.marketplace import add_new_marketplace



app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

titulo_app = 'Pratica 9'

@app.route('/')
def index():
    marketplaces = {'nome': 'Cadastrar novo marketplace', 'rota': '/addmkp'}
    produtos = {'nome': 'Cadastrar novo produto', 'rota': '/addprdt'}
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


app.run(debug=True)
