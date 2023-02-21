import pyautogui
import time

# repetir 10 vezes
for i in range(10):
    # tempo de espera antes de começar a digitar
    time.sleep(5)

    # gerar a mensagem aleatória
    message = "Testando" + str(i+1)

    # digitar a mensagem
    pyautogui.typewrite(message)

    # pressionar a tecla Enter para enviar a mensagem
    pyautogui.hotkey('ctrl', 'enter')
