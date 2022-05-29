import pyautogui
import webbrowser
import time

#The value for "new" was specified as "2" so that the url is opened in a new browser window instead of a new tab
webbrowser.open('http://gmail.com', new=2)

time.sleep(15)
myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'C:\Users\esand\OneDrive\Desktop\SCREENSHOTS\screenshot1.png')