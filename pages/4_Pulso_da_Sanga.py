import streamlit as st
import plotly.graph_objects as go

from core import repository
from ui.theme import inject_css, COLORS

st.set_page_config(
    page_title="🌸 Pulso da Sanga",
    page_icon="🌸",
    layout="wide",
)

inject_css()

st.markdown(
    f"""
    <h1 style="font-family:Georgia,serif;color:{COLORS['primary']};text-align:center;margin-bottom:0.2rem;">
        🌸 Pulso da Sanga
    </h1>
    <p style="text-align:center;color:{COLORS['mid']};font-size:1rem;margin-bottom:1.5rem;">
        Indicadores vivos da nossa comunidade —
        cada número representa uma vida tocada pelo seva.
    </p>
    """,
    unsafe_allow_html=True,
)

stats = repository.get_stats()

# ── Faixa 1 — Visão Geral ─────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="✅ Demandas Atendidas",
        value=f"{stats['pct_atendidas']}%",
        delta="+5% este mês",
    )
with col2:
    st.metric(
        label="🕊️ Aguardando Resposta",
        value=stats["aguardando"],
        delta="-2 esta semana",
        delta_color="inverse",
    )
with col3:
    st.metric(
        label="🤝 Ofertas Disponíveis",
        value=stats["total_ofertas"],
        delta="+3 novas",
    )
with col4:
    st.metric(
        label="🌱 Vidas Impactadas",
        value=stats["vidas_impactadas"],
        delta="+1 hoje",
    )

st.divider()

# ── Faixa 2 — Demandas por Categoria ─────────────────────────────────────────
st.markdown(
    f'<h3 style="font-family:Georgia,serif;color:{COLORS["dark"]};">'
    "Demandas por Categoria</h3>",
    unsafe_allow_html=True,
)

categorias = list(stats["dem_por_cat"].keys())
abertas   = [stats["dem_por_cat"][c]["abertas"]   for c in categorias]
atendidas = [stats["dem_por_cat"][c]["atendidas"] for c in categorias]

fig_bar = go.Figure()
fig_bar.add_trace(go.Bar(
    name="Abertas",
    y=categorias,
    x=abertas,
    orientation="h",
    marker_color=COLORS["warning"],
))
fig_bar.add_trace(go.Bar(
    name="Atendidas",
    y=categorias,
    x=atendidas,
    orientation="h",
    marker_color=COLORS["primary"],
))
fig_bar.update_layout(
    barmode="stack",
    plot_bgcolor=COLORS["background"],
    paper_bgcolor=COLORS["background"],
    font=dict(color=COLORS["text"]),
    margin=dict(l=0, r=0, t=10, b=0),
    legend=dict(orientation="h", y=-0.18),
    height=300,
    xaxis=dict(showgrid=False),
    yaxis=dict(gridcolor="#E0D8CC"),
)
st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# ── Faixas 3 e 4 — lado a lado ───────────────────────────────────────────────
col_esq, col_dir = st.columns(2)

with col_esq:
    st.markdown(
        f'<h3 style="font-family:Georgia,serif;color:{COLORS["dark"]};">'
        "Distribuição de Ofertas</h3>",
        unsafe_allow_html=True,
    )

    cats_ofe = [c for c, v in stats["ofe_por_cat"].items() if v > 0]
    vals_ofe = [stats["ofe_por_cat"][c] for c in cats_ofe]
    palette  = [
        COLORS["primary"], COLORS["warning"], COLORS["success"],
        COLORS["mid"],     COLORS["dark"],    "#A67C52",
        "#6B8E7B",         "#7A6B8E",
    ]

    fig_donut = go.Figure(go.Pie(
        labels=cats_ofe,
        values=vals_ofe,
        hole=0.5,
        marker=dict(colors=palette[: len(cats_ofe)]),
        textinfo="label+percent",
        textfont=dict(size=11),
    ))
    fig_donut.update_layout(
        plot_bgcolor=COLORS["background"],
        paper_bgcolor=COLORS["background"],
        font=dict(color=COLORS["text"]),
        showlegend=False,
        margin=dict(l=0, r=0, t=10, b=0),
        height=340,
    )
    st.plotly_chart(fig_donut, use_container_width=True)

with col_dir:
    st.markdown(
        f'<h3 style="font-family:Georgia,serif;color:{COLORS["dark"]};">'
        "Atividade nos Últimos 30 Dias</h3>",
        unsafe_allow_html=True,
    )

    datas  = [t["data"]     for t in stats["timeline"]]
    valores = [t["demandas"] for t in stats["timeline"]]

    fig_line = go.Figure(go.Scatter(
        x=datas,
        y=valores,
        mode="lines+markers",
        line=dict(color=COLORS["primary"], width=2.5),
        marker=dict(color=COLORS["warning"], size=5),
        fill="tozeroy",
        fillcolor="rgba(139,92,42,0.1)",
    ))
    fig_line.update_layout(
        plot_bgcolor=COLORS["background"],
        paper_bgcolor=COLORS["background"],
        font=dict(color=COLORS["text"]),
        margin=dict(l=0, r=0, t=10, b=0),
        xaxis=dict(showgrid=False, title=""),
        yaxis=dict(gridcolor="#E0D8CC", title="Demandas acumuladas"),
        height=340,
    )
    st.plotly_chart(fig_line, use_container_width=True)

st.divider()

# ── Faixa 5 — Categorias Mais Carentes ───────────────────────────────────────
st.markdown(
    f"""
    <h3 style="font-family:Georgia,serif;color:{COLORS['dark']};">
        Onde a comunidade mais precisa de você
    </h3>
    <p style="color:{COLORS['mid']};font-size:0.95rem;margin-bottom:1rem;">
        Categorias com maior diferença entre demandas abertas e ofertas disponíveis.
    </p>
    """,
    unsafe_allow_html=True,
)

rows_html = ""
for g in stats["gaps"]:
    cat = g["categoria"]
    gap = g["gap"]
    dem_ab = stats["dem_por_cat"].get(cat, {}).get("abertas", 0)
    ofe_qt = stats["ofe_por_cat"].get(cat, 0)

    if gap > 0:
        cor   = COLORS["warning"]
        label = f"+{gap} precisam de ajuda"
    elif gap == 0:
        cor   = COLORS["success"]
        label = "Em equilíbrio ✓"
    else:
        cor   = COLORS["success"]
        label = f"{abs(gap)} oferta(s) excedente(s)"

    rows_html += f"""
      <tr style="border-bottom:1px solid #E0D8CC;">
        <td style="padding:0.65rem 1rem;font-weight:500;">{cat}</td>
        <td style="padding:0.65rem 1rem;text-align:center;">{dem_ab}</td>
        <td style="padding:0.65rem 1rem;text-align:center;">{ofe_qt}</td>
        <td style="padding:0.65rem 1rem;text-align:center;">
          <span style="background:{cor};color:#fff;border-radius:12px;
                       padding:3px 12px;font-size:0.83rem;">{label}</span>
        </td>
      </tr>"""

st.markdown(
    f"""
    <div style="border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.07);">
      <table style="width:100%;border-collapse:collapse;
                    background:{COLORS['background']};">
        <thead>
          <tr style="background:{COLORS['dark']};color:#F5F0E8;">
            <th style="padding:0.75rem 1rem;text-align:left;">Categoria</th>
            <th style="padding:0.75rem 1rem;">Dem. Abertas</th>
            <th style="padding:0.75rem 1rem;">Ofertas</th>
            <th style="padding:0.75rem 1rem;">Situação</th>
          </tr>
        </thead>
        <tbody>{rows_html}</tbody>
      </table>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <p style="text-align:center;color:{COLORS['mid']};font-size:0.82rem;margin-top:2rem;">
        <em>Dados do protótipo · VedantaMe · Movimento Ramakrishna Vedanta no Brasil · 2026</em>
    </p>
    """,
    unsafe_allow_html=True,
)
