"""
Claudinei de Oliveira - pt-BR - 19-06-2023
Manipulando o banco de dados sqlite3 
Adaptado de Giridhar, 2016
"""
from sqlalchemy.orm import Mapped, mapped_column

# Importação da instância do SQLAlchemy criada no arquivo database.py
from src.services.database import db


class ProdutoModel(db.Model):
    """Definição da classe Produto, que representa a tabela 'produtos'
    no banco de dados."""
    __tablename__ = 'produtos'
    """Definindo o nome da tabela no banco de dados."""

    # Definição das colunas da tabela
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    """Identificador único do produto."""

    descricao: Mapped[str]
    """Descrição do produto."""

    preco: Mapped[float]
    """Preço do produto."""

    status: Mapped[bool] = mapped_column(default=True)
    """Status do produto: ativo (1) ou inativo (0)."""
