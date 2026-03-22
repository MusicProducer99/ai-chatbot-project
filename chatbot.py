import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

while True:
    user_input = input("You: ")
    if user_input == "quit":
        break
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    print("Claude:", message.content[0].text)