import streamlit as st
from ui.theme import CATEGORIA_COLORS, STATUS_COLORS, COLORS
from core.models import Demanda, Oferta, Membro


def badge(texto: str, cor: str) -> str:
    return f'<span class="badge" style="background-color:{cor};">{texto}</span>'


def badge_categoria(categoria: str) -> str:
    cor = CATEGORIA_COLORS.get(categoria, COLORS["mid"])
    return badge(categoria, cor)


def badge_status(status: str) -> str:
    cor = STATUS_COLORS.get(status, COLORS["mid"])
    return badge(status, cor)


def card_demanda(demanda: Demanda, membro: Membro | None = None):
    nome = membro.nome if membro else demanda.membro_id
    cidade = f" · {membro.cidade}/{membro.estado}" if membro else ""
    html = f"""
    <div class="vedanta-card" style="border-left-color:{CATEGORIA_COLORS.get(demanda.categoria, COLORS['primary'])};">
        <h4>📋 {demanda.descricao[:80]}{"..." if len(demanda.descricao) > 80 else ""}</h4>
        <p>{badge_categoria(demanda.categoria)} {badge_status(demanda.status)}</p>
        <p style="margin-top:0.5rem;">👤 <strong>{nome}</strong>{cidade} &nbsp;|&nbsp; 📅 {demanda.data}</p>
        <p style="margin-top:0.4rem;font-size:0.9rem;color:#555;">{demanda.descricao}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def card_oferta(oferta: Oferta, membro: Membro | None = None):
    nome = membro.nome if membro else oferta.membro_id
    cidade = f" · {membro.cidade}/{membro.estado}" if membro else ""
    html = f"""
    <div class="vedanta-card" style="border-left-color:{CATEGORIA_COLORS.get(oferta.categoria, COLORS['primary'])};">
        <h4>🤲 {oferta.descricao[:80]}{"..." if len(oferta.descricao) > 80 else ""}</h4>
        <p>{badge_categoria(oferta.categoria)}</p>
        <p style="margin-top:0.5rem;">👤 <strong>{nome}</strong>{cidade} &nbsp;|&nbsp; 📅 {oferta.data}</p>
        <p style="margin-top:0.4rem;font-size:0.9rem;color:#555;">{oferta.descricao}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def card_match(demanda: Demanda, oferta: Oferta, membro_d: Membro | None, membro_o: Membro | None):
    nome_d = membro_d.nome if membro_d else demanda.membro_id
    nome_o = membro_o.nome if membro_o else oferta.membro_id
    cor = CATEGORIA_COLORS.get(demanda.categoria, COLORS["primary"])
    html = f"""
    <div class="vedanta-card" style="border-left-color:{cor}; background: linear-gradient(135deg,#fff 80%,#f5f0e8 100%);">
        <p style="margin-bottom:0.3rem;">{badge_categoria(demanda.categoria)} {badge_status(demanda.status)}</p>
        <div style="display:flex;gap:1rem;align-items:flex-start;flex-wrap:wrap;">
            <div style="flex:1;min-width:200px;">
                <p style="font-size:0.8rem;color:{COLORS['mid']};margin:0;">📋 DEMANDA · <strong>{nome_d}</strong></p>
                <p style="font-size:0.92rem;margin:0.3rem 0 0 0;">{demanda.descricao}</p>
            </div>
            <div style="font-size:1.6rem;padding-top:0.5rem;color:{cor};">⇄</div>
            <div style="flex:1;min-width:200px;">
                <p style="font-size:0.8rem;color:{COLORS['mid']};margin:0;">🤲 OFERTA · <strong>{nome_o}</strong></p>
                <p style="font-size:0.92rem;margin:0.3rem 0 0 0;">{oferta.descricao}</p>
            </div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def formulario_demanda(key_prefix: str = "form_d") -> Demanda | None:
    from core.models import CATEGORIAS, STATUS_OPTIONS
    import uuid
    from datetime import date

    with st.form(key=f"{key_prefix}_form"):
        st.markdown("#### Nova Demanda")
        categoria = st.selectbox("Categoria", CATEGORIAS, key=f"{key_prefix}_cat")
        descricao = st.text_area("Descreva sua demanda", height=100, key=f"{key_prefix}_desc")
        nome = st.text_input("Seu nome", key=f"{key_prefix}_nome")
        cidade = st.text_input("Cidade / Estado", key=f"{key_prefix}_cidade")
        submitted = st.form_submit_button("Registrar Demanda")

        if submitted:
            if not descricao.strip() or not nome.strip():
                st.warning("Preencha ao menos o nome e a descrição.")
                return None
            return Demanda(
                id=f"d-{uuid.uuid4().hex[:6]}",
                membro_id=nome.strip(),
                categoria=categoria,
                descricao=descricao.strip(),
                status="Aguardando",
                data=str(date.today()),
            )
    return None


def formulario_oferta(key_prefix: str = "form_o") -> Oferta | None:
    from core.models import CATEGORIAS
    import uuid
    from datetime import date

    with st.form(key=f"{key_prefix}_form"):
        st.markdown("#### Nova Oferta")
        categoria = st.selectbox("Categoria", CATEGORIAS, key=f"{key_prefix}_cat")
        descricao = st.text_area("Descreva o que você oferece", height=100, key=f"{key_prefix}_desc")
        nome = st.text_input("Seu nome", key=f"{key_prefix}_nome")
        cidade = st.text_input("Cidade / Estado", key=f"{key_prefix}_cidade")
        submitted = st.form_submit_button("Registrar Oferta")

        if submitted:
            if not descricao.strip() or not nome.strip():
                st.warning("Preencha ao menos o nome e a descrição.")
                return None
            return Oferta(
                id=f"o-{uuid.uuid4().hex[:6]}",
                membro_id=nome.strip(),
                categoria=categoria,
                descricao=descricao.strip(),
                data=str(date.today()),
            )
    return None
