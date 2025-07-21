import random
import string
import pyautogui
import time
import hashlib

ANUNCIOS_PATH = r'C:\Users\Administrator\Desktop\bot_pyautogui\anuncios.txt'

COORD_X = 800
COORD_Y = 900

INTERVALO = 60
TEMPO_PREPARO = 5

def carregar_anuncios(path):
    with open(path, 'r', encoding='utf-8') as f:
        anuncios = [linha.strip() for linha in f.readlines() if linha.strip()]
    return anuncios

def gerar_hash_unica(texto):
    # Usa o timestamp para garantir unicidade a cada chamada
    unico = texto + str(time.time())
    hash_obj = hashlib.md5(unico.encode('utf-8'))
    return hash_obj.hexdigest()[:8]  # Pega os primeiros 8 caracteres para ser curto

def main():
    anuncios = carregar_anuncios(ANUNCIOS_PATH)
    if not anuncios:
        print("Arquivo de anúncios vazio! Verifique o arquivo e tente novamente.")
        return

    print(f"Você tem {TEMPO_PREPARO} segundos para focar a janela correta...")
    time.sleep(TEMPO_PREPARO)

    while True:
        anuncio = random.choice(anuncios)
        hash_unico = gerar_hash_unica(anuncio)
        texto = f"{anuncio} #{hash_unico}"  # Pode mudar o formato, aqui usei "#" antes do hash

        print(f"Enviando: {texto}")

        pyautogui.moveTo(COORD_X, COORD_Y, duration=0.5)
        pyautogui.click()
        time.sleep(0.5)

        pyautogui.write(texto, interval=0.05)
        pyautogui.press('enter')

        print(f"Comentário enviado! Aguardando {INTERVALO} segundos para próximo...")
        time.sleep(INTERVALO)

if __name__ == "__main__":
    main()
