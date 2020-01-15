################## csv file is not correct with redundant , " ===
from bs4 import BeautifulSoup
import requests
from csv import DictWriter, writer
url="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content with python built-in lxml parser
soup = BeautifulSoup(html_content, "lxml")
# print(soup.prettify()) # print the parsed data of html

print("-----title------")
print(soup.title)
print(soup.title.text)
print(".find: ",soup.find("title"))
print(".select_one: ",soup.select_one("title"))
print(".select: ",soup.select("title"))

# print("-------find_all('a')---test-----")
# for link in soup.find_all("a"):
    # print("Inner Text: {}".format(link.text))
    # print("Title: {}".format(link.get("title")))
    # print("href: {}".format(link.get("href")))

print("####### get a heading of table fm 'tr' ########")
gdp_table = soup.find("table", attrs={"class": "wikitable"})
gdp_table_data = gdp_table.tbody.find_all("tr")  # contains 2 rows

# Get all the headings of Lists
headings = []
for td in gdp_table_data[0].find_all("td"):
    # remove any newlines and extra spaces from left and right
    headings.append(td.b.text.replace('\n', ' ').strip())
    # headings.append(td.b.get_text())

print(headings)

print("-------tr 2nd------------")
# Moving on to the second tr tag of the outer table, 
# let's get the content of all the three tables by 
# iterating over each table and its rows. 

#second 'tr' -> 'table' -> 'th', second 'tr' -> 'table' -> 'tbody' -> 'tr'
for table, heading in zip(gdp_table_data[1].find_all("table"), headings):
    # Get headers of table i.e., Rank, Country, GDP.
    with open(f"test331_{heading}.csv", "w") as file:
        t_headers = []
        for th in table.find_all("th"):
            # remove any newlines and extra spaces from left and right
            t_headers.append(th.text.replace('\n', ' ').strip())
            # t_headers.append(th.text)
        headers = t_headers
        csv_dictwriter = DictWriter(file, fieldnames=headers) 
        csv_dictwriter.writeheader()

        # Get all the rows of table
        table_data = [] 
        bad_chars = ['\n', '\"','"',',,',',',"'"]
        for tr in table.tbody.find_all("tr"): # find all tr's from table's tbody
          
            # Each table row is stored in the form of
            # {'Rank': '', 'Country/Territory': '', 'GDP(US$million)': ''}

            # find all td's(3) in tr with t_header
            for td, th in zip(tr.find_all("td"), t_headers): 
                for i in bad_chars:
                    td.text.replace(i, '').strip()
                csv_dictwriter.writerow({
                    th : td.text
                })


