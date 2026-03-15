# CLAUDE.md — VedantaMe Protótipo

> Este arquivo é lido automaticamente pelo Claude Code ao abrir o projeto.
> Contém todas as instruções para geração e evolução do protótipo VedantaMe.

---

## Contexto do Projeto

**VedantaMe** é uma rede digital de apoio mútuo do movimento Ramakrishna Vedanta no Brasil,
liderada pelo Swami Nirmalatmananda. A plataforma conecta quem tem uma demanda com quem tem
uma solução, inspirada nos princípios védicos do **seva** (serviço desinteressado) e
**sanga** (associação com o sagrado).

Este repositório é um **protótipo funcional** para apresentação à equipe de idealizadores.
O foco é a visualização da experiência — sem banco de dados, sem autenticação, sem
infraestrutura. Os dados são fictícios, armazenados em JSON.

- **Repositório:** https://github.com/pedroregato/vedantame-proto
- **Deploy alvo:** Streamlit Community Cloud
- **URL esperada:** https://pedroregato-vedantame-proto.streamlit.app

---

## Estado Atual do Projeto

### Páginas implementadas

| Arquivo | Nome no menu | Status |
|---|---|---|
| `app.py` | Home (VedantaMe) | ✅ Implementado |
| `pages/1_Demandas.py` | Demandas | ✅ Implementado |
| `pages/2_Ofertas.py` | Ofertas | ✅ Implementado |
| `pages/3_Matching.py` | Matching | ✅ Implementado |
| `pages/4_Pulso_da_Sanga.py` | Pulso da Sanga | ✅ Implementado |

### Módulos core

| Arquivo | Métodos públicos |
|---|---|
| `core/models.py` | Dataclasses: `Demanda`, `Oferta`, `Membro` |
| `core/repository.py` | `get_membros()`, `get_membro_by_id()`, `get_demandas()`, `get_ofertas()`, `get_demandas_por_categoria()`, `get_ofertas_por_categoria()`, `get_stats()` |
| `core/matching.py` | `calcular_matches()`, `calcular_matches_por_categoria()` |
| `core/analytics.py` | `calcular_stats()` — agrega todos os indicadores do Pulso da Sanga |

### Assets

| Arquivo | Descrição |
|---|---|
| `assets/vedantame_logo.svg` | Logo principal usado na sidebar |
| `assets/vedantame_symbol.svg` | Símbolo isolado (lótus + ॐ) — para favicon, docs, etc. |

### Dependências (`requirements.txt`)

```
streamlit==1.42.0
plotly==5.22.0
```

---

## Arquitetura — Separação de Responsabilidades

```
vedantame-proto/
├── CLAUDE.md                     # este arquivo
├── app.py                        # entry point — navegação e layout global
├── pages/
│   ├── 1_Demandas.py             # tela de demandas
│   ├── 2_Ofertas.py              # tela de ofertas
│   ├── 3_Matching.py             # tela de matching
│   └── 4_Pulso_da_Sanga.py       # painel de indicadores da comunidade
├── core/
│   ├── models.py                 # dataclasses: Demanda, Oferta, Membro
│   ├── matching.py               # lógica de matching por categoria
│   ├── analytics.py              # agregados e indicadores (sem Streamlit)
│   └── repository.py             # leitura/escrita do JSON (interface de dados)
├── ui/
│   ├── components.py             # componentes reutilizáveis
│   └── theme.py                  # paleta, fontes e CSS injetados
├── data/
│   └── seed_data.json            # dados fictícios
├── assets/
│   ├── vedantame_logo.svg        # logo sidebar
│   └── vedantame_symbol.svg      # símbolo isolado
├── requirements.txt              # dependências com versões fixadas
└── README.md
```

### Responsabilidade de cada camada

| Camada | Responsabilidade | Restrição |
|---|---|---|
| `core/models.py` | Dataclasses puras: Demanda, Oferta, Membro | Sem lógica, sem Streamlit |
| `core/repository.py` | Única camada que lê/escreve `seed_data.json` | Páginas nunca acessam JSON diretamente |
| `core/matching.py` | Algoritmo de matching — recebe listas, retorna pares | Sem dependência de Streamlit; função pura |
| `core/analytics.py` | Agregados e indicadores — recebe listas, retorna dict | Sem dependência de Streamlit; função pura |
| `ui/theme.py` | Paleta de cores e CSS injetado via `st.markdown` | Nenhuma página define cores hardcoded |
| `ui/components.py` | Funções reutilizáveis: cards, badges, formulários, logo | Sem lógica de negócio |
| `pages/` | Orquestração: chama repository → components | Zero lógica de negócio nas páginas |
| `app.py` | `set_page_config()`, sidebar global, logo animado, apresentação | Sem lógica de negócio |

> **Princípio:** `core/` nunca importa Streamlit. `ui/` nunca importa `core/` diretamente.
> As páginas são controllers finos que fazem a ponte entre as duas camadas.

---

## Telas

### Home (`app.py`)
- Logo animado SVG inline (lótus girando + Shatkona pulsando) via `st.markdown`
- Heading "VedantaMe" em Georgia/saffron
- Cards de navegação para as 3 seções principais
- Sidebar com logo e descrição de seva/sanga

### 1 — Demandas (`pages/1_Demandas.py`)
- Filtro por categoria (selectbox)
- Lista de demandas abertas usando `card_demanda()`
- Formulário para registrar nova demanda (persiste em `st.session_state`)

### 2 — Ofertas (`pages/2_Ofertas.py`)
- Filtro por categoria
- Lista de ofertas disponíveis usando `card_oferta()`
- Formulário para registrar nova oferta

### 3 — Matching (`pages/3_Matching.py`)
- Chama `matching.py` para cruzar demandas e ofertas por categoria
- Exibe pares compatíveis visualmente (demanda ↔ oferta)
- Badge de status: `Aguardando` · `Em contato` · `Resolvido`

### 4 — Pulso da Sanga (`pages/4_Pulso_da_Sanga.py`)
Painel de indicadores vivos da comunidade. Cinco faixas:
1. **Visão Geral** — 4 métricas com `st.metric()`: % atendidas, aguardando, ofertas, vidas impactadas
2. **Demandas por Categoria** — barras horizontais empilhadas (plotly): abertas vs. atendidas
3. **Distribuição de Ofertas** — donut chart (plotly) por categoria
4. **Atividade nos Últimos 30 Dias** — linha do tempo fictícia com crescimento gradual
5. **Onde a comunidade mais precisa de você** — tabela de gaps (demandas abertas − ofertas)

---

## Categorias

```python
CATEGORIAS = [
    "Moradia Temporária",
    "Trabalho e Renda",
    "Transporte e Locomoção",
    "Apoio Emocional e Escuta",
    "Saúde e Acompanhamento Médico",
    "Eventos e Projetos Espirituais",
    "Talentos e Habilidades",
    "Apoio Espiritual",
    "Bate-papo Vedanta",
]
```

---

## Visual

```python
# theme.py — paleta obrigatória
COLORS = {
    "primary":    "#8B5C2A",   # saffron/marrom
    "dark":       "#1A1A2E",   # azul-escuro
    "background": "#F5F0E8",   # creme
    "text":       "#2D2D2D",   # quase preto
    "mid":        "#4A4A6A",   # índigo suave
    "success":    "#4A7C59",   # verde terra
    "warning":    "#C4813A",   # âmbar
}
```

- Fonte de títulos: Georgia (serif)
- Tom: acolhedor, espiritual, limpo — não corporativo
- Cards com cantos arredondados (`border-radius: 12px`), sombra suave, badge colorido por categoria
- Logo animado: pétalas externas girando (18s), internas girando ao contrário (12s), Shatkona pulsando (3s)

---

## Seed Data (`data/seed_data.json`)

Estrutura atual:
- **8 demandas** fictícias (status: Aguardando / Em contato / Resolvido)
- **8 ofertas** fictícias
- **5 membros** fictícios com nomes, cidades e estados brasileiros

```json
{
  "membros": [ { "id": "m1", "nome": "...", "cidade": "...", "estado": "SP" } ],
  "demandas": [
    { "id": "d1", "membro_id": "m1", "categoria": "...",
      "descricao": "...", "status": "Aguardando", "data": "2026-03-10" }
  ],
  "ofertas": [
    { "id": "o1", "membro_id": "m2", "categoria": "...",
      "descricao": "...", "data": "2026-03-08" }
  ]
}
```

---

## Constraints

- Python 3.11+
- Streamlit >= 1.32
- Sem banco de dados, sem autenticação, sem API externa
- Cada módulo deve poder ser importado de forma independente
- `seed_data.json` carregado com caminho relativo a `app.py` (obrigatório para Streamlit Cloud)
- Sem caminhos absolutos em nenhum arquivo
- `requirements.txt` com todas as dependências explícitas e versões fixadas
- O app deve fazer deploy sem erros no Streamlit Community Cloud com as configurações padrão

---

## Como Rodar Localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Como Fazer Deploy

1. Push para `https://github.com/pedroregato/vedantame-proto`
2. Acessar https://share.streamlit.io
3. Conectar repositório → arquivo principal: `app.py`
4. Clicar em **Deploy**

---

## Evolução Futura (não implementar agora)

Registrado aqui para orientar decisões de arquitetura desde o início:

- `repository.py` será substituído por uma camada de banco de dados (ex: Supabase) sem impacto nas páginas
- `matching.py` evoluirá para um modelo de IA sem alterar o contrato com as páginas
- `analytics.py` poderá consumir dados reais do banco sem alterar o contrato com as páginas
- Autenticação será adicionada em `app.py` de forma centralizada
- Expansão internacional: suporte a múltiplos idiomas via `i18n/`
- Emoji no nome da página Pulso da Sanga: renomear para `4_🌸_Pulso_da_Sanga.py` para exibir o emoji na sidebar

---

## Instruções para o Claude Code

Ao concluir qualquer tarefa neste projeto, atualize este arquivo
refletindo o que foi implementado:
- Novas páginas ou módulos criados
- Novos métodos adicionados em `repository.py`, `analytics.py` ou `matching.py`
- Dependências adicionadas ao `requirements.txt`
- Decisões de arquitetura tomadas

Mantenha o CLAUDE.md sempre como espelho fiel do estado atual do projeto.

---

*VedantaMe · Movimento Ramakrishna Vedanta no Brasil · 2026*
