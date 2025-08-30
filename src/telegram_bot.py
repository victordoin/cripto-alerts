import os
import json
import requests
from subscribers import SUBSCRIBERS

def send_message(message, env, group="free"):
    secrets_path = os.path.join("secrets", "telegram_tokens.json")
    with open(secrets_path) as f:
        tokens = json.load(f)

    token = os.getenv("TELEGRAM_TOKEN") or tokens[env]["bot_token"]

    # Envia mensagem para todos os inscritos no grupo especificado
    for chat_id in SUBSCRIBERS.get(group, []):
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        requests.post(url, data=payload)