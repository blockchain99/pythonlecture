# Web Scraping Project
# Introduction
# In this project you'll be building a quotes guessing game. 
# When run, your program will scrape a website for 
# a collection of quotes. Pick one at random and display it.
#  The player will have four chances to guess who said the quote. 
# After every wrong guess they'll get a hint about the author's identity.

# Requirements
# Create a file called `scraping_project.py` which, 
# when run, grabs data on every quote from 
# the website http://quotes.toscrape.com
# You can use `bs4` and `requests` to get the data. 
# For each quote you should grab the text of the quote, 
# the name of the person who said the quote, 
# and the href of the link to the person's bio. 
# Store all of this information in a list.
# Next, display the quote to the user and ask who said it.
#  The player will have four guesses remaining.
# After each incorrect guess, the number of guesses remaining 
# will decrement. If the player gets to zero guesses 
# without identifying the author, the player loses and 
# the game ends. If the player correctly identifies the author, 
# the player wins!
# After every incorrect guess, the player receives 
# a hint about the author. 
# For the first hint, make another request to 
# the author's bio page (this is why we originally scrape this data), 
# and tell the player the author's birth date and location.
# The next two hints are up to you! Some ideas: 
# the first letter of the author's first name, 
# the first letter of the author's last name, 
# the number of letters in one of the names, etc.
# When the game is over, ask the player 
# if they want to play again. If yes, restart the game
#  with a new quote. If no, the program is complete.

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import reader, DictReader, writer, DictWriter

base_url = "http://quotes.toscrape.com"
url = "/page/1"

with open("test333csvresult.csv", "w") as file:
    # headers = ["text", "author", "bio-link"]
    # csv_writer = DicWriter(file, fieldnames = headers)
    csv_writer = writer(file)
    # csv_writer.writeheader()
    csv_writer.writerow("text", "author", "bio-link")

    while url:

        res= requests.get(f"{base_url}{url}")
        print(f"Now Scrapping {base_url}{url}...")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote") #list
        for quote in quotes: # list of dictionaries
            csv_writer.writerow({
                "text" : quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"] 
            })

    #automate parsing every page using Next link
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        # sleep(1) #wait 2 second btwn scrapping. 

    with open("test333csvresult.csv", "r") as file:
        # csv_reader = reader(file)
        csv_reader = DictReader(file) #OrderedDictionary
        for quote in csv_reader:
            print(quote)
            # print(quote['text'])
        print("------------------------------------")    
        # choice = choice(list(csv_reader))    
        # print(choice)
        quote = csv_reader
    # print(list(csv_reader)) #one list consits of lists

        # quote = choice(csv_reader) #choose from list or set, not dict.
        # print(quote)
        # # print(quote[0])
        # print(quote["text"])

        # remaining_guesses = 4
        # print("Here's a quote: ")
        # print("------------ text -----------")
        # print(quote["text"])
        # print("------------ author -----------")
        # print(quote["author"])
        # guess = ''
        # while guess.lower() != quote["author"].lower() and remaining_guesses > 0: 
        #     guess = input(f"Who said this quote? Guesses remaining:{remaining_guesses} ")
        #     if guess.lower() == quote["author"].lower():
        #         print("You got it , Right!")
        #         break
        #     remaining_guesses -= 1
        #     if remaining_guesses == 3:
        #         res = requests.get(f"{base_url}{quote['bio-link']}")
        #         soup = BeautifulSoup(res.text, "html.parser")
        #         # print(soup.body)
        #         birth_date = soup.find(class_="author-born-date").get_text()
        #         birth_location = soup.find(class_="author-born-location").get_text()
        #         print(f"Here's hint: The author was born in {birth_date} in {birth_location}")
        #     elif remaining_guesses == 2:
        #         print(f"Here's hint: The author's first name start with: {quote['author'][0]}")
        #     elif remaining_guesses == 1:
        #         last_initial = quote["author"].split(" ")[1][0]    
        #         print(f"Here's hint: The author's last name start with: {last_initial}")
        #     else:
        #         print(f"Sorry you ran out of guesses. The answer was {quote['author']}" )
        # print("After while loop")