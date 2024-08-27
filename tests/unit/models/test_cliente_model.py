"""
Claudinei de Oliveira - utf-8 - pt-br
testeModel.py
"""

from flask_testing import TestCase

from src.models.cliente_model import ClienteModel
from src.services.database import db
from tests.mixins.flask_app_mixin import FlaskAppMixin


class TestClienteModel(FlaskAppMixin, TestCase):
    """Testando a classe Cliente."""

    def test_valid_values(self):
        """ClienteModel deve aceitar valores válidos."""
        cliente_dict = {
            'nome': 'Valid Value',
            'cpf': '00000000000',
            'logradouro': 'Valid Value',
            'numero': 123,
            'complemento': 'Valid Value',
            'bairro': 'Valid Value',
            'cep': '00000-000',
            'cidade': 'Valid Value',
            'uf': 'VV',
            'telefone': '00000000000',
            'email': 'valid_value@mail.test',
        }
        cliente = ClienteModel(**cliente_dict)
        db.session.add(cliente)
        db.session.commit()
        cliente_from_db = ClienteModel.query.first()
        self.assertEqual(
            cliente_from_db.logradouro, cliente_dict['logradouro']
        )
        self.assertEqual(cliente_from_db.numero, cliente_dict['numero'])
        self.assertEqual(
            cliente_from_db.complemento, cliente_dict['complemento']
        )
        self.assertEqual(cliente_from_db.bairro, cliente_dict['bairro'])
        self.assertEqual(cliente_from_db.cep, cliente_dict['cep'])
        self.assertEqual(cliente_from_db.cidade, cliente_dict['cidade'])
        self.assertEqual(cliente_from_db.uf, cliente_dict['uf'])
        self.assertEqual(cliente_from_db.nome, cliente_dict['nome'])
        self.assertEqual(cliente_from_db.cpf, cliente_dict['cpf'])
        self.assertEqual(cliente_from_db.telefone, cliente_dict['telefone'])
        self.assertEqual(cliente_from_db.email, cliente_dict['email'])

    def test_nome_is_not_none(self):
        """ClienteModel deve rejeitar nome nulo."""
        cliente_dict = {
            'nome': None,
            'cpf': '00000000000',
            'logradouro': 'Any Value',
            'numero': 123,
            'complemento': 'Any Value',
            'bairro': 'Any Value',
            'cep': '00000-000',
            'cidade': 'Any Value',
            'uf': 'AV',
            'telefone': '00000000000',
            'email': 'any_value@mail.test',
        }
        cliente = ClienteModel(**cliente_dict)
        db.session.add(cliente)
        with self.assertRaises(Exception):
            db.session.commit()

    def test_cpf_is_not_none(self):
        """ClienteModel deve rejeitar cpf nulo."""
        cliente_dict = {
            'nome': 'Any Value',
            'cpf': None,
            'logradouro': 'Any Value',
            'numero': 123,
            'complemento': 'Any Value',
            'bairro': 'Any Value',
            'cep': '00000-000',
            'cidade': 'Any Value',
            'uf': 'AV',
            'telefone': '00000000000',
            'email': 'any_value@mail.test',
        }
        cliente = ClienteModel(**cliente_dict)
        db.session.add(cliente)
        with self.assertRaises(Exception):
            db.session.commit()

    def test_logradouro_is_not_none(self):
        """ClienteModel deve rejeitar logradouro nulo."""
        cliente_dict = {
            'nome': 'Any Value',
            'cpf': '00000000000',
            'logradouro': None,
            'numero': 123,
            'complemento': 'Any Value',
            'bairro': 'Any Value',
            'cep': '00000-000',
            'cidade': 'Any Value',
            'uf': 'AV',
            'telefone': '00000000000',
            'email': 'any_value@mail.test',
        }
        cliente = ClienteModel(**cliente_dict)
        db.session.add(cliente)
        with self.assertRaises(Exception):
            db.session.commit()

    def test_numero_is_not_none(self):
        """ClienteModel deve rejeitar numero nulo."""
        cliente_dict = {
            'nome': 'Any Value',
            'cpf': '00000000000',
            'logradouro': 'Any Value',
            'numero': None,
            'complemento': 'Any Value',
            'bairro': 'Any Value',
            'cep': '00000-000',
            'cidade': 'Any Value',
            'uf': 'AV',
            'telefone': '00000000000',
            'email': 'any_value@mail.test',
        }
        cliente = ClienteModel(**cliente_dict)
        db.session.add(cliente)
        with self.assertRaises(Exception):
            db.session.commit()

    def test_complemento_is_none(self):
        """ClienteModel deve aceitar complemento nulo."""
        cliente_dict = {
            'nome': 'Any Value',
            'cpf': '00000000000',
            'logradouro': 'Any Value',
            'numero': 123,
            'complemento': None,
            'bairro': 'Any Value',
            'cep': '00000-000',
            'cidade': 'Any Value',
            'uf': 'AV',
            'telefone': '00000000000',
            'email': 'any_value@mail.test',
        }
        cliente = ClienteModel(**cliente_dict)
        db.session.add(cliente)
        db.session.commit()
        cliente_from_db = ClienteModel.query.first()
        self.assertEqual(cliente_from_db.complemento, None)

    def test_bairro_is_not_none(self):
        """ClienteModel deve rejeitar bairro nulo."""
        cliente_dict = {
            'nome': 'Any Value',
            'cpf': '00000000000',
            'logradouro': 'Any Value',
            'numero': 123,
            'complemento': 'Any Value',
            'bairro': None,
            'cep': '00000-000',
            'cidade': 'Any Value',
            'uf': 'AV',
            'telefone': '00000000000',
            'email': 'any_value@mail.test',
        }
        cliente = ClienteModel(**cliente_dict)
        db.session.add(cliente)
        with self.assertRaises(Exception):
            db.session.commit()

    def test_cep_is_not_none(self):
        """ClienteModel deve rejeitar cep nulo."""
        cliente_dict = {
            'nome': 'Any Value',
            'cpf': '00000000000',
            'logradouro': 'Any Value',
            'numero': 123,
            'complemento': 'Any Value',
            'bairro': 'Any Value',
            'cep': None,
            'cidade': 'Any Value',
            'uf': 'AV',
            'telefone': '00000000000',
            'email': 'any_value@mail.test',
        }
        cliente = ClienteModel(**cliente_dict)
        db.session.add(cliente)
        with self.assertRaises(Exception):
            db.session.commit()

    def test_cidade_is_not_none(self):
        """ClienteModel deve rejeitar cidade nulo."""
        cliente_dict = {
            'nome': 'Any Value',
            'cpf': '00000000000',
            'logradouro': 'Any Value',
            'numero': 123,
            'complemento': 'Any Value',
            'bairro': 'Any Value',
            'cep': '00000-000',
            'cidade': None,
            'uf': 'AV',
            'telefone': '00000000000',
            'email': 'any_value@mail.test',
        }
        cliente = ClienteModel(**cliente_dict)
        db.session.add(cliente)
        with self.assertRaises(Exception):
            db.session.commit()

    def test_uf_is_not_none(self):
        """ClienteModel deve rejeitar uf nulo."""
        cliente_dict = {
            'nome': 'Any Value',
            'cpf': '00000000000',
            'logradouro': 'Any Value',
            'numero': 123,
            'complemento': 'Any Value',
            'bairro': 'Any Value',
            'cep': '00000-000',
            'cidade': 'Any Value',
            'uf': None,
            'telefone': '00000000000',
            'email': 'any_value@mail.test',
        }
        cliente = ClienteModel(**cliente_dict)
        db.session.add(cliente)
        with self.assertRaises(Exception):
            db.session.commit()

    def test_telefone_is_not_none(self):
        """ClienteModel deve rejeitar telefone nulo."""
        cliente_dict = {
            'nome': 'Any Value',
            'cpf': '00000000000',
            'logradouro': 'Any Value',
            'numero': 123,
            'complemento': 'Any Value',
            'bairro': 'Any Value',
            'cep': '00000-000',
            'cidade': 'Any Value',
            'uf': 'AV',
            'telefone': None,
            'email': 'any_value@mail.test',
        }
        cliente = ClienteModel(**cliente_dict)
        db.session.add(cliente)
        with self.assertRaises(Exception):
            db.session.commit()

    def test_email_is_not_none(self):
        """ClienteModel deve rejeitar email nulo."""
        cliente_dict = {
            'nome': 'Any Value',
            'cpf': '00000000000',
            'logradouro': 'Any Value',
            'numero': 123,
            'complemento': 'Any Value',
            'bairro': 'Any Value',
            'cep': '00000-000',
            'cidade': 'Any Value',
            'uf': 'AV',
            'telefone': '00000000000',
            'email': None,
        }
        cliente = ClienteModel(**cliente_dict)
        db.session.add(cliente)
        with self.assertRaises(Exception):
            db.session.commit()
