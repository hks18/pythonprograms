import pywhatkit
import pyautogui
import time

# Send the message
pywhatkit.sendwhatmsg("+919937557977", "abe ooo khankir chele", 19, 26)

# Wait for the WhatsApp Web page to load
time.sleep(15)  # Adjust if needed

# Press "Enter" to send the message automatically
pyautogui.press("enter")
