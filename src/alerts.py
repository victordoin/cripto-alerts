def generate_alerts(env):
    # Lógica para gerar alertas baseado no ambiente
    if env == "dev":
        return f"[DEV] Alerta diário gerado para ambiente de testes no dia {__import__('datetime').datetime.now()}"
    else:
        return f"[PROD] 🔔 Alerta diário oficial gerado no dia {__import__('datetime').datetime.now()}"