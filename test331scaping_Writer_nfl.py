##not completed !
import requests
from bs4 import BeautifulSoup
from csv import writer, DictWriter

response = requests.get("http://en.wikipedia.org/wiki/NFL_win-loss_records")
# print(response.text)
with open('test331Write1nfl.text', 'w') as file:
    file.write(response.text)

# print("==============================================================")
# #go to above url -> open developer tool in chrome. 
soup = BeautifulSoup(response.text, "html.parser")
# # articles = soup.find_all("tbody")
# # articles = soup.select(".wikitable.sortable.jquery-tablesorter")
# articles = soup.select(".wikitable")
# # articles = soup.find_all(class_="wikitable")
# print(articles)

# print("-------------------csv Writer---------------------")
# with open("test331nflWriter.csv", "w") as file:
   
#     csv_writer = writer(file)
#     csv_writer.writerow(["Rank", "Team", "Won","Lost","Tied","Pct.","First NFL Season", "Total Games", "Divison"])
#     td_tags = articles.find("td")
#     for td_tag in td_tags:
#         #get_text: access the inner text in an element("a")
#         # print(article.find("a").get_text()) #anchor tag -> convert to text
       
       
#         rank  = td_tag[0].get_text()
#         team  = td_tag[1].find("a").get_text()
#         won  = td_tag[2].get_text()
#         lost  = td_tag[3].get_text()
#         tied  = td_tag[4].get_text()
#         pct  = td_tag[5].get_text()
#         first  = td_tag[6].get_text()
#         total  = td_tag[7].find("a").get_text()
#         division  = td_tag[8].find("a").get_text()

# #         csv_writer.writerow([rank, team, won, lost, tied, pct, first, total, division])
        

############ one table scap ##############     
# from bs4 import BeautifulSoup
# import csv
# html = open("table.html").read()
# soup = BeautifulSoup(html)
table = soup.find("table")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('output.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)


