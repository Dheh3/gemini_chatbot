# Google Generative AI Chatbot
 
This project is a Python-based chatbot that integrates with the Google Generative AI (Gemini) API to simulate conversations with a language model. The chatbot stores conversation history, and provides text-to-speech functionality using `pyttsx3`. 

## Features
- Integrates with the Google Generative AI API (`gemini-1.5-flash`).
- Supports text-to-speech (TTS) using the `pyttsx3` library.
- Stores and loads conversation history from a JSON file.

### Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

## Install dependencies
Run the following command to install all required dependencies:

```bash
pip install -q -U google-generativeai pyttsx3 python-dotenv
```


## Setup
1. API Key Configuration
To connect to the Google Generative AI API, you need to set up your API key. Store it in a .env file at the root of your project.

Create a .env file and add the following line:

```bash
API_KEY = "YOUR_API_KEY"
```
## Run the chatbot
To start the chatbot, run the following command:

```bash
python main.py
```
## Conversation History
The conversation history is automatically saved in a JSON file named history.json. The chatbot loads previous interactions when started, so you can pick up the conversation from where it left off.

Project Structure

```bash

├── README.md
├── .env                  # API key configuration
├── history.json           # Stores conversation history
├── your_script.py         # Main chatbot script
├── promptTemp.py          # Stores the chatbot prompt template
├── generationConfig.py    # Generation configuration (temperature, top_k, top_p, etc.)
└── requirements.txt       # Required packages (optional)

```






