""" Claudinei de Oliveira - pt-BR - 19-06-2023
Adaptado de Giridhar, 2016
O arquivo main.py arquivo principal 
"""

# Importação das bibliotecas e módulos necessários
from flask import Flask, render_template, request, redirect, url_for, flash

from controllers.cliente_controller import cliente_blueprint
from controllers.produto_controller import produto_blueprint
from database import db  # Importação da instância do SQLAlchemy criada em database.py
import os


# Função para criar uma instância do aplicativo Flask
def create_app():
    app = Flask(__name__)  # Cria a instância do aplicativo Flask
    app.register_blueprint(produto_blueprint)
    app.register_blueprint(cliente_blueprint)

    # Configura o URI do banco de dados de maneira portátil
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # captura o diretório absoluto
    # onde o script está sendo executado

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'ifro2024.db')
    # junta o caminho de forma portátil

    app.secret_key = 'seu segredo'  # adiciona uma chave secreta para permitir flash messages
    db.init_app(app)  # Inicializa o SQLAlchemy com o aplicativo Flask
    return app


# Função para criar as tabelas no banco de dados
def create_tables():
    with APP.app_context():  # Cria um contexto para o aplicativo Flask
        db.create_all()  # Cria todas as tabelas no banco de dados
        print('Tabelas criadas com sucesso!')


# Cria a instância do aplicativo Flask e configura o banco de dados
APP = create_app()

# Cria as tabelas no banco de dados se necessário
create_tables()


# Rota principal do aplicativo que exibe todos os produtos
@APP.route('/')
def index():
    return render_template('index.html')  # Renderiza o template novo.html com os produtos
