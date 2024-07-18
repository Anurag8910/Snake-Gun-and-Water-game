import random

ele = ['s','w','g']
totalChances = 10
chances = 0
playerPoints = 0
computerPoints = 0
print("....Welcome to snake, water and gun game game....")
print("entr s for snake, w for water and g for gun")

while(chances < totalChances):
    print(f"chance {chances+1}")
    player = input(" : enter your choice : ")
    computer = random.choice(ele)
    while(player==computer):
        computer = random.choice(ele)
    print(f"computer choice {computer}")
    if(player == 's' and computer == 'w'):
        playerPoints+=1
        print("you won this round +1 point")
    elif(player == 's' and computer == 'g'):
        computerPoints+=1
        print("computer won this round +1 point")
    elif(player == 'w' and computer == 's'):
        computerPoints+=1
        print("computer won this round +1 point")
    elif(player == 'w' and computer == 'g'):
        playerPoints+=1
        print("you won this round +1 point")
    elif(player == 'g' and computer == 's'):
        playerPoints+=1
        print("you won this round +1 point")
    elif(player == 'g' and computer == 'w'):
        computerPoints+=1
        print("computer won this round +1 point")
    chances+=1

if(playerPoints > computerPoints):
    print(f"you won total points {playerPoints}")
else:
    print(f"computer won total points {computerPoints}")