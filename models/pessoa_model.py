from sqlalchemy.orm import Mapped, mapped_column

from models.endereco_model import EnderecoModel
from services.database import db


class PessoaModel(EnderecoModel):
    __abstract__ = True
    nome: Mapped[str] = mapped_column(db.String(80), nullable=False)
    cpf: Mapped[str] = mapped_column(db.String(11), nullable=False)
    email: Mapped[str] = mapped_column(db.String(80), nullable=False)
    telefone: Mapped[str] = mapped_column(db.String(11), nullable=False)
