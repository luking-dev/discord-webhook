import os

import requests
from dotenv import load_dotenv

load_dotenv()

# Discord webhook URL
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

# Message to send
message = os.getenv("DISCORD_STOP_MESSAGE", "Server offline")

# Send the message to Discord
data = {"content": message}

response = requests.post(webhook_url, json=data)
if response.status_code == 204:
    print("Stop message sent successfully.")
else:
    print(f"Failed to send stop message. Status code: {response.status_code}")
