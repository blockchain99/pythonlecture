names=["James", "Michel"]
print(names)
names[1], names[0] = "Michel", "James" #no swapping

print(names)
names[1], names[0] = names[0], names[1]
print(names)