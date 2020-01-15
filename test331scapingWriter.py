import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
# print(response.text)
with open('test331out.text', 'w') as file:
    file.write(response.text)

print("==============================================================")
#go to above url -> open developer tool in chrome. 
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
# print(articles)

print("-------------------csv writer---------------------")
with open("test331blog.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["title", "link", "date"])

    for article in articles:
        #get_text: access the inner text in an element("a")
        # print(article.find("a").get_text()) #anchor tag -> convert to text
        a_tag = article.find("a")
        title = a_tag.get_text() #anchor tag -> convert to text
        url = a_tag['href']
        # print(article.find("time")) #<time datetime="2019-10-22" pubdate=""></time>
        time = article.find("time")
        date = time['datetime']
        # print(date) #2019-09-03
        # print(title, url, date)

        # csv_writer.writerow(title, url, date) #TypeError: writerow() takes exactly one argument (3 given)
        csv_writer.writerow([title, url, date]) 



print("------------p-------------")
for article in articles:
    print(article.find("p").get_text()) #p tag -> convert to text
    print("----------*--------")

 