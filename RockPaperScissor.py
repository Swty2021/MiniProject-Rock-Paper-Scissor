#All modules
import random
print("Game Instructions")
print("Rock Crushes Scissors")
print("Scissors cuts Paper")
print("Paper covers Rock")
player1 = input("Enter player 1:")
print("Welcome:",player1)
player2 = input("Enter player 2:")
print("Welcome:",player2)
#Initialising the scores of the game
user_score=0
system_score = 0
Tie = 0
#Collecting from players the number of games to be
def collect_int_input():
    try:
        n = int(input("Enter how many times you want to play:"))
        return n
    except ValueError:
        print("Please enter a correct integer value")
        collect_int_input()

n = collect_int_input()

for i in range(1,n+1):
    print("GAME-",i)
    try:
        player1_choice = input("Enter your choice:rock,paper,scissor:")
        print("User inputs:",player1_choice)
    except ValueError:
        print("Wrong choice")
    Li1 = ["rock","paper","scissor"]
    player2_choice = random.choice(Li1)
    print("System inputs:",player2_choice)
    if player1_choice == player2_choice:
        print("Score is Tie")
            #user_score = user_score+1
            #system_score = system_score+1
        Tie = Tie+1
        print("Current User score is:",user_score)
        print("Current System score is:",system_score)
        print("Current Tie Score:",Tie)
    elif player1_choice == "rock":
        if player2_choice == "scissor":
            print("User wins!,"+str(player1_choice))
            user_score = user_score+1
            print("Current User score is:",user_score)
        else:
            print("System wins!," +str(player2_choice))
            system_score = system_score+1
            print("Current System score is:",system_score)
    elif player1_choice == "scissor":
        if player2_choice == "paper":
            print("User wins!,"+str(player1_choice))
            user_score = user_score+1
            print("Current User score is:",user_score)
        else:
            print("System wins!," +str(player2_choice))
            system_score = system_score+1
            print("Current System score is:",system_score)
    elif player1_choice == "paper":
        if player2_choice == "rock":
            print("User wins!,"+str(player1_choice))
            user_score = user_score+1
            print("Current User score is:",user_score)
        else:
            print("System wins!," +str(player2_choice))
            system_score = system_score+1
            print("Current System score is:",system_score)
    else:
        print("Invalid play. Check spelling")
    
print("=======Results======")
print("Total Number of Games:",i)
print("Total User Scores:",user_score)
print("Total System Score:",system_score)
print("Total TIE scores:",Tie)
if user_score > system_score:
    print("USER wins the game !!! Congrats !!!!")
elif user_score < system_score:
    print("System wins the game")
else: 
    print("Score is TIE")
