import google.generativeai as genai
import os

# Setting the environment variable correctly in Python
os.environ["API_KEY"] = "Your_API_Key"

# Configuring the API key
genai.configure(api_key=os.environ["API_KEY"])

# Initialize the model (ensure you're using the correct method to initialize)
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate content using the model
response = model.generate_content("write simple code for factorial in cpp")

# Print the response
print(response.text)
