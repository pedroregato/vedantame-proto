## App para execução no Streamlit
import streamlit as st
from ui.theme import inject_css, COLORS
from ui.components import render_logo, render_symbol

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

# ── Texto motivacional ────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div style="
        max-width: 680px;
        margin: 0.5rem auto 2rem auto;
        text-align: center;
        padding: 0 1rem;
    ">
        <p style="
            font-family: Georgia, serif;
            font-size: 1.15rem;
            color: {COLORS['mid']};
            line-height: 1.85;
            margin-bottom: 0.9rem;
        ">
            Em toda comunidade existe uma teia invisível de dons e necessidades —
            talentos que aguardam uma chamada, mãos prontas para estender-se,
            corações que buscam encontrar os seus.
        </p>
        <p style="
            font-family: Georgia, serif;
            font-size: 1.05rem;
            color: {COLORS['mid']};
            line-height: 1.85;
            margin-bottom: 0.9rem;
        ">
            O <strong style="color:{COLORS['primary']};">VedantaMe</strong> nasce
            para tornar essa teia visível — um espaço onde o
            <em>seva</em> (serviço desinteressado) e a <em>sanga</em>
            (associação com o sagrado) ganham forma digital,
            conectando quem precisa com quem pode ajudar.
        </p>
        <p style="
            font-family: Georgia, serif;
            font-size: 0.95rem;
            color: {COLORS['mid']};
            line-height: 1.75;
            font-style: italic;
        ">
            Liderado pelo Swami Nirmalatmananda, o projeto é uma iniciativa
            do Movimento Ramakrishna Vedanta no Brasil — aberta a membros,
            amigos e simpatizantes que desejam servir e ser servidos com amor.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

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
