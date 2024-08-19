from services.database import db


class EnderecoModel:
    logradouro = db.Column(db.String(80), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(80), nullable=False)
    bairro = db.Column(db.String(80), nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    cidade = db.Column(db.String(80), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
