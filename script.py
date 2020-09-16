#auto texter


#bad way of clearning the terminal window
def clearscreen(iterations=0):
	if iterations != 0:
		iterations = 50-iterations
	a = iterations
	while a < 50:
		print("\n")
		a += 1

def sendcycle(tomsg, message):
	global sendnewmessage, tomessage, typemessage, sendmessage
	print("Clicking new message")
	py.click(sendnewmessage)
	print("Writing to number")
	py.write(f"{tomsg}")
	time.sleep(.5)
	py.press('enter')
	time.sleep(.5)
	print(f"Clicking 'send to {tomsg}'")
	py.click(tomessage)
	print("Clicking type message")
	py.click(typemessage)
	py.click(typemessage) #for whatever reason it needs to double click. This is because the screen is currently entering who you'll send the text to. First click is to close that prompt, the second click is to select where the message goes.	
	print("Typing message")
	time.sleep(1)
	py.write(f"{message}")
	time.sleep(1)
	print("Hitting Send!")
	py.click(sendmessage)
	print("\n")



clearscreen()

print("Welcome to the autotexter.\n\n")



#imports
try:
	import pandas as pd
except:
	print("Pandas Import needed. Try running 'pip install pandas'.")
	exit()
	
try:
	import pyautogui as py
except:
	print("Pyautoguu import needed. Try running 'pip install pyautogui'.")
	exit()
	
try:
	import pygetwindow
except:
	print("Pygetwindow import needed. Try running 'pip install pygetwindow'.")
	exit()
	
try:
	import time
except:
	print("Time import needed  Try running 'pip install time'.")
	exit()


#other variables we'll need later
try:
	try:
		terminalwindow = pygetwindow.getWindowsWithTitle('script.py')[0] #sets the terminal window that will be opened. This should never be the cause of an error.
	except:
		print("Error find this terminal window")
	try:
		py.PAUSE = 1 #sets the default pause time between clicks
	except:
		print("Error setting pause time in pyautogui.") #this should also never be seen.
except:
	exit()



#import datafile
try:
	data = pd.read_csv('data.csv') 
except:
	try:
		data = pd.read_excel('data.xlsx', header=0)
	except NameError:
		print("Error finding data.xlsx. Do you have XLRD installed? (pip install xlrd)")
		print("Error reading file.")	

print("\n\nHere is the data well be analyzing\n", data, "\n\n\n")

message = input("Enter the message you want to send out. Use curly brackets to indicate the name. Example - 'Hello {name}'. Or press enter for the default testing message")
message = message.strip()
if message == '':
	message = "Hello {name}. This is just a test."

clearscreen(5)

print("Here is a sample of each of the texts sent.")
for index, row in data.iterrows():
	newmessage = message.split("{name}")
	name = row['first name'].lower().capitalize()
	messagetosend = newmessage[0] + name + newmessage[1]
	print(messagetosend)


clearscreen(5)


#Gets information about where things are on screen
print("This script is a macro, whoch means it simulates computer clicks to complete the task of sending messages via Google Voice. For this to properly work, we will need to log where the following buttons are.")
print("The script will try to automatically locate these buttons, however when prompted, you may need to follow the directions")
print("Please open google voice to the text screen.")
input("Press enter to continue.")

#locates 'send new message' button
try: 
	sendnewmessage = py.locateCenterOnScreen('images/send_new_message.png')
except:
	terminalwindow.activate()
	input("Move your mouse to the 'send new message' button and press enter.")
	sendnewmessage = py.position()

py.click(sendnewmessage)
time.sleep(1)
py.write("360") #needed to get the following button to appear
time.sleep(1)
py.press('enter')
time.sleep(.5)

#locates 'type a name or number' button
try:
	tomessage = py.locateCenterOnScreen("images/type_a_name.png")
except:
	terminalwindow.activate()
	input("Move your mouse to where you enter the to number, then press enter.")
	tomessage = py.position()
py.click(tomessage)

#locates where you type the message
try:
	typemessage = py.locateCenterOnScreen("images/type_a_message.png")
except:
	terminalwindow.activate()
	input("Move your mouse to where you click to type the message, press enter.")
	typemessage = py.position()
py.click(typemessage)

#locates send button
try:
	sendmessage = py.locateCenterOnScreen("images/send.png")
except:
	terminalwindow.activate()
	input("Lastly, move your mouse to where you hit send, then press enter")
	sendmessage = py.position()
py.click(sendmessage)



terminalwindow.activate()
if input("Press enter to send, or enter any character then enter to quit.") != '':
	exit("Exited before sending. Goodbye.")

textssent = 0
for index, row in data.iterrows():
	newmessage = message.split("{name}")
	name = row['first name'].lower().capitalize()
	messagetosend = newmessage[0] + name + newmessage[1]
	print(f"Message to send is {messagetosend}")
	sendcycle(row['phone number'], messagetosend)
	time.sleep(2)
	textssent += 1
print(f"{textssent} texts have been sent.")
print("Program complete. Goodbye!")


