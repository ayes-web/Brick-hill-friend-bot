from selenium import webdriver
import json, requests, time
from random import *

# Browser used by the bot
driver = webdriver.Firefox()

# how long it waits going to next user
waitTime1 = [10,15]

# how long it waits on 404 pages
waitTime2 = 30

# the id it starts counting up from
startingID = 354022

# You have to login or else it doesn't work
driver.get("https://www.brick-hill.com/login")
t = input("Please press enter after you have logged in to the site! ")
print(" ")

#loops infinite
while startingID != -666:
	driver.get("https://www.brick-hill.com/user/" + str(startingID))

	try:
		# Finds the username
		name = driver.find_element_by_xpath("//div[@class='content text-center bold medium-text relative ellipsis']//span[@class='ellipsis']")
	except:
		try:
			# checks for error message
			errorMessage = driver.find_element_by_xpath("//div[@class='main-holder grid']/div[2]/span")
		except:
			print("No error message found!")

		g = 0
		print("Empty page found!")
		try:
			# i have no idea why does trys are needed but it closes otherwise please help i am going insane
			try:
				while errorMessage.text == "Error 404: Page Not Found" or g == 0:
					print("Waiting " + str(waitTime2) + " seconds!")
					time.sleep(waitTime2)

					driver.get("https://www.brick-hill.com/user/" + str(startingID))

					try:
						# checks for error message
						errorMessage = driver.find_element_by_xpath("//div[@class='main-holder grid']/div[2]/span")
					except:
						print("New account found!")
						#gets out of loop
						g = 1
			except:
				print("FUck you it crashed ahahaah")
		except:
			print("HAHAHAHAHAHH")

	try:
		# prints username and id
		driver.get("https://www.brick-hill.com/user/" + str(startingID))
		name = driver.find_element_by_xpath("//div[@class='content text-center bold medium-text relative ellipsis']//span[@class='ellipsis']")
		print("Username: " + name.text + " ID: " + str(startingID))
	except:
		# username fail message
		print("I failed to send you the username and id :(")

	try:
		# Finds the friend request button
		button = driver.find_element_by_xpath("//a[@class='button small inline blue']")
		button.click()
	except:
		# if it doesnt find the button it sends this and doesnt click
		print("I already sent friend request to them.")
		print("Going to the next one!")

	startingID += 1

	#gives random wait time
	chosenWait = uniform(waitTime1[0], waitTime1[1])
	print("Waiting " + str(chosenWait) + " Seconds")
	#waits the given time
	time.sleep(chosenWait)
	print(" ")