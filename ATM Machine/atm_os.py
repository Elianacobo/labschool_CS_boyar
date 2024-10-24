# PROGRAMMING AN ATM

# Greet the user
print("Welcome to CoBo Bank. Please make a choice.")
# Create database variable
accountBalance1 = 15000

# Create accountBalance1 variable
accountBalance2 = 15000

# Create accountBalance2 variable
accountBalance3 = 15000

# Ask the user for their pin
passcode = 2006
userPin = int(input("Please type your 4 digit pin. "))
if userPin == passcode:
    userDecision = input("Type d for deposit, w for withdrawal, or t for transfer ")
    if userDecision == "d":
        # Ask the user for the amount they are depositing
        destination = int(input("Which account would you be depositing from? Type 1 for accountBalance1, 2 for accountBalance2, or 3 for accountBalance3. "))
        if destination == 1:
            amount = int(input("How much would you like to deposit from accountBalance1? "))
        elif destination == 2:
            amount = int(input("How much would you like to deposit accountBalance2? "))
        elif destination == 3:
            amount = int(input("How much would you like to deposit accountBalance3? "))
elif userPin != passcode:
    print("The pin you entered is not found in the database. Please try again.")
# do not loop back yet

