import time
import keyboard, pyautogui, sys, math
test = 0
test3 = 0

while True:
    if keyboard.is_pressed('escape'):
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press(' ')
        test += 1
        test3 += 1
        pyautogui.press('enter')
        
        if test3 == 7:
            time.sleep(1)
            test3 = 0
        if test == 100:
            sys.exit()