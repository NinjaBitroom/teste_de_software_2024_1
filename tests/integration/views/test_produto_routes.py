"""
Claudinei de Oliveira - pt-BR, UTF-8 - 15-08-2024
Manipulando o banco de dados sqlite3 
# test_produto_controller.py
"""
import os

from flask import Flask
from flask_testing import TestCase

from src.models.produto_model import ProdutoModel
from src.services.database import db
from src.utils.setup import create_tables
from src.views.root_view import root_blueprint
from tests.mixins.flask_app_mixin import FlaskAppMixin


class TestProdutoRoutes(FlaskAppMixin, TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        app = Flask(
            __name__,
            template_folder=os.path.abspath('templates'),
            static_folder=os.path.abspath('static')
        )
        app.config['SQLALCHEMY_DATABASE_URI'] = self.SQLALCHEMY_DATABASE_URI
        app.config['TESTING'] = self.TESTING
        app.register_blueprint(root_blueprint)
        app.secret_key = 'test'
        db.init_app(app)
        return app

    def setUp(self):
        create_tables(self.app)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_novo_get(self):
        response = self.client.get('/produto/novo')
        self.assertEqual(response.status_code, 200)

    def test_novo_post(self):
        response = self.client.post(
            '/produto/novo', data={'descricao': 'Produto Teste', 'preco': 10.0}
        )
        self.assertEqual(
            response.status_code, 302
        )  # Esperando redirecionamento após POST

    def test_atualiza_route(self):
        # Primeiro adicionamos um produto para depois tentar atualizar
        produto = ProdutoModel(descricao='Produto Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        response = self.client.post(f'/produto/editar/{produto.id}')
        self.assertEqual(
            response.status_code, 302
        )  # Redirecionamento após atualizar

    def test_deleta_route(self):
        # Primeiro adicionamos um produto para depois tentar deletar
        produto = ProdutoModel(descricao='Produto Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        response = self.client.post(f'/produto/deletar/{produto.id}')
        self.assertEqual(
            response.status_code, 302
        )  # Redirecionamento após deletar
