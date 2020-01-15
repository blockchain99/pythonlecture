#random choice is wrong , always Dr. Seuss shown!!

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import reader, DictReader, writer, DictWriter

base_url = "http://quotes.toscrape.com"
url = "/page/1"

with open("test333csvresult.csv", "w") as file:
    headers = ["text", "author", "bio-link"]
    csv_writer = DictWriter(file, fieldnames = headers)
    csv_writer.writeheader()

    while url:

        res= requests.get(f"{base_url}{url}")
        print(f"Now Scrapping {base_url}{url}...")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote") #list
        total = 0
        for quote in quotes:
            csv_writer.writerow({
                "text" : quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"] 
            })
            total += 1
        print("=====total=======", total)    
        my_chosen_num = choice(range(0, total))
        print("****chosen num*****",my_chosen_num)
    #automate parsing every page using Next link
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        # sleep(1) #wait 2 second btwn scrapping. 

    with open("test333csvresult.csv", "r") as file:
        # csv_reader = reader(file)
        totalnum_csv_reader = 0
        chosen_line_list = []
        csv_reader = DictReader(file) #OrderedDictionary
        # for quote in csv_reader:
        #     # print(quote)
        #     print(quote['text'])
        #     totalnum_csv_reader += 1
        # chosen_index = choice(range(0,totalnum_csv_reader))
        # print("***", chosen_index)
        quote_num = 0
        for quote in csv_reader:
            # if chosen_index == quote_num:
            if my_chosen_num == quote_num:
                # chosen_line_list.append(quote)
                quote = {
                    "text":quote["text"], 
                    "author":quote["author"],
                    "bio-link":quote["bio-link"]
                    }
            quote_num += 1
        print("------------chosen OrderedDict-------------------")    
        print(quote)
        print(quote["text"])
        print(quote["author"])

        print("+++++++++++++++ game start!+++++++++++++++++++")

        remaining_guesses = 4
        print("Here's a quote: ")
        print("-------- text --------")
        print(quote["text"])
        print("-------- author--------")
        print(quote["author"])
        guess = ''
        while guess.lower() != quote["author"].lower() and remaining_guesses > 0: 
            guess = input(f"Who said this quote? Guesses remaining:{remaining_guesses} ")
            if guess.lower() == quote["author"].lower():
                print("You got it , Right!")
                break
            remaining_guesses -= 1
            if remaining_guesses == 3:
                res = requests.get(f"{base_url}{quote['bio-link']}")
                soup = BeautifulSoup(res.text, "html.parser")
                # print(soup.body)
                birth_date = soup.find(class_="author-born-date").get_text()
                birth_location = soup.find(class_="author-born-location").get_text()
                print(f"Here's hint: The author was born in {birth_date} in {birth_location}")
            elif remaining_guesses == 2:
                print(f"Here's hint: The author's first name start with: {quote['author'][0]}")
            elif remaining_guesses == 1:
                last_initial = quote["author"].split(" ")[1][0]    
                print(f"Here's hint: The author's last name start with: {last_initial}")
            else:
                print(f"Sorry you ran out of guesses. The answer was {quote['author']}" )
        print("After while loop")