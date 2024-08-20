"""
Claudinei de Oliveira - pt-BR, UTF-8 - 15-08-2024
Manipulando o banco de dados sqlite3 
test_IndexHtml.py
"""

from app import create_app, db
from flask_testing import TestCase

from controllers.produto_controller import produto_blueprint
from models.produto_model import ProdutoModel


class TestIntegration(TestCase):

    def create_app(self):
        app = create_app()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        app.register_blueprint(produto_blueprint)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index_page_with_products(self):
        # Criando produtos de teste
        produto1 = ProdutoModel(descricao='Produto A', preco=50.0, status=True)
        produto2 = ProdutoModel(
            descricao='Produto B', preco=100.0, status=False
        )
        db.session.add(produto1)
        db.session.add(produto2)
        db.session.commit()

        response = self.client.get(url_for('produto.index'))
        self.assert200(response)
        self.assertIn(b'Produto A', response.data)
        self.assertIn(b'Produto B', response.data)
        self.assertIn(b'Ativo', response.data)
        self.assertIn(b'Inativo', response.data)

    def test_index_page_without_products(self):
        response = self.client.get(url_for('produto.index'))
        self.assert200(response)
        self.assertIn(
            'Ainda não existem produtos cadastrados...', response.data
        )


if __name__ == '__main__':
    import unittest

    unittest.main()
