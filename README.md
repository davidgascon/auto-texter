# auto-texter
Used to automatically send texts using google voice.

Data has to be stored as a data.xlsx (excel) file with the columns set as 'first name', 'last name', 'phone number'. 

Required imports are 
pyautogui
time
pygetwindow
pandas


Script will do the follow
-Run imports
-Import data from 'data.xlsx' twice (one as a proof)
-Lets you enter the message (type {name} where you want their first name to appear. You can only do this once per message.)
-Show you who you're going to be texting and thee sample message that will be sent
-Script will try to automatically locate the buttons that it needs in Google Voice. If it does not find the buttons it needs, it will prompt you to mvoe the mouse to where they're at and click enter. This is tested on Google Voice in Chrome with a screen resolutino of 1920x1280. It's recommended to have the script on the left, and google voice on the right.
-A final confirm window to make sure you want to send the messages. Press enter and enjoy!
