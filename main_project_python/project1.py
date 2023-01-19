'''
Number guessing game in python 3

step:
1: Build a Number guessing game, in which the user selects a range.

'''

import random
import math

# taking input()

lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

# generating random number between the upper and lower

x = random.randint(lower, upper)
print("you've only", round(math.log(upper-lower + 1,2)), "chances to guess the integer")

# initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range

while count < math.log(upper-lower + 1, 2):
    count+=1
    
    guess = int(input("Guess a number: "))
    # condition testing
    
    if x == guess:
        print("Congratulations you have guess number in", count, "try")
        break
    elif x > guess:
        print("you guess too small")
        
    elif x < guess:
        print("you guess too high")
        
        # IF guessing is more then required guesses,
        # then shows this output.
        
    if count >= math.log(upper-lower+ 1, 2):
        print("the number is %d" %x)
        print("Better luck next time")
            
