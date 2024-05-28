import keyboard
import pyautogui

while True:
    keyboard.wait("`")
    screenshot = pyautogui.screenshot()
    screenshot.save(r"C:\tmp\screen.png")
