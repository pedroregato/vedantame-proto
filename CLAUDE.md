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

## Tarefa Inicial

Gerar toda a estrutura do projeto conforme a arquitetura abaixo, incluindo código funcional,
seed data e configuração de deploy. O protótipo deve estar pronto para rodar localmente com
`streamlit run app.py` e para deploy imediato no Streamlit Community Cloud.

---

## Arquitetura — Separação de Responsabilidades

```
vedantame-proto/
├── CLAUDE.md                     # este arquivo
├── app.py                        # entry point — navegação e layout global
├── pages/
│   ├── 1_Demandas.py             # tela de demandas
│   ├── 2_Ofertas.py              # tela de ofertas
│   └── 3_Matching.py             # tela de matching
├── core/
│   ├── models.py                 # dataclasses: Demanda, Oferta, Membro
│   ├── matching.py               # lógica de matching por categoria
│   └── repository.py             # leitura/escrita do JSON (interface de dados)
├── ui/
│   ├── components.py             # componentes reutilizáveis
│   └── theme.py                  # paleta, fontes e CSS injetados
├── data/
│   └── seed_data.json            # dados fictícios
├── requirements.txt              # dependências com versões fixadas
└── README.md
```

### Responsabilidade de cada camada

| Camada | Responsabilidade | Restrição |
|---|---|---|
| `core/models.py` | Dataclasses puras: Demanda, Oferta, Membro | Sem lógica, sem Streamlit |
| `core/repository.py` | Única camada que lê/escreve `seed_data.json` | Páginas nunca acessam JSON diretamente |
| `core/matching.py` | Algoritmo de matching — recebe listas, retorna pares | Sem dependência de Streamlit; função pura |
| `ui/theme.py` | Paleta de cores e CSS injetado via `st.markdown` | Nenhuma página define cores hardcoded |
| `ui/components.py` | Funções reutilizáveis: cards, badges, formulários | Sem lógica de negócio |
| `pages/` | Orquestração: chama repository → components | Zero lógica de negócio nas páginas |
| `app.py` | `set_page_config()`, sidebar global, logo, apresentação | Sem lógica de negócio |

> **Princípio:** `core/` nunca importa Streamlit. `ui/` nunca importa `core/` diretamente.
> As páginas são controllers finos que fazem a ponte entre as duas camadas.

---

## Telas

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

---

## Seed Data (`data/seed_data.json`)

Incluir ao menos:
- **8 demandas** fictícias distribuídas entre as categorias
- **8 ofertas** fictícias distribuídas entre as categorias
- **5 membros** fictícios com nomes, cidades e habilidades brasileiras realistas

Exemplo de estrutura:

```json
{
  "membros": [
    { "id": "m1", "nome": "Ananda Silva", "cidade": "São Paulo", "estado": "SP" }
  ],
  "demandas": [
    {
      "id": "d1", "membro_id": "m1",
      "categoria": "Moradia Temporária",
      "descricao": "Preciso de hospedagem por 2 semanas em SP enquanto me restabeleço.",
      "status": "Aguardando",
      "data": "2026-03-10"
    }
  ],
  "ofertas": [
    {
      "id": "o1", "membro_id": "m2",
      "categoria": "Moradia Temporária",
      "descricao": "Tenho um quarto disponível no Ashrama por até 30 dias.",
      "data": "2026-03-08"
    }
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
- Autenticação será adicionada em `app.py` de forma centralizada
- Expansão internacional: suporte a múltiplos idiomas via `i18n/`

---

*VedantaMe · Movimento Ramakrishna Vedanta no Brasil · 2026*
