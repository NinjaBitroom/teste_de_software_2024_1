from unittest import TestCase

from src.utils.produto_validator import ProdutoValidator


class TestProdutoValidator(TestCase):
    def test_valid_preco(self):
        preco = '10.0'
        self.assertEqual(ProdutoValidator.valida_preco(preco), 10.0)

    def test_invalid_preco(self):
        preco = 'abc'
        self.assertIsInstance(ProdutoValidator.valida_preco(preco), ValueError)
