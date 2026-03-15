import streamlit as st
from ui.theme import inject_css, COLORS
from ui.components import card_oferta, formulario_oferta
from core.repository import get_ofertas, get_membro_by_id
from core.models import CATEGORIAS

st.set_page_config(page_title="Ofertas · VedantaMe", page_icon="🤲", layout="wide")
inject_css()

st.markdown(
    f"<h1 style='font-family:Georgia,serif;color:{COLORS['dark']};'>🤲 Ofertas</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='color:#4A4A6A;'>O que a comunidade tem a oferecer com seva e amor.</p>",
    unsafe_allow_html=True,
)
st.markdown("<hr>", unsafe_allow_html=True)

# Inicializa session_state para novas ofertas
if "novas_ofertas" not in st.session_state:
    st.session_state.novas_ofertas = []

# Filtro
categorias_opcoes = ["Todas"] + CATEGORIAS
filtro = st.selectbox("Filtrar por categoria", categorias_opcoes, index=0)

st.markdown("### Ofertas disponíveis")

ofertas = get_ofertas() + st.session_state.novas_ofertas

if filtro != "Todas":
    ofertas = [o for o in ofertas if o.categoria == filtro]

if not ofertas:
    st.info("Nenhuma oferta encontrada para esta categoria.")
else:
    for oferta in sorted(ofertas, key=lambda o: o.data, reverse=True):
        membro = get_membro_by_id(oferta.membro_id)
        card_oferta(oferta, membro)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("### Registrar nova oferta")

nova = formulario_oferta(key_prefix="oferta_page")
if nova:
    st.session_state.novas_ofertas.append(nova)
    st.success("Oferta registrada com sucesso!")
    st.rerun()
