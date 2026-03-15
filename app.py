## App para execução no Streamlit
import streamlit as st
from ui.theme import inject_css, COLORS
from ui.components import render_logo

st.set_page_config(
    page_title="VedantaMe",
    page_icon="🪷",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

# Sidebar
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

# Home page
st.markdown('<div style="padding:2rem 0 0.5rem 0;">', unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align:center;margin:0.5rem 0;">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" style="max-width:220px;width:100%;">
        <defs>
          <style>
            .petals-outer { transform-origin: 100px 100px; animation: spin-slow 18s linear infinite; }
            .petals-inner { transform-origin: 100px 100px; animation: spin-slow-rev 12s linear infinite; }
            .shatkona     { transform-origin: 100px 100px; animation: pulse 3s ease-in-out infinite; }
            @keyframes spin-slow     { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
            @keyframes spin-slow-rev { from { transform: rotate(0deg); } to { transform: rotate(-360deg); } }
            @keyframes pulse {
              0%, 100% { opacity: 1;   transform: scale(1); }
              50%      { opacity: 0.7; transform: scale(0.93); }
            }
          </style>
        </defs>
        <g class="petals-outer">
          <ellipse cx="100" cy="48" rx="10" ry="24" fill="#C4813A" opacity="0.3" transform="rotate(0   100 100)"/>
          <ellipse cx="100" cy="48" rx="10" ry="24" fill="#C4813A" opacity="0.3" transform="rotate(45  100 100)"/>
          <ellipse cx="100" cy="48" rx="10" ry="24" fill="#C4813A" opacity="0.3" transform="rotate(90  100 100)"/>
          <ellipse cx="100" cy="48" rx="10" ry="24" fill="#C4813A" opacity="0.3" transform="rotate(135 100 100)"/>
          <ellipse cx="100" cy="48" rx="10" ry="24" fill="#C4813A" opacity="0.3" transform="rotate(180 100 100)"/>
          <ellipse cx="100" cy="48" rx="10" ry="24" fill="#C4813A" opacity="0.3" transform="rotate(225 100 100)"/>
          <ellipse cx="100" cy="48" rx="10" ry="24" fill="#C4813A" opacity="0.3" transform="rotate(270 100 100)"/>
          <ellipse cx="100" cy="48" rx="10" ry="24" fill="#C4813A" opacity="0.3" transform="rotate(315 100 100)"/>
        </g>
        <g class="petals-inner">
          <ellipse cx="100" cy="58" rx="8" ry="18" fill="#8B5C2A" opacity="0.55" transform="rotate(22.5  100 100)"/>
          <ellipse cx="100" cy="58" rx="8" ry="18" fill="#8B5C2A" opacity="0.55" transform="rotate(67.5  100 100)"/>
          <ellipse cx="100" cy="58" rx="8" ry="18" fill="#8B5C2A" opacity="0.55" transform="rotate(112.5 100 100)"/>
          <ellipse cx="100" cy="58" rx="8" ry="18" fill="#8B5C2A" opacity="0.55" transform="rotate(157.5 100 100)"/>
          <ellipse cx="100" cy="58" rx="8" ry="18" fill="#8B5C2A" opacity="0.55" transform="rotate(202.5 100 100)"/>
          <ellipse cx="100" cy="58" rx="8" ry="18" fill="#8B5C2A" opacity="0.55" transform="rotate(247.5 100 100)"/>
          <ellipse cx="100" cy="58" rx="8" ry="18" fill="#8B5C2A" opacity="0.55" transform="rotate(292.5 100 100)"/>
          <ellipse cx="100" cy="58" rx="8" ry="18" fill="#8B5C2A" opacity="0.55" transform="rotate(337.5 100 100)"/>
        </g>
        <g class="shatkona">
          <polygon points="100,72 122,110 78,110" fill="none" stroke="#1A1A2E" stroke-width="2"/>
          <polygon points="100,128 122,90  78,90"  fill="none" stroke="#8B5C2A" stroke-width="2"/>
          <circle cx="100" cy="100" r="6" fill="#8B5C2A"/>
          <circle cx="100" cy="100" r="3" fill="#F5F0E8"/>
        </g>
      </svg>
    </div>
    <h1 style="text-align:center;font-family:Georgia,serif;color:#8B5C2A;margin:0.25rem 0 1rem 0;">VedantaMe</h1>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    f"""
    <div style="text-align:center;padding:0.5rem 0 1.5rem 0;">
        <p style="color:{COLORS['mid']};font-size:1.15rem;max-width:600px;margin:0 auto 1.5rem auto;line-height:1.7;">
            Uma rede digital de apoio mútuo do Movimento Ramakrishna Vedanta no Brasil —
            conectando quem <strong>precisa</strong> com quem <strong>pode ajudar</strong>.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown('</div>', unsafe_allow_html=True)

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
