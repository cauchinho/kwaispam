import pyautogui
import webbrowser as web
from time import sleep

web.open("link de whatsapp web del contacto a spamear")
sleep(10)
with open(r"path del archivo de texto de kwai") as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
