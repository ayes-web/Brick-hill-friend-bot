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

#gets the username and password so it can login to account
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
print(" ")

# stores all of the people you have friended so its easier to skip later
# has different file for different accounts
try:
    with open("accounts/" + username + ".txt") as f:
    	print("Found accounts.txt!")
except IOError:
    print("No accounts.txt found, creating one!")
    f = open("accounts/" + username + ".txt", "x")

print("Enter the id to start from")
print("Nothing for default")

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

print(" ")

#loops go brrr
while True:
	# some user pages are broken, this is the easiest way to solve it
	if currentID == 0:
		currentID += 1
	with open("accounts/" + username + ".txt") as f:
		if "user:" + str(currentID) + "\n" in f.read():
			#if it finds the username in the list it skips
			print("Skipping ID: " + str(currentID))
		else:

			#opens user page
			driver.get("https://www.brick-hill.com/user/" + str(currentID))

			#adds the username to the txt file
			f = open("accounts/" + username + ".txt", "a")
			f.write("user:" + str(currentID) + "\n")
			f.close()

			try:
				# looks for error message
				errorMessage = driver.find_element_by_xpath("//div[@class='main-holder grid']/div[2]/span")
				g = 0
				print(" ")
				print("404 page found!")
				# gets error when it finds new account so this counters it
				try:
					while errorMessage.text == "Error 404: Page Not Found" or g == 0:
						# waits a little bit then tries again
						print("Waiting " + str(waitTime2) + " seconds!")
						time.sleep(waitTime2)

						driver.get("https://www.brick-hill.com/user/" + str(currentID))

						try:
							# checks for error message
							errorMessage = driver.find_element_by_xpath("//div[@class='main-holder grid']/div[2]/span")
						except:
							#gets out of loop
							g = 1	
				except:
					print(" ")
					print("New account found!")
			except:
				print("")

			try:
				#gets the username using brick-hill api
				apiLink = "https://api.brick-hill.com/v1/user/profile?id=" + str(currentID)
				userInfo = requests.get(apiLink)
				userName = json.loads(userInfo.text)

				# prints username and id
				print("Username: " + userName["username"] + " ID: " + str(currentID))
				sendWebhook("Request sent, Username: " + userName["username"] + " ID: " + str(currentID))
			except:
				# username fail message
				print("I can't send the userinfo for some reason!")

			try:
				# Finds the friend request button
				button = driver.find_element_by_xpath("//a[@class='button small inline blue']")
				button.click()
			except:
				#chooses wait time between pages
				chosenWait = uniform(waitTime3[0], waitTime3[1])

				# if it doesnt find the button it sends this and doesnt click
				print("I already sent friend request to them. (Or im not logged in)")
				print("Waiting " + str(chosenWait) + " Seconds")
			else:
				#chooses wait time between pages
				chosenWait = uniform(waitTime1[0], waitTime1[1])

				print("Request sent, waiting " + str(chosenWait) + " Seconds")
			# sleeps only if it didnt skip a page
			time.sleep(chosenWait)

	currentID += 1