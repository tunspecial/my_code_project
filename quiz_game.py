print("Hello welcome to my quiz game")
game = input("do you want to play the game? Yes or No? :").lower() #user input data to change to all lower case letter.
if game != "yes":
    quit()
print("Ok let play the game :P ")
total_score = []

player = input("what is the CUP stand for? ")
if player.lower() == "central processing unit":
    print("Correct")
    total_score =+ 1
else:
    print("Incorrect Answer")
player = input("what is the GUI stand for? ")
if player.lower() == "graphics user interface":
    print("Correct")
    total_score += 1
else:
    print("Incorrect Answer")
player = input("what is the RAM stand for? ")
if player.lower() == "random access memory":
    print("Correct")
    total_score += 1
else:
    print("Incorrect Answer")
player = input("what is the USB stand for? ")
if player.lower() == "universal serials bus":
    print("Correct")
    total_score += 1
else:
    print("Incorrect Answer")
print("Your total score is " + str(total_score) + " answer corrects")
print("Your total score is " + str((total_score/4)*100) + "%.")



