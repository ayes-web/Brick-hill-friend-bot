import json, requests, time, getpass, os
from random import *
from selenium import webdriver
from discord_webhook import DiscordWebhook

# how long it waits going to next user
waitTime1 = [10,15]

# how long it waits on 404 pages
waitTime2 = 60

# when it doesnt find button goes faster
waitTime3 = [5, 10]

# the id it starts counting up from
startingID =  354225
currentID = ""

#Fill this in if you want discord webhooks
webhookURL = ""

def sendWebhook(bigChungus):
	if webhookURL != "":
		webhook = DiscordWebhook(url=webhookURL, content=bigChungus)
		response = webhook.execute()


#checks if input is number
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#gets info about user
def userInfo(id):
	apiLink = "https://api.brick-hill.com/v1/user/profile?id=" + str(id)
	userInfo = requests.get(apiLink)
	userInfos = json.loads(userInfo.text)
	return userInfos

#gets the username and password so it can login to account
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
print(" ")

# stores all of the people you have friended so its easier to skip later
# has different file for different accounts
try:
    with open("accounts/" + username + ".txt") as f:
    	print("Found accounts log!")
except IOError:
    print("Can't find accounts log found, creating one!")
    f = open("accounts/" + username + ".txt", "x")

print("Enter the id to start from\nNothing for default")

#checks if input is number or empty
try:
	currentID = int(input("ID: "))
except:
	if currentID != "":
		while is_number(currentID) == False:
			try:
				# chooses the user input
				currentID = int(input("ID: "))
			except:
				print("Not a number, try again")
	else:
		#chooses the default id
		currentID = startingID
		print("You chose " + str(currentID))

# Opens browser and login page
driver = webdriver.Firefox()
driver.get("https://www.brick-hill.com/login")

# password, username and submit fields for the bot to use them
passwordField = driver.find_element_by_id("password")
usernameField = driver.find_element_by_id("username")
submitButton = driver.find_element_by_xpath("//div[@class='content']/form/button[@class='green']")

#send the inputs and clicks button
passwordField.send_keys(password)
usernameField.send_keys(username)
submitButton.click()

while True:
	# some user pages are broken, this is the easiest way to solve it
	if currentID == 0:
		print("broken user " + str(currentID) ", skipping.")
		currentID += 1

	# looks for the current id in account log
	with open("accounts/" + username + ".txt") as f:
		if "user:" + str(currentID) + "\n" in f.read():
			print("Skipping ID: " + str(currentID))
		else:
			try:
				# looks for error message
				errorInfo = userInfo(currentID)
				while errorInfo['error'] == "Record not found":
					print("Record not found, waiting " + str(waitTime2) + " seconds!")
					time.sleep(waitTime2)
					errorInfo = userInfo(currentID)
			except:
				print("")
			#opens user page
			driver.get("https://www.brick-hill.com/user/" + str(currentID))
			try:
				userStuff = userInfo(currentID)

				# prints username and id
				print("Username: " + userStuff["username"] + " ID: " + str(currentID))
				sendWebhook("Request sent, username: " + userStuff["username"] + " ID: " + str(currentID))
			except:
				# username fail message
				print("I can't send the userinfo for some reason!")

			try:
				# Finds the friend request button
				button = driver.find_element_by_xpath("//a[@class='button small inline blue']")
				button.click()

				#adds the username to the txt file
				f = open("accounts/" + username + ".txt", "a")
				f.write("user:" + str(currentID) + "\n")
				f.close()

				#chooses wait time between pages
				chosenWait = uniform(waitTime1[0], waitTime1[1])
				print("Request sent, waiting " + str(chosenWait) + " Seconds")
				time.sleep(chosenWait)	
			except:
				#chooses wait time between pages
				chosenWait = uniform(waitTime3[0], waitTime3[1])
				print("I already sent friend request to them. (Or im not logged in)\nWaiting " + str(chosenWait) + " Seconds")
				time.sleep(chosenWait)

	currentID += 1