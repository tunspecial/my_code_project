import  random

user_win = 0
computer_win  = 0
options = ["rock" , "paper" , "scissors"]

while True:
    user_input = input("please choose Rock/Paper/Scissors or Q for to Quit Game : ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("computer pick " , computer_pick , ".")


    if user_input == "rock" and computer_pick =="scissors":
        print("you win")
        user_win += 1
    elif user_input == "paper" and computer_pick =="rock":
        print("you win")
        user_win += 1
    elif user_input == "scissors" and computer_pick =="paper":
        print("you win")
        user_win += 1
    else:
        print("you lost!!!")
        computer_win +=1

print("you win " , user_win , "times")
print("computer win" , computer_win , "times")
print("Good Bye!!!")
