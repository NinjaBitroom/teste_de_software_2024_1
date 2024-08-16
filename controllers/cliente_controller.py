from dao.dao import Dao
from models.cliente_model import Cliente
from utils.cliente_validator import ClienteValidator


class ClienteController:
    __cliente_dao = Dao(Cliente)

    @classmethod
    def get_clientes(cls) -> list[Cliente]:
        """Obtém todos os clientes do banco de dados."""
        return cls.__cliente_dao.get_all()

    @classmethod
    def create_cliente(
            cls, nome: str, cpf: str, logradouro: str, numero, complemento,
            bairro: str, cep: str, cidade: str,
            uf: str, telefone, email: str
    ) -> None | Exception:
        """Cria um novo cliente."""
        try:
            validated_nome = ClienteValidator.valida_nome(nome)
            validated_cpf = ClienteValidator.valida_cpf(cpf)
            validated_email = ClienteValidator.valida_email(email)
            validated_telefone = telefone

            ClienteValidator.valida_endereco(logradouro, numero, complemento, bairro, cep, cidade, uf)

            novo_cliente = Cliente(
                nome=validated_nome,
                cpf=validated_cpf,
                email=validated_email,
                telefone=validated_telefone,
                logradouro=logradouro,
                numero=numero,
                complemento=complemento,
                bairro=bairro,
                cep=cep,
                cidade=cidade,
                uf=uf,
            )

            cls.__cliente_dao.add_one(novo_cliente)
        except Exception as error:
            return error

    @classmethod
    def get_cliente(cls, id_) -> Cliente | None:
        """Obtém cliente pelo id."""
        return cls.__cliente_dao.get_one(id_)

    @classmethod
    def delete_cliente(cls, id):
        cliente = cls.__cliente_dao.get_one(id)
        cls.__cliente_dao.delete_one(cliente)

    @classmethod
    def update_cliente(cls, id, cpf, nome, logradouro, numero, complemento, bairro, cep, cidade, uf, telefone, email):

        cliente = cls.__cliente_dao.get_one(id)
        cliente.nome = nome
        cliente.cpf = cpf
        cliente.logradouro = logradouro
        cliente.numero = numero
        cliente.complemento = complemento
        cliente.bairro = bairro
        cliente.cep = cep
        cliente.cidade = cidade
        cliente.uf = uf
        cliente.telefone = telefone
        cliente.email = email

        cls.__cliente_dao.update()

        return cliente
