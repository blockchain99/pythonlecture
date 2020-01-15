import requests
from bs4 import BeautifulSoup
from csv import writer, DictWriter

response = requests.get("https://www.rithmschool.com/blog")
# print(response.text)
with open('test331out.text', 'w') as file:
    file.write(response.text)

print("==============================================================")
#go to above url -> open developer tool in chrome. 
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
# print(articles)

print("-------------------csv DicWriter---------------------")
with open("test331blogDict.csv", "w") as file:
    headers = ["title", "link", "date"]
    csv_dictwriter = DictWriter(file, fieldnames=headers)
    csv_dictwriter.writeheader()

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
        csv_dictwriter.writerow({
            "title" : title, 
            "link" : url, 
            "date" : date
            }) 


