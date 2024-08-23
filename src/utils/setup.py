import os

# Importação das bibliotecas e módulos necessários
from flask import Flask

# Importação da instância do SQLAlchemy criada em database.py
from src.services.database import db
from src.views.root_view import root_blueprint


def create_tables(app: Flask) -> None:
    """Função para criar as tabelas no banco de dados"""
    with app.app_context():  # Cria um contexto para o aplicativo Flask
        db.create_all()  # Cria todas as tabelas no banco de dados
        print('Tabelas criadas com sucesso!')


def create_app() -> Flask:
    """Função para criar uma instância do aplicativo Flask"""

    app = Flask(
        __name__,
        template_folder=os.path.abspath('templates'),
        static_folder=os.path.abspath('static'),
        instance_path=os.path.abspath(os.path.join('src', 'dao')),
    )
    """Cria a instância do aplicativo Flask."""

    app.register_blueprint(root_blueprint)

    # Junta o caminho de forma portátil
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # Adiciona uma chave secreta para permitir flash messages
    app.secret_key = 'seu segredo'

    db.init_app(app)  # Inicializa o SQLAlchemy com o aplicativo Flask

    create_tables(app)  # Cria as tabelas no banco de dados se necessário

    return app
