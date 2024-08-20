from src.dao.flask_sqlalchemy_dao import FlaskSQLAlchemyDAO
from src.models.cliente_model import ClienteModel
from src.utils.cliente_validator import ClienteValidator


class ClienteController:
    __cliente_dao = FlaskSQLAlchemyDAO(ClienteModel)

    @classmethod
    def get_clientes(cls) -> list[ClienteModel]:
        """Obtém todos os clientes do banco de dados."""
        return cls.__cliente_dao.get_all()

    @classmethod
    def create_cliente(
        cls, cliente_dict: dict[str, str | None]
    ) -> None | Exception:
        """Cria um novo cliente."""
        try:
            validated_nome = ClienteValidator.valida_nome(cliente_dict['nome'])
            validated_cpf = ClienteValidator.valida_cpf(cliente_dict['cpf'])
            validated_email = ClienteValidator.valida_email(
                cliente_dict['email']
            )
            validated_telefone = ClienteValidator.valida_telefone(
                cliente_dict['telefone']
            )

            validated_endereco = ClienteValidator.valida_endereco(
                cliente_dict['logradouro'], cliente_dict['numero'],
                cliente_dict['complemento'], cliente_dict['bairro'],
                cliente_dict['cep'], cliente_dict['cidade'], cliente_dict['uf']
            )

            novo_cliente = ClienteModel(
                nome=validated_nome,
                cpf=validated_cpf,
                email=validated_email,
                telefone=validated_telefone,
                **validated_endereco
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
