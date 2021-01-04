from flask import Flask, render_template, request
import sys
sys.path.append('back')
from produto.produto import Produto


class Main:
    
    
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('index.html')
        
    @app.route('/produto')
    def cadastrar_produto():
        p = Produto()
        nome = request.args.get('nome')
        desc = request.args.get('descricao')
        preco = request.args.get('preco')
        p.cadastrar_produto(nome, desc, preco)
        return render_template('produto.html')
    
    app.run(debug=True) 