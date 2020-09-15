#auto texter


#bad way of clearning the terminal window
def clearscreen(iterations=0):
	if iterations != 0:
		iterations = 50-iterations
	a = iterations
	while a < 50:
		print("\n")
		a += 1



clearscreen()
print("Welcome to the autotexter.\n\n")



#imports
try:
	import pandas as pd
	import pyautogui as py
	import pygetwindow
	import time

	#other variables well need later
	terminalwindow = pygetwindow.getWindowsWithTitle('script.py')[0]

except:
	print("Not all required imports present. Please confirm all imports are satisfied then relaunch.")
	exit()



#import datafile
try:
	data = pd.read_excel('data.xlsx', header=0)
	data2 = pd.read_excel('data.xlsx', header=0)
except NameError:
	print("Error finding file. Do you have XLRD installed? (pip install xlrd)")
except:
	print("Error reading file.")	

print("\n\nHere is the data well be analyzing\n", data, "\n\n\n")

message = input("Enter the message you want to send out. Use curly brackets to indicate the name. Example - 'Hello {name}'. Or press enter for the default testing message")
if message == '':
	message = "Hello {name}. This is just a test."

clearscreen(5)
print("Here is a sample of each of the texts sent.")
for index, row in data.iterrows():
	ogmessage = message
	newmessage = ogmessage.split("{name}")
	name = row['first name'].lower().capitalize()
	messagetosend = newmessage[0] + name + newmessage[1]
	print(messagetosend)


clearscreen(5)


#Gets information about where things are on screen
print("We will now figure out where everything is on your screen. ")
print("Please open google voice to the text screen and press enter.")
input("Press enter to continue.")

input("Move your mouse to the 'send new message' button and press enter")
sendnewmessage = py.position()
py.click(sendnewmessage)
time.sleep(1)
py.write("360")
time.sleep(1)

terminalwindow.activate()

input("Move your mouse to where you enter the to number")
tomessage = py.position()
py.click(tomessage)
terminalwindow.activate()

input("Move your mouse to where you click to type the message")
typemessage = py.position()
py.click(typemessage)
terminalwindow.activate()

input("Lastly, move your mouse to where you hit send")
sendmessage = py.position()
py.click(sendmessage)
terminalwindow.activate()

py.PAUSE = 1 #sets the default pause time between clicks


def sendcycle(tomsg, message):
	global sendnewmessage, tomessage, typemessage, sendmessage
	print("Clicking new message")
	py.click(sendnewmessage)
	print("Writing to number")
	py.write(f"{tomsg}")
	time.sleep(1)
	print(f"Clicking 'send to {tomsg}'")
	py.click(tomessage)
	print("Clicking type message")
	py.click(typemessage)
	py.click(typemessage)
	print("Typing message")
	time.sleep(1)
	py.write(f"{message}")
	time.sleep(1)
	print("Hitting Send!")
	py.click(sendmessage)


if input("Press enter to send, or enter any character then enter to quit.") != '':
	exit("Exited before sending. Goodbye.")

textssent = 0
for index, row in data2.iterrows():
	ogmessage = message
	newmessage = ogmessage.split("{name}")
	name = row['first name'].lower().capitalize()
	messagetosend = newmessage[0] + name + newmessage[1]
	print(f"Message to send is {messagetosend}")
	sendcycle(row['phone number'], messagetosend)
	time.sleep(2)
	textssent += 1
print(f"{textssent} texts have been sent.")
print("Program complete. Goodbye!")


