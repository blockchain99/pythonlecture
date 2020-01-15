#truncate string to shorter string containing at most n characters 
# including (3chars)... at the end.(must be char string)

'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''
print("---------- not perfect---------")
def truncate(astring, num):
    # return astring[:num-3]+"..." if num >= 3 else "Truncation must be at least 3 characters." #not perfect
    return ((astring[:num-3]+"..." if len(astring) > num else astring) if num >= 3 else "Truncation must be at least 3 characters.") 

print(truncate("Super cool", 2)) # "Truncation must be at least 3 characters."
print(truncate("Super cool", 1)) # "Truncation must be at least 3 characters."
print(truncate("Super cool", 0)) # "Truncation must be at least 3 characters."
print(truncate("Hello World", 6)) # "Hel..."
print(truncate("Problem solving is the best!", 10)) # "Problem..."
print(truncate("Another test", 12)) # "Another t..."
print(truncate("Woah", 4)) # "W..."
print(truncate("Woah", 3)) # "..."
print(truncate("Yo",100)) # "Yo"
print(truncate("Yo",4)) # "Y..."
print(truncate("Holy guacamole!", 152)) # "Holy guacamole!"


print("-------lec-------")
def truncate1(string, n):
    if (n < 3):
        return "Truncation must be at least 3 characters."
    if (n > len(string) + 2):
        return string
 
    return string[:n - 3] + "..."

print(truncate1("Super cool", 2)) # "Truncation must be at least 3 characters."
print(truncate1("Super cool", 1)) # "Truncation must be at least 3 characters."
print(truncate1("Super cool", 0)) # "Truncation must be at least 3 characters."
print(truncate1("Hello World", 6)) # "Hel..."
print(truncate1("Problem solving is the best!", 10)) # "Problem..."
print(truncate1("Another test", 12)) # "Another t..."
print(truncate1("Woah", 4)) # "W..."
print(truncate1("Woah", 3)) # "..."
print(truncate1("Yo",100)) # "Yo"
print(truncate1("Yo",4)) # "Y..."
print(truncate1("Holy guacamole!", 152)) # "Holy guacamole!"

########## test #######
# comb2 = list(map(lambda x: f"Your instructor is {x}",filter(lambda x: len(x) < 5, names)))
# full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'