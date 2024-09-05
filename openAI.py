import openai

# Set up your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Function to interact with the model
def ask_chatgpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can also use "gpt-3.5-turbo" for better efficiency
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
user_prompt = "Explain sorting algorithms in simple terms."
response = ask_chatgpt(user_prompt)
print(response)
