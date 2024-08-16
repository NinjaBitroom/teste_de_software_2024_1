from services.database import db


class PessoaModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
