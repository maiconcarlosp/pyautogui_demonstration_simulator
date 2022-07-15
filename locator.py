import pyautogui

# screenWidth, screenHeight = pyautogui.size() # returns the monitor size  
# print("The Screen Width is: ", screenWidth)  
# print("The Screen Height is: ", screenHeight)

# while True:
#     print (pyautogui.displayMousePosition())

currentMouseX, currentMouseY = pyautogui.position()  
print("X Cordinate is: ", currentMouseX)  
print("Y Cordinate is: ", currentMouseY) 