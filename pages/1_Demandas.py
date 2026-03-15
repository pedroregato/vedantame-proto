import streamlit as st
from ui.theme import inject_css, COLORS
from ui.components import card_demanda, formulario_demanda
from core.repository import get_demandas, get_membro_by_id
from core.models import CATEGORIAS

st.set_page_config(page_title="Demandas · VedantaMe", page_icon="📋", layout="wide")
inject_css()

st.markdown(
    f"<h1 style='font-family:Georgia,serif;color:{COLORS['dark']};'>📋 Demandas</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='color:#4A4A6A;'>Necessidades abertas na comunidade. Veja se você pode ajudar.</p>",
    unsafe_allow_html=True,
)
st.markdown("<hr>", unsafe_allow_html=True)

# Inicializa session_state para novas demandas
if "novas_demandas" not in st.session_state:
    st.session_state.novas_demandas = []

# Filtro
categorias_opcoes = ["Todas"] + CATEGORIAS
filtro = st.selectbox("Filtrar por categoria", categorias_opcoes, index=0)

st.markdown("### Demandas abertas")

demandas = get_demandas() + st.session_state.novas_demandas

if filtro != "Todas":
    demandas = [d for d in demandas if d.categoria == filtro]

if not demandas:
    st.info("Nenhuma demanda encontrada para esta categoria.")
else:
    for demanda in sorted(demandas, key=lambda d: d.data, reverse=True):
        membro = get_membro_by_id(demanda.membro_id)
        card_demanda(demanda, membro)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### Registrar nova demanda")

nova = formulario_demanda(key_prefix="demanda_page")
if nova:
    st.session_state.novas_demandas.append(nova)
    st.success("Demanda registrada com sucesso!")
    st.rerun()
