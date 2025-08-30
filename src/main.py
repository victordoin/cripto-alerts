import os
import sys
from alerts import generate_alerts
from telegram_bot import send_message

ENV = os.getenv("ENV", "dev")
GROUP = os.getenv("GROUP", "free")

def main():
    alerts = generate_alerts(ENV)
    send_message(alerts, ENV, GROUP)

if __name__ == "__main__":
    main()