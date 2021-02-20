#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 16:32:05 2021

@author: davidstansbury
"""

# import modules
import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# sets where to find lists of words and question words for queries
WORDLIST_FILENAME = ".../shortlist.txt"
QUESTION_WORDS_FILENAME = ".../questions.txt"

# sets which browser we want to use
BROWSER = webdriver.Firefox(executable_path=".../geckodriver")

def create_wordlist():
	""" 
	sets up list of words we will 
	assemble queries from.
	"""
	word_list = loadWords()
	return(word_list)


def create_questionlist():
	"""
	sets up list of question words we can use
	for queries.
	"""
	question_list = loadQuestions()
	return(question_list)

def main(words, questions):
	""" 
	main function of the program
	"""
		
	# get a query
	query = assemble_query(words, questions)
	print(f"search is {query}")
	
	googleSearch(query)
	
	# get random number for which 
	# result to click on (1-5)
	link_to_click = random.randrange(1, 6)

	# get random number of how long to 
	# stay on the page (3-30s)
	seconds_on_page = random.randrange(3, 31)

	# click that result and remain on the page for that long.

	# close down the page

	# get random number for how long to 
	# wait until next search (30s-5m)
	#wait_time = random.randrange(60, 65)
	#print(f"wait time is {wait_time}")

	# wait that long.
	#time.sleep(wait_time) 

	# execute the program again, from the stage after log in.




def loadWords():
	"""
	Takes file where query words are provided and 
	returns a list of these words.
	"""
	print("Loading word list from file...")
	
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r')
	
	# line: string
	line = inFile.readline()
	
	# wordlist: list of strings
	wordlist = line.split()
	print("  ", len(wordlist), "words loaded.")
	return wordlist

def loadQuestions():
	"""
	Takes file where question words are provided and
	returns a list of them.
	"""
	print("Loading question words from file...")

	# inFile: file
	inFile = open(QUESTION_WORDS_FILENAME, 'r')

	# line: string
	line = inFile.readline()

	#questionlist: list of strings
	questionlist = line.split()
	print(" ", len(questionlist), "question words loaded.")
	return questionlist


def isQuestion():
	"""
	Determines if the query is a question by
	randomly flipping a coin. 50/50 it's 
	a question
	"""
	number = random.randrange(1,3)
	if number == 1:
		return 0
	else:
		return 1


# creates the search query we will run
def assemble_query(wordlist, questionlist):
	"""
	ADD EXPLANATION
	"""
	query = []

	# get random number for search query length (1-8 words)
	query_length = random.randrange(1, 10)

	# error test if query length longer than list of words
	if query_length > len(wordlist):
		query_length = len(wordlist)

	i = 1
	# randomly select words from list of words
	while i <= query_length:
		chosen_word = random.choice(wordlist)

		# if selected word already in query, chooses another
		if chosen_word in query:
			i += 0

		# if not, adds the word to the query
		else:
			query.append(chosen_word)
			
			##print(f"added {chosen_word} to query. Query is now {query}")
			i += 1		

	# check if question word should be included
	# if yes, adds the question to the start of the query
	
	if isQuestion() == 1:
		
		##print("This is a question.")
		
		question = random.choice(questionlist)
		query.insert(0, question)
		query.append("?")
	
	# iterate through the query list and 
	# create a string for the final query.
	
	empty_string = " "

	finalquery = empty_string.join(query)

	# checks if last character a question mark
	# if it is, deletes the space before the question mark
	
	if finalquery.endswith("?"):
		finalquery = finalquery[:-2]
		finalquery += "?"

	return(finalquery)

def facebookLogIn(username, password):
	"""
	tries to log the user in to their Facebook account
	"""
	try:
		BROWSER.get('https://www.facebook.com')
		BROWSER.implicitly_wait(15)

		usernameBox = BROWSER.find_element_by_id('email')
		usernameBox.send_keys(username)
		print("Entered username")
		time.sleep(5)

		passwordBox = BROWSER.find_element_by_id('pass')
		passwordBox.send_keys(password)
		print("Entered password")
		time.sleep(5)

		loginButton = BROWSER.find_elements_by_css_selector('input[type=submit]') 
		loginButton.click()
		print("Clicked button")

		print("Login successful")
	
	except:
		print("Login Failed") 
		time.sleep(5)

	time.sleep(5)
	BROWSER.quit()


def googleSearch(searchterm):
	"""
	runs a Google search on a given search term
	"""
	BROWSER.get('https://www.google.com')
	
	# finds the search bar
	inputelement = BROWSER.find_element_by_name('q') 
	
	# puts the desired search into the search bar
	inputelement.send_keys(searchterm)
	
	# hits 'return' on the search
	inputelement.send_keys(Keys.ENTER)
	
	# sleep for 5 seconds so you can see the results
	time.sleep(5) 
	
	# closes the browser
	BROWSER.quit()
	

main(create_wordlist(), create_questionlist())


