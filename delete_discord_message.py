import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Discord webhook URL
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

# Read the message ID
with open("/message_id.txt", "r") as f:
    message_id = f.read().strip()

# Delete the message from Discord
delete_url = f"{webhook_url}/messages/{message_id}"
response = requests.delete(delete_url)
if response.status_code == 204:
    print("Stop message deleted successfully.")
else:
    print(f"Failed to delete stop message. Status code: {response.status_code}")