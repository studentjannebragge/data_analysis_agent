import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Set the OpenAI API key
openai.api_key = openai_api_key

# Create a chat completion
completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about recursion in programming."}
    ]
)

# Print the assistant's response
print(completion.choices[0].message.content)
