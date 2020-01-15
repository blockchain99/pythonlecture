sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ''
### TypeError: unsupported operand type(s) for +=: 'NoneType' and 'str'
# result = None # If the variable is none or empty, then it's equivalent to False.

for elem in sounds:
    result += elem.upper()
print(result)

print(type(None))
print(type(''))