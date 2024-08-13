"""
Claudinei de Oliveira - pt-BR - 19-06-2023
Manipulando o banco de dados sqlite3 
Adaptado de Giridhar, 2016
"""

# Importação da instância do SQLAlchemy criada no arquivo database.py
from services.database import db


class Produto(db.Model):
    """Definição da classe Produto, que representa a tabela 'produtos'
    no banco de dados."""
    __tablename__ = 'produtos'
    """Definindo o nome da tabela no banco de dados."""

    # Definição das colunas da tabela
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    """Identificador único do produto."""

    descricao = db.Column(db.String, nullable=False)
    """Descrição do produto."""

    preco = db.Column(db.Float, nullable=False)
    """Preço do produto."""

    status = db.Column(db.Integer, default=1)
    """Status do produto: ativo (1) ou inativo (0)."""

    def __init__(
        self, descricao: str, preco: float, id_: int | None = None
    ) -> None:
        """Método construtor da classe."""
        self.id = id_
        self.descricao = descricao
        self.preco = preco

    def salvar(self) -> None:
        """Método para salvar um produto no banco de dados."""
        db.session.add(self)  # Adicionando o produto na sessão do SQLAlchemy
        db.session.commit()  # Salvando as alterações no banco de dados

    def atualizar(self) -> None:
        """Método para atualizar um produto no banco de dados."""
        db.session.commit()  # Salvando as alterações no banco de dados

    def deletar(self):
        """Método para deletar um produto no banco de dados."""
        db.session.delete(self)  # Removendo o produto da sessão do SQLAlchemy
        db.session.commit()  # Salvando as alterações no banco de dados

    @staticmethod
    def get_produto(id_):
        """Retorna um produto específico pelo ID."""
        return db.session.query(Produto).get(id_)
