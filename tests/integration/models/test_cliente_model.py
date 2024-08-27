"""
Claudinei de Oliveira - pt-BR, UTF-8 - 15-08-2024
Manipulando o banco de dados sqlite3 
# test_models.py
"""

from flask_testing import TestCase

from src.dao.flask_sqlalchemy_dao import FlaskSQLAlchemyDAO
from src.models.cliente_model import ClienteModel
from src.services.database import db
from tests.mixins.flask_app_mixin import FlaskAppMixin


class TestClienteModel(FlaskAppMixin, TestCase):
    __cliente_dao = FlaskSQLAlchemyDAO(ClienteModel)
    FAKE_DATA = {
        'nome': 'Valid Value',
        'cpf': '00000000000',
        'logradouro': 'Valid Value',
        'numero': 123,
        'complemento': 'Valid Value',
        'bairro': 'Valid Value',
        'cep': '00000-000',
        'cidade': 'Valid Value',
        'uf': 'VV',
        'telefone': '00000000000',
        'email': 'valid_value@mail.test',
    }

    def test_create_cliente(self):
        """Teste: criar produto."""
        produto = ClienteModel(**self.FAKE_DATA)
        db.session.add(produto)
        db.session.commit()
        self.assertEqual(ClienteModel.query.count(), 1)

    def test_get_cliente(self):
        """Teste: obter um produto."""
        produto = ClienteModel(**self.FAKE_DATA)
        db.session.add(produto)
        db.session.commit()
        produto_query = self.__cliente_dao.get_one(produto.id)
        self.assertEqual(produto_query.id, produto.id)

    def test_update_cliente(self):
        """Teste: atualizar produto."""
        produto = ClienteModel(**self.FAKE_DATA)
        db.session.add(produto)
        db.session.commit()
        produto.descricao = 'Teste Atualizado'
        produto.preco = 20.0
        self.__cliente_dao.update()
        produto_atualizado = db.session.query(ClienteModel).get(produto.id)

        self.assertEqual(produto_atualizado.descricao, 'Teste Atualizado')
        self.assertEqual(produto_atualizado.preco, 20.0)

    def test_delete_cliente(self):
        """Teste: deletar produto."""
        produto = ClienteModel(**self.FAKE_DATA)
        db.session.add(produto)
        db.session.commit()
        self.__cliente_dao.delete_one(produto)
        produto_deletado = db.session.query(ClienteModel).get(produto.id)
        self.assertIsNone(produto_deletado)

    def test_get_all_cliente(self):
        """Teste: obter todos os produtos."""
        fake_data_1 = self.FAKE_DATA.copy()
        fake_data_2 = self.FAKE_DATA.copy()
        fake_data_1['nome'] = 'Teste 1'
        fake_data_2['nome'] = 'Teste 2'
        fake_data_1['cpf'] = 'Teste 01'
        fake_data_2['cpf'] = 'Teste 02'
        produto1 = ClienteModel(**fake_data_1)
        produto2 = ClienteModel(**fake_data_2)
        db.session.add(produto1)
        db.session.add(produto2)
        db.session.commit()
        todos_produtos = self.__cliente_dao.get_all()
        self.assertEqual(len(todos_produtos), 2)


"""
from flask_testing import TestCase
from app import create_app, db  
# importa create_app e db do seu arquivo app.py
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
