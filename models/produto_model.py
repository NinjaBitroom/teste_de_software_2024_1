"""
Claudinei de Oliveira - pt-BR - 19-06-2023
Manipulando o banco de dados sqlite3 
Adaptado de Giridhar, 2016
"""

# Importação da instância do SQLAlchemy criada no arquivo database.py
from services.database import db


class Produto(db.Model):
    """Definição da classe Produto, que representa a tabela 'produtos'
    no banco de dados."""
    __tablename__ = 'produtos'
    """Definindo o nome da tabela no banco de dados."""

    # Definição das colunas da tabela
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    """Identificador único do produto."""

    descricao = db.Column(db.String, nullable=False)
    """Descrição do produto."""

    preco = db.Column(db.Float, nullable=False)
    """Preço do produto."""

    status = db.Column(db.Integer, default=1)
    """Status do produto: ativo (1) ou inativo (0)."""

    def deletar(self):
        """Método para deletar um produto no banco de dados."""
        db.session.delete(self)  # Removendo o produto da sessão do SQLAlchemy
        db.session.commit()  # Salvando as alterações no banco de dados
