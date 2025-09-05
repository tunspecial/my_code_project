master_pass = input("please enter your master password: ")

def view():
    with open("password.txt", mode="r") as file:
        for line in file.readlines(): ##reads all lines into a list
            data = (line.rstrip()) ## This splits from the right by whitespace
            user, passw = data.split("|")
            print("user;" , user , ", password:" , passw)


def add():
    name = input("please Account Name : ")
    pwd = input("please Account Password : ")

    with open("password.txt" , mode="a") as file:
        file.write(name + "|" + pwd + "\n")

while True:
    user_input = input("you would like to view and add password(view,add), Q for Quit").lower()
    if user_input == "q":
        quit()

    if user_input == "view":
        view()
    elif user_input == "add":
        add()
    else:
        print("Invalid mode.")
        continue
