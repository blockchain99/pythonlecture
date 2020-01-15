'''
valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''

print("-----------all T/F for each elements----wrong logic-----")
def valid_parentheses(str_paraentheses): #check order of it is correct
    #wrong logic
    result =  [True if str_paraentheses[i] == '(' and str_paraentheses[-i] ==')' or str_paraentheses[i] == '(' and str_paraentheses[-i] ==')'else False for (i, val) in enumerate(str_paraentheses)]
    if False in result:
        return False
    return True

print(valid_parentheses("()") )# True 
print(valid_parentheses(")(()))")) # False 
print(valid_parentheses("(") )# False 
print(valid_parentheses("(())((()())())")) # True 
print(valid_parentheses('))((') )# False
print(valid_parentheses('())(')) # False
print(valid_parentheses('()()()()())()(')) # False

print("---------all T/F for each elements2---wrong!------")
def valid_parentheses2(str_paraentheses): #check order of it is correct
    # return [False if any(str_paraentheses[i] != str_paraentheses[-i]) else True for i in range(0, len(str_paraentheses))] #TypeError, boo obj not ietrable
    return [False if str_paraentheses[i] != str_paraentheses[-i] else True for i in range(0, len(str_paraentheses))] #TypeError, boo obj not ietrable


print(valid_parentheses2("()") )# True 
print(valid_parentheses2(")(()))")) # False 
print(valid_parentheses2("(") )# False 
print(valid_parentheses2("(())((()())())")) # True 
print(valid_parentheses2('))((') )# False
print(valid_parentheses2('())(')) # False
print(valid_parentheses2('()()()()())()(')) # False

print("---1. first: '('  2. end: ')'  3. same number of '(' and ')' -correct! ------")
def valid_parentheses3(str_paraentheses): #check order of it is correct
    return True if ( str_paraentheses[0]=='(' and str_paraentheses[-1] ==')' and str_paraentheses.count('(') == str_paraentheses.count(')') ) else False #TypeError, boo obj not ietrable


print(valid_parentheses3("()") )# True 
print(valid_parentheses3(")(()))")) # False 
print(valid_parentheses3("(") )# False 
print(valid_parentheses3("(())((()())())")) # True 
print(valid_parentheses3('))((') )# False
print(valid_parentheses3('())(')) # False
print(valid_parentheses3('()()()()())()(')) # False

print("------test------")
test = '(())((()())())'
print([(i,val) for (i, val) in enumerate(test)])