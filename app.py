## App para execução no Streamlit
import streamlit as st
from ui.theme import inject_css, COLORS
from ui.components import render_logo, render_symbol
from ui.hero import render_hero          # ← hero carrossel desacoplado

st.set_page_config(
    page_title="VedantaMe",
    page_icon="🪷",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    render_logo(max_width="200px")
    st.markdown(
        '<hr style="border-color:#333;margin:0.5rem 0 1rem 0;">',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <p style="color:#ccc;font-size:0.85rem;line-height:1.6;">
        <strong style="color:#F5F0E8;">Seva</strong> — serviço desinteressado<br>
        <strong style="color:#F5F0E8;">Sanga</strong> — associação com o sagrado
        </p>
        """,
        unsafe_allow_html=True,
    )

# ── Hero carrossel ────────────────────────────────────────────────────────────
render_hero()

# ── Cards de navegação ────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="vedanta-card" style="text-align:center;border-left-color:{COLORS['primary']};">
            <div style="font-size:2rem;">📋</div>
            <h3 style="font-size:1.1rem;margin:0.5rem 0 0.3rem 0;">Demandas</h3>
            <p>Veja ou registre uma necessidade da comunidade.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div class="vedanta-card" style="text-align:center;border-left-color:{COLORS['success']};">
            <div style="font-size:2rem;">🤲</div>
            <h3 style="font-size:1.1rem;margin:0.5rem 0 0.3rem 0;">Ofertas</h3>
            <p>Compartilhe talentos, recursos e serviços com o sanga.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <div class="vedanta-card" style="text-align:center;border-left-color:{COLORS['warning']};">
            <div style="font-size:2rem;">✨</div>
            <h3 style="font-size:1.1rem;margin:0.5rem 0 0.3rem 0;">Matching</h3>
            <p>Encontre pares entre demandas e ofertas por categoria.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    f"""
    <p style="text-align:center;color:{COLORS['mid']};font-size:0.85rem;">
        Use o menu lateral para navegar entre as seções.<br>
        <em>VedantaMe · Movimento Ramakrishna Vedanta no Brasil · 2026</em>
    </p>
    """,
    unsafe_allow_html=True,
)
