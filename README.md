# 🤖 Bot de Alertas Cripto

Este projeto é um bot que envia alertas diários sobre criptomoedas via Telegram, com suporte a diferentes níveis de assinatura (Free, VIP, Premium).

## 📁 Estrutura do Projeto

```
cripto/
├── .github/
│   └── workflows/
│       ├── daily_alerts_dev.yml
│       └── daily_alerts_prod.yml
├── config/
│   ├── __init__.py
│   ├── dev.py
│   └── prod.py
├── secrets/
│   └── telegram_tokens.json (não commitado)
├── src/
│   ├── main.py
│   ├── alerts.py
│   ├── telegram_bot.py
│   └── subscribers.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 🔐 Segurança

- Tokens do Telegram são armazenados em `secrets/telegram_tokens.json` (não commitado).
- Também podem ser configurados via GitHub Secrets.
  
## 🚀 Como Usar

### 1. Configurar Ambientes

- `dev`: Ambiente de desenvolvimento e testes.
- `prod`: Ambiente de produção.

### 2. Configurar Secrets no GitHub

Vá em **Settings > Secrets and variables > Actions** e adicione:

```
TELEGRAM_TOKEN_DEV
TELEGRAM_CHAT_ID_DEV
TELEGRAM_TOKEN_PROD
TELEGRAM_CHAT_ID_PROD
```

### 3. Assinaturas

Os assinantes são gerenciados em `src/subscribers.py`:

```python
SUBSCRIBERS = {
    "free": ["chat_id_1"],
    "vip": ["chat_id_2"],
    "premium": ["chat_id_3"]
}
```

## 🧪 Testando Localmente

```bash
# Para ambiente de desenvolvimento
ENV=dev GROUP=free python src/main.py

# Para ambiente de produção
ENV=prod GROUP=vip python src/main.py
```

## 🕐 Agendamento

- **Dev**: Roda todo dia às 18h (horário de Brasília).
- **Prod**: Roda todo dia às 9h (horário de Brasília).

## 🛠️ Dependências

```bash
pip install -r requirements.txt
```