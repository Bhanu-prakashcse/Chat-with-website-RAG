import openai

# Set your API key
openai.api_key = "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"

# Generate a response using GPT-4oaa
response = openai.ChatCompletion.create(
    model="gpt-4o-mini",  # Correct model name
    messages=[
        {"role": "user", "content": "write a haiku about AI"}
    ]
)

# Print the response
print(response['choices'][0]['message']['content'])
