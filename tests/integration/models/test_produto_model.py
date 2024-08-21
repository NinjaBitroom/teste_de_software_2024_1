"""
Claudinei de Oliveira - pt-BR, UTF-8 - 11-04-2024
Manipulando o banco de dados sqlite3 
test_models.py
"""
import os

from flask import Flask
from flask_testing import TestCase

from src.controllers.produto_controller import ProdutoController
from src.dao.flask_sqlalchemy_dao import FlaskSQLAlchemyDAO
from src.models.produto_model import ProdutoModel
from src.services.database import db
from src.utils.setup import create_tables


class TestProdutoModel(TestCase):
    __produto_dao = FlaskSQLAlchemyDAO(ProdutoModel)
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        """Configurações do aplicativo para testes."""
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
        """Será chamado antes de cada teste.

        Configura o banco de dados para testes."""
        create_tables(self.app)

    def tearDown(self):
        """Será chamado após cada teste.

        Limpa o banco de dados após os testes."""
        db.session.remove()
        db.drop_all()

    def test_create_produto(self):
        """Teste: criar produto."""
        produto = ProdutoModel(descricao='Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        self.assertEqual(ProdutoModel.query.count(), 1)

    def test_get_produto(self):
        """Teste: obter um produto."""
        produto = ProdutoModel(descricao='Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        produto_query = ProdutoController.get_produto(produto.id)
        self.assertEqual(produto_query.id, produto.id)

    def test_update_produto(self):
        """Teste: atualizar produto."""
        produto = ProdutoModel(descricao='Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        produto.descricao = 'Teste Atualizado'
        produto.preco = 20.0
        self.__produto_dao.update()
        produto_atualizado = db.session.query(ProdutoModel).get(produto.id)

        self.assertEqual(produto_atualizado.descricao, 'Teste Atualizado')
        self.assertEqual(produto_atualizado.preco, 20.0)

    def test_delete_produto(self):
        """Teste: deletar produto."""
        produto = ProdutoModel(descricao='Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        self.__produto_dao.delete_one(produto)
        produto_deletado = db.session.query(ProdutoModel).get(produto.id)
        self.assertIsNone(produto_deletado)

    def test_get_all_produtos(self):
        """Teste: obter todos os produtos."""
        produto1 = ProdutoModel(descricao='Teste 1', preco=10.0)
        produto2 = ProdutoModel(descricao='Teste 2', preco=20.0)
        db.session.add(produto1)
        db.session.add(produto2)
        db.session.commit()
        todos_produtos = ProdutoController.get_produtos()
        self.assertEqual(len(todos_produtos), 2)


"""
from flask_testing import TestCase
from app import create_app, db  
# importa create_app e db do seu arquivo wsgi.py
from models.produto_model import Produto  
# importa a classe Produto


class TestProdutoModel(TestCase):

    def create_app(self):
        # Configurações do app para testes
        app = create_app()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        return app

     # Será chamado antes de cada teste
    def setUp(self):
        # Configura o banco de dados para testes
        db.create_all()

    # Será chamado após cada teste
    def tearDown(self):
        # Limpa o banco de dados após os testes
        db.session.remove()
        db.drop_all()
    
    def test_create_produto(self):
        produto = Produto(descricao='Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        self.assertEqual(Produto.query.count(), 1)

    def test_get_produto(self):
        produto = Produto(descricao='Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        produto_query = Produto.get_produto(produto.id)
        self.assertEqual(produto_query.id, produto.id)

    def test_update_produto(self):
        # Adiciona um produto, depois atualiza
        produto = Produto(descricao='Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        
        # Atualiza o produto
        produto.descricao = 'Teste Atualizado'
        produto.preco = 20.0
        produto.atualizar()

        # Busca o produto atualizado para verificar se as alterações foram salvas
        produto_atualizado = Produto.query.get(produto.id)
        self.assertEqual(produto_atualizado.descricao, 'Teste Atualizado')
        self.assertEqual(produto_atualizado.preco, 20.0)

    def test_delete_produto(self):
        # Adiciona um produto e depois o deleta
        produto = Produto(descricao='Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        
        # Deleta o produto
        produto.deletar()
        
        # Verifica se o produto foi deletado
        produto_deletado = Produto.query.get(produto.id)
        self.assertIsNone(produto_deletado)

    def test_get_all_produtos(self):
        # Adiciona alguns produtos
        produto1 = Produto(descricao='Teste 1', preco=10.0)
        produto2 = Produto(descricao='Teste 2', preco=20.0)
        db.session.add(produto1)
        db.session.add(produto2)
        db.session.commit()

        # Pega todos os produtos e verifica se todos estão lá
        todos_produtos = Produto.get_produtos()
        self.assertEqual(len(todos_produtos), 2)


if __name__ == '__main__':
    from flask_testing import LiveServerTestCase
    import unittest
    unittest.main()
"""
