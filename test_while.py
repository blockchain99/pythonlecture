# user_response = None
# while user_response != "please":
#     user_response = input("Ah ah ah, you didn't say the magic word: ")

for number in range(1, 10):
   print("\U0001f600 " * number)

flag = False
while not flag:
    input_msg = input("input text : ")
    print(input_msg)
    if input_msg == "stop copying me":
        print("Fine you win")
        flag = True
# while input_msg != "stop copying me" :
#     print(input_msg)   #copying text endlessly 

