# VedantaMe — Documentação do Protótipo

> Rede digital de apoio mútuo do Movimento Ramakrishna Vedanta no Brasil
> Liderada pelo Swami Nirmalatmananda
> Protótipo funcional para apresentação à equipe de idealizadores

---

## Índice

1. [Visão Geral](#1-visão-geral)
2. [Conceito e Filosofia](#2-conceito-e-filosofia)
3. [Arquitetura do Projeto](#3-arquitetura-do-projeto)
4. [Estrutura de Arquivos](#4-estrutura-de-arquivos)
5. [Camada de Dados — `core/`](#5-camada-de-dados--core)
   - [models.py](#51-modelspy)
   - [repository.py](#52-repositorypy)
   - [matching.py](#53-matchingpy)
6. [Camada de Interface — `ui/`](#6-camada-de-interface--ui)
   - [theme.py](#61-themepy)
   - [components.py](#62-componentspy)
7. [Páginas — `pages/`](#7-páginas--pages)
   - [1_Demandas.py](#71-1_demandaspy)
   - [2_Ofertas.py](#72-2_ofertaspy)
   - [3_Matching.py](#73-3_matchingpy)
8. [Entry Point — `app.py`](#8-entry-point--apppy)
9. [Dados de Seed — `data/seed_data.json`](#9-dados-de-seed--dataseed_datajson)
10. [Fluxo de Dados](#10-fluxo-de-dados)
11. [Sistema de Matching](#11-sistema-de-matching)
12. [Tema Visual](#12-tema-visual)
13. [Categorias](#13-categorias)
14. [Como Rodar Localmente](#14-como-rodar-localmente)
15. [Como Fazer Deploy](#15-como-fazer-deploy)
16. [Restrições e Decisões de Design](#16-restrições-e-decisões-de-design)
17. [Evolução Futura](#17-evolução-futura)

---

## 1. Visão Geral

O **VedantaMe** é um protótipo de plataforma web que conecta membros do Movimento Ramakrishna Vedanta no Brasil. A proposta central é facilitar a troca de apoio mútuo — alguém que **tem uma demanda** encontra alguém que **tem uma oferta** compatível — tudo dentro de um ambiente acolhedor, espiritual e comunitário.

**Stack tecnológica:**
- Python 3.11+
- Streamlit 1.32+
- JSON como armazenamento de dados (protótipo)
- Sem banco de dados, sem autenticação, sem APIs externas

**O que este protótipo demonstra:**
- Visualização de demandas e ofertas da comunidade
- Algoritmo de matching por categoria
- Formulários de registro (persistidos em memória de sessão)
- Identidade visual inspirada na espiritualidade védica

---

## 2. Conceito e Filosofia

A plataforma é organizada em torno de dois conceitos centrais do Vedanta:

- **Seva** — serviço desinteressado, oferecer sem expectativa de retorno
- **Sanga** — associação com o sagrado e com a comunidade espiritual

Qualquer membro pode ser ao mesmo tempo quem **pede** e quem **oferece**. O sistema não busca transações comerciais, mas conexões de cuidado genuíno dentro da comunidade.

---

## 3. Arquitetura do Projeto

O projeto segue uma separação estrita de responsabilidades em três camadas:

```
┌─────────────────────────────────────────────────┐
│                  PÁGINAS (pages/)                │
│          Controller fino — sem lógica            │
│   Orquestra: repository → components → UI        │
└──────────────┬──────────────────┬────────────────┘
               │                  │
               ▼                  ▼
┌──────────────────────┐  ┌───────────────────────┐
│      CORE (core/)    │  │       UI (ui/)         │
│  Sem Streamlit       │  │  Sem lógica de negócio │
│  models.py           │  │  theme.py              │
│  repository.py       │  │  components.py         │
│  matching.py         │  │                        │
└──────────┬───────────┘  └───────────────────────┘
           │
           ▼
┌──────────────────────┐
│   data/seed_data.json│
│   Fonte única de     │
│   verdade dos dados  │
└──────────────────────┘
```

**Regras da arquitetura:**
- `core/` **nunca** importa Streamlit
- `ui/` **nunca** importa `core/` diretamente
- As páginas são os únicos pontos de integração entre as duas camadas
- Apenas `repository.py` lê o arquivo JSON — nenhuma outra camada acessa diretamente

---

## 4. Estrutura de Arquivos

```
vedantame-proto/
├── app.py                        # Entry point — home page e configuração global
├── pages/
│   ├── 1_Demandas.py             # Tela de demandas (listagem + formulário)
│   ├── 2_Ofertas.py              # Tela de ofertas (listagem + formulário)
│   └── 3_Matching.py             # Tela de matching (pares compatíveis)
├── core/
│   ├── __init__.py
│   ├── models.py                 # Dataclasses: Demanda, Oferta, Membro + constantes
│   ├── matching.py               # Algoritmo de matching (função pura)
│   └── repository.py             # Única camada que lê seed_data.json
├── ui/
│   ├── __init__.py
│   ├── components.py             # Componentes reutilizáveis: cards, badges, formulários
│   └── theme.py                  # Paleta de cores, CSS global injetado
├── data/
│   └── seed_data.json            # Dados fictícios: 5 membros, 8 demandas, 8 ofertas
├── requirements.txt              # streamlit==1.32.2
├── .gitignore
├── CLAUDE.md                     # Instruções para o agente de IA
└── README.md                     # Este arquivo
```

---

## 5. Camada de Dados — `core/`

### 5.1 `models.py`

Define as estruturas de dados do domínio usando `dataclasses`. Sem nenhuma dependência de Streamlit ou de bibliotecas externas.

**Constantes globais:**

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

STATUS_OPTIONS = ["Aguardando", "Em contato", "Resolvido"]
```

**Dataclasses:**

| Classe | Campos | Descrição |
|---|---|---|
| `Membro` | `id`, `nome`, `cidade`, `estado` | Pessoa registrada na comunidade |
| `Demanda` | `id`, `membro_id`, `categoria`, `descricao`, `status`, `data` | Necessidade aberta por um membro |
| `Oferta` | `id`, `membro_id`, `categoria`, `descricao`, `data` | Recurso ou serviço disponibilizado |

**Observação:** `Demanda` tem o campo `status` (ciclo de vida); `Oferta` não tem status — é sempre considerada disponível.

---

### 5.2 `repository.py`

Única camada autorizada a ler `seed_data.json`. Exporta funções de consulta simples. Nenhuma página ou componente acessa o arquivo JSON diretamente.

**Caminho do arquivo:**
```python
_DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "seed_data.json")
```
O caminho é calculado relativamente ao próprio arquivo `repository.py`, garantindo portabilidade no Streamlit Cloud (sem caminhos absolutos).

**Funções exportadas:**

| Função | Retorno | Descrição |
|---|---|---|
| `get_membros()` | `List[Membro]` | Todos os membros |
| `get_membro_by_id(id)` | `Optional[Membro]` | Membro específico; `None` se não encontrado |
| `get_demandas()` | `List[Demanda]` | Todas as demandas do seed |
| `get_ofertas()` | `List[Oferta]` | Todas as ofertas do seed |
| `get_demandas_por_categoria(cat)` | `List[Demanda]` | Demandas filtradas por categoria |
| `get_ofertas_por_categoria(cat)` | `List[Oferta]` | Ofertas filtradas por categoria |

**Comportamento:** Cada chamada reabre e relê o JSON. Adequado para protótipo — em produção seria substituído por queries a banco de dados.

---

### 5.3 `matching.py`

Algoritmo de matching: função pura, sem dependências de Streamlit. Recebe listas de objetos, retorna pares compatíveis.

**Lógica atual:** matching por igualdade de `categoria` (produto cartesiano filtrado).

```
Para cada (Demanda d, Oferta o):
    se d.categoria == o.categoria → par válido
```

**Funções:**

```python
def calcular_matches(demandas, ofertas) -> List[Tuple[Demanda, Oferta]]
```
Retorna lista plana de todos os pares compatíveis.

```python
def calcular_matches_por_categoria(demandas, ofertas) -> dict
```
Retorna `{categoria: [(Demanda, Oferta), ...]}`, agrupado para facilitar a renderização por seção.

**Por que função pura?** Permite testar o algoritmo de forma isolada, sem renderizar UI, e facilita a substituição futura por um modelo de IA sem impacto nas páginas.

---

## 6. Camada de Interface — `ui/`

### 6.1 `theme.py`

Centraliza toda a identidade visual. Nenhuma página define cores hardcoded — tudo parte daqui.

**Paleta principal (`COLORS`):**

| Chave | Hex | Uso |
|---|---|---|
| `primary` | `#8B5C2A` | Saffron/marrom — cor principal, bordas de cards |
| `dark` | `#1A1A2E` | Azul-escuro — sidebar, títulos |
| `background` | `#F5F0E8` | Creme — fundo geral da aplicação |
| `text` | `#2D2D2D` | Quase preto — texto corrente |
| `mid` | `#4A4A6A` | Índigo suave — subtítulos, metadados |
| `success` | `#4A7C59` | Verde terra — status "Resolvido", confirmações |
| `warning` | `#C4813A` | Âmbar — status "Aguardando", hover de botões |

**Cores por categoria (`CATEGORIA_COLORS`):**
Cada uma das 9 categorias tem uma cor específica aplicada na borda esquerda dos cards e nos títulos de seção do matching.

**Cores de status (`STATUS_COLORS`):**

| Status | Cor |
|---|---|
| Aguardando | `#C4813A` (âmbar) |
| Em contato | `#2E7D9A` (azul) |
| Resolvido | `#4A7C59` (verde) |

**Função `inject_css()`:**
Injeta um bloco `<style>` global via `st.markdown(unsafe_allow_html=True)`. Define:
- Fonte `Lato` (Google Fonts) para corpo, `Georgia` para títulos
- Fundo creme em `.stApp`
- Sidebar com fundo `#1A1A2E`
- Classe `.vedanta-card` — card com `border-radius: 12px`, sombra suave, borda esquerda colorida
- Classe `.badge` — pill colorida para categoria e status
- Estilo de botão com hover âmbar

---

### 6.2 `components.py`

Funções reutilizáveis que renderizam HTML/Streamlit. Recebem dataclasses do `core/` — sem lógica de negócio própria.

**Funções de badge:**

| Função | Descrição |
|---|---|
| `badge(texto, cor)` | HTML de uma pill colorida genérica |
| `badge_categoria(categoria)` | Badge com cor do `CATEGORIA_COLORS` |
| `badge_status(status)` | Badge com cor do `STATUS_COLORS` |

**Funções de card:**

| Função | O que renderiza |
|---|---|
| `card_demanda(demanda, membro)` | Card com título truncado, badges, nome do membro, cidade, data, descrição completa |
| `card_oferta(oferta, membro)` | Idem para ofertas (sem badge de status) |
| `card_match(demanda, oferta, membro_d, membro_o)` | Card lado-a-lado com demanda ⇄ oferta, gradiente suave |

**Formulários:**

| Função | Campos | Retorno |
|---|---|---|
| `formulario_demanda(key_prefix)` | Categoria, Descrição, Nome, Cidade | `Demanda` ou `None` |
| `formulario_oferta(key_prefix)` | Categoria, Descrição, Nome, Cidade | `Oferta` ou `None` |

Os formulários geram IDs únicos com `uuid4().hex[:6]` e definem a data automaticamente como `date.today()`. Validam campos obrigatórios (nome e descrição) antes de retornar.

---

## 7. Páginas — `pages/`

O Streamlit detecta automaticamente arquivos na pasta `pages/` e os exibe como itens de menu lateral. O prefixo numérico (`1_`, `2_`, `3_`) define a ordem de exibição.

### 7.1 `1_Demandas.py`

**Responsabilidade:** Listar demandas existentes e permitir o registro de novas.

**Fluxo:**
1. `inject_css()` — aplica o tema
2. Inicializa `st.session_state.novas_demandas = []` se não existir
3. Selectbox de filtro por categoria (opção "Todas" + 9 categorias)
4. Combina `get_demandas()` + `session_state.novas_demandas`
5. Filtra por categoria selecionada
6. Ordena por data decrescente e renderiza cada card com `card_demanda()`
7. Exibe `formulario_demanda()` — se submetido e válido, appenda ao session_state e chama `st.rerun()`

**Persistência:** Apenas em memória de sessão (`st.session_state`). Ao recarregar a página, novas demandas registradas pelo usuário são perdidas — comportamento esperado no protótipo.

---

### 7.2 `2_Ofertas.py`

**Responsabilidade:** Listar ofertas e permitir registro de novas. Espelho estrutural de `1_Demandas.py`.

**Diferenças em relação a Demandas:**
- Usa `get_ofertas()` e `novas_ofertas` no session_state
- Cards sem badge de status (ofertas não têm ciclo de vida no protótipo)
- Formulário via `formulario_oferta()`

---

### 7.3 `3_Matching.py`

**Responsabilidade:** Cruzar demandas e ofertas e exibir pares compatíveis.

**Fluxo:**
1. Carrega dados do seed + dados da sessão (demandas e ofertas registradas na sessão atual)
2. Dois filtros independentes:
   - Filtro por **categoria** (afeta tanto demandas quanto ofertas)
   - Filtro por **status da demanda** (`Aguardando`, `Em contato`, `Resolvido`)
3. Chama `calcular_matches_por_categoria()` com os dados filtrados
4. Exibe contador geral de pares e categorias
5. Para cada categoria com matches, renderiza um cabeçalho colorido e os `card_match()` abaixo

**Integração com sessão:** Demandas e ofertas registradas na mesma sessão aparecem no matching em tempo real.

---

## 8. Entry Point — `app.py`

Arquivo principal que o Streamlit executa ao iniciar. Define:

- `st.set_page_config()` — título "VedantaMe", ícone 🪷, layout wide, sidebar expandida
- `inject_css()` — tema global aplicado à home page
- **Sidebar** com logo, nome e glossário (Seva/Sanga)
- **Home page** com três cards de apresentação das seções (Demandas, Ofertas, Matching)

O `app.py` não tem lógica de negócio — apenas apresentação e configuração.

---

## 9. Dados de Seed — `data/seed_data.json`

Arquivo JSON com dados fictícios brasileiros realistas. Estrutura:

```json
{
  "membros": [...],
  "demandas": [...],
  "ofertas":  [...]
}
```

**Membros (5):**

| ID | Nome | Cidade | Estado |
|---|---|---|---|
| m1 | Ananda Silva | São Paulo | SP |
| m2 | Priya Ferreira | Rio de Janeiro | RJ |
| m3 | Ramakrishna Souza | Belo Horizonte | MG |
| m4 | Lakshmi Santos | Curitiba | PR |
| m5 | Vivekananda Costa | Florianópolis | SC |

**Demandas (8) — cobrindo 8 categorias:**

| ID | Membro | Categoria | Status |
|---|---|---|---|
| d1 | Ananda Silva | Moradia Temporária | Aguardando |
| d2 | Ramakrishna Souza | Trabalho e Renda | Em contato |
| d3 | Vivekananda Costa | Transporte e Locomoção | Aguardando |
| d4 | Priya Ferreira | Apoio Emocional e Escuta | Resolvido |
| d5 | Lakshmi Santos | Saúde e Acompanhamento Médico | Aguardando |
| d6 | Ananda Silva | Eventos e Projetos Espirituais | Em contato |
| d7 | Ramakrishna Souza | Talentos e Habilidades | Aguardando |
| d8 | Vivekananda Costa | Bate-papo Vedanta | Aguardando |

**Ofertas (8) — cobrindo as mesmas 8 categorias:**

| ID | Membro | Categoria |
|---|---|---|
| o1 | Priya Ferreira | Moradia Temporária |
| o2 | Lakshmi Santos | Trabalho e Renda |
| o3 | Ananda Silva | Transporte e Locomoção |
| o4 | Vivekananda Costa | Apoio Emocional e Escuta |
| o5 | Ramakrishna Souza | Saúde e Acompanhamento Médico |
| o6 | Priya Ferreira | Eventos e Projetos Espirituais |
| o7 | Lakshmi Santos | Talentos e Habilidades |
| o8 | Ananda Silva | Bate-papo Vedanta |

**Resultado do matching com o seed completo:** 8 pares, 1 por categoria (matching perfeito 1-para-1).

---

## 10. Fluxo de Dados

```
seed_data.json
      │
      ▼
repository.py          session_state
  get_demandas()    +  novas_demandas
  get_ofertas()     +  novas_ofertas
      │
      ▼
  pages/*.py  (controller)
      │
      ├── matching.py  →  calcular_matches_por_categoria()
      │
      └── components.py
            card_demanda()
            card_oferta()
            card_match()
            formulario_*()
                  │
                  ▼
            Streamlit UI (browser)
```

---

## 11. Sistema de Matching

O algoritmo atual é determinístico e baseado em categoria:

```
matches = []
para cada demanda d:
    para cada oferta o:
        se d.categoria == o.categoria:
            matches.append((d, o))
```

**Complexidade:** O(n × m), onde n = número de demandas e m = número de ofertas. Adequado para protótipo com dezenas de registros.

**O que o algoritmo NÃO considera (intencionalmente, para o protótipo):**
- Localização geográfica (cidade/estado)
- Urgência ou prioridade
- Histórico de interações
- Compatibilidade de perfil

**Contrato do algoritmo:** Recebe `List[Demanda]` e `List[Oferta]`, retorna pares. As páginas aplicam filtros **antes** de chamar o algoritmo — o algoritmo em si não filtra por status nem por categoria.

---

## 12. Tema Visual

**Fontes:**
- Títulos (h1, h2, h3): `Georgia, 'Times New Roman', serif` — transmite tradição e seriedade
- Corpo: `Lato, sans-serif` (Google Fonts) — legibilidade moderna

**Cards (`.vedanta-card`):**
- Fundo branco
- `border-radius: 12px` — cantos arredondados, toque acolhedor
- `box-shadow: 0 2px 8px rgba(26,26,46,0.08)` — sombra suave
- Borda esquerda de 4px colorida pela categoria

**Badges (`.badge`):**
- Pill com `border-radius: 20px`
- Cor de fundo determinada pela categoria ou status
- Texto branco, peso 700, letra maiúscula

**Sidebar:**
- Fundo `#1A1A2E` (azul-escuro) contrasta com o creme do conteúdo principal
- Texto em `#F5F0E8` para legibilidade

**Tom geral:** Acolhedor, espiritual, limpo — sem elementos corporativos ou frios.

---

## 13. Categorias

As 9 categorias cobrem as principais necessidades e talentos circulantes em uma comunidade espiritual:

| Categoria | Cor | Exemplos de uso |
|---|---|---|
| Moradia Temporária | `#8B5C2A` | Hospedagem para retiros, períodos de transição |
| Trabalho e Renda | `#4A7C59` | Freelances, oportunidades alinhadas com valores |
| Transporte e Locomoção | `#4A4A6A` | Caronas para eventos, retiros |
| Apoio Emocional e Escuta | `#C4813A` | Escuta ativa, acompanhamento espiritual |
| Saúde e Acompanhamento Médico | `#2E7D9A` | Indicações médicas, acompanhamento |
| Eventos e Projetos Espirituais | `#7B3FA0` | Organização de pujas, kirtans, retiros |
| Talentos e Habilidades | `#B5451B` | Música, artesanato, culinária |
| Apoio Espiritual | `#1A6B4A` | Orientação, estudo, prática |
| Bate-papo Vedanta | `#5C4033` | Grupos de estudo, discussão filosófica |

---

## 14. Como Rodar Localmente

**Pré-requisitos:** Python 3.11+

```bash
# 1. Clone o repositório
git clone https://github.com/pedroregato/vedantame-proto.git
cd vedantame-proto

# 2. (Opcional) Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute
streamlit run app.py
```

O app abrirá automaticamente em `http://localhost:8501`.

**Navegação:**
- A home page é o `app.py`
- Use o menu lateral para acessar **Demandas**, **Ofertas** e **Matching**

---

## 15. Como Fazer Deploy

O protótipo está configurado para deploy imediato no **Streamlit Community Cloud** (gratuito).

1. Faça push do repositório para `https://github.com/pedroregato/vedantame-proto`
2. Acesse [https://share.streamlit.io](https://share.streamlit.io)
3. Clique em **New app**
4. Conecte o repositório e selecione:
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Clique em **Deploy**

**URL esperada após deploy:**
`https://pedroregato-vedantame-proto.streamlit.app`

**Requisitos para o deploy funcionar:**
- `requirements.txt` na raiz com versões fixadas ✓
- Caminhos relativos (sem `/home/user/...` ou `C:\...`) ✓
- Sem variáveis de ambiente obrigatórias ✓
- Sem banco de dados externo ✓

---

## 16. Restrições e Decisões de Design

| Restrição | Motivação |
|---|---|
| Sem banco de dados | Protótipo de visualização — simplicidade acima de tudo |
| Sem autenticação | Foco na experiência, não em segurança |
| Sem APIs externas | Deploy zero-config no Streamlit Cloud |
| Dados em `session_state` | Novos registros sobrevivem à navegação entre páginas, mas não ao reload |
| Caminhos relativos | Obrigatório para Streamlit Cloud — `__file__` como âncora |
| `core/` sem Streamlit | Permite testar a lógica de negócio de forma isolada |
| `ui/` sem `core/` direto | Componentes recebem dataclasses prontos — sem acoplamento ao repositório |
| `requirements.txt` com versão fixada | Reprodutibilidade do build no Cloud |

---

## 17. Evolução Futura

Decisões de arquitetura tomadas hoje que facilitarão a evolução:

**Banco de dados:**
- `repository.py` será substituído por uma implementação com Supabase ou PostgreSQL
- As páginas e o matching não precisarão mudar — elas consomem listas de dataclasses independente da fonte

**Algoritmo de IA:**
- `matching.py` poderá evoluir para embeddings semânticos (ex: `sentence-transformers`)
- O contrato `(List[Demanda], List[Oferta]) → List[Tuple]` permanece igual

**Autenticação:**
- Adicionada centralmente em `app.py` via `st.experimental_user` ou integração OAuth
- Sem impacto nas páginas individuais

**Internacionalização:**
- Strings de UI migradas para `i18n/` com suporte a `pt-BR`, `en`, `es`
- `CATEGORIAS` e constantes terão versões traduzidas

**Persistência de registros:**
- Formulários poderão escrever diretamente no banco em vez de `session_state`
- A assinatura de `formulario_demanda()` permanece a mesma

---

*VedantaMe · Movimento Ramakrishna Vedanta no Brasil · 2026*
