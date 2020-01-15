num_for=[]
for number in range(1, 8): #range(startnumber, last_number): last_number not incl
    num_for.append(number)
print(num_for)

print("##########while version ####")
num = 1
while num < 8:
    print(num)
    num += 1

print("#####range(7)####")
for number in range(7): #0 ~ 6 : 7 elements
    print(number)
print("-----------")
for nu in range(1, 10, 2):
    print(nu)

print("##########while ver")
num = 1
while num < 11:
    print(num)
    num += 2
print("---+++++++++++++++++++-")
for nu in range(7, 0, -1): #last not incl(0)
    print(nu)

