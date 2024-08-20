from dao.flask_sqlalchemy_dao import FlaskSQLAlchemyDAO
from models.produto_model import ProdutoModel
from utils.produto_validator import ProdutoValidator


class ProdutoController:
    __produto_dao = FlaskSQLAlchemyDAO(ProdutoModel)

    @classmethod
    def get_produto(cls, id_) -> ProdutoModel | None:
        return cls.__produto_dao.get_one(id_)

    @classmethod
    def get_produtos(cls) -> list[ProdutoModel]:
        return cls.__produto_dao.get_all()

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
            new_produto = ProdutoModel(
                descricao=descricao, preco=converted_preco
            )
            cls.__produto_dao.add_one(new_produto)

        return tuple(errors)

    @classmethod
    def update_produto(
        cls, id_: int, descricao: str | None, preco: str | None,
        status: str | None
    ) -> ProdutoModel | ValueError:
        produto = cls.__produto_dao.get_one(id_)
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

        cls.__produto_dao.update()

        return produto

    @classmethod
    def delete_produto(cls, id_: int) -> None:
        produto = cls.__produto_dao.get_one(id_)
        cls.__produto_dao.delete_one(produto)
