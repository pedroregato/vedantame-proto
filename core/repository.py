import json
import os
from typing import List, Optional
from core.models import Demanda, Oferta, Membro

_DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "seed_data.json")


def _load() -> dict:
    with open(_DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_membros() -> List[Membro]:
    data = _load()
    return [Membro(**m) for m in data["membros"]]


def get_membro_by_id(membro_id: str) -> Optional[Membro]:
    for m in get_membros():
        if m.id == membro_id:
            return m
    return None


def get_demandas() -> List[Demanda]:
    data = _load()
    return [Demanda(**d) for d in data["demandas"]]


def get_ofertas() -> List[Oferta]:
    data = _load()
    return [Oferta(**o) for o in data["ofertas"]]


def get_demandas_por_categoria(categoria: str) -> List[Demanda]:
    return [d for d in get_demandas() if d.categoria == categoria]


def get_ofertas_por_categoria(categoria: str) -> List[Oferta]:
    return [o for o in get_ofertas() if o.categoria == categoria]


def get_stats() -> dict:
    from core.analytics import calcular_stats
    return calcular_stats(get_demandas(), get_ofertas(), get_membros())
