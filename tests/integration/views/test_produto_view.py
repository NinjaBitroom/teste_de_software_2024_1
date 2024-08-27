"""
Claudinei de Oliveira - pt-BR, UTF-8 - 15-08-2024
Manipulando o banco de dados sqlite3 
test_produto_view.py
"""

from flask import url_for
from flask_testing import TestCase

from src.models.produto_model import ProdutoModel
from src.services.database import db
from tests.mixins.flask_app_mixin import FlaskAppMixin


class TestProdutoView(FlaskAppMixin, TestCase):
    def test_index_page_with_products(self):
        # Criando produtos de teste
        produto1 = ProdutoModel(descricao='Produto A', preco=50.0, status=True)
        produto2 = ProdutoModel(
            descricao='Produto B', preco=100.0, status=False
        )
        db.session.add(produto1)
        db.session.add(produto2)
        db.session.commit()

        response = self.client.get(url_for('root.produto.index'))
        self.assert200(response)
        self.assertIn('Produto A'.encode(), response.data)
        self.assertIn('Produto B'.encode(), response.data)
        self.assertIn('Ativo'.encode(), response.data)
        self.assertIn('Desativado'.encode(), response.data)

    def test_index_page_without_products(self):
        response = self.client.get(url_for('root.produto.index'))
        self.assert200(response)
        self.assertIn(
            'Ainda não existem produtos cadastrados...'.encode(), response.data
        )

    def test_integration_novo_to_index(self):
        # Testa a criação de um novo produto e verifica se ele aparece na index
        self.client.post(
            '/produto/novo',
            data={'descricao': 'Produto Integrado', 'preco': 20.0}
        )
        response = self.client.get('/produto/')
        self.assertIn(b'Produto Integrado', response.data)

    def test_integration_deleta_to_index(self):
        # Testa a deleção de um produto e verifica se ele foi removido da index
        produto = ProdutoModel(descricao='Produto para Deletar', preco=30.0)
        db.session.add(produto)
        db.session.commit()
        self.client.get(f'/produto/deletar/{produto.id}')
        response = self.client.get('/produto')
        self.assertNotIn(b'Produto para Deletar', response.data)
