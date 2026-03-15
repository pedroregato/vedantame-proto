from dataclasses import dataclass, field
from typing import Optional

CATEGORIAS = [
    "Moradia Temporária",
    "Trabalho e Renda",
    "Transporte e Locomoção",
    "Apoio Emocional e Escuta",
    "Saúde e Acompanhamento Médico",
    "Eventos e Projetos Espirituais",
    "Talentos e Habilidades",
    "Apoio Espiritual",
    "Bate-papo Vedanta",
]

STATUS_OPTIONS = ["Aguardando", "Em contato", "Resolvido"]


@dataclass
class Membro:
    id: str
    nome: str
    cidade: str
    estado: str


@dataclass
class Demanda:
    id: str
    membro_id: str
    categoria: str
    descricao: str
    status: str
    data: str


@dataclass
class Oferta:
    id: str
    membro_id: str
    categoria: str
    descricao: str
    data: str
