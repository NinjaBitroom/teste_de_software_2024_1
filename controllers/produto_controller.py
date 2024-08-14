from dao.produto_dao import ProdutoDAO
from models.produto_model import Produto
from utils.produto_validator import ProdutoValidator


class ProdutoController:

    @classmethod
    def get_produto(cls, id_) -> Produto | None:
        return ProdutoDAO.get_produto(id_)

    @classmethod
    def get_produtos(cls) -> list[Produto]:
        return ProdutoDAO.get_produtos()

    @classmethod
    def create_produto(
        cls, descricao: str | None, preco: str | None
    ) -> tuple[str, ...]:
        errors: list[str] = []
        converted_preco = ProdutoValidator.valida_preco(preco)

        if isinstance(converted_preco, ValueError):
            for msg in converted_preco.args:
                errors.append(str(msg))
        else:
            new_produto = Produto(descricao=descricao, preco=converted_preco)
            ProdutoDAO.salvar(new_produto)

        return tuple(errors)

    @classmethod
    def update_produto(
        cls, id_: int, descricao: str | None, preco: str | None,
        status: str | None
    ) -> Produto | ValueError:
        produto = ProdutoDAO.get_produto(id_)
        converted_preco: float | ValueError | None = None

        if preco is not None:
            converted_preco = ProdutoValidator.valida_preco(preco)

        if isinstance(converted_preco, ValueError):
            return converted_preco

        if descricao is not None:
            produto.descricao = descricao

        if converted_preco is not None:
            produto.preco = converted_preco

        if status is not None:
            produto.status = True if status == 'True' else False

        ProdutoDAO.atualizar()

        return produto

    @classmethod
    def delete_produto(cls, id_: int) -> None:
        produto = ProdutoDAO.get_produto(id_)
        ProdutoDAO.deletar(produto)
