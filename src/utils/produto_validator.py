class ProdutoValidator:
    @classmethod
    def valida_preco(cls, preco: str) -> float | ValueError:
        """Verifica se o preço é um número válido."""
        try:
            return float(preco)
        except ValueError:
            return ValueError('O preço deve ser um número válido.')
