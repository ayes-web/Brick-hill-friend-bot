from selenium import webdriver
import json, requests, time
from random import *

# Browser used by the bot
driver = webdriver.Firefox()
waitTime = [10,15]
firstAccount = 354022

# You have to login or else it doesn't work
driver.get("https://www.brick-hill.com/login")
t = input("Please press enter after you have logged in to the site! ")
print(" ")

#loops infinite
while firstAccount != -666:
	driver.get("https://www.brick-hill.com/user/" + str(firstAccount))

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
					print("Waiting 30 seconds!")
					time.sleep(30)

					driver.get("https://www.brick-hill.com/user/" + str(firstAccount))

					try:
						# checks for error message
						errorMessage = driver.find_element_by_xpath("//div[@class='main-holder grid']/div[2]/span")
					except:
						print("New account found!")
						g = 1
			except:
				print("FUck you it crashed ahahaah")
		except:
			print("HAHAHAHAHAHH")

	try:
		# prints username and id
		print("Username: " + name.text + " ID: " + str(firstAccount))
	except:
		#tries to get the name again
		driver.get("https://www.brick-hill.com/user/" + str(firstAccount))
		name = driver.find_element_by_xpath("//div[@class='content text-center bold medium-text relative ellipsis']//span[@class='ellipsis']")
		print("Username: " + name.text + " ID: " + str(firstAccount))
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

	firstAccount += 1

	#gives random wait time
	chosenWait = uniform(waitTime[0], waitTime[1])
	print("Waiting " + str(chosenWait) + " Seconds")
	#waits the given time
	time.sleep(chosenWait)
	print(" ")