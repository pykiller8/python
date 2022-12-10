# rock paper scissor using python ..

import random
com_choice = ["Rock", "Paper", "Scissor"]
while True:
        print("Rock Paper Scissor Game:")
        youwin, computerwin = 0, 0
        for i in range(1,6):  # 5 round 
            print("Round",i, "start:")
            print("Please select any option: ")
            print("1.Rock", "2.Paper", "3.Scissor", sep=" ")
            yourchoice = int(input())
            if yourchoice==1:
                print("You select Rock")
                yourchoice="Rock"
            elif yourchoice==2:
                print("You select Paper")
                yourchoice="Paper"
            elif yourchoice==3:
                print("You select Scissor")
                yourchoice="Scissor"
            else:
                print("Invalid choice")
                break
            
            Computerchoice = random.choice(com_choice)
            print("Computer choice:", Computerchoice)
        
            if yourchoice==Computerchoice:
                youwin+=1
                computerwin+=1
                print("Draw")
            elif (yourchoice=="Rock" and Computerchoice=="Scissor") or (yourchoice=="Paper" and Computerchoice=="Rock") or (yourchoice=="Scissor" and Computerchoice=="Paper"):
                youwin+=1
                print("you won this round")
        
            else:
                computerwin+=1
                print("Computer win this round")
                
        if youwin>computerwin:
            print("you won the game:")
            print("Score is", "Your score:",youwin,"computer score:",computerwin, sep=" ")
        elif computerwin>youwin:
            print("you lost game")
            print("Score is","Your Score:", youwin, "computer score:", computerwin, sep=" ")
        else:
            print("match draw")
            print("Score is:","Your score:",youwin,"Computer score:",computerwin,sep=" ")
        
        user_choice = input("want to play again?(Yes/Exist)")
        if user_choice=="Yes" or user_choice=="Yes" or user_choice=="Yes":
            continue
        else:
            break