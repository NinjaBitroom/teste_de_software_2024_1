from utils.cliente_validator import ClienteValidator


class Pessoa:
    def __init__(
        self, nome, cpf, logradouro, numero, complemento, bairro, cep, cidade,
        uf, telefone, email
    ):
        self.nome = ClienteValidator.valida_nome(nome)
        self.__cpf = ClienteValidator.valida_cpf(cpf)
        self.email = ClienteValidator.valida_email(email)
        self.telefone = telefone

        logradouro, numero, complemento, bairro, cep, cidade, uf = ClienteValidator.valida_endereco(
            logradouro, numero,
            complemento, bairro, cep,
            cidade, uf
        )

        self.endereco = {
            'logradouro': logradouro,
            'numero': numero,
            'complemento': complemento,
            'bairro': bairro,
            'cep': cep,
            'cidade': cidade,
            'uf': uf
        }

    @property
    def cpf(self):
        return self.__cpf
