import google.generativeai as genai
import os
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

def ask_gemini(prompt):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt)
    return response.text