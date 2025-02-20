import pyperclip
from googletrans import Translator
import time

# Inicializa o tradutor
translator = Translator()

# Função para traduzir a palavra
def traduzir_palavra(palavra):
    try:
        traducao = translator.translate(palavra, src='en', dest='pt')
        return traducao.text
    except Exception as e:
        return f"Erro ao traduzir: {e}"

# Monitora se há algo novo na área de transferência
def monitorar_area_de_transferencia():
    ultimo_texto = ""
    while True:
        texto_copiado = pyperclip.paste()
        if texto_copiado != ultimo_texto:
            ultimo_texto = texto_copiado
            print(f"Palavra selecionada: {texto_copiado}")
            traducao = traduzir_palavra(texto_copiado)
            print(f"Tradução: {traducao}")
        time.sleep(4)  

monitorar_area_de_transferencia()