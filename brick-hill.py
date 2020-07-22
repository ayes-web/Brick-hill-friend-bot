from selenium import webdriver
import json, requests, time, random

# Browser used by the bot
driver = webdriver.Firefox()
waitTime = [5,6,7,8,9,10]

# You have to login or else it doesn't work
driver.get("https://www.brick-hill.com/login")
t = input("Press enter after you have logged in to the site! ")
print(" ")

# I don't really know where to get the account count 
# so i just went to the newest account and put that number :D
lastAccount = 353913
firstAccount = -1

while firstAccount <= lastAccount:
	driver.get("https://www.brick-hill.com/user/" + str(lastAccount))

	try:
		# Finds the username
		name = driver.find_element_by_xpath("//div[@class='content text-center bold medium-text relative ellipsis']//span[@class='ellipsis']")
		print("Username: " + name.text + " ID: " + str(lastAccount))
	except: 
		print("I can't find the username!")
		print("ID: " + str(lastAccount))


	try:
		# Finds the friend request button
		button = driver.find_element_by_xpath("//a[@class='button small inline blue']")
		button.click()
	except:
		print("I can't find the button, going to the next one!")

	lastAccount -= 1
	chosenWait = random.choice(waitTime)
	print("Waited " + str(chosenWait) + " Seconds")
	time.sleep(chosenWait)
	print(" ")
