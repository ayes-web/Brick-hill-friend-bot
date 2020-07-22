from selenium import webdriver
import json, requests, time

# Browser used by the bot
driver = webdriver.Firefox()
waitTime = 10

# You have to login or else it doesn't work
driver.get("https://www.brick-hill.com/login")
t = input("Press enter after you have logged in to the site! ")
print(" ")

# I don't really know where to get the account count 
# so i just went to the newest account and put that number :D
lastAccount = 353863
firstAccount = -1

while firstAccount <= lastAccount:
	driver.get("https://www.brick-hill.com/user/" + str(firstAccount))

	try:
		# Finds the username
		name = driver.find_element_by_xpath("//div[@class='content text-center bold medium-text relative ellipsis']//span[@class='ellipsis']")
		print("Username: " + name.text + " ID: " + str(firstAccount))
	except: 
		print("I can't find the username!")
		print("ID: " + str(firstAccount))


	try:
		# Finds the friend request button
		button = driver.find_element_by_xpath("//a[@class='button small inline blue']")
	except:
		print("I can't find the button, going to the next one!")

	firstAccount += 1
	time.sleep(waitTime)
	print(" ")
