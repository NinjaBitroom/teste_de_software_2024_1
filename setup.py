import os

# Importação das bibliotecas e módulos necessários
from flask import Flask

from controllers.cliente_controller import cliente_blueprint
from controllers.produto_controller import produto_blueprint
# Importação da instância do SQLAlchemy criada em database.py
from database import db


def create_app() -> Flask:
    """Função para criar uma instância do aplicativo Flask"""
    app = Flask(__name__)
    """Cria a instância do aplicativo Flask."""

    app.register_blueprint(produto_blueprint)
    app.register_blueprint(cliente_blueprint)

    # Configura o URI do banco de dados de maneira portátil
    base_dir = os.path.abspath(os.path.dirname(__file__))
    """Captura o diretório absoluto onde o script está sendo executado."""

    # Junta o caminho de forma portátil
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
        base_dir, 'db.sqlite3'
    )

    # Adiciona uma chave secreta para permitir flash messages
    app.secret_key = 'seu segredo'
    db.init_app(app)  # Inicializa o SQLAlchemy com o aplicativo Flask
    return app


def create_tables(app: Flask) -> None:
    """Função para criar as tabelas no banco de dados"""
    with app.app_context():  # Cria um contexto para o aplicativo Flask
        db.create_all()  # Cria todas as tabelas no banco de dados
        print('Tabelas criadas com sucesso!')
