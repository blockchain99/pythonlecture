* VS code setting: prefernce : 
You can also open the Settings editor from the Command Palette 
  * (Ctrl+Shift+P) with Preferences: 
  * Open Settings or use the keyboard shortcut (Ctrl+,)-> type line number -> off
  
* control + alt +n : code run shortcut - i installed coderunner extention. 
* contrl + alt +m : for stop
* vs cod python guide: https://code.visualstudio.com/docs/languages/python
* https://medium.com/issuehunt/
* [vscod python extention](https://medium.com/issuehunt/10-visual-studio-code-extensions-for-python-development-de0be51bbeed)
* The key differences between Python 2.7.x and Python 3.x with examples
  * http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html
* I disabled thruogh extention sidebar; choose disble dropdown menu:
* Python 3 support graph for the 360 most popular Python pahttps://code.visualstudio.com/docs/languages/pythonkages! 
  * http://py3readiness.org/
*  complete python 3 bootcamp slide : 
   *  https://github.com/jmportilla/Complete-Python-Bootcamp
   *  https://drive.google.com/drive/folders/1cAM251bjoBCYF2bHfMM07MOGEgU2Q2VQ
1. I use vscode in this course: python extention installed which gave python 3.6 version to use \
   inspite of default python version is 2.7.
   * vscode >  shift + alt + below arrow to choose multiple cursor
   * such as print (...) -> multi lines : esc to back to single cursor. 
2. In python file  , check python version
 
```
import sys
print(sys.version) 
```
3. show difference between two  files:   `` code --diff app1.js app2.js ``


4.  [source slide ](http://python.slides.com/colt/oop-21#/)
    1.  http://python.slides.com/colt/oop-21#/
5. Dynamic typing means that you don't have to declare the type of a variable; a variable can hold values of any type, and the type is determined at run time when the variable is used. Most scripting languages use dynamic typing: Javascript, PHP, Python.
6. 
 ```
 decimal = 12.56345634534
integer = int(decimal)  # 12
my_list = [1, 2, 3]
my_list_as_a_string = str(my_list)  # "[1, 2, 3]"
```
7. None is python version of null
8.
```
>>> mountain="/\\/\\/\\"
>>> mountain
'/\\/\\/\\'
>>> print(mountain)
/\/\/\
```
```
>>> name ="park"
>>> name2 = 2
>>> name += name2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int

```
9. f"---{variable}---" : F-Strings (python 3.6 above)- 
```
>>> x = 10
>>> formatted = f"I've told you {x} times already !"
>>> print(formatted)
I've told you 10 times already !
```
10. .format(variable) - The tried-and-true way - python2 and 3.5
```
>>> y = 20
>>> format_method = "I've told you {} times".format(y)
>>> print(format_method)
I've told you 20 times
```
11.
```
>>> fruit = "banana"
>>> ripeness = "unripe"
>>> print(fruit + " is " + ripeness)
banana is unripe
>>> new_sentense1 = f"{fruit} is {ripeness}"
>>> print(new_sentense1)
banana is unripe
>>> new_sentense2 = "{} is {}".format(fruit, ripeness)
>>> print(new_sentense2)
banana is unripe
```
12
```
aaa = "testindex"
print(len(aaa))
import sys
print("print byte of variable :{}".format(sys.getsizeof(aaa)))

```

13
```
>>> int = "I am a number!"
>>> int
'I am a number!'
>>> int(9.4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
```
14
```
print("How many km did you cycle todoy ?")
kms = input()
miles = float(kms) / 1.60934
roundmiles = round(miles, 1)
#python3.6 above: f"-- {var} --"
print(f"OK, you said {roundmiles} miles") 
#2.7 - 3.5 : "--{}--".fommat(var)
print("OK. you said {} miles".format(roundmiles))
```

```
print("How many km did you cycle todoy ?")
kms = input()
miles = float(kms) / 1.60934
miles = round(miles, 1)
#python3.6 above: f"-- {var} --"
print(f"OK, you said {miles} miles") 
#2.7 - 3.5 : "--{}--".fommat(var)
print("OK. you said {} miles".format(miles))
```
15. slide (BOOLEAN AND CONDITIONAL LOGIC)

http://python.slides.com/colt/variables-and-data-types#/

16 naturally falsy include: empty objects, empty strings, None, and zero.

17 "is" is only truthy if the variables reference the same item in memory
```
>>> x  =1
>>> x is 1
True
>>> x is 0
False

a = [1, 2, 3]  # a list of numbers
b = [1, 2, 3]
a == b  # True
a is b  # False

c = b
b is c  # True
```
18.
```
#=============flat list from nested list===========

b_nested = [[2, 4, 6, 8], [1, 3, 5, 7, 9]]
print([element for alist in b_nested for element in alist])

print("---- [n for n in range(1,4)] for val in range(1,4)---")
board = [[num for num in range(1,4)] for val in range(1,4)]

print(board) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

print([["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)])
# [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]
```
* for multiple_elements in list_of_tuples: 
  * for a_elem, b_elem, cond in zip(A,B,condition)
```
# numpy where
A = np.array([1,2,3,4])
B = np.array([100,200,300,400])
condition = np.array([True,True, False, False])
# slow way
zip(A,B,condition)
#[(1, 100, True), (2, 200, True), (3, 300, False), (4, 400, False)]
answer1 = [a_elem if cond else b_elem for a_elem, b_elem, cond in zip(A,B,condition)]
print(answer1)
#[1, 2, 300, 400]
```

```
x = 15 
y = 0 #False
print (x or y) # 15
print (bool(x or y)) #True 
```
* multiple if : not list but ((exp1 if cond2 else exp2 ) if cond1 else exp) format. 
```
def truncate(astring, num):
  return ((astring[:num-3]+"..." if len(astring) > num else astring) if num >= 3 else "Truncation must be at least 3 characters.") 
```
* list comprehension [.x_expression.. for x in list] format. 
```
def titleize2(astring):
    return "".join([word[0].upper()+word[1:]+" " for word in astring.split(" ")])
```


1.  slide(loops)http://python.slides.com/colt/functions-part-1#/
2.  python style guide
3.  sliede lists http://python.slides.com/colt/lists-13#/
4.  slide dictionaries http://python.slides.com/colt/lists-22#/
5.  slice tuples and set http://python.slides.com/colt/lists-23#/
6.  slide function http://python.slides.com/colt/lists-16#/
7.  slide function2 http://python.slides.com/colt/generators-and-decorators#/
8.  slide lambdas http://python.slides.com/colt/generators-and-decorators#/14
9.  slide debug http://python.slides.com/colt/lists-24#/
10. slide module http://python.slides.com/colt/testing-25#/
11. $python3 -m pip install termcolor
12. (Ctrl+Shift+P) and select the Python: Select Linter command. This command adds "python.linting. linter Enabled": true to your settings, where linter is the name of the chosen linter. https://code.visualstudio.com/docs/python/linting
    1.  https://www.pylint.org/
    2.  can disable all Python linting with the Python: Enable Linting command, which shows a dropdown with the current linting state and options to turn Python linting on or off.
    3.  To perform linting:
    Linting runs automatically when you save a file.
    Open the Command Palette (Ctrl+Shift+P), 
    then enter and select Python: Run Linting.
    1.  eslint is for javascript, jsx 
13. pep8: python style guide: https://realpython.com/python-pep8/
    1.  https://pypi.org/project/autopep8/0.8/
    2.  $ pip install --upgrade autopep8 
    3.  $ autopep8 --in-place -a -a filename (works!!)
14. 
    1.   DNS Lookup
    2.  computer makes a REQUEST to a server
    3.  Server pricess the REQUEST
    4.  Srever issues a RESPONSE
        1. 2 3 4 is cycle:
        2. 2xx: success, 3xx: rerouting, 4xx: your error, 5xx: server error. 
15.  GET vs. POST
     1.   GET
          1. useful for retrieving data
          2. data processed in query string
          3. shd have no side-effects
     2.   POST
          1.   useful for writing data
          2.   data processed in request body
          3.   can have side-effect
16.  $ python3 -m pip install requests
17.  Query String
     1.   http://www.example.com/?key1=value1&key2=value2
     2.   in goole, marten in searchbox. 
18.  slide oop: http://python.slides.com/colt/lists-18#/
19.  Encapsulation is the process of designing a programmatic 
     class using public and private methods and attributes 
     to implement abstraction
20. abstraction in OOP: The ides of exposing only"revant" data in a class interface, hiding private attributes and methods("inner workings") from users
21. Waht __init__ , self do ? 
    1.  This method __init__is called when an object is created from a class and it allows the class to initialize the attributes of the class.
    2. while creating the car object we passed arguments  "James",160, 120, 2000 these arguments will pass to "__init__" method  to initialize the object. 
    3. self represents the instance of class. It binds the attributes with the given arguments.
    4. "self" represents the object inside the class. "self" works just like "r" in the statement  "r = Rectangle(160, 120, 2000)".  
    5. Inside "def get_area(self): ", we have used "self" as a parameter in the method because whenever we call the method, the object (instance of class) automatically passes as a first argument along with other argumets of the method.
       1. If no other arguments are provided only "self" is passed to the method. That's the reason we use "self" to call the method inside the class("self.get_area()").  
       2. we use object( instance of class) to call the method outside of the class definition("r.get_area()"). "r" is the instance of the class, when we call method "r.get_area()".
       3. "r" is the instance of the class, when we call method "r.get_area()"  the instance "r" is passed as as first argument in the place of self.
```
class Rectangle:
   def __init__(self, name, length, breadth, unit_cost=0):
       self.name = name
       self.length = length
       self.breadth = breadth
       self.unit_cost = unit_cost
   def get_area(self):
       return self.length * self.breadth
   def calculate_cost(self):
       area = self.get_area()
       return area * self.unit_cost

r = Rectangle("James",160, 120, 2000)
print("Hey %s, Area of Rectangle: %s sq units" % (r.name, r.get_area()))
```
* Decorator boliterplate
```
from functools import wraps
 
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper

@double_return 
def add(x, y):
    return x + y
    
add(1, 2) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]    
```

40. iterator, generator slide http://python.slides.com/colt/lists-14#/
41. code generator : http://www.telosys.org/
42. testing slide http://python.slides.com/colt/oop#/
43. file i/o slide http://python.slides.com/colt/modules#/
    1.  open : return file object to you 
    2.  then read object with read() method  

```
file = open("story.txt")
file.read()
```             
44. To remove only spaces use str.replace:

* ``sentence = sentence.replace(' ', '')``


    To remove all whitespace characters (space, tab, newline, and so on) you can use split then join:

* ``sentence = ''.join(sentence.split()) ``     

45.  $ python3 -m pip install jsonpickle
46.  slide beautiful soup: webscraping http://python.slides.com/colt/testing#/2
47.  python3 -m pip install bs4
48.  python3 -m pip install scrapy
50.  spiders are classes which define how a certain site willbe scraped, including how to crawling and parsing pages for site. ->srapy.spider
51.  
```
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
  <div data-example="yes">bye</div>
</body>
</html>
"""
```
* Parsing and Navigating HTML

BeautifulSoup(html_string, "html.parser") - parse HTML
Once parsed, There are several ways to navigate:
* select() accepts CSS selectors, find() does not
  * css selector: element( p {color: red}) -> p), .class, #id, [attribute]
* select finds multiple instances and returns a list, find finds the first, so they don't do the same thing. select_one would be the equivalent to find.
* I almost always use select(css selectors) when chaining tags or using tag.classname, if looking for a single element without a class I use find. 
* By Tag Name
* Using find - returns one matching tag
* Using find_all - returns a list of matching tags

```
soup = BeautifulSoup(html_string, "html.parser") # parse HTML
soup.find(id="first")
soup.select("#first)[0]   #id="first -> first element
soup.find_all(class_="special")
soup.select(".special") #class name
for el in soup.select(".special"):
  print(el.name)
  print(el.attrs)
soup.select("div") #tag
soup.find_all(attrs={"data-example" : "yes"})
soup.select([#data-example]) #atribute -> two items
soup.find("h3").attrs["data-example"]
soup.find("h3")["data-example"] #yes
soup.find("div")["data-example"] #yes
soup.find("div")["id"] #first
```

* Accessing data in elements
  * get_text - access the inner text in an element
  * name - tag name
  * attrs - dictionary of attributes
  * also access atttribute values using bracket: []

get_text example
```
quotes = soup.find_all(class_="quote") #list

for quote in quotes:
        all_quotes.append({
            "text" : quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio-link": quote.find("a")["href"] 
        })
```
```
next_btn = soup.find(class_="next")
url = next_btn.find("a")["href"] if next_btn else None
```
1.  https://www.rithmschool.com/blog
2.  
* Navigating with Beautiful Soup
  * Via Tags : 
    * parent / parents
    * contents
    * next_sibling / next_siblings
    * previous_sibling / previous_siblings
  * Via Searching : 
    * find_parent / find_parents
    * find_next_sibling / find_next_siblings
    * find_previous_sibling / find_previous_siblings
```
soup = BeautifulSoup(html_string, "html.parser") # parse HTML
data = soup.body.contents
print(data)
data = soup.find(class_="super-special").parent
print(data) # <ol> ..</ol>

data = soup.find(id="first").find_next_sibling() #<ol>..</ol>
data = soup.find(id="first").find_next_sibling() #<ol>..</ol>
data = soup.find(id="first").find_next_sibling().find_next_sibling() #<div data-example..>
quote.find("a")["href"]
```
* soup.find_all(class_="quote")
```
import request
from bs4 imort BeautifulSoup

all_quotes = []
res = requests.get("http://quotes.toscrape.com")
quotes = soup.find_all(class_="quote")

for quote in quotes:
  all_quotes.append({
    "text" : quote.find(class_="text").get_text(),
    "author": quote.find(class_="author").get_text(),
    "bio-link": quote.find("a")["href"] #.find("a") => anchor tag 
  })

```

1.   slide regex : http://python.slides.com/colt/regex#/
2.   regex cheat sheet: http://www.rexegg.com/regex-quickstart.html
3.   regex editor : https://pythex.org/

* \d	digit 0-9
* \w	letter, digit, or underscore
* \s	whitespace character
* \D	not a digit
* \W	not a word character
* \S	not a whitespace character
* .	any character except line break
* ----------------------
* Example : "The rain in Spain"
* \A	Returns a match if the specified characters are at the beginning of the string : ("\AThe") -> ['The']
* \b	Returns a match where the specified characters are at the beginning or at the end of a word : re.findall(r"\bain")-> [], (r"ain\b") -> ['ain', 'ain'] : r -> no need ``\\`` for \b 
* \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word : re.findall(r"\Bain")-> ['ain', 'ain'], (r"ain\B"_ -> []
* ----------------------
* ?	Zero(None) or Once (optional) : name, names
* \*	Zero or more times (*)
*  \+	One or more (+)
* {3}	Exactly x times.  {3} - 3 times
* {3,5}	Three to five times
* {4,}	Four or more times
* ---------------------
* ^	Start of string or line
* $	End of string or line
* \b	Word boundary
  * ---------------------
* \d{3} \d{3}-?\d{4} <- 334 245-3657 : '-' is optional
* ^\d{3} \d{3}-?\d{4}  <- start with digit, ex)  asdd334 249-3657 is wrong representation.
* ^\d{3} \d{3}-?\d{4}$ <- $ end 
* "hello world I am typing" -> Just want word instead of white space before word and after word. -> \b  : word boundary -> \b\w+\b : hello, world, I, am, typing
  * Bob.*\bcat\b -> Bob ate the cat
* ``re.compile(r'\b\d{3} \d{3}-\d{4}\b)``  -> ``("my number is 423 564-5623")-> match: ("my number is 423 564-5623343") -> not match(5623 is 4digit boundary by \b)``
* ---------[] just return one char(digit)--------------
* [^arn]	Returns a match for any character EXCEPT a, r, and n
  * but ^ not inside of [] - start of string or start of line
  * ex)  ^abc.* -> abc (line start) <-> $: end of string, line
* [a-n]	Returns a match for any lower case character, alphabetically between a and n
* [arn]	Returns a match where one of the specified characters (a, r, or n) are present
* [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
* [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
* ----------------------
* | logical or ex) Need to accept two forms of phone number: (124) 234 3265, 124 234 3265 ->
``(\(\d{3}\)|\d{3}) \d{3} \d{4}  ``
* ex) Mr. James Earn , Mrs. Maria Kim -> ``(Mr|Mrs\.) ([a-zA-Z]+) ([a-zA-Z]+) # 3 different components``
* ex) https://pythex.org, http://teraedu.com -> ``https?://([A-Za-z_-]+\.[A-Za-z_-]+)``
* Regex : ``Mr.|Mister Holmes``
  1. "Mr. Davis"
  2. "Mister Holmes"
  3. "Mr."
* Regex :  numbers 1 - 25 :  0-5, 10-15, 20-25 OR 0-9
  
```
 \b(0?[1-9]|1[0-9]|2[0-5])\b #good (no 00)
([01]?[0-9]|2[0-5]) # not good (00 exits)

// should omit those pesky one-offs you're seeing as mentioned in the comments.
^([01]?[0-9]|2[0-5])$
\b([01]?[0-9]|2[0-5])\b

// if you also want to exclude 0...
^([1-9]|1[0-9]|2[0-5])$
\b([1-9]|1[0-9]|2[0-5])\b
```

* Regex : | (or)
``` 
import re
def parse_name(input):
  name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<second>[A-Za-z]+) (?P<third>[A-Za-z]+)$')
  matches = name_regex.search(input) 
  # matches = name_regex.findall(input) 
  print(matches.groups())
  #print(matches.group())
  #print(matches.group(0))
  #print(matches.group(second))

parse_name("Mdme. Shown Bobari")
```  
  1. At the beginning , verify nothing else in the string -> ^ $
  2. ``?P<second>`` : group name 'second' -> label for the group ->  ``print(matches.group(second))`` same as ``print(matches.group(1)``)
1.   w3school useful regex example :  https://www.w3schools.com/python/python_regex.asp
    
2.  import re, re.finadll() -> all return, re.search() -> return first matched

```
import re
pattern = re.compile(r'\d{3} \d{3}-\d{4}')
res = pattern.search("call me at 310 456-6532")
print(res)
print(res.group())
##########################
res2 = pattern.search("call me at 310 456-6532 or 321-635-9654")
print(res2)
print(res2.group())
###########################
res3 = pattern.findall("call me at 310 456-6532 or 321-635-9654")
print(res3)
print(res3.group())
re.search(r'\d{3} \d{3}-\d{4}',"call me at 310 456-6532" ).group()
```
* ?P<label_name> 
  ``` 
  name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
	matches = name_regex.search(input) res = name_regex.search("Mr. Niel Brown")
  matches.group('first')
  ```
53. [SQLite keyword] https://www.sqlite.org/lang.html
```
$ sqlite3 ex1
SQLite version 3.28.0 2019-03-02 15:25:24
Enter ".help" for usage hints.
sqlite> create table tbl1(one varchar(10), two smallint);
sqlite> insert into tbl1 values('hello!',10);
sqlite> insert into tbl1 values('goodbye', 20);
sqlite> select * from tbl1;
hello!|10
goodbye|20
sqlite>
```
* a semicolon at the end of each SQL command!
```
sqlite> CREATE TABLE tbl2 (
   ...>   f1 varchar(30) primary key,
   ...>   f2 text,
   ...>   f3 real
   ...> );
sqlite>
```
54.  sqlite command line shell ; https://sqlite.org/cli.html
* SQLite will use a temporary database that is deleted when the session exits. To use a persistent disk file as the database, enter the ".open" command immediately after the terminal window starts up:
  *  database file named "ex1.db" to be opened and used. The "ex1.db" file is created if it does not previously exist. 
```
SQLite version 3.28.0 2019-03-02 15:25:24
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .open ex1.db
sqlite>
```
* Alternatively, you can create a new database using the default temporary storage, then save that database into a disk file using the ".save" command:
  * Caution:".save" command as it will overwrite any preexisting database files having the same name without prompting for confirmation. As with the ".open" command, you might want to use a full pathname with forward-slash directory separators to avoid ambiguity.
```
SQLite version 3.28.0 2019-03-02 15:25:24
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> ... many SQL commands omitted ...
sqlite> .save ex1.db
sqlite
```
55. pandas html reader
    1.  need Beautifulsoup, html5lib, lxml
        1.  $ python3 -m pip install html5lib
        2.  $ python3 -m pip install lxml
        3.  $  python3 -m pip install bs4 #already installed
            1.  from bs4 import BeautifulSoup 
56. toggle between command and markdown in jupyter notebook(Enter to markdown, Esc to command)
57. To work with Jupyter notebooks, you must activate an Anaconda environment in VS Code, or another Python environment in which you've installed the Jupyter package. To select an environment, use the Python: Select Interpreter command from the Command Palette (Ctrl+Shift+P). - $ python3 -m pip install jupyter notebook : in pythonlec dir: -> I changed ~/.bashrc path to anaconda3 , so default python --version is python3.7 and install pandas,, sklite etc.. (jupyter notebook ins already installed)
  : so I run jupyter notebook + vscode no in conda virtual env but default installed env. !!!!
    1.  https://code.visualstudio.com/docs/python/jupyter-support
    2.  Once the appropriate environment is activated, you can create and open a Jupyter Notebook, connect to a remote Jupyter server for running code cells, and export a Jupyter Notebook as a Python files.
    3.   create a Jupyter Notebook by running the Python: Create Blank New Jupyter Notebook command from the Command Palette (Ctrl+Shift+P) or by creating a new .ipynb file in your workspace. 

Note: By default, the Visual Studio Code Python extension will open a Jupyter Notebook (.ipynb) in the Notebook Editor. If you want to disable this behavior you can turn it off in settings. (Python > Data Science: Use Notebook Editor).


1.  vscode for python : jupyter 400 not connect error -> I changed to activate anaconda3(python3 ver) instead of anaconda2(python2.7 ver) through ~/.bashrc path change to anaconda3 , then $source ~/.bashrc , check $ python --version -> shows python 3.7..
    1.  $conda create -n mypython3 python=3 (or, $conda create -n python=2.7 anaconda)
    2.  $conda activate mypython3
    3.  $(mypython3) conda install anaconda (to install jupyter notebook, numpy matplot...)
    4.  $(mypython3) conda install (whatever you want)
    5.  For activating : $ conda activate mypython3
    6.  $ (mypython3) conda deactivate
    7.  $ conda info -e : list of all your environment
    8.  $ conda remove --name myenv --all (or conda remove -n mypython3 --all)
* python2 conda env
  1.  $conda create -n mypy2 python=2.7 anaconda
    * Press y to proceed. This will install the Python version and all the associated anaconda packaged libraries at “path_to_your_anaconda_location/anaconda/envs/yourenvname”
  2. $conda create -n mypy2 python=2.7
    * $source activate mypy2
    * $conda install anaconda ...
   
* remove conda env: $ $ conda env remove -n py2

************************************
* I install anaconda3 and it automatically run source ~/.bashrc -> (base): python3.7 conda env & default terminal -> (base) env ..!
  *  conda deactivate -> 
* 1 conda create -n Python27 python=2.7 ( no need to install anaconda2, just anaconda3 install & use this command for python2.7 env)
* 2 jupyter notebook kernel select by following setup.
```
#If you have Python 3 in your conda env, you can set up a Python 2 kernel like this;
python2 -m pip install ipykernel
python2 -m ipykernel install --user

#If you have Python 2 in conda env,
python3 -m pip install ipykernel
python3 -m ipykernel install --user
```

* ex) (your_conda_env_is_3.7) conda_env, which is python3.7 I excute 
```
$ python --version #check first version
$ python2 -m pip install ipykernel  #Once I installed in (base)env
# $ python2 -m uninstall ipykernel (excuted to uninstalle in base env)
# It works (sc27) conda env -> python 2.7 works with original Ucacity ipynb 
$ python2 -m ipykernel install --user 
```
3. I remove anaconda3 and reinstall w/o default (base) env 
* in (base) env, which is python3.7 I excute  -> $ python --version: shows 3.7..
```
$ sudo apt-get install python3-pip
$ sudo apt-get install python-pip

$ python2 -m pip install ipykernel  
$ python2 -m ipykernel install --user 

$conda install -c anaconda spyder #no need to excute!
$ anaconda-navigator
$jupyter lab
```
4. in py2 conda env : jupyter notebook python3 kernel used for
udacity ML iptython code. (we work in this env setting)
  * Or in py3 just use python3 kernel 

*******************************************

*********** Use this one! -Working !! ********************
* ~/.bashrc -> anaconda2 -> python --version (2.7)
* pygame install in (base) env.

1. `` $(base) ~/anaconda2/bin$ python -m pip install pygame --user``
2. test in python ide: -> O.K !!
  * $(base) python
  * >> import pygame # 
  * >> print (pyghame.ver) #
3. $ /ucacityML/smartc_mytest/python smartcat/agent.py
-> It works!!
**********************************

************************************

1.  Vscode work with Jupyter-like code cells https://code.visualstudio.com/docs/python/jupyter-support-py
2.  [vs code datascince]  https://devblogs.microsoft.com/python/data-science-with-python-in-visual-studio-code/
    1.  Exploring data and experimenting with ideas in Visual Studio Code
        1. Like jupyter Notebook, you can define code cells in your Python code by using “#%%” and Markdown cells by using “#%% [markdown]”.
        2. “Run cell” links start to light up once “#%%” are detected. The first time the “Run cell” link is clicked (or Shift-enter are pressed), the “Python Interactive” window on the right will show up and a Jupyter server will start in the background. Code in the cells will then be sent to the Jupyter server to execute and results will be rendered in the window.
        3. By using the top toolbar in the Python Interactive window, you can clear results, restart the iPython kernel, and export results to a Jupyter Notebook.
        4. You can navigate back to the source code by clicking on the “Go To Code” button in each cell.
    2. Import Jupyter Notebooks into Python code

       1.   (ctrl + shift + P)command “Python: Import Jupyter Notebook”: this will extract Python code as well as Markdown blocks from the notebook, and put everything into a Python file.
* Excel csv viewer Extention: For files with a .csv, .tsv, or .tab extension, use the explorer context menu or editor title menu to invoke the Open Preview command. The contents of the file will be displayed in a FlexGrid control, which supports sorting and filtering via its column headers.


*  gedit ~/.bashrc -> change between python --version -> 2.7, 3.7
  * change below : anaconda2  or anaconda3 
```
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/snupos/anaconda2/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/snupos/anaconda2/etc/profile.d/conda.sh" ]; then
        . "/home/snupos/anaconda2/etc/profile.d/conda.sh"
    else
        export PATH="/home/snupos/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

*******************************
* pandas:
1. index column access
  * df1.loc[['Segment 0'],:]
  * df1.loc[['Segment 0', 'Segment 1'],['Fresh', 'Milk']]
2. 
  * samples = pd.DataFrame(data.loc[indices], columns = data.keys()).reset_index(drop = True)
  * samples2=samples.rename(index={0:"sample 0" ,1:"sample 1", 2:"sample 2"})

******** docker tensorflow install *********
[install site](https://medium.com/@madmenhitbooker/install-tensorflow-docker-on-ubuntu-18-04-with-gpu-support-ed58046a2a56)

* Here is a command to play with TensorFlow 2 : 
`` $ docker run --rm --runtime=nvidia -v -it -p 8888:8888 tensorflow/tensorflow:2.0.0a0-gpu-py3-jupyter ``
* belows can save in the directory designated!
``$ docker run -it -p 8888:8888 -v /media/snupos/hdd2/udacityML/street-address-image-recognition-master:/tf/tensorflow-tutorials --rm --runtime=nvidia tensorflow/tensorflow:2.0.0a0-gpu-py3-jupyter``
  * open the URL in your host web browser: `` http://127.0.0.1:8888/?token=...``
  * But add packages ex.pandas to existing container is challenging! 
* docker premission denied : solution -> Not working!
* 0.0.0.0:8888 port using error !->
```
This '$ fuser 8888/tcp' will print you PID of process bound on that port.

And this '$ fuser -k 8888/tcp' will kill that process.
or 
'$ fuser -k -n tcp 8888'
```
```
#current user : $whoami -> 'ys'
$ sudo setfacl -m user:your_user_name:rw /var/run/docker.sock
```
############# python 2, 3 ###########
1.  No need to go though all these loops in the other answers. Just install the 'python3' package. Ubuntu employs an additional naming convention for related packages: 'python-matplotlib' is the python2 version, 'python3-matplotlib' is python3.

* To use a python3 shell, just use the 'python3' command. For python3 scripts, use the shebang line "#! /usr/bin/env python3".

  * ##activate python 3  in python file, add follows in the begining. : 
``#! /usr/bin/env python3 ``
  * ##activate python 2  in python file, add follows in the begining. : 
``#! /usr/bin/env python2 ``

2.  you get a self-contained environment where you can load and run totally separate environments.

How it works (on Ubuntu):

  1. install virtualenv

``$ apt-get install python-virtualenv``

or maybe (depending on your version of Ubuntu)

``$ apt-get install python3-virtualenv``


  2. Create a virtual environment for a project: virtualenv venv will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages
  
  ``` 
  # This creates a copy of Python in whichever directory you ran the command in, placing it in a folder named venv.

  $ cd project_folder
  $ virtualenv venv
  ``` 
  You can also use the Python interpreter of your choice (like python2.7).
```
$ virtualenv -p /usr/bin/python2.7 venv

#or 
$ virtualenv -p python2 ve
$ virtualenv -p python3 ve3 
# Then, you can run ve/bin/python for python2, or ve3/bin/python for python3.
```
or change the interpreter globally with an env variable in ~/.bashrc: 
```
$ export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7
```

To begin using the virtual environment, it needs to be activated:
```
$ source venv/bin/activate
```
* The name of the current virtual environment will now appear on the left of the prompt (e.g. (venv)Your-Computer:project_folder UserName$) to let you know that it’s active. From now on, any package that you install using pip will be placed in the venv folder, isolated from the global Python installation.

*****************************************
* (using 1.0 in ) tensorflow 2.0 : 
1. 1.0 works in 2.0 env
```
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
```
2. Automatic conversion script:
3. Top-level behavioral changes
If your code works in TensorFlow 2.0 using tf.compat.v1.disable_v2_behavior(), there are still global behavioral changes you may need to address. The major changes are:

Eager execution, v1.enable_eager_execution() : Any code that implicitly uses a tf.Graph will fail. Be sure to wrap this code in a with tf.Graph().as_default() context.

Resource variables, v1.enable_resource_variables(): Some code may depends on non-deterministic behaviors enabled by TF reference variables. Resource variables are locked while being written to, and so provide more intuitive consistency guarantees.

This may change behavior in edge cases.
This may create extra copies and can have higher memory usage.
This can be disabled by passing use_resource=False to the tf.Variable constructor.
Tensor shapes, v1.enable_v2_tensorshape(): TF 2.0 simplifies the behavior of tensor shapes. Instead of t.shape[0].value you can say t.shape[0]. These changes should be small, and it makes sense to fix them right away. See TensorShape for examples.

Control flow, v1.enable_control_flow_v2(): The TF 2.0 control flow implementation has been simplified, and so produces different graph representations. Please file bugs for any issues.

4. [make code 2.0-native](https://www.tensorflow.org/guide/migrate)
5. [effective tf2 coding guide](https://www.tensorflow.org/guide/effective_tf2)
6. convert with upgrade script(tf_upgrade_ve)
``` 
!tf_upgrade_v2 \
  --infile models/samples/cookbook/regression/custom_regression.py \
  --outfile /tmp/custom_regression_v2.py
```
*****
Use following conda env to develop and test tensorflow!
*****
* conda navigator : `` $ anaconda-navigator ``
  * in(base) env -> environment : create new env-> shows python
  version from 3.7 to 2.7 (need $ conda config --set changps1 True, if False show python 3.7 only)
  [tensorflow with anaconda-navigator](https://www.freecodecamp.org/news/install-tensorflow-and-keras-using-anaconda-navigator-without-command-line/)
  
* conda base_prompt remove :
``ys:~$ conda config --set changeps1 False``
***

*****
jupyter: esc + m: markdonw, esc + y:code
*****

* ubuntu automatic login: ``$ sudo nano /etc/gdm3/custom.conf``
  * uncomment below tow lines -> automatic login
  * comment -> type login password to login 
 
 ```
# Enabling automatic login
AutomaticLoginEnable = true
AutomaticLogin = ys
  ```

* change color in markdown (md)
```
<span style="color: red">passing a list of layer instances</span>
```
