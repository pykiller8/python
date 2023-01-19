user_input_num1=float(input("enter your 1st number: "))
operator =input("enter a operator: ")
user_input_num2=float(input("enter your 2nd number: "))


if operator=="+":
    print(user_input_num1+user_input_num2)
elif operator=="-":
    print(user_input_num1-user_input_num2)
elif operator=="*":
     print(user_input_num1*user_input_num2)
elif operator=="/":
     print(user_input_num1/user_input_num2)
else:
    print("Invalid operator")
while True:
    user_input_num1,user_input_num2=float(input("lets do another calculation", ("yes"or"no")))
    if (user_input_num1,user_input_num2)=="no":
        break
    else:
        print("ok")
    
