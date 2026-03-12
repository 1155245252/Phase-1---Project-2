# Gemini Web Agent

A command-line AI assistant that combines Google Gemini LLM and Google Custom Search to answer your questions intelligently. The agent decides if a web search is needed, retrieves and summarizes relevant information, and provides a concise, accurate answer.

## Features
- Intelligent decision: Uses Gemini to decide if web search is needed for your question.
- Web search: Retrieves and summarizes top web results using Google Custom Search.
- LLM-powered answers: Uses Gemini LLM to generate clear, concise answers.
- Clean, user-friendly command-line interface with color formatting.

## Setup

### 1. Install Required Libraries
```
pip install google-generativeai requests
```

### 2. Set Environment Variables (Recommended)
- `GEMINI_API_KEY`: Your Gemini API key
- `GOOGLE_API_KEY`: Your Google Custom Search API key
- `SEARCH_ENGINE_ID`: Your Custom Search Engine ID

Alternatively, you can hardcode these values in the script.

### 3. Run the Agent
```
python agent_bot.py
```

## Usage
- Type your question and press Enter.
- The agent will decide if web search is needed, show web results if used, and provide a final answer.
- Type `exit` or `quit` to leave the program.

## Example
```
==============================
  Gemini Web Agent
==============================

Type your question below. Type 'exit' or 'quit' to leave.

[You] What is the latest news about AI chips?

[Agent] Web search required.
[Web Search Results]
1. ...
2. ...

[Agent Answer]
(Gemini's concise summary)
```

## Notes
- If web search is not required, the agent will answer using only Gemini LLM.
- If web search is required, the agent will summarize web results and use Gemini to generate a final answer.

---

**Author:** Your Name
**License:** MIT# Gemini Bot

A simple Python script that connects to the Google Gemini API, prompts the user for a question, and prints the LLM's response.

## Features
- User prompt for any question
- Sends the question to Gemini LLM
- Prints the direct, relevant response

## Requirements
- Python 3.8+
- Google Gemini API key

## Setup

1. **Clone this repository**
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Set your Gemini API key as an environment variable:**
   - On Windows PowerShell:
     ```
     $env:GEMINI_API_KEY="your_api_key_here"
     ```
   - On macOS/Linux:
     ```
     export GEMINI_API_KEY=your_api_key_here
     ```
4. **Run the bot:**
   ```
   python gemini_bot.py
   ```

## Security Note
**Never share your API key publicly or commit it to version control.**

## How it works
- The script loads your API key from the environment.
- It uses the `google-genai` library to connect to Gemini.
- It prompts you for a question, sends it to the model, and prints the answer.

## License
MIT
