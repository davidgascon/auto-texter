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
-Let you enter the message (type {name} where you want their first name to appear. You can only do this once per message.)
-Show you who you're going to be texting and thee sample message that will be sent
-Gather clicking points in google voice. It's recommended to have the script on the left, and google voice on the right.
-A final confirm window to make sure you want to send the messages
