import os
import google.genai as genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

client = genai.Client(api_key=api_key)
question = input("Ask a question: ")
response = client.models.generate_content(model="models/gemini-2.5-flash", contents=question)
print("Gemini says:", response.candidates[0].content.parts[0].text)