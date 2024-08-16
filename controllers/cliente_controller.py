from dao.cliente_dao import MemoryDAO
from models.cliente_model import ClienteModel
from models.endereco_model import EnderecoModel
from utils.cliente_validator import ClienteValidator


class ClienteController:
    __cliente_dao = MemoryDAO(ClienteModel)

    @classmethod
    def get_clientes(cls) -> list[ClienteModel]:
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
            validated_endereco = ClienteValidator.valida_endereco(
                logradouro, numero,
                complemento, bairro, cep,
                cidade, uf
            )
            new_endereco = EnderecoModel(*validated_endereco)
            new_cliente = ClienteModel(
                validated_nome,
                validated_cpf,
                validated_email,
                validated_telefone,
                new_endereco,
            )
            cls.__cliente_dao.add_one(new_cliente)
        except Exception as error:
            return error

    @classmethod
    def get_cliente(cls, cpf_) -> ClienteModel | None:
        """Obtém cliente pelo cpf."""
        return cls.__cliente_dao.get_one(cpf_)

    @classmethod
    def update_cliente(cls, id, descricao, preco, status):
        pass

    @classmethod
    def delete_cliente(cls, cpf):
        cliente = cls.__cliente_dao.get_one(cpf)
        cls.__cliente_dao.delete_one(cliente)

