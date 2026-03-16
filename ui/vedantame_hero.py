"""
VedantaMe · Hero Carrossel para Streamlit
Página inicial da aplicação — inspirado no deck "The Living Thread of Seva and Sanga"
Paleta: creme (#F5F0E8), terracota (#8B3A2A), âmbar (#C8860A), dourado (#D4A843), marrom escuro (#2C1810)
Tipografia: Georgia (serif) para títulos, estilo refinado/editorial
"""

import streamlit as st
import time

# ── Configuração da página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="VedantaMe",
    page_icon="🪷",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS principal ────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&display=swap');

/* Reset & base */
*, *::before, *::after { box-sizing: border-box; }

.stApp {
    background: #F7F2E9;
    font-family: 'EB Garamond', Georgia, serif;
}

/* Esconde elementos padrão do Streamlit */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }

/* ── HERO WRAPPER ── */
.hero-wrapper {
    position: relative;
    width: 100%;
    min-height: 100vh;
    background: #F7F2E9;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Textura de fundo sutil */
.hero-wrapper::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image:
        radial-gradient(ellipse at 15% 20%, rgba(200,134,10,0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 85% 80%, rgba(139,58,42,0.07) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 50%, rgba(212,168,67,0.04) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

/* ── NAVBAR ── */
.vm-navbar {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.4rem 3.5rem;
    position: relative;
    z-index: 10;
    border-bottom: 1px solid rgba(139,58,42,0.12);
}

.vm-logo {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.6rem;
    font-weight: 600;
    color: #2C1810;
    letter-spacing: 0.02em;
}

.vm-logo span {
    color: #8B3A2A;
}

.vm-tagline-nav {
    font-size: 0.82rem;
    color: #8B7355;
    font-style: italic;
    letter-spacing: 0.05em;
}

/* ── CARROSSEL ── */
.carousel-outer {
    position: relative;
    z-index: 5;
    width: 100%;
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2rem 2rem 1rem;
}

/* Slide container */
.slide {
    display: none;
    width: 100%;
    max-width: 960px;
    margin: 0 auto;
    animation: fadeSlide 0.6s ease forwards;
}

.slide.active {
    display: flex;
    flex-direction: column;
    align-items: center;
}

@keyframes fadeSlide {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ── Slide 1: Hero ── */
.slide-hero {
    text-align: center;
    padding: 3rem 2rem 2rem;
}

.slide-hero .living-thread {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.2rem;
}

.slide-hero .thread-line {
    height: 1px;
    width: 80px;
    background: linear-gradient(90deg, transparent, #C8860A, transparent);
}

.thread-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: #C8860A;
    box-shadow: 0 0 12px rgba(200,134,10,0.5);
    margin: 0 8px;
}

.slide-hero h1 {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(3.5rem, 8vw, 6rem);
    font-weight: 400;
    color: #2C1810;
    letter-spacing: -0.01em;
    line-height: 1;
    margin: 0 0 0.6rem;
}

.slide-hero .subtitle {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: clamp(1rem, 2vw, 1.3rem);
    color: #6B5240;
    font-style: italic;
    margin-bottom: 0.5rem;
    letter-spacing: 0.02em;
}

.slide-hero .description {
    font-size: clamp(0.9rem, 1.5vw, 1.05rem);
    color: #8B7355;
    max-width: 520px;
    margin: 0 auto 2.5rem;
    line-height: 1.7;
}

.vm-cta {
    display: inline-block;
    background: #8B3A2A;
    color: #F7F2E9;
    padding: 0.75rem 2.2rem;
    border-radius: 2px;
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 1rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    text-decoration: none;
    transition: background 0.2s, transform 0.2s;
    border: 1px solid #8B3A2A;
}

.vm-cta:hover {
    background: #6B2A1A;
    transform: translateY(-1px);
}

/* ── Slide 2: Dois pilares ── */
.slide-pillars {
    padding: 2.5rem 1rem;
    text-align: center;
    width: 100%;
}

.slide-pillars .slide-eyebrow {
    font-size: 0.78rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #C8860A;
    margin-bottom: 0.5rem;
}

.slide-pillars h2 {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(1.8rem, 4vw, 2.8rem);
    font-weight: 400;
    color: #2C1810;
    margin-bottom: 2.5rem;
    line-height: 1.2;
}

.pillars-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    max-width: 860px;
    margin: 0 auto;
}

.pillar-card {
    padding: 2rem 1.8rem;
    border-radius: 4px;
    text-align: left;
    position: relative;
    overflow: hidden;
}

.pillar-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
}

.pillar-vuln {
    background: rgba(139,58,42,0.07);
    border: 1px solid rgba(139,58,42,0.18);
}
.pillar-vuln::before { background: linear-gradient(90deg, #8B3A2A, #C8860A); }

.pillar-ideas {
    background: rgba(200,134,10,0.06);
    border: 1px solid rgba(200,134,10,0.2);
}
.pillar-ideas::before { background: linear-gradient(90deg, #C8860A, #D4A843); }

.pillar-icon {
    font-size: 2rem;
    margin-bottom: 0.8rem;
    display: block;
}

.pillar-card h3 {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.5rem;
    font-weight: 600;
    color: #2C1810;
    margin-bottom: 0.5rem;
}

.pillar-card p {
    font-size: 0.93rem;
    color: #6B5240;
    line-height: 1.65;
    margin-bottom: 1rem;
}

.pillar-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
}

.pillar-tag {
    font-size: 0.75rem;
    padding: 0.2rem 0.6rem;
    border-radius: 2px;
    letter-spacing: 0.04em;
}

.tag-coral { background: rgba(139,58,42,0.1); color: #6B2A1A; }
.tag-amber { background: rgba(200,134,10,0.12); color: #7A5000; }

/* ── Slide 3: Motor de Matching ── */
.slide-matching {
    padding: 2.5rem 1rem;
    text-align: center;
    width: 100%;
}

.slide-matching .slide-eyebrow {
    font-size: 0.78rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #C8860A;
    margin-bottom: 0.5rem;
}

.slide-matching h2 {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(1.8rem, 4vw, 2.8rem);
    font-weight: 400;
    color: #2C1810;
    margin-bottom: 2rem;
}

.matching-tiers {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 680px;
    margin: 0 auto;
}

.tier-item {
    display: flex;
    align-items: center;
    gap: 1.4rem;
    padding: 1.2rem 1.6rem;
    border-radius: 4px;
    text-align: left;
    border: 1px solid;
    transition: transform 0.2s;
}

.tier-item:hover { transform: translateX(4px); }

.tier-1 { background: rgba(212,168,67,0.08); border-color: rgba(212,168,67,0.25); }
.tier-2 { background: rgba(139,58,42,0.07); border-color: rgba(139,58,42,0.2); }
.tier-3 { background: rgba(200,134,10,0.06); border-color: rgba(200,134,10,0.18); }

.tier-badge {
    width: 48px; height: 48px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.4rem;
    flex-shrink: 0;
}

.tier-1 .tier-badge { background: rgba(212,168,67,0.2); }
.tier-2 .tier-badge { background: rgba(139,58,42,0.15); }
.tier-3 .tier-badge { background: rgba(200,134,10,0.15); }

.tier-content h4 {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.2rem;
    font-weight: 600;
    color: #2C1810;
    margin-bottom: 0.2rem;
}

.tier-content p {
    font-size: 0.9rem;
    color: #6B5240;
    line-height: 1.55;
    margin: 0;
}

/* ── Slide 4: Pulso da Sanga ── */
.slide-pulso {
    padding: 2.5rem 1rem;
    text-align: center;
    width: 100%;
}

.slide-pulso .slide-eyebrow {
    font-size: 0.78rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #C8860A;
    margin-bottom: 0.5rem;
}

.slide-pulso h2 {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(1.8rem, 4vw, 2.8rem);
    font-weight: 400;
    color: #2C1810;
    margin-bottom: 0.5rem;
}

.slide-pulso .slide-desc {
    font-size: 0.95rem;
    color: #8B7355;
    font-style: italic;
    margin-bottom: 2rem;
    max-width: 500px;
    margin-left: auto;
    margin-right: auto;
}

.pulso-metrics {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.2rem;
    max-width: 760px;
    margin: 0 auto 1.5rem;
}

.metric-card {
    background: white;
    border: 1px solid rgba(139,58,42,0.12);
    border-radius: 4px;
    padding: 1.6rem 1rem;
    position: relative;
    overflow: hidden;
}

.metric-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #8B3A2A, #D4A843);
}

.metric-icon { font-size: 1.5rem; margin-bottom: 0.5rem; }

.metric-number {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 2.4rem;
    font-weight: 600;
    color: #8B3A2A;
    line-height: 1;
    margin-bottom: 0.3rem;
}

.metric-label {
    font-size: 0.82rem;
    color: #8B7355;
    line-height: 1.4;
    letter-spacing: 0.02em;
}

.metric-trend {
    font-size: 0.75rem;
    color: #3B7A2A;
    font-weight: 500;
    margin-top: 0.3rem;
}

/* ── Slide 5: Gateway ── */
.slide-gateway {
    padding: 2.5rem 1rem;
    text-align: center;
    width: 100%;
}

.slide-gateway .slide-eyebrow {
    font-size: 0.78rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #C8860A;
    margin-bottom: 0.5rem;
}

.slide-gateway h2 {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(1.8rem, 4vw, 2.8rem);
    font-weight: 400;
    color: #2C1810;
    margin-bottom: 2rem;
}

.gateway-steps {
    display: flex;
    align-items: flex-start;
    justify-content: center;
    gap: 0;
    max-width: 860px;
    margin: 0 auto;
    flex-wrap: wrap;
}

.gateway-step {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    flex: 1;
    min-width: 140px;
    position: relative;
    padding: 0 0.5rem;
}

.gateway-step::after {
    content: '→';
    position: absolute;
    right: -12px;
    top: 20px;
    color: #C8860A;
    font-size: 1.2rem;
    opacity: 0.5;
}

.gateway-step:last-child::after { display: none; }

.step-circle {
    width: 52px; height: 52px;
    border-radius: 50%;
    background: rgba(139,58,42,0.08);
    border: 1.5px solid rgba(139,58,42,0.25);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.4rem;
    margin-bottom: 0.8rem;
    transition: all 0.3s;
}

.gateway-step:hover .step-circle {
    background: rgba(139,58,42,0.15);
    transform: scale(1.08);
}

.step-label {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 0.95rem;
    font-weight: 600;
    color: #2C1810;
    margin-bottom: 0.3rem;
}

.step-desc {
    font-size: 0.8rem;
    color: #8B7355;
    line-height: 1.5;
}

/* ── CONTROLES DO CARROSSEL ── */
.carousel-controls {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1.5rem;
    padding: 1.5rem 0 2rem;
    position: relative;
    z-index: 10;
    width: 100%;
}

.carousel-dots {
    display: flex;
    gap: 0.5rem;
    align-items: center;
}

.dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: rgba(139,58,42,0.2);
    cursor: pointer;
    transition: all 0.3s;
    border: none;
    padding: 0;
}

.dot.active {
    background: #8B3A2A;
    width: 22px;
    border-radius: 3px;
}

.nav-btn {
    background: transparent;
    border: 1px solid rgba(139,58,42,0.3);
    color: #8B3A2A;
    width: 36px; height: 36px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 1rem;
    display: flex; align-items: center; justify-content: center;
    transition: all 0.2s;
}

.nav-btn:hover {
    background: rgba(139,58,42,0.08);
    border-color: #8B3A2A;
}

/* ── RODAPÉ ── */
.vm-footer {
    text-align: center;
    padding: 1rem;
    font-size: 0.75rem;
    color: #A89880;
    font-style: italic;
    letter-spacing: 0.05em;
    border-top: 1px solid rgba(139,58,42,0.08);
    position: relative;
    z-index: 5;
    width: 100%;
}

/* Responsive */
@media (max-width: 640px) {
    .pillars-grid { grid-template-columns: 1fr; }
    .pulso-metrics { grid-template-columns: 1fr 1fr; }
    .vm-navbar { padding: 1rem 1.5rem; }
    .vm-tagline-nav { display: none; }
    .gateway-steps { gap: 1rem; }
    .gateway-step::after { display: none; }
}
</style>
""", unsafe_allow_html=True)

# ── Estado do carrossel ──────────────────────────────────────────────────────
if "slide_idx" not in st.session_state:
    st.session_state.slide_idx = 0
if "auto_play" not in st.session_state:
    st.session_state.auto_play = True
if "last_auto" not in st.session_state:
    st.session_state.last_auto = time.time()

TOTAL_SLIDES = 5
AUTO_INTERVAL = 6  # segundos

# ── Slides: conteúdo ─────────────────────────────────────────────────────────
slides_html = [

    # ── Slide 1: Hero ──
    """
    <div class="slide active slide-hero">
      <div class="living-thread">
        <div class="thread-line"></div>
        <div class="thread-dot"></div>
        <div class="thread-line"></div>
        <div class="thread-dot" style="opacity:0.5; width:5px; height:5px;"></div>
        <div class="thread-line"></div>
      </div>
      <h1>VedantaMe</h1>
      <p class="subtitle">The Living Thread of Seva and Sanga</p>
      <p class="description">
        Uma rede digital de apoio mútuo para membros, amigos e simpatizantes 
        do Movimento Ramakrishna Vedanta no Brasil — conectando quem tem uma 
        demanda com quem tem uma solução.
      </p>
      <a href="#" class="vm-cta">Solicitar Convite</a>
    </div>
    """,

    # ── Slide 2: Dois Eixos ──
    """
    <div class="slide active slide-pillars">
      <div class="slide-eyebrow">Os dois eixos da plataforma</div>
      <h2>Uma rede viva de solidariedade</h2>
      <div class="pillars-grid">
        <div class="pillar-card pillar-vuln">
          <span class="pillar-icon">🏠</span>
          <h3>Eixo 1 — Vulnerabilidade</h3>
          <p>
            Membros em situação de dificuldade financeira, emocional, de saúde 
            ou profissional encontram apoio real dentro da própria sanga.
          </p>
          <div class="pillar-tags">
            <span class="pillar-tag tag-coral">Moradia</span>
            <span class="pillar-tag tag-coral">Trabalho</span>
            <span class="pillar-tag tag-coral">Saúde</span>
            <span class="pillar-tag tag-coral">Apoio Emocional</span>
          </div>
        </div>
        <div class="pillar-card pillar-ideas">
          <span class="pillar-icon">✨</span>
          <h3>Eixo 2 — Ideias e Inspirações</h3>
          <p>
            Membros com energia criativa conectam-se com quem pode colaborar, 
            cocriá-las e transformar iniciativas individuais em realizações coletivas.
          </p>
          <div class="pillar-tags">
            <span class="pillar-tag tag-amber">Talentos</span>
            <span class="pillar-tag tag-amber">Projetos</span>
            <span class="pillar-tag tag-amber">Apoio Espiritual</span>
            <span class="pillar-tag tag-amber">Grupos de Estudo</span>
          </div>
        </div>
      </div>
    </div>
    """,

    # ── Slide 3: Motor de Matching ──
    """
    <div class="slide active slide-matching">
      <div class="slide-eyebrow">Como funciona</div>
      <h2>O Motor de Conexão</h2>
      <div class="matching-tiers">
        <div class="tier-item tier-1">
          <div class="tier-badge">🤝</div>
          <div class="tier-content">
            <h4>Tier 1 — A Comunidade (Orgânico)</h4>
            <p>Demandas abertas são postadas e respondidas diretamente pelos membros da sanga.</p>
          </div>
        </div>
        <div class="tier-item tier-2">
          <div class="tier-badge">🛡️</div>
          <div class="tier-content">
            <h4>Tier 2 — Os Curadores (Moderação Humana)</h4>
            <p>Equipe designada coordena pedidos sensíveis — saúde, financeiro, emocional — com alinhamento ético ao Vedanta.</p>
          </div>
        </div>
        <div class="tier-item tier-3">
          <div class="tier-badge">✦</div>
          <div class="tier-content">
            <h4>Tier 3 — O Assistente Inteligente (IA)</h4>
            <p>Sistema de matching sugere conexões que humanos poderiam não perceber — trabalhando silenciosamente em segundo plano.</p>
          </div>
        </div>
      </div>
    </div>
    """,

    # ── Slide 4: Pulso da Sanga ──
    """
    <div class="slide active slide-pulso">
      <div class="slide-eyebrow">Impacto em tempo real</div>
      <h2>Pulso da Sanga</h2>
      <p class="slide-desc">
        Um painel vivo que transforma dados abstratos em um sentimento 
        tangível de conquista coletiva.
      </p>
      <div class="pulso-metrics">
        <div class="metric-card">
          <div class="metric-icon">🤲</div>
          <div class="metric-number">247</div>
          <div class="metric-label">Demandas atendidas este mês</div>
          <div class="metric-trend">↑ +15% vs. mês anterior</div>
        </div>
        <div class="metric-card">
          <div class="metric-icon">🎁</div>
          <div class="metric-number">183</div>
          <div class="metric-label">Ofertas de apoio disponíveis</div>
          <div class="metric-trend">↑ +8% esta semana</div>
        </div>
        <div class="metric-card">
          <div class="metric-icon">🌱</div>
          <div class="metric-number">94%</div>
          <div class="metric-label">Taxa de resolução da comunidade</div>
          <div class="metric-trend">↑ Recorde histórico</div>
        </div>
      </div>
    </div>
    """,

    # ── Slide 5: Gateway ──
    """
    <div class="slide active slide-gateway">
      <div class="slide-eyebrow">Como participar</div>
      <h2>O Portal de Entrada</h2>
      <div class="gateway-steps">
        <div class="gateway-step">
          <div class="step-circle">📱</div>
          <div class="step-label">Descubra</div>
          <div class="step-desc">Encontre o VedantaMe pelas redes sociais</div>
        </div>
        <div class="gateway-step">
          <div class="step-circle">🪷</div>
          <div class="step-label">Conheça</div>
          <div class="step-desc">Explore valores e missão da plataforma</div>
        </div>
        <div class="gateway-step">
          <div class="step-circle">✉️</div>
          <div class="step-label">Solicite</div>
          <div class="step-desc">Peça convite ou seja indicado por um membro</div>
        </div>
        <div class="gateway-step">
          <div class="step-circle">🛡️</div>
          <div class="step-label">Seja Avaliado</div>
          <div class="step-desc">Moderador curador aprova o ingresso</div>
        </div>
        <div class="gateway-step">
          <div class="step-circle">🌟</div>
          <div class="step-label">Bem-vindo!</div>
          <div class="step-desc">Acesso à plataforma e acolhimento pela sanga</div>
        </div>
      </div>
    </div>
    """,
]

# ── Auto-play ────────────────────────────────────────────────────────────────
if st.session_state.auto_play:
    now = time.time()
    if now - st.session_state.last_auto > AUTO_INTERVAL:
        st.session_state.slide_idx = (st.session_state.slide_idx + 1) % TOTAL_SLIDES
        st.session_state.last_auto = now

# ── Renderização do HTML principal ──────────────────────────────────────────
current = st.session_state.slide_idx
slide_content = slides_html[current]

# Dots HTML
dots_html = ""
for i in range(TOTAL_SLIDES):
    active_class = "active" if i == current else ""
    dots_html += f'<button class="dot {active_class}" title="Slide {i+1}"></button>'

st.markdown(f"""
<div class="hero-wrapper">
  <nav class="vm-navbar">
    <div class="vm-logo">Vedanta<span>Me</span></div>
    <div class="vm-tagline-nav">Seva · Sanga · Serviço</div>
  </nav>

  <div class="carousel-outer">
    {slide_content}
  </div>
</div>
""", unsafe_allow_html=True)

# ── Controles via Streamlit ──────────────────────────────────────────────────
st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

cols = st.columns([1, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 1])

with cols[1]:
    if st.button("←", key="prev", help="Slide anterior", use_container_width=True):
        st.session_state.slide_idx = (current - 1) % TOTAL_SLIDES
        st.session_state.auto_play = False
        st.session_state.last_auto = time.time()
        st.rerun()

slide_labels = ["①", "②", "③", "④", "⑤"]
for i, col in enumerate(cols[2:7]):
    with col:
        btn_type = "primary" if i == current else "secondary"
        if st.button(slide_labels[i], key=f"dot_{i}", use_container_width=True, type=btn_type):
            st.session_state.slide_idx = i
            st.session_state.auto_play = False
            st.session_state.last_auto = time.time()
            st.rerun()

with cols[6]:
    if st.button("→", key="next", help="Próximo slide", use_container_width=True):
        st.session_state.slide_idx = (current + 1) % TOTAL_SLIDES
        st.session_state.auto_play = False
        st.session_state.last_auto = time.time()
        st.rerun()

# Auto-play toggle
st.markdown("<div style='text-align:center; margin-top: 0.5rem;'>", unsafe_allow_html=True)
col_a, col_b, col_c = st.columns([2, 1, 2])
with col_b:
    auto_label = "⏸ Pausar" if st.session_state.auto_play else "▶ Auto"
    if st.button(auto_label, key="autoplay", use_container_width=True):
        st.session_state.auto_play = not st.session_state.auto_play
        st.session_state.last_auto = time.time()
        st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div class="vm-footer">
  VedantaMe · Movimento Ramakrishna Vedanta no Brasil · 2026
</div>
""", unsafe_allow_html=True)

# Auto-refresh para auto-play
if st.session_state.auto_play:
    time.sleep(0.5)
    st.rerun()
