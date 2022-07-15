import pyautogui
import time
# import startup
    

def simulador():

    pyautogui.moveTo(3000, 1000, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(0.5)

    # zoom inicial
    pyautogui.keyDown('up')
    pyautogui.keyDown('left')
    time.sleep(0.1)
    pyautogui.keyUp('left')
    time.sleep(0.3)
    pyautogui.keyUp('up')
    time.sleep(1)

def cameraFrontal():
    # dropdown
    pyautogui.moveTo(4464, 1602, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    # câmera frontal
    pyautogui.moveTo(4361, 1664, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

def estoque(pos):

    descarte = 29 - pos

    #36[pos]
    pyautogui.moveTo(3252, 1893, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, pos, 0.1, 'left')
    time.sleep(0.1)

    #24
    pyautogui.moveTo(3708, 1863, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
    time.sleep(6)

    #20
    pyautogui.moveTo(3342, 1863, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(3)

    #21
    pyautogui.moveTo(3434, 1862, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(1)

    #20
    pyautogui.moveTo(3342, 1863, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(2)

    #36[descarte]
    pyautogui.moveTo(3252, 1893, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, descarte, 0.1, 'left')
    time.sleep(0.1)

    #24
    pyautogui.moveTo(3708, 1862, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
    time.sleep(5)

    #20
    pyautogui.moveTo(3342, 1863, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(3)

    #21
    pyautogui.moveTo(3434, 1862, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(1)

    #20
    pyautogui.moveTo(3342, 1863, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(2)

    #26
    pyautogui.moveTo(3342, 1892, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(0.1)

    #17
    pyautogui.moveTo(3615, 1835, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(1)

    #19
    pyautogui.moveTo(3251, 1865, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(7)

    #19
    pyautogui.moveTo(3251, 1865, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(0.1)

    #17
    pyautogui.moveTo(3615, 1835, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(0.1)

    #18
    pyautogui.moveTo(3707, 1835, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(0.1)

    #36[home]
    pyautogui.moveTo(3252, 1893, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
    time.sleep(0.1)

    #24
    pyautogui.moveTo(3708, 1862, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
    time.sleep(2)

    #27
    pyautogui.moveTo(3437, 1895, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(2)

    #27
    pyautogui.moveTo(3437, 1895, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(0.1)

    #26
    pyautogui.moveTo(3342, 1892, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(0.1)

    #18
    pyautogui.moveTo(3707, 1835, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(0.1)

def processo(pega, solta, gravacao=True):

    grava = 7 - pega
    if gravacao == True:
        solta = 1 + solta
        home = 8 - solta
    else:
        solta = (8 - pega) + solta
        home = 15 - (pega + solta)

    #0[pega]
    pyautogui.moveTo(3801, 1866, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, pega, 0.1, 'left')
    time.sleep(0.1)

    #18
    pyautogui.moveTo(4257, 1835, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
    time.sleep(2)

    #14
    pyautogui.moveTo(3891, 1832, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(0.1)

    #13
    pyautogui.moveTo(3798, 1832, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(3)

    #13
    pyautogui.moveTo(3798, 1832, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(1)

    if gravacao == True:
        #0[7]
        pyautogui.moveTo(3801, 1866, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, grava, 0.1, 'left')
        time.sleep(0.1)

        #18
        pyautogui.moveTo(4257, 1835, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
        time.sleep(2)

        #13
        pyautogui.moveTo(3798, 1832, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
        time.sleep(3)

        #15
        pyautogui.moveTo(3986, 1833, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
        time.sleep(0.1)

        #14
        pyautogui.moveTo(3891, 1832, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
        time.sleep(0.1)

        #13
        pyautogui.moveTo(3798, 1832, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
        time.sleep(2)


        #0[8]
        pyautogui.moveTo(3801, 1866, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 1, 0.1, 'left')
        time.sleep(0.1)

        #18
        pyautogui.moveTo(4257, 1835, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
        time.sleep(1)

        #13
        pyautogui.moveTo(3798, 1832, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
        time.sleep(3)

        #13
        pyautogui.moveTo(3798, 1832, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
        time.sleep(2)

        #0[7]
        pyautogui.moveTo(3801, 1866, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 14, 0.1, 'left')
        time.sleep(0.1)

        #18
        pyautogui.moveTo(4257, 1835, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
        time.sleep(1)

        #14
        pyautogui.moveTo(3891, 1832, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
        time.sleep(0.1)

        #13
        pyautogui.moveTo(3798, 1832, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
        time.sleep(3)

        #15
        pyautogui.moveTo(3986, 1833, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
        time.sleep(0.1)

        #13
        pyautogui.moveTo(3798, 1832, duration = 0.2)
        time.sleep(0.1)
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
        time.sleep(2)

    #0[solta]
    pyautogui.moveTo(3801, 1866, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, solta, 0.1, 'left')
    time.sleep(0.1)

    #18
    pyautogui.moveTo(4257, 1835, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
    time.sleep(2)

    #14
    pyautogui.moveTo(3891, 1832, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(0.1)

    #0[0]
    pyautogui.moveTo(3801, 1866, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, home, 0.1, 'left')
    time.sleep(0.1)

    #18
    pyautogui.moveTo(4257, 1835, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
    time.sleep(1)

def montagem(processo, funcao=None, tempo=7):

        match processo:
            # Pega peça e coloca em alguma posição, funções 1, 2 ou 3
            case "entrada":
                
                home = 28 - funcao

                #19
                pyautogui.moveTo(4532, 1832, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(0.1)

                #15
                pyautogui.moveTo(4803, 1803, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(0.1)

                #13
                pyautogui.moveTo(4623, 1802, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(9)

                #13
                pyautogui.moveTo(4623, 1802, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(0.1)

                #14
                pyautogui.moveTo(4715, 1802, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(6)

                #15
                pyautogui.moveTo(4803, 1803, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(1)

                #14
                pyautogui.moveTo(4715, 1802, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(0.1)

                #19
                pyautogui.moveTo(4532, 1832, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(0.1)

                #0[funcao]
                pyautogui.moveTo(4625, 1863, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, funcao, 0.1, 'left')
                time.sleep(0.1)

                #21
                pyautogui.moveTo(4713, 1833, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
                time.sleep(tempo)

                #0[home]
                pyautogui.moveTo(4625, 1863, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, home, 0.1, 'left')
                time.sleep(0.1)

                return
            
            # Devolve a peça para a esteira, funções 21, 22 ou 23
            case "saida":
                
                home = 28 - funcao

                #0[funcao]
                pyautogui.moveTo(4625, 1863, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, funcao, 0.1, 'left')
                time.sleep(0.1)

                #21
                pyautogui.moveTo(4713, 1833, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
                time.sleep(tempo)

                #0[home]
                pyautogui.moveTo(4625, 1863, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, home, 0.1, 'left')
                time.sleep(0.1)

                #19
                pyautogui.moveTo(4532, 1832, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(0.1)

                #15
                pyautogui.moveTo(4803, 1803, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(0.1)

                #13
                pyautogui.moveTo(4623, 1802, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(9)

                #15
                pyautogui.moveTo(4803, 1803, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(0.5)

                #13
                pyautogui.moveTo(4623, 1802, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(0.1)

                #14
                pyautogui.moveTo(4715, 1802, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(9)

                #14
                pyautogui.moveTo(4715, 1802, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(0.1)

                #20
                pyautogui.moveTo(4620, 1832, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(2)

                #20
                pyautogui.moveTo(4620, 1832, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(0.1)

                #19
                pyautogui.moveTo(4532, 1832, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
                time.sleep(0.1)
                
                return
            
            # Movimenta Robô
            case "robo":
                home = 28 - funcao

                #0[funcao]
                pyautogui.moveTo(4625, 1863, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, funcao, 0.1, 'left')
                time.sleep(0.1)

                #21
                pyautogui.moveTo(4713, 1833, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
                time.sleep(tempo)

                #0[home]
                pyautogui.moveTo(4625, 1863, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, home, 0.1, 'left')
                time.sleep(0.1)

                return
            
            # Tira foto
            case "foto":
                #25
                pyautogui.moveTo(4532, 1865, duration = 0.2)
                time.sleep(0.1)
                currentMouseX, currentMouseY = pyautogui.position()
                pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
                time.sleep(0.1)

                return

def expedicao(pos):

    home = 15 - pos

    #19
    pyautogui.moveTo(4922, 1865, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(0.1)

    #18[pega]
    pyautogui.moveTo(5328, 1833, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 14, 0.1, 'left')
    time.sleep(0.1)

    #17
    pyautogui.moveTo(5247, 1835, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
    time.sleep(3)  

    #13
    pyautogui.moveTo(4920, 1833, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(4)

    #14
    pyautogui.moveTo(5003, 1833, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(0.1)

    #13
    pyautogui.moveTo(4920, 1833, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(3)

    #18[pos]
    pyautogui.moveTo(5328, 1833, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, pos + 1, 0.1, 'left')
    time.sleep(0.1)

    #17
    pyautogui.moveTo(5247, 1835, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
    time.sleep(3) 

    #19
    pyautogui.moveTo(4922, 1865, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(0.1)

    #13
    pyautogui.moveTo(4920, 1833, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(4)

    #14
    pyautogui.moveTo(5003, 1833, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(0.1)

    #13
    pyautogui.moveTo(4920, 1833, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 1, 0.2, 'left')
    time.sleep(2)

    #18[home]
    pyautogui.moveTo(5328, 1833, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, home, 0.1, 'left')
    time.sleep(0.1)

    #17
    pyautogui.moveTo(5247, 1835, duration = 0.2)
    time.sleep(0.1)
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.click(currentMouseX, currentMouseY, 2, 0.2, 'left')
    time.sleep(3)

def focoEstoque(sentido):

    match sentido:

        case "in":
            pyautogui.keyDown('left')
            pyautogui.keyDown('up')
            time.sleep(0.7)
            pyautogui.keyUp('up')
            time.sleep(0.8)
            pyautogui.keyUp('left')
            time.sleep(1)
        
        case "out":
            pyautogui.keyDown('right')
            pyautogui.keyDown('down')
            time.sleep(0.7)
            pyautogui.keyUp('down')
            time.sleep(0.8)
            pyautogui.keyUp('right')
            time.sleep(1)

def focoProcesso(sentido):

    match sentido:

        case "in":
            pyautogui.keyDown('left')
            pyautogui.keyDown('up')
            time.sleep(0.6)
            pyautogui.keyUp('up')
            time.sleep(0.1)
            pyautogui.keyUp('left')
            time.sleep(1)
        
        case "out":
            pyautogui.keyDown('right')
            pyautogui.keyDown('down')
            time.sleep(0.6)
            pyautogui.keyUp('down')
            time.sleep(0.1)
            pyautogui.keyUp('right')
            time.sleep(1)

def focoMontagem(sentido):

    match sentido:

        case "in":
            pyautogui.keyDown('right')
            pyautogui.keyDown('up')
            time.sleep(0.1)
            pyautogui.keyUp('right')
            time.sleep(0.2)
            pyautogui.keyUp('up')
            time.sleep(1)
        
        case "out":
            pyautogui.keyDown('left')
            pyautogui.keyDown('down')
            time.sleep(0.1)
            pyautogui.keyUp('left')
            time.sleep(0.2)
            pyautogui.keyUp('down')
            time.sleep(1)

def focoExpedicao(sentido):

    match sentido:

        case "in":
            pyautogui.keyDown('right')
            pyautogui.keyDown('up')
            time.sleep(0.7)
            pyautogui.keyUp('up')
            time.sleep(1)
            pyautogui.keyUp('right')
            time.sleep(1)
        
        case "out":
            pyautogui.keyDown('left')
            pyautogui.keyDown('down')
            time.sleep(0.7)
            pyautogui.keyUp('down')
            time.sleep(1)
            pyautogui.keyUp('left')
            time.sleep(1)

simulador()
# startup.estoque()
# startup.processo()
# startup.montagem()
# startup.expedicao()

time.sleep(2)

focoEstoque('in')
estoque(6)
focoEstoque('out')
time.sleep(2)

focoMontagem('in')
montagem("entrada",3)
focoMontagem('out')
time.sleep(2)

focoEstoque('in')
estoque(5)
focoEstoque('out')
time.sleep(2)

focoMontagem('in')
montagem("entrada",1)
focoMontagem('out')
time.sleep(2)

focoProcesso('in')
processo(4,3)
processo(2,2,gravacao=False)
processo(5,1)
focoProcesso('out')

focoMontagem('in')
montagem("robo",4, tempo=6)
montagem("foto")
montagem("robo",15, tempo=6)
montagem("robo",5, tempo=6)
montagem("foto")
montagem("robo",16, tempo=6)
montagem("robo",6, tempo=6)
montagem("foto")
montagem("robo",17,tempo=6)
focoMontagem('out')
time.sleep(2)

focoProcesso('in')
processo(3,3)
processo(6,2)
processo(1,1)
focoProcesso('out')

focoMontagem('in')
montagem("robo",4, tempo=6)
montagem("foto")
montagem("robo",9, tempo=6)
montagem("robo",5, tempo=6)
montagem("foto")
montagem("robo",10, tempo=6)
montagem("robo",6, tempo=6)
montagem("foto")
montagem("robo",11, tempo=6)
montagem("robo",18,tempo=18)
montagem("robo",19, tempo=9)
montagem("saida",22)
focoMontagem('out')
time.sleep(1)

focoExpedicao('in')
expedicao(2)
focoExpedicao('out')