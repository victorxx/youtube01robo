import pyautogui
import random
import string
import time
import hashlib

def iniciar():

    # --- CONFIGURAÇÕES ---
    coord_x = 794  # ajuste para a posição X da caixa de comentários
    coord_y = 500  # ajuste para a posição Y da caixa de comentários

    intervalo_min = 1800  # mínimo 30 minutos entre comentários
    intervalo_max = 3600  # máximo 60 minutos entre comentários

    # Frases base para variar a mensagem
    mensagens_base = [
        "CONFIRA MUITO BOM -> https://www.youtube.com/watch?v=pny3_4_jKo0",
        "Dá uma olhada nesse vídeo incrível -> https://www.youtube.com/watch?v=pny3_4_jKo0",
        "Você precisa ver isso! -> https://www.youtube.com/watch?v=pny3_4_jKo0",
        "Vale a pena assistir -> https://www.youtube.com/watch?v=pny3_4_jKo0",
        "Conteúdo top aqui -> https://www.youtube.com/watch?v=pny3_4_jKo0",
    ]

    def gerar_texto_unico(base):
        aleatorio = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        hash_curto = hashlib.md5(str(time.time()).encode()).hexdigest()[:6]
        return f"{base}\n\n{aleatorio}_{hash_curto}\n"

    print("Você tem 5 segundos para posicionar a janela do YouTube com a caixa de comentário visível...")
    time.sleep(5)

    while True:
        # Escolhe uma mensagem base aleatória para variar
        mensagem_base = random.choice(mensagens_base)
        texto = gerar_texto_unico(mensagem_base)
        print(f"Enviando comentário: {texto}")

        # Move o mouse e clica na caixa de comentário
        pyautogui.moveTo(coord_x, coord_y, duration=0.5)
        pyautogui.click()
        time.sleep(0.5)

        # Digita o comentário
        pyautogui.write(texto, interval=0.05)

        # Pressiona Enter para enviar
        pyautogui.press('enter')

        # Espera um intervalo aleatório entre comentários
        intervalo = random.randint(intervalo_min, intervalo_max)
        print(f"Comentário enviado! Esperando {intervalo} segundos para o próximo...")
        time.sleep(intervalo)


try:
    iniciar()
except Exception as e:
    print(f"Ocorreu um erro: {e}")
