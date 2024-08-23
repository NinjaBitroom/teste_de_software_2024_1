import os
import unittest
from flask import Flask
from flask_testing import TestCase
from src.models.produto_model import ProdutoModel
from src.services.database import db


class TestProdutoModel(TestCase):
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
        app.secret_key = 'test'
        db.init_app(app)
        return app

    def setUp(self):
        self.app = self.create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_produto(self):
        produto = ProdutoModel(descricao='Teste 1', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        self.assertEqual(ProdutoModel.query.count(), 1)

    def test_update_produto(self):
        produto = ProdutoModel(descricao='Teste 2', preco=10.0)
        db.session.add(produto)
        db.session.commit()

        produto.descricao = 'Teste Atualizado'
        produto.preco = 20.0
        db.session.commit()

        produto_atualizado = db.session.get(ProdutoModel, produto.id)
        self.assertEqual(produto_atualizado.descricao, 'Teste Atualizado')
        self.assertEqual(produto_atualizado.preco, 20.0)

    def test_delete_produto(self):
        produto = ProdutoModel(descricao='Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()

        db.session.delete(produto)
        db.session.commit()

        produto_deletado = db.session.get(ProdutoModel, produto.id)
        self.assertIsNone(produto_deletado)

    def test_get_all_produtos(self):
        produto1 = ProdutoModel(descricao='Teste 1', preco=10.0)
        produto2 = ProdutoModel(descricao='Teste 2', preco=20.0)
        db.session.add(produto1)
        db.session.add(produto2)
        db.session.commit()

        todos_produtos = ProdutoModel.query.all()
        self.assertEqual(len(todos_produtos), 2)
        self.assertEqual(todos_produtos[0].descricao, 'Teste 1')
        self.assertEqual(todos_produtos[1].descricao, 'Teste 2')


if __name__ == '__main__':
    unittest.main()
