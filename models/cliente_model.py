"""
Claudinei de Oliveira - utf-8 - pt-br
cliente_model.py
"""
from models.pessoa_model import PessoaModel
from services.database import db


class Cliente(db.Model, PessoaModel):
    """
    Definição da classe Cliente, que representa a tabela 'clientes' no banco de dados.
    """
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
