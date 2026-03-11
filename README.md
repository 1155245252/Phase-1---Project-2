# Gemini Bot

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
