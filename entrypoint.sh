#!/bin/sh

# Send start message
python /send_discord_message.py

# Trap the stop signal and send stop message
trap 'python /delete_discord_message.py' SIGTERM

# Start the main process
exec "$@"