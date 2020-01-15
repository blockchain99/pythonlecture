dict1 = {num : num *2 for num in [1,2,3,4,5]}
print(dict1)

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)

print("=========== make dictionary out of lists=========")
testlist1 =["name", "weight", "height"]
testlist2 =["James", 200, 5.7]
dicfmlist ={testlist1[i] : testlist2[i] for i in range(0, len(testlist1))}
print(dicfmlist)

print("----------")
num_list= range(1,5)
oddeven = {x: "even" if x %2 ==0 else "odd" for x in num_list}
oddeven = {x: ("even" if x %2 ==0 else "odd") for x in num_list}
print(oddeven)

instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

print("############make capital for name############")
new_inst = { str(k).upper() if k is 'name' else str(k)+'!' : v for k,v in instructor.items()}
new_inst = { (str(k).upper() if k is 'name' else str(k)+'!') : v for k,v in instructor.items()}
print(new_inst)

print("---------convert two list to one dictionary--------***")
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer1 = list(zip(list1,list2))
print(answer1)
answer2 = dict(zip(list1,list2))
print(answer2)

answer = {list1[i]: list2[i] for i in range(0,3)}
print("=========zip unzip===========")
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 
  
# using zip() to map values 
mapped = zip(name, roll_no, marks) 
  
# converting values to print as list 
mapped = list(mapped) 
  
# printing resultant values  
print ("The zipped result is : ",end="") 
print (mapped) 

#unzipping values 
namz, roll_noz, marksz = zip(*mapped) 
  
print ("The unzipped result: \n",end="") 
# printing initial lists 
print ("The name list is : ",end="") 
print (namz) 
  
print ("The roll_no list is : ",end="") 
print (roll_noz) 
  
print ("The marks list is : ",end="") 
print (marksz)

print("=====list to dic ============")
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {e[0]:e[1] for e in person}
print(answer)
#using a dict comprehension, 
# without any references to list indexes:
answer = {k:v for k,v in person}
# If you have a list of pairs, you can very easily 
# turn it into a dictionary using dict() 
answer = dict(person)
print(answer)

print("--------------------")
answer = dict.fromkeys("aeiou", 0)
answer = {}.fromkeys(['a','e','i','o','u'], 0)
print(answer)
answer = {char:0 for char in 'aeiou'} 
 
 # make sure your solution is assigned to the answer variable so the tests can work!
print(range(65,91)) #this make object
# ex. for e in range(65, 91): , in this case range(65, 91) is object not list
numlist = list(range(65, 91)) #convert to list
print(numlist)
charlist =list(range(65, 91))
# answer = {numlist[i]: chr(charlist[i]) for i in numlist} #error! 
answer = {numlist[i]: chr(charlist[i]) for i in range(0, len(numlist))}
print(answer)
answer = {count: chr(count) for count in range(65,91)}
