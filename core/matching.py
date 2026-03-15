from typing import List, Tuple
from core.models import Demanda, Oferta


def calcular_matches(
    demandas: List[Demanda], ofertas: List[Oferta]
) -> List[Tuple[Demanda, Oferta]]:
    """
    Retorna pares (Demanda, Oferta) com a mesma categoria.
    Função pura — sem dependência de Streamlit.
    """
    matches: List[Tuple[Demanda, Oferta]] = []
    for demanda in demandas:
        for oferta in ofertas:
            if demanda.categoria == oferta.categoria:
                matches.append((demanda, oferta))
    return matches


def calcular_matches_por_categoria(
    demandas: List[Demanda], ofertas: List[Oferta]
) -> dict:
    """
    Retorna um dict {categoria: [(Demanda, Oferta), ...]} com todos os matches agrupados.
    """
    result: dict = {}
    for demanda, oferta in calcular_matches(demandas, ofertas):
        cat = demanda.categoria
        if cat not in result:
            result[cat] = []
        result[cat].append((demanda, oferta))
    return result
