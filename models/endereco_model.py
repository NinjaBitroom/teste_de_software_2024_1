from sqlalchemy.orm import Mapped, mapped_column

from services.database import db


class EnderecoModel(db.Model):
    __abstract__ = True
    logradouro: Mapped[str] = mapped_column(db.String(80), nullable=False)
    numero: Mapped[int] = mapped_column(db.Integer, nullable=False)
    complemento: Mapped[str] = mapped_column(db.String(80), nullable=False)
    bairro: Mapped[str] = mapped_column(db.String(80), nullable=False)
    cep: Mapped[str] = mapped_column(db.String(9), nullable=False)
    cidade: Mapped[str] = mapped_column(db.String(80), nullable=False)
    uf: Mapped[str] = mapped_column(db.String(2), nullable=False)
