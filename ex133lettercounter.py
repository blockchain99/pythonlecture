'''
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 
'''
#inner function: accept letter parameter, return frequency of letter appeared.
# and it's case insenstive
def letter_counter(astring):#accept string and return function.
    astring = astring.lower()
    def letter_freq(aletter):
        return astring.count(aletter)
    return letter_freq

    
counter = letter_counter('Amazing')
print(counter('a') )# 2
print(counter('m')) # 1

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i')) # 2
print(counter2('t')) # 1 

print("-----------test-inner outer1------------")
def multiply_by(num):
  def multiply_by_num(k):
    return num * k
  return multiply_by_num
  
five = multiply_by(5)
print(five(2))	# 10
print(five(4))	# 20
 
decimal = multiply_by(10)
print(decimal(20))	# 200gi
print(decimal(3))	# 30

print("------------test2 inner outer-----")
print("--# NameError: name 'get_first_item' is not defined--")
def remove_first_item(my_array):
  def get_first_item(s):
    return s[0]
  my_array.remove(get_first_item(my_array))
  return my_array
    
print(remove_first_item(['1','2','3']))	# ['2','3']
# print(get_first_item([1,2,3,4]))# NameError: name 'get_first_item' is not defined

print("------------ decorator --------")
def capitalize(func):
  def uppercase():
    result = func()
    return result.upper()
  return uppercase
 
@capitalize
def say_hello():
  return "hello"
  
print(say_hello())	# 'HELLO'