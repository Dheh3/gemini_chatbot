import google.generativeai as genai
import os
import pyttsx3
from dotenv import load_dotenv
from promptTemp import prompt
from generationConfig import generation_config 
import json
import logging


# logging config
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

HISTORY_FILE = "history.json"
set_end = 'set_end'

# Function to load history saved in a JSON file
def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r') as f:
                history = json.load(f)
                if not history:  # Handle empty file
                    return [{"role": "model", "parts": [prompt]}]
                return history
        except json.JSONDecodeError:
            logging.error("Erro ao carregar o historico. Inicializando com o prompt.")
            return [{"role": "model", "parts": [prompt]}]
    else:
        # If no history is found, initialize with prompt
        return [{"role": "model", "parts": [prompt]}]

# Function to save history
def save_history(history):
    try:
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history, f, indent=4)
    except Exception as e:
        logging.error(f"Erro ao salvar o histórico: {e}")

generation_config

# main function
def anime_ai(user_text, history):
    history.append({"role": "user", "parts": [user_text]})
    
    try:
        # chat init (usando todo o histórico sem limitação)
        chat = model.start_chat(history=history)
        response = chat.send_message(user_text, safety_settings="BLOCK_NONE")
        
        history.append({"role": "model", "parts": [response.text]})
        
        return response.text
    except Exception as e:
        logging.error(f"Erro ao interagir com a IA: {e}")
        return "Desculpe, houve um erro ao processar sua solicitação."

# TTS
def speak_text(text_in):
    engine = pyttsx3.init()
    engine.setProperty('rate', 250)
    engine.say(text_in)
    engine.runAndWait()

# ======= MAIN =======

logging.info(f'Programa iniciado')

load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("A chave de API não foi encontrada. Verifique o arquivo .env.")

genai.configure(api_key=api_key)

# model init
model = genai.GenerativeModel("gemini-1.5-flash")

# load history or create new
history = load_history()

# user input
output_of_text = input('input: ')

while output_of_text != set_end:
    if output_of_text.strip():  
        # IA res
        res = anime_ai(output_of_text, history)
        
        print("Ego:", res)
        speak_text(res)

        # save history after AI
        save_history(history)
    else:
        output_of_text = input('...')

    # new user entry
    output_of_text = input('input: ')

# save after session
save_history(history)

logging.info(f'Programa encerrado')
