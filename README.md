# VedantaMe — Protótipo

Rede digital de apoio mútuo do Movimento Ramakrishna Vedanta no Brasil.

## Como rodar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Como fazer deploy

1. Push para `https://github.com/pedroregato/vedantame-proto`
2. Acesse https://share.streamlit.io
3. Conecte o repositório → arquivo principal: `app.py`
4. Clique em **Deploy**

## Estrutura

```
vedantame-proto/
├── app.py                    # entry point
├── pages/
│   ├── 1_Demandas.py
│   ├── 2_Ofertas.py
│   └── 3_Matching.py
├── core/
│   ├── models.py
│   ├── matching.py
│   └── repository.py
├── ui/
│   ├── components.py
│   └── theme.py
├── data/
│   └── seed_data.json
└── requirements.txt
```
