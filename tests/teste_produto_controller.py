"""
Claudinei de Oliveira - pt-BR, UTF-8 - 15-08-2024
Manipulando o banco de dados sqlite3 
# test_produto_controller.py
"""

from flask_testing import TestCase
from app import create_app, db
from models.produto_model import Produto
from controllers.produto_controller import produto_blueprint

class TestProdutoController(TestCase):

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

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_novo_get(self):
        response = self.client.get('/novo')
        self.assertEqual(response.status_code, 200)

    def test_novo_post(self):
        response = self.client.post('/novo', data={'descricao': 'Produto Teste', 'preco': 10.0})
        self.assertEqual(response.status_code, 302)  # Esperando redirecionamento após POST

    def test_atualiza_route(self):
        # Primeiro adicionamos um produto para depois tentar atualizar
        produto = Produto(descricao='Produto Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        response = self.client.get(f'/atualiza/{produto.id}/0')
        self.assertEqual(response.status_code, 302)  # Redirecionamento após atualizar

    def test_deleta_route(self):
        # Primeiro adicionamos um produto para depois tentar deletar
        produto = Produto(descricao='Produto Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        response = self.client.get(f'/deleta/{produto.id}')
        self.assertEqual(response.status_code, 302)  # Redirecionamento após deletar

if __name__ == '__main__':
    import unittest
    unittest.main()
