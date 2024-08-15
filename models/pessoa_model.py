from models.endereco_model import EnderecoModel


class PessoaModel:
    def __init__(
        self, nome: str, cpf: str, email, telefone, endereco: EnderecoModel
    ):
        self.nome = nome
        self.__cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    @property
    def cpf(self):
        return self.__cpf
