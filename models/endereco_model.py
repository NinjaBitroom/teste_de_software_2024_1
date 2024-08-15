from dataclasses import dataclass
from typing import Any


@dataclass
class EnderecoModel:
    logradouro: str
    numero: Any
    complemento: Any
    bairro: str
    cep: str
    cidade: str
    uf: str
