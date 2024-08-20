"""
Claudinei de Oliveira - pt-BR - 19-06-2023
Manipulando o banco de dados sqlite3 
Adaptado de Giridhar, 2016
"""
from sqlalchemy.orm import Mapped, mapped_column

# Importação da instância do SQLAlchemy criada no arquivo database.py
from services.database import db


class Produto(db.Model):
    """Definição da classe Produto, que representa a tabela 'produtos'
    no banco de dados."""
    __tablename__ = 'produtos'
    """Definindo o nome da tabela no banco de dados."""

    # Definição das colunas da tabela
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    """Identificador único do produto."""

    descricao: Mapped[str] = mapped_column(nullable=False)
    """Descrição do produto."""

    preco: Mapped[float] = mapped_column(nullable=False)
    """Preço do produto."""

    status: Mapped[str] = mapped_column(default=True)
    """Status do produto: ativo (1) ou inativo (0)."""
