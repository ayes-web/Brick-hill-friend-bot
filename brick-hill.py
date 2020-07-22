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
startingID = 354036


# You have to login or else it doesn't work
driver.get("https://www.brick-hill.com/login")

# Waits for the user to login to account
t = input("Please press enter after you have logged in to the site! ")
print(" ")

#loops go brrr
while startingID != -666:
	driver.get("https://www.brick-hill.com/user/" + str(startingID))

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

				driver.get("https://www.brick-hill.com/user/" + str(startingID))

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
		print("No error message found.")

	try:
		# prints username and id
		driver.get("https://www.brick-hill.com/user/" + str(startingID))
		name = driver.find_element_by_xpath("//div[@class='content text-center bold medium-text relative ellipsis']//span[@class='ellipsis']")
		print("Username: " + name.text + " ID: " + str(startingID))
	except:
		# username fail message
		print("I can't send the username and id for some reason!")

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