import webbrowser
import pyautogui
import time
import keyboard

time.sleep(3)

# t_end = time.time() + 60 * 1
# while time.time() < t_end:
while True:
    if (keyboard.is_pressed('q')):
        break
    loc = pyautogui.locateCenterOnScreen('C:\\Users\\USER\\Documents\\dot.png')
    pyautogui.moveTo(loc)
    pyautogui.click()


