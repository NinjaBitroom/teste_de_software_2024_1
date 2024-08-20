from dao.flask_sqlalchemy_dao import FlaskSQLAlchemyDAO
from models.cliente_model import ClienteModel
from utils.cliente_validator import ClienteValidator


class ClienteController:
    __cliente_dao = FlaskSQLAlchemyDAO(ClienteModel)

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
            validated_telefone = ClienteValidator.valida_telefone(telefone)

            ClienteValidator.valida_endereco(
                logradouro, numero, complemento, bairro, cep, cidade, uf
            )

            novo_cliente = ClienteModel(
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
    def get_cliente(cls, id_) -> ClienteModel | None:
        """Obtém cliente pelo id."""
        return cls.__cliente_dao.get_one(id_)

    @classmethod
    def delete_cliente(cls, id):
        cliente = cls.__cliente_dao.get_one(id)
        cls.__cliente_dao.delete_one(cliente)

    @classmethod
    def update_cliente(
        cls, id, cpf, nome, logradouro, numero, complemento, bairro, cep,
        cidade, uf, telefone, email
    ) -> ClienteModel | Exception:
        try:
            cliente = cls.__cliente_dao.get_one(id)
            cliente.nome = ClienteValidator.valida_nome(nome)
            cliente.cpf = ClienteValidator.valida_cpf(cpf)
            cliente.logradouro, cliente.numero, cliente.complemento, cliente.bairro, cliente.cep, cliente.cidade, cliente.uf = ClienteValidator.valida_endereco(
                logradouro, numero, complemento, bairro, cep, cidade, uf
            )
            cliente.telefone = ClienteValidator.valida_telefone(telefone)
            cliente.email = ClienteValidator.valida_email(email)
            cls.__cliente_dao.update()
        except Exception as error:
            return error
        return cliente
