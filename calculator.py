from calculator_func import *

while True:
    print("what would you like to do")
    print("1. additional (+)")
    print("2. subtraction (-)")
    print("3. multiply (*)")
    print("4. division (/)")
    print("Q for exit program")

    user_choice = input("please enter your chose number: ")
    if user_choice == "q" or user_choice == "q":
        break

    num1 = float(input("please enter your first digit number "))
    num2 = float(input("please enter your second digit number "))

    if user_choice == "1":
        addition(num1 , num2) #calling from function module
    elif user_choice == "2":
        subtraction(num1 ,num2) #calling from function module
    elif user_choice == "3":
        multiply(num1 , num2) #calling from function module
    elif user_choice == "4":
        division(num1 , num2) #calling from function module
    else:
        print("invalid request")

    print("\n")
