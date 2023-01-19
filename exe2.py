# Simple calculator using python

def add(x, y):
    return x+y
def sub(x, y):
    return x-y
def mul(x, y):
    return x*y
def div(x, y):
    return x/y
print("select operation: ")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")


    # take input from user
while True:   
    choice = input("enter your choice(1/2/3/4): ")
    if choice in ("1","2","3","4"):
        num1 = int(input("enter a number: "))
        num2 = int(input("enter another number: "))
    if choice == "1":
        print(num1, "+", num2, "=", add(num1,num2))
        add(num1, num2)
    elif choice == "2":
        print(num1, "-", num2, "=", sub(num1, num2))
        
    elif choice == "3":
        print(num1, "*", num2, "=", mul(num1, num2))
        
    elif choice =="4":
        print(num1, "/", num2, "=", div(num1, num2))
        
    # check if user wants another calculation
    # break the while loop if answer is no
    
    next_calculation = input ("Let's do another calculation? (yes/no): ")
    if next_calculation=="no":
        break
    else:
        print("ok")
        
    