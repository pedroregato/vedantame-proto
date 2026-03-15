import random
from datetime import date, timedelta
from typing import List

from core.models import Demanda, Oferta, Membro


def calcular_stats(
    demandas: List[Demanda],
    ofertas: List[Oferta],
    membros: List[Membro],
) -> dict:
    """Agrega todos os indicadores do Pulso da Sanga. Função pura — sem Streamlit."""

    total_demandas = len(demandas)
    resolvidas = sum(1 for d in demandas if d.status == "Resolvido")
    aguardando = sum(1 for d in demandas if d.status == "Aguardando")
    pct_atendidas = round(resolvidas / total_demandas * 100, 1) if total_demandas else 0.0

    ids_envolvidos = {d.membro_id for d in demandas} | {o.membro_id for o in ofertas}
    vidas_impactadas = len(ids_envolvidos)

    categorias = sorted(
        {d.categoria for d in demandas} | {o.categoria for o in ofertas}
    )

    dem_por_cat = {
        cat: {
            "abertas": sum(
                1 for d in demandas
                if d.categoria == cat and d.status != "Resolvido"
            ),
            "atendidas": sum(
                1 for d in demandas
                if d.categoria == cat and d.status == "Resolvido"
            ),
        }
        for cat in categorias
    }

    ofe_por_cat = {
        cat: sum(1 for o in ofertas if o.categoria == cat)
        for cat in categorias
    }

    gaps = sorted(
        [
            {
                "categoria": cat,
                "gap": dem_por_cat.get(cat, {}).get("abertas", 0)
                       - ofe_por_cat.get(cat, 0),
            }
            for cat in categorias
        ],
        key=lambda x: x["gap"],
        reverse=True,
    )

    # Linha do tempo fictícia com semente fixa — crescimento gradual consistente
    rng = random.Random(42)
    hoje = date(2026, 3, 15)
    acumulado = 4
    timeline = []
    for i in range(30, -1, -1):
        dia = hoje - timedelta(days=i)
        acumulado += rng.randint(0, 2)
        timeline.append({"data": dia.isoformat(), "demandas": acumulado})

    return {
        "total_demandas": total_demandas,
        "pct_atendidas": pct_atendidas,
        "aguardando": aguardando,
        "total_ofertas": len(ofertas),
        "vidas_impactadas": vidas_impactadas,
        "dem_por_cat": dem_por_cat,
        "ofe_por_cat": ofe_por_cat,
        "gaps": gaps,
        "timeline": timeline,
    }
