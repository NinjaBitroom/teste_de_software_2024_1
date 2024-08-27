from unittest import TestCase

import email_validator

from src.utils.cliente_validator import ClienteValidator


class TestClienteValidator(TestCase):
    @classmethod
    def setUpClass(cls):
        email_validator.TEST_ENVIRONMENT = True

    @classmethod
    def tearDownClass(cls):
        email_validator.TEST_ENVIRONMENT = False

    def test_nome_vazio(self):
        self.assertRaises(ValueError, ClienteValidator.valida_nome, '')

    def test_nome_invalido(self):
        self.assertRaises(ValueError, ClienteValidator.valida_nome, '123')

    def test_nome_valido(self):
        nome = ClienteValidator.valida_nome('João da Silva')
        self.assertEqual(nome, 'João da Silva')

    def test_cpf_invalido(self):
        self.assertRaises(ValueError, ClienteValidator.valida_cpf, '123')
        self.assertRaises(
            ValueError, ClienteValidator.valida_cpf, '00000000000'
        )
        self.assertRaises(
            ValueError, ClienteValidator.valida_cpf, '12345678900'
        )
        self.assertRaises(
            ValueError, ClienteValidator.valida_cpf, '00123456789'
        )

    def test_cpf_valido(self):
        cpf = ClienteValidator.valida_cpf('01234567890')
        self.assertEqual(cpf, '01234567890')

    def test_invalid_email(self):
        self.assertRaises(ValueError, ClienteValidator.valida_email, 'abc')

    def test_valid_email(self):
        email = ClienteValidator.valida_email('valid@email.test')
        self.assertIsInstance(email, str)

    def test_formata_texto(self):
        texto = ClienteValidator.formata_texto('joão da silva')
        self.assertEqual(texto, 'João da Silva')

    def test_endereco_vazio(self):
        endereco = {
            'logradouro': '',
            'bairro': '',
            'cidade': '',
            'estado': '',
            'cep': '',
            'numero': '',
            'complemento': '',
            'uf': '',
        }
        self.assertRaises(
            ValueError, ClienteValidator.valida_endereco, endereco
        )

    def test_cep_invalido(self):
        endereco = {
            'logradouro': 'Rua',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'cep': '123',
            'numero': '123',
            'complemento': '',
            'uf': 'UF',
        }
        self.assertRaises(
            ValueError, ClienteValidator.valida_endereco, endereco
        )

    def test_uf_invalido(self):
        endereco = {
            'logradouro': 'Rua',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'cep': '12345-678',
            'numero': '123',
            'complemento': '',
            'uf': 'ABC',
        }
        self.assertRaises(
            ValueError, ClienteValidator.valida_endereco, endereco
        )

    def test_numero_invalido(self):
        endereco = {
            'logradouro': 'Rua',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'cep': '12345-678',
            'numero': 'abc',
            'complemento': '',
            'uf': 'UF',
        }
        self.assertRaises(
            ValueError, ClienteValidator.valida_endereco, endereco
        )

    def test_endereco_valido(self):
        endereco = {
            'logradouro': 'Rua',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'cep': '12345-678',
            'numero': '123',
            'complemento': '',
            'uf': 'UF',
        }
        endereco_valido = ClienteValidator.valida_endereco(endereco)
        self.assertIsInstance(endereco_valido, dict)

    def test_telefone_invalido(self):
        self.assertRaises(ValueError, ClienteValidator.valida_telefone, '123')

    def test_telefone_valido(self):
        telefone = ClienteValidator.valida_telefone('1234567890')
        self.assertEqual(telefone, '1234567890')
