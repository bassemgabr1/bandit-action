from slack_sdk import WebClient
import os
# Sends message to Slack channel with given message
async def send_message(message: dict, SLACK_CHANNEL: str) -> dict:
    SLACK_TOKEN = os.getenv("SLACK_TOKEN", "none")
    SLACK_USERNAME = os.getenv("SLACK_USERNAME", "bandit-test")
    client = WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(
        channel=SLACK_CHANNEL, 
        blocks=message, 
        username=SLACK_USERNAME
    )