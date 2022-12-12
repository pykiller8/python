# guessing number:
import random
random_num = random.randrange(1,10)


for i in range (5):
        user_guess  = int(input("Guess the number: "))
    
        if user_guess == random_num:
            print("Congratulation! you have guess the number in", i,"times")
            break
    
        elif user_guess > random_num :
            print("your guess is high!")
    
        elif user_guess < random_num:
            print("your guess is low!")
            
        
            







