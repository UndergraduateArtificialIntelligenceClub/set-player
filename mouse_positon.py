import pyautogui

while True:
    print(f'\r{pyautogui.position()}', end='', flush=True)
