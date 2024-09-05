import requests

GEMINI_API_URL = "https://generativelanguage.googleapis.com"

API_KEY = "AIzaSyC0nJvpCuqT5gl2HBb4GXVL6g2a91su_L4"

import google.generativeai as genai

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

def analyze_text_with_gemini(user_input):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    data = {
        "text": user_input,
        "task": "sentiment-analysis",
    }
    
    response = requests.post(GEMINI_API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    user_input = input("Enter text to analyze with Gemini AI: ")
    result = analyze_text_with_gemini(user_input)
    print("Analysis Result:", result)

