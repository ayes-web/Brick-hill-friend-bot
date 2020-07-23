from selenium import webdriver
import json, requests, time, getpass
from random import *

# how long it waits going to next user
waitTime1 = [10,15]

# how long it waits on 404 pages
waitTime2 = 60

# the id it starts counting up from
startingID =  354225
currentID = ""

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
print(" ")

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print("Enter the id to start from")
print("Nothing for default")

try:
	currentID = int(input("ID: "))
except:
	if currentID != "":
		while is_number(currentID) == False:
			try:
				currentID = int(input("ID: "))
			except:
				print("Not a number, try again")
	else:
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
	driver.get("https://www.brick-hill.com/user/" + str(currentID))

	try:
		# looks for error message
		errorMessage = driver.find_element_by_xpath("//div[@class='main-holder grid']/div[2]/span")
		g = 0
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
		# prints username and id
		driver.get("https://www.brick-hill.com/user/" + str(currentID))
		name = driver.find_element_by_xpath("//div[@class='content text-center bold medium-text relative ellipsis']//span[@class='ellipsis']")
		print("Username: " + name.text + " ID: " + str(currentID))
	except:
		# username fail message
		print("I can't send the username and id for some reason!")

	try:
		# Finds the friend request button
		button = driver.find_element_by_xpath("//a[@class='button small inline blue']")
		button.click()
	except:
		# if it doesnt find the button it sends this and doesnt click
		print("I already sent friend request to them. (Or you aren't logged in)")

	currentID += 1

	#gives random wait time
	chosenWait = uniform(waitTime1[0], waitTime1[1])
	print("Request sent, waiting " + str(chosenWait) + " Seconds")
	#waits the given time
	time.sleep(chosenWait)