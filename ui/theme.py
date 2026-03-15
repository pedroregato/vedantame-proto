import streamlit as st

COLORS = {
    "primary":    "#8B5C2A",
    "dark":       "#1A1A2E",
    "background": "#F5F0E8",
    "text":       "#2D2D2D",
    "mid":        "#4A4A6A",
    "success":    "#4A7C59",
    "warning":    "#C4813A",
}

CATEGORIA_COLORS = {
    "Moradia Temporária":            "#8B5C2A",
    "Trabalho e Renda":              "#4A7C59",
    "Transporte e Locomoção":        "#4A4A6A",
    "Apoio Emocional e Escuta":      "#C4813A",
    "Saúde e Acompanhamento Médico": "#2E7D9A",
    "Eventos e Projetos Espirituais":"#7B3FA0",
    "Talentos e Habilidades":        "#B5451B",
    "Apoio Espiritual":              "#1A6B4A",
    "Bate-papo Vedanta":             "#5C4033",
}

STATUS_COLORS = {
    "Aguardando": "#C4813A",
    "Em contato": "#2E7D9A",
    "Resolvido":  "#4A7C59",
}


def inject_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Lato', sans-serif;
            color: {COLORS['text']};
        }}

        h1, h2, h3 {{
            font-family: Georgia, 'Times New Roman', serif;
            color: {COLORS['dark']};
        }}

        .stApp {{
            background-color: {COLORS['background']};
        }}

        section[data-testid="stSidebar"] {{
            background-color: {COLORS['dark']};
        }}

        section[data-testid="stSidebar"] * {{
            color: {COLORS['background']} !important;
        }}

        .vedanta-card {{
            background: #fff;
            border-radius: 12px;
            padding: 1.2rem 1.4rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 8px rgba(26,26,46,0.08);
            border-left: 4px solid {COLORS['primary']};
        }}

        .vedanta-card h4 {{
            font-family: Georgia, serif;
            margin: 0 0 0.3rem 0;
            font-size: 1rem;
            color: {COLORS['dark']};
        }}

        .vedanta-card p {{
            margin: 0.2rem 0;
            font-size: 0.92rem;
            color: {COLORS['mid']};
        }}

        .badge {{
            display: inline-block;
            padding: 0.2rem 0.7rem;
            border-radius: 20px;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.03em;
            color: #fff;
            margin-right: 0.4rem;
        }}

        .match-connector {{
            text-align: center;
            font-size: 1.5rem;
            color: {COLORS['primary']};
            padding: 0.3rem 0;
        }}

        .stButton > button {{
            background-color: {COLORS['primary']};
            color: #fff;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1.4rem;
            font-weight: 700;
            transition: background 0.2s;
        }}

        .stButton > button:hover {{
            background-color: {COLORS['warning']};
        }}

        hr {{
            border: none;
            border-top: 1px solid #e0d8cc;
            margin: 1.5rem 0;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
