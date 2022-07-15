import pyautogui
import time

def simulador():
    # click no simulador
    pyautogui.moveTo(3000, 1000, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.5)

def estoque():
    # Estoque
    #automatico
    pyautogui.moveTo(3705, 1731, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #reset
    pyautogui.moveTo(3662, 1728, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #22
    pyautogui.moveTo(3527, 1866, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #23
    pyautogui.moveTo(3618, 1863, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #27
    pyautogui.moveTo(3437, 1895, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

def processo():
    # Processo
    #automatico
    pyautogui.moveTo(4256, 1736, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #reset
    pyautogui.moveTo(4209, 1730, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #16
    pyautogui.moveTo(4074, 1835, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #17
    pyautogui.moveTo(4163, 1835, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

def montagem():
    # Montagem
    #automatico
    pyautogui.moveTo(4803, 1731, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #reset
    pyautogui.moveTo(4757, 1728, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #16
    pyautogui.moveTo(4349, 1835, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #17
    pyautogui.moveTo(4440, 1835, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #20
    pyautogui.moveTo(4623, 1835, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

def expedicao():
    # Expedição
    #automatico
    pyautogui.moveTo(5354, 1731, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #reset
    pyautogui.moveTo(5310, 1728, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #15
    pyautogui.moveTo(5088, 1835, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #16
    pyautogui.moveTo(5166, 1835, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #20
    pyautogui.moveTo(5003, 1865, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

def removeBloco():
    # dropdown
    pyautogui.moveTo(4464, 1602, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.2)

    # câmera topo
    pyautogui.moveTo(4371, 1692, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.2)

    # remove bloco
    pyautogui.moveTo(3075, 597, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    # remove bloco B3
    pyautogui.moveTo(4389, 776, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    # remove bloco
    pyautogui.moveTo(3075, 597, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    # remove bloco B2
    pyautogui.moveTo(4484, 776, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    # remove bloco
    pyautogui.moveTo(3075, 597, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    # remove bloco B1
    pyautogui.moveTo(4587, 774, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    # dropdown
    pyautogui.moveTo(4464, 1602, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.2)

    # câmera frontal
    pyautogui.moveTo(4361, 1664, duration = 0.1)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

simulador()
estoque()
processo()
montagem()
expedicao()
removeBloco()

pyautogui.alert(text='Simulador pronto, execute o app.py!', title='Smart4.0', button='OK')  