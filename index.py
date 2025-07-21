import pyautogui
import random
import string
import hashlib
import time

# === CONFIGURAÇÕES ===

# Coordenadas da caixa de comentário (ajuste conforme sua tela)
coord_x = 800  # substitua pelo valor certo
coord_y = 900  # substitua pelo valor certo

# Texto fixo que será enviado antes da parte aleatória
mensagem_base = "Ótimo vídeo!"

# Tempo entre cada envio de comentário (em segundos)
intervalo = 60

# Tempo para o usuário focar a janela ao iniciar
tempo_preparar = 5

# === FUNÇÃO PARA GERAR TEXTO ÚNICO ===
def gerar_texto_unico():
    aleatorio = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    hash_curto = hashlib.md5(str(time.time()).encode()).hexdigest()[:6]
    return f"{mensagem_base} {aleatorio}_{hash_curto}"

# === INÍCIO DO BOT ===
print("Bot iniciando...")
print(f"Você tem {tempo_preparar} segundos para focar o YouTube ou a janela desejada.")
time.sleep(tempo_preparar)

while True:
    texto = gerar_texto_unico()
    print(f"Comentário gerado: {texto}")

    # Clica na caixa de comentários e digita
    pyautogui.moveTo(coord_x, coord_y, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)

    pyautogui.write(texto, interval=0.05)
    pyautogui.press('enter')

    print(f"Comentário enviado. Aguardando {intervalo} segundos...\n")
    time.sleep(intervalo)
