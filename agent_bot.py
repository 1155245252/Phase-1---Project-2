import os
import requests
import google.genai as genai

"""
Agent Bot: Gemini LLM + Google Custom Search

Usage:
1. Install required libraries:
   pip install google-generativeai requests

2. Set the following environment variables (recommended):
   - GEMINI_API_KEY: Your Gemini API key
   - GOOGLE_API_KEY: Your Google Custom Search API key
   - SEARCH_ENGINE_ID: Your Custom Search Engine ID
   (Alternatively, you can hardcode these values in the script.)

3. Run the agent:
   python agent_bot.py

4. Enter your question when prompted. The agent will decide if web search is needed, retrieve relevant information, and provide a concise answer.

Notes:
- If web search is not required, the agent will answer using only Gemini LLM.
- If web search is required, the agent will summarize web results and use Gemini to generate a final answer.
"""
# --- Gemini LLM Setup ---
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")
gemini_client = genai.Client(api_key=gemini_api_key)

# --- Google Custom Search Setup ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or 'YOUR_API_KEY'
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID") or 'YOUR_SEARCH_ENGINE_ID'


def google_search(query, api_key=GOOGLE_API_KEY, cse_id=SEARCH_ENGINE_ID, num=5):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': query,
        'key': api_key,
        'cx': cse_id,
        'num': num
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def summarize_search_results(results):
    items = results.get('items', [])
    if not items:
        return 'No relevant web results found.'
    summary = ''
    for i, item in enumerate(items, 1):
        title = item.get('title', '')
        link = item.get('link', '')
        snippet = item.get('snippet', '')
        summary += f"{i}. {title}\n{link}\n{snippet}\n\n"
    return summary


def needs_web_search(question):
    # Ask Gemini if web search is needed
    prompt = f"Question: {question}\nDoes this question require up-to-date web information to answer accurately? Answer yes or no."
    response = gemini_client.models.generate_content(model="models/gemini-2.5-flash", contents=prompt)
    answer = response.candidates[0].content.parts[0].text.strip().lower()
    return 'yes' in answer


def agent_answer(question):
    if needs_web_search(question):
        print("[Agent] Web search required. Searching...")
        try:
            search_results = google_search(question)
            search_summary = summarize_search_results(search_results)
        except Exception as e:
            search_summary = f"Web search failed: {e}"
        # Ask Gemini to answer using the search summary
        prompt = f"Question: {question}\nWeb search results (summarized):\n{search_summary}\n\nProvide a concise, accurate answer to the question above using the web results."
        response = gemini_client.models.generate_content(model="models/gemini-2.5-flash", contents=prompt)
        answer = response.candidates[0].content.parts[0].text.strip()
        return answer
    else:
        print("[Agent] Web search not required. Using LLM only.")
        response = gemini_client.models.generate_content(model="models/gemini-2.5-flash", contents=question)
        return response.candidates[0].content.parts[0].text.strip()


def main():
    question = input("Ask your question: ")
    answer = agent_answer(question)
    print("\n[Agent Answer]\n", answer)

if __name__ == "__main__":
    main()
