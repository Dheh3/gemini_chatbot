import google.generativeai as genai
import os
import pyttsx3
from dotenv import load_dotenv
from promptTemp import prompt

# Prompt inicial
prompt_template = prompt
set_end = 'set_end'

# Carregar variáveis de ambiente
load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("A chave de API não foi encontrada. Verifique o arquivo .env.")

# Configurar a API
genai.configure(api_key=api_key)

# Inicializar o modelo
model = genai.GenerativeModel("gemini-1.5-flash")

# Configuração de geração de texto
generation_config = genai.GenerationConfig(
    temperature=1.0,  # Controla a criatividade da resposta
)

# Função que mantém o histórico e gera resposta
def anime_ai(user_text, history):
    # Adicionar a mensagem do usuário ao histórico
    history.append({"role": "user", "parts": [user_text]})
    
    # Enviar a mensagem e obter a resposta
    chat = model.start_chat(history=history)
    response = chat.send_message(user_text)
    
    # Adicionar a resposta da IA ao histórico
    history.append({"role": "model", "parts": [response.text]})
    
    return response.text

# Função para converter texto em fala
def speak_text(text_in):
    engine = pyttsx3.init()
    engine.say(text_in)
    engine.runAndWait()

# ======= Principal =======

# Inicializar o histórico com o prompt inicial
history = [{"role": "model", "parts": [prompt_template]}]

# Entrada do usuário
output_of_text = input('input: ')

while output_of_text != set_end:
    # Obter a resposta da IA, passando o histórico
    res = anime_ai(output_of_text, history)
    
    # Exibir e falar a resposta
    print("Ego:", res)
    speak_text(res)
    
    # Nova entrada do usuário
    output_of_text = input('input: ')
