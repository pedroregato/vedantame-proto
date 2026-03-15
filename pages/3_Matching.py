import streamlit as st
from ui.theme import inject_css, COLORS, CATEGORIA_COLORS
from ui.components import card_match
from core.repository import get_demandas, get_ofertas, get_membro_by_id
from core.matching import calcular_matches_por_categoria
from core.models import CATEGORIAS, STATUS_OPTIONS

st.set_page_config(page_title="Matching · VedantaMe", page_icon="✨", layout="wide")
inject_css()

st.markdown(
    f"<h1 style='font-family:Georgia,serif;color:{COLORS['dark']};'>✨ Matching</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='color:#4A4A6A;'>Pares compatíveis entre demandas e ofertas — onde a necessidade encontra o serviço.</p>",
    unsafe_allow_html=True,
)
st.markdown("<hr>", unsafe_allow_html=True)

# Combina dados do seed com dados da sessão
demandas_seed = get_demandas()
ofertas_seed = get_ofertas()
demandas_extras = st.session_state.get("novas_demandas", [])
ofertas_extras = st.session_state.get("novas_ofertas", [])

todas_demandas = demandas_seed + demandas_extras
todas_ofertas = ofertas_seed + ofertas_extras

# Filtro por categoria
categorias_opcoes = ["Todas"] + CATEGORIAS
filtro = st.selectbox("Filtrar por categoria", categorias_opcoes, index=0)

# Filtro por status
status_opcoes = ["Todos"] + STATUS_OPTIONS
filtro_status = st.selectbox("Filtrar por status da demanda", status_opcoes, index=0)

# Aplica filtros antes do matching
if filtro != "Todas":
    todas_demandas = [d for d in todas_demandas if d.categoria == filtro]
    todas_ofertas = [o for o in todas_ofertas if o.categoria == filtro]

if filtro_status != "Todos":
    todas_demandas = [d for d in todas_demandas if d.status == filtro_status]

matches_por_categoria = calcular_matches_por_categoria(todas_demandas, todas_ofertas)

if not matches_por_categoria:
    st.info("Nenhum par encontrado com os filtros selecionados.")
else:
    total = sum(len(v) for v in matches_por_categoria.values())
    st.markdown(
        f"<p style='color:{COLORS['success']};font-weight:700;'>"
        f"🔗 {total} par(es) encontrado(s) em {len(matches_por_categoria)} categoria(s)</p>",
        unsafe_allow_html=True,
    )

    for categoria, pares in sorted(matches_por_categoria.items()):
        cor = CATEGORIA_COLORS.get(categoria, COLORS["primary"])
        st.markdown(
            f"<h3 style='color:{cor};font-family:Georgia,serif;margin-top:1.5rem;'>"
            f"● {categoria} &nbsp;<span style='font-size:0.85rem;color:{COLORS['mid']};'>"
            f"({len(pares)} par{'es' if len(pares) > 1 else ''})</span></h3>",
            unsafe_allow_html=True,
        )
        for demanda, oferta in pares:
            membro_d = get_membro_by_id(demanda.membro_id)
            membro_o = get_membro_by_id(oferta.membro_id)
            card_match(demanda, oferta, membro_d, membro_o)
