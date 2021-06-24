
# spammer
import pyautogui, time


time.sleep(5)

x = open("script.txt", "r") # "r" means open as read
for word in x:
    pyautogui.typewrite("a") # types
    pyautogui.press("enter") # press enter on kb

exit()
