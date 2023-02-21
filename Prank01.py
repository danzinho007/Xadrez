import pyautogui as gui
import time

number = input("Enter the number: ")

time.sleep(5)

for i in range(int(number)):
        message = " OK 🤔"
        gui.typewrite(message)
        gui.press('Enter')
