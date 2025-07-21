import pyautogui
import random
import string
import time
import hashlib



# --- CONFIGURAÇÕES ---
coord_x = 794  # ajuste aqui para a posição X da caixa de comentários no seu monitor
coord_y = 500  # ajuste aqui para a posição Y da caixa de comentários no seu monitor

intervalo = 18000  # segundos entre cada comentário

# Mensagem base fixa
mensagem_base = "Confira essa oportunidade_>http://www.espiritosanto-es.com.br/cloudflare"

def gerar_texto_unico(base):
    aleatorio = ''.join(random.choices(string.ascii_letters + string.digits, k=33))
    hash_curto = hashlib.md5(str(time.time()).encode()).hexdigest()[:6]
    return f"{base}\n {aleatorio}_{hash_curto}\n     confira->seguro auto (27)99949-7001 \ncalvice nós temos  a solução->https://www.larissasaib.com.br/ \n{aleatorio}_{hash_curto}\nhttps://www.instagram.com/robertaotcham/\nhttps://www.instagram.com/geocredibnkvitoria/\n{aleatorio}_{hash_curto}"    



print("Você tem 5 segundos para posicionar a janela do YouTube com a caixa de comentário visível...")
time.sleep(5)

while True:
    texto = gerar_texto_unico(mensagem_base)
    print(f"Enviando comentário: {texto}")

    # Move o mouse até a caixa de comentários e clica
    pyautogui.moveTo(coord_x, coord_y, duration=0.5)
    pyautogui.click()
    time.sleep(0.5)

    # Digita o texto
    pyautogui.write(texto, interval=0.05)

    # Pressiona Enter para enviar
    pyautogui.press('enter')

    print(f"Comentário enviado! Esperando {intervalo} segundos para o próximo...")
    time.sleep(intervalo)
