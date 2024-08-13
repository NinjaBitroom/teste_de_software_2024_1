from dao.produto_dao import ProdutoDAO
from models.produto_model import Produto


class ProdutoController:

    @classmethod
    def get_produtos(cls) -> list[Produto]:
        return ProdutoDAO.get_produtos()
