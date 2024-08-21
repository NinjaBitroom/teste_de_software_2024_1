from sqlalchemy.orm import Mapped, mapped_column

from src.services.database import db


class EnderecoModel(db.Model):
    __abstract__ = True
    logradouro: Mapped[str] = mapped_column(db.String(80))
    numero: Mapped[int] = mapped_column(db.Integer)
    complemento: Mapped[str | None] = mapped_column(db.String(80))
    bairro: Mapped[str] = mapped_column(db.String(80))
    cep: Mapped[str] = mapped_column(db.String(9))
    cidade: Mapped[str] = mapped_column(db.String(80))
    uf: Mapped[str] = mapped_column(db.String(2))
