from flask_testing import TestCase

from src.models.produto_model import ProdutoModel
from src.services.database import db
from tests.mixins.flask_app_mixin import FlaskAppMixin


class TestProdutoModel(FlaskAppMixin, TestCase):
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
