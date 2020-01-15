print("Choose , rock scissor paper")
print("permutation with repetition: nPIr = n**r , 3**3 -> 9 but 3 kinds are tie, so just 1 kind \
 total: 6 +1  = 7 kind and plus 1(something wrong:) makes 8 case:")
player1 = input("Player1 , make your move : ")
player2 = input("Player2 , make your move : ")

if player1 == player2:
    print("It's tie")
elif player1 == "rock" and player2 == "scissor":
    print("plyer1 win")
elif player1 == "paper" and player2 == "rock":
    print("plyer1 win")
elif player1 == "scissor" and player2 == "paper":
    print("plyer1 win")
else: #but no wrong input cheking logic was missing 
    print("plyer2 win")
    
