import random

user_numer = input("please enter the number :")
if user_numer.isdigit(): #user input change from string data type to integer data type.
    user_numer = int(user_numer)
    if user_numer <= 0 :
        print("hey , please enter above zero number")
        quit()
else:
    print("please type number only next time")
    quit()

random_number = random.randrange(0,10)
guess = 0
while True:
    guess += 1
    guess_number = input("type your number")
    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("please enter digit only!!!")
        continue
    if guess_number == random_number:
        print("your win!!!")
        break
    elif guess_number > random_number:
        print("your number is above guess number")
    else:
        print("your number is less guess number")

print("you got it in" , guess , "guesses!!")