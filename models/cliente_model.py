"""
Claudinei de Oliveira - utf-8 - pt-br
cliente_model.py
"""
from models.pessoa_model import PessoaModel
from services.database import db


class Cliente(PessoaModel):
    """
    Definição da classe Cliente, que representa a tabela 'clientes' no banco de dados.
    """
    __tablename__ = 'clientes'

    logradouro = db.Column(db.String(80), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(80), nullable=False)
    bairro = db.Column(db.String(80), nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    cidade = db.Column(db.String(80), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
