from models.produto_model import Produto
from services.database import db


class ProdutoDAO:
    @staticmethod
    def get_produtos() -> list[Produto]:
        """Retorna todos os produtos."""
        return db.session.query(Produto).all()

    @staticmethod
    def get_produto(id):
        pass

    @staticmethod
    def salvar(produto):
        pass

    @staticmethod
    def atualizar(produto):
        pass

    @staticmethod
    def deletar(id):
        pass
