import os

import requests
from dotenv import load_dotenv

load_dotenv()

# Discord webhook URL
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

# Message to send
message = os.getenv("DISCORD_START_MESSAGE", "Server online!")

# Send the message to Discord
data = {"content": message}

response = requests.post(webhook_url, json=data)
if response.status_code == 204:
    print("Start message sent successfully.")
    # Save the message ID for later deletion
    message_id = response.headers["X-Message-Id"]
    with open("/message_id.txt", "w") as f:
        f.write(message_id)
else:
    print(f"Failed to send start message. Status code: {response.status_code}")
