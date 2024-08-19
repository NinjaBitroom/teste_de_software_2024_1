from models.endereco_model import EnderecoModel
from services.database import db


class PessoaModel(EnderecoModel):
    nome = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
