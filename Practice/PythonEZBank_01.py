# Beckham Phillips
# EZBank 1
import basics

app = basics.newProgram()

user = basics.newUser()

app.balance = 1000

app.running = True

while app.running == True:
    print("1 = Deposit, 2 = Withdraw, 3 = Quit")

    user.choice = input("1, 2, or 3 ")

    if user.choice == "1":
        user.deposit = input("How much would you like to deposit?")
        user.deposit = int(user.deposit)
        app.balance = (app.balance + user.deposit)
        print("Here is your new balance:",app.balance)

    elif user.choice == "2":
        user.withdraw = input("How much would you like to withdraw?")
        user.withdraw = int(user.withdraw)
        app.balance = (app.balance - user.withdraw)
        print("Here is your new balance:",app.balance)

    elif user.choice == "3":
        print("You have quit EZBank")
        app.running = False

    else:
        print("Invalid input")
