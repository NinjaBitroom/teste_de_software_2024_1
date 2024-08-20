"""
Claudinei de Oliveira - utf-8 - pt-br
cliente_model.py
"""
from sqlalchemy.orm import Mapped, mapped_column

from models.pessoa_model import PessoaModel


class ClienteModel(PessoaModel):
    """
    Definição da classe Cliente, que representa a tabela 'clientes' no banco de dados.
    """
    __tablename__ = 'clientes'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
