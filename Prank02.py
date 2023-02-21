import pyautogui as gui
import time
import random

number = input("Enter the number: ")
length = input("Enter the length of the word: ")

time.sleep(5)

with open('words.txt', 'r') as file:
    words = file.read().splitlines()

for i in range(int(number)):
    while True:
        word = random.choice(words)
        if len(word) == int(length):
            break
    gui.typewrite(word)
    gui.press('Enter')
