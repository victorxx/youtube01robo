import random
import pyautogui
import time

# Configurações
POSICAO_X_PATH = r'C:\Users\Administrator\Desktop\bot_pyautogui\coordenadax.txt'
POSICAO_Y_PATH = r'C:\Users\Administrator\Desktop\bot_pyautogui\coordenaday.txt'
ANUNCIOS_PATH = r'C:\Users\Administrator\Desktop\bot_pyautogui\anuncios.txt'
RANDOMIZAR_PATH = r'C:\Users\Administrator\Desktop\bot_pyautogui\randomizar.txt'

TEMPO_ESPERA_INICIAL = 5          # Tempo para preparar a janela (na 1ª rodada)
INTERVALO_DIGITACAO = 0.05        # Intervalo entre caracteres digitados
TEMPO_ESPERA_APOS_CLICK = 1       # Pausa após clicar antes de digitar
TEMPO_ESPERA_ENTRE_RODADAS = 30   # Tempo entre digitação de anúncios (em segundos)

def carregar_coordenadas(x_path, y_path):
    with open(x_path, 'r') as f:
        x = int(f.read().strip())
    with open(y_path, 'r') as f:
        y = int(f.read().strip())
    return x, y

def carregar_anuncios(path):
    with open(path, 'r', encoding='utf-8') as f:
        linhas = [linha.strip() for linha in f.readlines() if linha.strip()]
    return linhas

def carregar_caracteres_randomizar(path):
    with open(path, 'r', encoding='utf-8') as f:
        texto = f.read()
    # Remove espaços, quebras de linha e duplicatas
    caracteres = list(set(texto.strip().replace('\n', '').replace('\r', '').replace(' ', '')))
    if not caracteres:
        raise ValueError("Arquivo de randomizar está vazio ou inválido!")
    return caracteres

def gerar_string_aleatoria(caracteres, tamanho=12):
    return ''.join(random.choices(caracteres, k=tamanho))

def main():
    coord_x, coord_y = carregar_coordenadas(POSICAO_X_PATH, POSICAO_Y_PATH)
    anuncios = carregar_anuncios(ANUNCIOS_PATH)
    caracteres_randomizar = carregar_caracteres_randomizar(RANDOMIZAR_PATH)

    if not anuncios:
        print("Arquivo de anúncios está vazio! Finalizando programa.")
        return

    print(f"Movendo mouse para ({coord_x}, {coord_y}).")
    print(f"Aguardando {TEMPO_ESPERA_INICIAL} segundos para focar na janela.")
    time.sleep(TEMPO_ESPERA_INICIAL)

    while True:
        # Gera a string única usando só os caracteres do arquivo randomizar.txt
        stringunica = gerar_string_aleatoria(caracteres_randomizar, tamanho=16)

        anuncio_escolhido = random.choice(anuncios)
        texto_completo = f"{anuncio_escolhido} {stringunica}"

        print(f"Anúncio escolhido: '{anuncio_escolhido}'")
        print(f"String única gerada: '{stringunica}'")
        print(f"Texto que será digitado: '{texto_completo}'")

        pyautogui.moveTo(coord_x, coord_y)
        pyautogui.click()
        time.sleep(TEMPO_ESPERA_APOS_CLICK)

        pyautogui.write(texto_completo, interval=INTERVALO_DIGITACAO)
        pyautogui.press('enter')

        print(f'Anúncio digitado. Aguardando {TEMPO_ESPERA_ENTRE_RODADAS} segundos para próxima rodada...\n')
        time.sleep(TEMPO_ESPERA_ENTRE_RODADAS)

if __name__ == "__main__":
    main()
