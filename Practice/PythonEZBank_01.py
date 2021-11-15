# Beckham Phillips
# EZBank 1

# Imports our custom module
import basics

# Create a new "app" and "user" object from the basics module
app = basics.newProgram()
user = basics.newUser()

# Store the users bank balance as a property of the "app"
app.balance = 1000

# Loop while the app.running is True
while True:
    # Tell the user their balance
    print("Your balance is: $",app.balance)
    # Ask the user to select an option
    print("1 = Deposit, 2 = Withdraw, 3 = Quit")
    user.choice = input("1, 2, or 3 ")
# input() always returns a string, so compare to a string
    if user.choice == "1":
        # Ask how much they want to deposit
        user.deposit = input("How much would you like to deposit?")
        # Check to see if input was a number
        user.deposit = float(user.deposit)
        app.balance = (app.balance + user.deposit)
        print("Here is your new balance: $",app.balance)

    elif user.choice == "2":
        # Ask for withdraw amount
        user.withdraw = input("How much would you like to withdraw?")
        # Check to see if input was a number
        user.withdraw = float(user.withdraw)
        if user.withdraw < app.balance:
            app.balance -= user.withdraw
            print("Here is your new balance:",app.balance)
        else:
            print("You don't have enough money\n")

    elif user.choice == "3":
        # make running False so the loop does not continue
        print("You have quit EZBank")
        app.running = False

    else:
        print("Invalid input")
