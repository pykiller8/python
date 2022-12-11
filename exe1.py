# Rock paper game in python using simple logic:

import random
possible_play = ["rock","paper","scissor"]
computer_choice = random.choice(possible_play) 

youwin, compwin = 0,0

for i in range(1,3):
    print("Round", i, "start")
    print("Rock", "Paper", "Scissor")
    user_choice = input()
    if user_choice=="rock":
        print("you choose rock")
    elif user_choice=="paper":
        print("you choose paper")
    elif user_choice == "scissor":
        print("you choose scissor")   
    else:
        print("invalid choice")
        break
        
    
    print("Computer choose", computer_choice)

    
    if user_choice==computer_choice:
        print("game tie")
        youwin+=1
        compwin=+1
    elif (user_choice=="rock" and computer_choice=="scissor")or(user_choice=="paper"and computer_choice=="rock")or(user_choice=="scissor"and computer_choice=="paper"):
        print("you win")
        youwin+=1
    else:
        print("computer win")
        compwin+=1
        
    print("your score is", youwin, "and computer score is", compwin)

    if youwin>compwin:
        print("you won the game")
    elif youwin<compwin:
        print("computer won the game")
else:
    print("game is tied")

    user_choice=input("Restart the game again,(yes/no)")
while True: 
    if user_choice=="yes" or user_choice=="yes" or user_choice=="yes":
        continue
    else:
        break


    
    


    