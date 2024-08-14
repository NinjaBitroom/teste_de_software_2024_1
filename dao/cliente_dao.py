from models.cliente_model import Cliente
from services.database import db


class ClienteDAO:

    def salvar(self):
        db.session.add(self)  # Adicionando o cliente na sessão do SQLAlchemy
        db.session.commit()  # Salvando as alterações no banco de dados

    def atualizar(self):
        """Método para atualizar um cliente no banco de dados."""
        db.session.commit()  # Salvando as alterações no banco de dados

    def deletar(self):
        """Método para deletar um cliente no banco de dados."""
        db.session.delete(self)  # Removendo o cliente da sessão do SQLAlchemy
        db.session.commit()  # Salvando as alterações no banco de dados

    @staticmethod
    def get_clientes():
        """Retorna todos os clientes."""
        return db.session.query(Cliente).all()

    @staticmethod
    def get_cliente(id):
        """Retorna um cliente específico pelo ID"""
        return db.session.query(Cliente).get(id)
