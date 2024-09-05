import google.generativeai as genai
import os

# Setting-up API key
os.environ["API_KEY"] = "AIzaSyC0nJvpCuqT5gl2HBb4GXVL6g2a91su_L4"

genai.configure(api_key=os.environ["API_KEY"])

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

paragraph = ""
print("Enter your paragraph (press Enter twice to finish):")

while True:
    line = input()
    if line:
        paragraph += line + "\n"
    else:
        break

# Get response from API
response = model.generate_content(paragraph)

# Print the response
print(response.text)