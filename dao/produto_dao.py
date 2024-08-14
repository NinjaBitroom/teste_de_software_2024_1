from models.produto_model import Produto
from services.database import db


class ProdutoDAO:
    @staticmethod
    def get_produtos() -> list[Produto]:
        """Retorna todos os produtos."""
        return db.session.query(Produto).all()

    @staticmethod
    def get_produto(id_) -> Produto | None:
        """Retorna um produto específico pelo ID."""
        return db.session.query(Produto).get(id_)

    @classmethod
    def salvar(cls, produto: Produto) -> None:
        """Método para salvar um produto no banco de dados."""
        db.session.add(
            produto
        )  # Adicionando o produto na sessão do SQLAlchemy
        cls.atualizar()  # Salvando as alterações no banco de dados

    @staticmethod
    def atualizar() -> None:
        """Método para atualizar um produto no banco de dados."""
        db.session.commit()  # Salvando as alterações no banco de dados

    @staticmethod
    def deletar(id):
        pass
