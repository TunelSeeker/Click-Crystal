from pyautogui import *
import pyautogui
import time
import random
import win32api, win32con
import keyboard

while True:
    # Set the confidence level for image matching (between 0 and 1)
    confidence_level = 0.8

    if keyboard.is_pressed("q"):
        print("Exiting the script...")
        break

    image_location = pyautogui.locateOnScreen('crystal.png', confidence=confidence_level)

    if image_location is not None:
        print("clicking!")
        image_x, image_y, _, _ = image_location
        image_center_x = image_x + image_location.width / 2
        image_center_y = image_y + image_location.height / 2
        pyautogui.click(image_center_x, image_center_y)
        time.sleep(0.5)  # You can adjust the delay here if needed
    else:
        print("I am unable to see it")
        time.sleep(0.5)
