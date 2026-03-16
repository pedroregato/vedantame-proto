"""
ui/hero.py
----------
Hero carrossel da página inicial do VedantaMe.
Módulo autônomo — não depende de nenhum outro arquivo de ui/.
Inspirado no deck "The Living Thread of Seva and Sanga" (NotebookLM, março 2026).

Uso:
    from ui.hero import render_hero
    render_hero()
"""

import time
import streamlit as st

# ── Paleta (espelha ui/theme.py sem importá-la) ─────────────────────────────
_CREAM   = "#F7F2E9"
_DARK    = "#2C1810"
_TERRA   = "#8B3A2A"
_AMBER   = "#C8860A"
_GOLD    = "#D4A843"
_MID     = "#6B5240"
_MUTED   = "#8B7355"
_BORDER  = "rgba(139,58,42,0.15)"

# ── Configurações do carrossel ───────────────────────────────────────────────
_TOTAL_SLIDES  = 5
_AUTO_INTERVAL = 6          # segundos entre avanços automáticos
_STATE_IDX     = "hero_slide_idx"
_STATE_AUTO    = "hero_auto_play"
_STATE_LAST    = "hero_last_auto"


# ────────────────────────────────────────────────────────────────────────────
# CSS — injetado uma única vez por sessão
# ────────────────────────────────────────────────────────────────────────────
_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&display=swap');

/* ── Hero wrapper ── */
.vm-hero {{
    position: relative;
    width: 100%;
    background: {_CREAM};
    border-radius: 8px;
    overflow: hidden;
    margin-bottom: 1.5rem;
    border: 1px solid {_BORDER};
}}

.vm-hero::before {{
    content: '';
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse at 10% 20%, rgba(200,134,10,0.07) 0%, transparent 55%),
        radial-gradient(ellipse at 90% 80%, rgba(139,58,42,0.06) 0%, transparent 55%);
    pointer-events: none;
    z-index: 0;
}}

/* ── Slide genérico ── */
.vm-slide {{
    position: relative;
    z-index: 1;
    padding: 2.8rem 3rem 2.2rem;
    min-height: 320px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    animation: vmFadeIn 0.5s ease forwards;
}}

@keyframes vmFadeIn {{
    from {{ opacity: 0; transform: translateY(10px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}

/* ── Eyebrow label ── */
.vm-eyebrow {{
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: {_AMBER};
    margin-bottom: 0.4rem;
    text-align: center;
}}

/* ── Títulos ── */
.vm-slide h1 {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(2.6rem, 6vw, 4.2rem);
    font-weight: 400;
    color: {_DARK};
    letter-spacing: -0.01em;
    line-height: 1;
    margin: 0 0 0.4rem;
    text-align: center;
}}

.vm-slide h2 {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(1.6rem, 3.5vw, 2.4rem);
    font-weight: 400;
    color: {_DARK};
    line-height: 1.2;
    margin: 0 0 1.6rem;
    text-align: center;
}}

/* ── Subtítulo/descrição ── */
.vm-subtitle {{
    font-family: 'EB Garamond', Georgia, serif;
    font-size: clamp(0.95rem, 1.8vw, 1.15rem);
    color: {_MID};
    font-style: italic;
    margin-bottom: 0.4rem;
    text-align: center;
    letter-spacing: 0.02em;
}}

.vm-desc {{
    font-family: 'EB Garamond', Georgia, serif;
    font-size: clamp(0.88rem, 1.5vw, 1rem);
    color: {_MUTED};
    max-width: 520px;
    text-align: center;
    line-height: 1.75;
    margin: 0 auto 2rem;
}}

/* ── Fio vivo (hero) ── */
.vm-living-thread {{
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1rem;
    gap: 0;
}}

.vm-thread-line {{
    height: 1px;
    width: 72px;
    background: linear-gradient(90deg, transparent, {_AMBER}, transparent);
}}

.vm-thread-dot {{
    width: 8px; height: 8px;
    border-radius: 50%;
    background: {_AMBER};
    box-shadow: 0 0 10px rgba(200,134,10,0.55);
    margin: 0 6px;
    flex-shrink: 0;
}}

.vm-thread-dot-sm {{
    width: 5px; height: 5px;
    border-radius: 50%;
    background: {_GOLD};
    opacity: 0.5;
    margin: 0 6px;
    flex-shrink: 0;
}}

/* ── CTA ── */
.vm-cta {{
    display: inline-block;
    background: {_TERRA};
    color: {_CREAM};
    padding: 0.65rem 2rem;
    border-radius: 2px;
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.95rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    text-decoration: none;
    border: 1px solid {_TERRA};
    transition: background 0.2s;
}}

.vm-cta:hover {{ background: #6B2A1A; color: {_CREAM}; }}

/* ── Grid dos Eixos ── */
.vm-pillars {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.2rem;
    width: 100%;
    max-width: 820px;
    margin: 0 auto;
}}

.vm-pillar {{
    padding: 1.6rem 1.5rem;
    border-radius: 4px;
    text-align: left;
    border: 1px solid;
    position: relative;
    overflow: hidden;
}}

.vm-pillar::before {{
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
}}

.vm-pillar-vuln {{
    background: rgba(139,58,42,0.05);
    border-color: rgba(139,58,42,0.2);
}}

.vm-pillar-vuln::before {{
    background: linear-gradient(90deg, {_TERRA}, {_AMBER});
}}

.vm-pillar-ideas {{
    background: rgba(200,134,10,0.05);
    border-color: rgba(200,134,10,0.22);
}}

.vm-pillar-ideas::before {{
    background: linear-gradient(90deg, {_AMBER}, {_GOLD});
}}

.vm-pillar-icon {{ font-size: 1.7rem; margin-bottom: 0.6rem; }}

.vm-pillar h3 {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.25rem;
    font-weight: 600;
    color: {_DARK};
    margin: 0 0 0.4rem;
}}

.vm-pillar p {{
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.9rem;
    color: {_MID};
    line-height: 1.65;
    margin: 0 0 0.8rem;
}}

.vm-tags {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
}}

.vm-tag {{
    font-size: 0.72rem;
    padding: 0.15rem 0.55rem;
    border-radius: 2px;
    letter-spacing: 0.04em;
    font-family: 'EB Garamond', Georgia, serif;
}}

.vm-tag-coral {{ background: rgba(139,58,42,0.1); color: #6B2A1A; }}
.vm-tag-amber {{ background: rgba(200,134,10,0.12); color: #7A5000; }}

/* ── Tiers do matching ── */
.vm-tiers {{
    display: flex;
    flex-direction: column;
    gap: 0.9rem;
    width: 100%;
    max-width: 660px;
    margin: 0 auto;
}}

.vm-tier {{
    display: flex;
    align-items: center;
    gap: 1.2rem;
    padding: 1rem 1.4rem;
    border-radius: 4px;
    text-align: left;
    border: 1px solid;
    transition: transform 0.2s;
}}

.vm-tier:hover {{ transform: translateX(4px); }}

.vm-tier-1 {{
    background: rgba(212,168,67,0.07);
    border-color: rgba(212,168,67,0.28);
}}

.vm-tier-2 {{
    background: rgba(139,58,42,0.06);
    border-color: rgba(139,58,42,0.2);
}}

.vm-tier-3 {{
    background: rgba(200,134,10,0.05);
    border-color: rgba(200,134,10,0.18);
}}

.vm-tier-badge {{
    width: 44px; height: 44px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem;
    flex-shrink: 0;
}}

.vm-tier-1 .vm-tier-badge {{ background: rgba(212,168,67,0.18); }}
.vm-tier-2 .vm-tier-badge {{ background: rgba(139,58,42,0.14); }}
.vm-tier-3 .vm-tier-badge {{ background: rgba(200,134,10,0.14); }}

.vm-tier h4 {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.1rem;
    font-weight: 600;
    color: {_DARK};
    margin: 0 0 0.15rem;
}}

.vm-tier p {{
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.87rem;
    color: {_MID};
    line-height: 1.55;
    margin: 0;
}}

/* ── Métricas Pulso ── */
.vm-metrics {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    width: 100%;
    max-width: 720px;
    margin: 0 auto;
}}

.vm-metric {{
    background: white;
    border: 1px solid {_BORDER};
    border-radius: 4px;
    padding: 1.4rem 1rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}}

.vm-metric::after {{
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, {_TERRA}, {_GOLD});
}}

.vm-metric-icon {{ font-size: 1.4rem; margin-bottom: 0.4rem; }}

.vm-metric-num {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 2.2rem;
    font-weight: 600;
    color: {_TERRA};
    line-height: 1;
    margin-bottom: 0.25rem;
}}

.vm-metric-label {{
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.8rem;
    color: {_MUTED};
    line-height: 1.4;
}}

.vm-metric-trend {{
    font-size: 0.72rem;
    color: #3B7A2A;
    margin-top: 0.25rem;
    font-family: 'EB Garamond', Georgia, serif;
}}

/* ── Gateway steps ── */
.vm-gateway {{
    display: flex;
    align-items: flex-start;
    justify-content: center;
    gap: 0;
    width: 100%;
    max-width: 820px;
    margin: 0 auto;
    flex-wrap: wrap;
}}

.vm-gstep {{
    flex: 1;
    min-width: 120px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    position: relative;
    padding: 0 0.4rem;
}}

.vm-gstep::after {{
    content: '→';
    position: absolute;
    right: -10px;
    top: 16px;
    color: {_AMBER};
    font-size: 1rem;
    opacity: 0.45;
}}

.vm-gstep:last-child::after {{ display: none; }}

.vm-gstep-circle {{
    width: 48px; height: 48px;
    border-radius: 50%;
    background: rgba(139,58,42,0.07);
    border: 1.5px solid rgba(139,58,42,0.22);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem;
    margin-bottom: 0.65rem;
    transition: all 0.25s;
}}

.vm-gstep:hover .vm-gstep-circle {{
    background: rgba(139,58,42,0.14);
    transform: scale(1.08);
}}

.vm-gstep-label {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 0.92rem;
    font-weight: 600;
    color: {_DARK};
    margin-bottom: 0.2rem;
}}

.vm-gstep-desc {{
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.78rem;
    color: {_MUTED};
    line-height: 1.5;
}}

/* ── Responsive ── */
@media (max-width: 680px) {{
    .vm-slide {{ padding: 2rem 1.2rem 1.6rem; min-height: 260px; }}
    .vm-pillars {{ grid-template-columns: 1fr; }}
    .vm-metrics {{ grid-template-columns: 1fr 1fr; }}
    .vm-gstep::after {{ display: none; }}
    .vm-gateway {{ gap: 0.8rem; }}
}}
</style>
"""

# ── Conteúdo HTML dos 5 slides ───────────────────────────────────────────────
_SLIDES = [

    # 1 — Hero
    """
    <div class="vm-slide">
      <div class="vm-living-thread">
        <div class="vm-thread-line"></div>
        <div class="vm-thread-dot"></div>
        <div class="vm-thread-line"></div>
        <div class="vm-thread-dot-sm"></div>
        <div class="vm-thread-line"></div>
      </div>
      <h1>VedantaMe</h1>
      <p class="vm-subtitle">The Living Thread of Seva and Sanga</p>
      <p class="vm-desc">
        Uma rede digital de apoio mútuo para membros, amigos e simpatizantes
        do Movimento Ramakrishna Vedanta no Brasil — conectando quem tem uma
        demanda com quem tem uma solução.
      </p>
      <a href="#" class="vm-cta">Solicitar Convite</a>
    </div>
    """,

    # 2 — Dois Eixos
    """
    <div class="vm-slide">
      <div class="vm-eyebrow">Os dois eixos da plataforma</div>
      <h2>Uma rede viva de solidariedade</h2>
      <div class="vm-pillars">
        <div class="vm-pillar vm-pillar-vuln">
          <div class="vm-pillar-icon">🏠</div>
          <h3>Eixo 1 — Vulnerabilidade</h3>
          <p>Membros em dificuldade financeira, emocional, de saúde ou profissional encontram apoio real dentro da própria sanga.</p>
          <div class="vm-tags">
            <span class="vm-tag vm-tag-coral">Moradia</span>
            <span class="vm-tag vm-tag-coral">Trabalho</span>
            <span class="vm-tag vm-tag-coral">Saúde</span>
            <span class="vm-tag vm-tag-coral">Apoio Emocional</span>
          </div>
        </div>
        <div class="vm-pillar vm-pillar-ideas">
          <div class="vm-pillar-icon">✨</div>
          <h3>Eixo 2 — Ideias e Inspirações</h3>
          <p>Membros com energia criativa conectam-se com quem pode colaborar e transformar iniciativas individuais em realizações coletivas.</p>
          <div class="vm-tags">
            <span class="vm-tag vm-tag-amber">Talentos</span>
            <span class="vm-tag vm-tag-amber">Projetos</span>
            <span class="vm-tag vm-tag-amber">Apoio Espiritual</span>
            <span class="vm-tag vm-tag-amber">Grupos de Estudo</span>
          </div>
        </div>
      </div>
    </div>
    """,

    # 3 — Motor de Matching
    """
    <div class="vm-slide">
      <div class="vm-eyebrow">Como funciona</div>
      <h2>O Motor de Conexão</h2>
      <div class="vm-tiers">
        <div class="vm-tier vm-tier-1">
          <div class="vm-tier-badge">🤝</div>
          <div>
            <h4>Tier 1 — A Comunidade (Orgânico)</h4>
            <p>Demandas abertas são postadas e respondidas diretamente pelos membros da sanga.</p>
          </div>
        </div>
        <div class="vm-tier vm-tier-2">
          <div class="vm-tier-badge">🛡️</div>
          <div>
            <h4>Tier 2 — Os Curadores (Moderação Humana)</h4>
            <p>Equipe designada coordena pedidos sensíveis com alinhamento ético ao Vedanta.</p>
          </div>
        </div>
        <div class="vm-tier vm-tier-3">
          <div class="vm-tier-badge">✦</div>
          <div>
            <h4>Tier 3 — O Assistente Inteligente (IA)</h4>
            <p>Sistema de matching sugere conexões trabalhando silenciosamente em segundo plano.</p>
          </div>
        </div>
      </div>
    </div>
    """,

    # 4 — Pulso da Sanga
    """
    <div class="vm-slide">
      <div class="vm-eyebrow">Impacto em tempo real</div>
      <h2>Pulso da Sanga</h2>
      <p class="vm-desc" style="margin-bottom:1.4rem;">
        Um painel vivo que transforma dados em um sentimento tangível de conquista coletiva.
      </p>
      <div class="vm-metrics">
        <div class="vm-metric">
          <div class="vm-metric-icon">🤲</div>
          <div class="vm-metric-num">247</div>
          <div class="vm-metric-label">Demandas atendidas este mês</div>
          <div class="vm-metric-trend">↑ +15% vs. mês anterior</div>
        </div>
        <div class="vm-metric">
          <div class="vm-metric-icon">🎁</div>
          <div class="vm-metric-num">183</div>
          <div class="vm-metric-label">Ofertas de apoio disponíveis</div>
          <div class="vm-metric-trend">↑ +8% esta semana</div>
        </div>
        <div class="vm-metric">
          <div class="vm-metric-icon">🌱</div>
          <div class="vm-metric-num">94%</div>
          <div class="vm-metric-label">Taxa de resolução da comunidade</div>
          <div class="vm-metric-trend">↑ Recorde histórico</div>
        </div>
      </div>
    </div>
    """,

    # 5 — Gateway
    """
    <div class="vm-slide">
      <div class="vm-eyebrow">Como participar</div>
      <h2>O Portal de Entrada</h2>
      <div class="vm-gateway">
        <div class="vm-gstep">
          <div class="vm-gstep-circle">📱</div>
          <div class="vm-gstep-label">Descubra</div>
          <div class="vm-gstep-desc">Encontre o VedantaMe pelas redes sociais</div>
        </div>
        <div class="vm-gstep">
          <div class="vm-gstep-circle">🪷</div>
          <div class="vm-gstep-label">Conheça</div>
          <div class="vm-gstep-desc">Explore os valores e a missão</div>
        </div>
        <div class="vm-gstep">
          <div class="vm-gstep-circle">✉️</div>
          <div class="vm-gstep-label">Solicite</div>
          <div class="vm-gstep-desc">Peça convite ou seja indicado por um membro</div>
        </div>
        <div class="vm-gstep">
          <div class="vm-gstep-circle">🛡️</div>
          <div class="vm-gstep-label">Avaliação</div>
          <div class="vm-gstep-desc">Moderador curador aprova o ingresso</div>
        </div>
        <div class="vm-gstep">
          <div class="vm-gstep-circle">🌟</div>
          <div class="vm-gstep-label">Bem-vindo!</div>
          <div class="vm-gstep-desc">Acesso e acolhimento pela sanga</div>
        </div>
      </div>
    </div>
    """,
]


# ────────────────────────────────────────────────────────────────────────────
# Função pública
# ────────────────────────────────────────────────────────────────────────────
def render_hero() -> None:
    """
    Renderiza o hero carrossel na página atual do Streamlit.
    Gerencia seu próprio estado em st.session_state com prefixo 'hero_'.
    Pode ser chamado em qualquer ponto do layout, após st.set_page_config().
    """

    # ── Inicializa estado ────────────────────────────────────────────────────
    if _STATE_IDX  not in st.session_state:
        st.session_state[_STATE_IDX]  = 0
    if _STATE_AUTO not in st.session_state:
        st.session_state[_STATE_AUTO] = True
    if _STATE_LAST not in st.session_state:
        st.session_state[_STATE_LAST] = time.time()

    idx  = st.session_state[_STATE_IDX]
    auto = st.session_state[_STATE_AUTO]

    # ── Auto-play ────────────────────────────────────────────────────────────
    if auto:
        now = time.time()
        if now - st.session_state[_STATE_LAST] >= _AUTO_INTERVAL:
            st.session_state[_STATE_IDX]  = (idx + 1) % _TOTAL_SLIDES
            st.session_state[_STATE_LAST] = now
            idx = st.session_state[_STATE_IDX]

    # ── Injeta CSS (uma vez por sessão) ─────────────────────────────────────
    if "hero_css_injected" not in st.session_state:
        st.markdown(_CSS, unsafe_allow_html=True)
        st.session_state["hero_css_injected"] = True

    # ── Renderiza slide atual ────────────────────────────────────────────────
    st.markdown(
        f'<div class="vm-hero">{_SLIDES[idx]}</div>',
        unsafe_allow_html=True,
    )

    # ── Controles ────────────────────────────────────────────────────────────
    labels = ["① Hero", "② Eixos", "③ Matching", "④ Pulso", "⑤ Portal"]

    cols = st.columns([0.5, 0.4, 1, 1, 1, 1, 1, 0.4, 0.7, 0.5])

    # Botão anterior
    with cols[1]:
        if st.button("←", key="hero_prev", help="Slide anterior", use_container_width=True):
            st.session_state[_STATE_IDX]  = (idx - 1) % _TOTAL_SLIDES
            st.session_state[_STATE_AUTO] = False
            st.session_state[_STATE_LAST] = time.time()
            st.rerun()

    # Dots de navegação
    for i, col in enumerate(cols[2:7]):
        with col:
            btn_type = "primary" if i == idx else "secondary"
            if st.button(labels[i], key=f"hero_dot_{i}", use_container_width=True, type=btn_type):
                st.session_state[_STATE_IDX]  = i
                st.session_state[_STATE_AUTO] = False
                st.session_state[_STATE_LAST] = time.time()
                st.rerun()

    # Botão próximo
    with cols[7]:
        if st.button("→", key="hero_next", help="Próximo slide", use_container_width=True):
            st.session_state[_STATE_IDX]  = (idx + 1) % _TOTAL_SLIDES
            st.session_state[_STATE_AUTO] = False
            st.session_state[_STATE_LAST] = time.time()
            st.rerun()

    # Botão auto-play
    with cols[8]:
        label = "⏸ Pausar" if auto else "▶ Auto"
        if st.button(label, key="hero_auto", use_container_width=True):
            st.session_state[_STATE_AUTO] = not auto
            st.session_state[_STATE_LAST] = time.time()
            st.rerun()

    st.markdown("<div style='margin-bottom:1.2rem;'></div>", unsafe_allow_html=True)

    # ── Re-run para auto-play ────────────────────────────────────────────────
    if st.session_state[_STATE_AUTO]:
        time.sleep(0.5)
        st.rerun()
