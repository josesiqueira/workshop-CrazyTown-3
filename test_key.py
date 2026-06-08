"""Simple test to check that an Anthropic API key works."""

import os
import sys

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key or api_key == "paste-your-key-here":
    sys.exit("No API key found. Paste your key into the .env file first.")

client = Anthropic(api_key=api_key)

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Give me 5 Finnish movies."},
    ],
)

print("API key works! Response:\n")
print(response.content[0].text)
