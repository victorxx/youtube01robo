import pyautogui
import random
import string
import time
import hashlib

def iniciar():

                        # --- CONFIGURAÇÕES ---
                        coord_x = 794  # ajuste aqui para a posição X da caixa de comentários no seu monitor
                        coord_y = 500  # ajuste aqui para a posição Y da caixa de comentários no seu monitor

                        intervalo = 2400   # segundos entre cada comentário

                        # Mensagem base fixaddd
                        mensagem_base = "CONFIRA MUITO BOM ->https://www.youtube.com/watch?v=pny3_4_jKo0"

                        def gerar_texto_unico(base):
                            aleatorio = ''.join(random.choices(string.ascii_letters + string.digits, k=33))
                            hash_curto = hashlib.md5(str(time.time()).encode()).hexdigest()[:6]
                            return f"{base}\n\n {aleatorio}_{hash_curto}\n     "    



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


try:
    iniciar()
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    iniciar()
