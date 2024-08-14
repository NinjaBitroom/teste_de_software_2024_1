"""
Claudinei de Oliveira - pt-BR, UTF-8 - 11-04-2024
Manipulando o banco de dados sqlite3 
test_models.py
"""

from flask_testing import TestCase

from controllers.produto_controller import ProdutoController
from dao.produto_dao import ProdutoDAO
from models.produto_model import Produto
from services.database import db
from wsgi import create_app


class TestProdutoModel(TestCase):

    def create_app(self):
        """Configurações do aplicativo para testes."""
        app = create_app()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        return app

    def setUp(self):
        """Será chamado antes de cada teste.

        Configura o banco de dados para testes."""
        db.create_all()

    def tearDown(self):
        """Será chamado após cada teste.

        Limpa o banco de dados após os testes."""
        db.session.remove()
        db.drop_all()

    def test_create_produto(self):
        """Teste: criar produto."""
        produto = Produto(descricao='Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        self.assertEqual(Produto.query.count(), 1)

    def test_get_produto(self):
        """Teste: obter um produto."""
        produto = Produto(descricao='Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        produto_query = ProdutoController.get_produto(produto.id)
        self.assertEqual(produto_query.id, produto.id)

    def test_update_produto(self):
        """Teste: atualizar produto."""
        produto = Produto(descricao='Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        produto.descricao = 'Teste Atualizado'
        produto.preco = 20.0
        ProdutoDAO.atualizar()
        produto_atualizado = db.session.query(Produto).get(produto.id)

        self.assertEqual(produto_atualizado.descricao, 'Teste Atualizado')
        self.assertEqual(produto_atualizado.preco, 20.0)

    def test_delete_produto(self):
        """Teste: deletar produto."""
        produto = Produto(descricao='Teste', preco=10.0)
        db.session.add(produto)
        db.session.commit()
        ProdutoDAO.deletar(produto)
        produto_deletado = db.session.query(Produto).get(produto.id)
        self.assertIsNone(produto_deletado)

    def test_get_all_produtos(self):
        """Teste: obter todos os produtos."""
        produto1 = Produto(descricao='Teste 1', preco=10.0)
        produto2 = Produto(descricao='Teste 2', preco=20.0)
        db.session.add(produto1)
        db.session.add(produto2)
        db.session.commit()
        todos_produtos = ProdutoController.get_produtos()
        self.assertEqual(len(todos_produtos), 2)


if __name__ == '__main__':
    import unittest

    unittest.main()

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
