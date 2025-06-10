import os
import google.generativeai as genai

def call_gemini(prompt: str):
    API_KEY = os.getenv("GEMINI_API_KEY")
    if not API_KEY:
        raise Exception("API Key Gemini tidak ditemukan! Pastikan sudah diset di .env")
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash-lite")
    response = model.generate_content(prompt)
    return response.text
