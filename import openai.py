import openai

# Set up your API key
openai.api_key = "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"

# Set up the prompt and parameters
prompt = "What is One Piece"
model = "text-davinci-002"
temperature = 0.7
max_tokens = 100

# Generate text using OpenAI's GPT-3
response = openai.Completion.create(
  engine=model,
  prompt=prompt,
  temperature=temperature, 
  max_tokens=max_tokens
)

# Print the generated text
print(response.choices[0].text.strip())
