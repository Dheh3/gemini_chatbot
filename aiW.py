import google.generativeai as genai
import os
import pyttsx3
from dotenv import load_dotenv

from promptTemp import prompt

prompt_template = prompt
set_end ='set_end'

load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("A chave de API não foi encontrada. Verifique o arquivo .env.")

# chave de API
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

# geração de texto config
generation_config = genai.GenerationConfig(
    temperature=1.0,  # Controla a criatividade da resposta
)

# Função AI
def anime_ai(user_text):
    
    chat = model.start_chat(
        history=[
            {"role": "model", "parts": [prompt_template]},
            {"role": "user", "parts": ["Olá"]},
        ]
    )

    # obter a resposta
    response = chat.send_message(user_text)

    #return response.candidates[0].content 
    return response.text

# texto em fala
def speak_text(text_in):
    engine = pyttsx3.init()
    #voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[1].id)
    engine.say(text_in)
    engine.runAndWait()

#================

output_of_text = input('input: ')

while output_of_text != set_end:
    res = anime_ai(output_of_text)
    print("Ego:", res)
    speak_text(res)
    output_of_text = input('input: ')


