import pyautogui
import  os
import time
from pathlib import Path

# Wait for Teams to open
time.sleep(5)

current_dir = os.getcwd()
png_file = os.path.join(current_dir, "gmailCheckbox.png")
png_file1 = os.path.join(current_dir, "gmailDeleteButton.PNG")

# Locate the "Join Now" button on the screen
#button_location = pyautogui.locateOnScreen('C:\\Users\\SanjeevaKumarGeejula\\Desktop\\TeamJoinNow\\teams.PNG', confidence=0.8)
button_location = pyautogui.locateOnScreen(png_file, confidence=0.8)
# delete_button = pyautogui.locateOnScreen(png_file1, confidence=0.8)


if button_location:
    for n in range(50):
        pyautogui.click(button_location)
        time.sleep(3)
        delete_button = pyautogui.locateOnScreen(png_file1, confidence=0.8)
        pyautogui.click(delete_button)
        time.sleep(3)
        
else:
    print("Join Now button not found!")