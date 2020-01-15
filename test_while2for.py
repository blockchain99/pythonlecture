# while True:
#     command = input("Type 'exit'  to exit : ")
#     if command == "exit":
#         break

# while True:
#     input_msg2 = input("input msg : ")
#     if input_msg2 =="exit":
#         print("Fine you win")

#         break
#     else :
#         print(input_msg2)


for x in range(1, 101):
    print(x)
    if x == 3:
        break

times = int(input("How many times do I have to tell you? "))

for time in range(times):
	print("CLEAN UP YOUR ROOM!")
	if time >= 4: 
		print("do you even listen anymore?")
		break

   