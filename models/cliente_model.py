"""
Claudinei de Oliveira - utf-8 - pt-br
cliente_model.py
"""
from models.pessoa_model import Pessoa


class Cliente(Pessoa):
    def __init__(
        self, nome, cpf, logradouro, numero, complemento, bairro, cep, cidade,
        uf, telefone, email
    ):
        super().__init__(
            nome, cpf, logradouro, numero, complemento, bairro, cep, cidade,
            uf, telefone, email
        )
