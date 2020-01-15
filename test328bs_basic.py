# install: $ python3 -m pip install bs4

from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example= 
  "yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
d = soup.select("[data-example]") #[..] -> attribute
print(d)

for el in soup.select(".special"):
    # print(el)
    # print(el.name)
    # print(el.get_text())
    print(el.attrs)
    # print(el.attrs['class'])
attr = soup.find("h3")["data-example"]
print(attr)
attr = soup.find("div")["id"]
# attr = soup.find("div").attrs
print(attr)
print("-----------")
data = soup.body.contents
print(data)
print("============")
data = soup.body.contents[1]
print(data)
print("======---======")
data = soup.body.contents[1].contents
print(data)