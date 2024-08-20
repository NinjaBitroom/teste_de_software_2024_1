from src.dao.flask_sqlalchemy_dao import FlaskSQLAlchemyDAO
from src.models.produto_model import ProdutoModel
from src.utils.produto_validator import ProdutoValidator


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
        cls, produto_dict: dict[str, str | None]
    ) -> ProdutoModel | ValueError:

        converted_preco = ProdutoValidator.valida_preco(produto_dict['preco'])
        if isinstance(converted_preco, ValueError):
            return converted_preco

        new_produto = ProdutoModel(
            descricao=produto_dict['descricao'], preco=converted_preco
        )

        cls.__produto_dao.add_one(new_produto)
        return new_produto

    @classmethod
    def update_produto(
        cls, produto_dict: dict[str, str | int | None]
    ) -> ProdutoModel | ValueError:
        produto = cls.__produto_dao.get_one(produto_dict['id'])
        converted_preco: float | ValueError | None = None

        if produto_dict['preco'] is not None:
            converted_preco = ProdutoValidator.valida_preco(
                produto_dict['preco']
            )

        if isinstance(converted_preco, ValueError):
            return converted_preco

        if produto_dict['descricao'] is not None:
            produto.descricao = produto_dict['descricao']

        if converted_preco is not None:
            produto.preco = converted_preco

        if produto_dict['status'] is not None:
            produto.status = (
                True if produto_dict['status'] == 'True' else False
            )

        cls.__produto_dao.update()

        return produto

    @classmethod
    def delete_produto(cls, id_: int) -> None:
        produto = cls.__produto_dao.get_one(id_)
        cls.__produto_dao.delete_one(produto)
