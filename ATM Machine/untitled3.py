# PROGRAMMING AN ATM

# Greet the user
print("Welcome to CoBo Bank. Please make a choice.")
# Create database variable
accountBalance1 = 15000

# Create accountBalance1 variable
accountBalance2 = 15000

# Create accountBalance2 variable
accountBalance3 = 15000

hundred = 100
fifties = 50
twenties = 20
tens = 10
fives = 5
ones = 1

# Ask the user for their pin
passcode = 2006
userPin = int(input("Please type your 4 digit pin. "))
if userPin == passcode:
    userDecision = input("Type d for deposit, w for withdrawal, or t for transfer. ")
    if userDecision == "d":
        # Ask the user for the amount they are depositing
        destination = int(input("Which account would you be depositing from? Type 1 for accountBalance1, 2 for accountBalance2, or 3 for accountBalance3. "))
        if destination == 1:
            amount = int(input("How much would you like to deposit from accountBalance1? "))
            accountBalance1 = accountBalance1 + amount
            print(f"You have ${accountBalance1} in your bank account.")
        elif destination == 2:
            amount = int(input("How much would you like to deposit accountBalance2? "))
            accountBalance2 = accountBalance2 + amount
            print(f"You have ${accountBalance2} in your bank account.")
        elif destination == 3:
            amount = int(input("How much would you like to deposit accountBalance3? "))
            accountBalance3 = accountBalance3 + amount
            print(f"You have ${accountBalance3} in your bank account.")
    elif userDecision == "w":
        destination = int(input("Which account would you be withdrawaling from? Type 1 for accountBalance1, 2 for accountBalance2, or 3 for accountBalance3. "))
        if destination == 1:
            amount = int(input("How much would you like to withdrawal from accountBalance1? "))
            if amount > accountBalance1:
                print("You are trying to withdrawal more money then you have in the bank account. Please try again.")
            elif amount <= accountBalance1:
                accountBalance1 = accountBalance1 - amount
                print(f"You have ${accountBalance1} in your bank account.")
                numberOfHundreds = int(amount/hundred)
                amount = amount - numberOfHundreds
                numberOfFifties = int(amount/fifties - 2*numberOfHundreds)
                amount = amount - numberOfFifties
                numberOfTwenties = int(amount/twenties - numberOfFifties)
                amount = amount - numberOfTwenties
                numberOfTens = int(amount/tens - n)
                amount = amount - numberOfTens
                numberOfFives = int(amount/fives)
                amount = amount - numberOfFives
                numberOfOnes = int(amount/ones)
                amount = amount - numberOfOnes
                print(f"You will receive {numberOfHundreds} hundreds, {numberOfFifties} fifties, {numberOfTwenties} twenties, {numberOfTens} tens, {numberOfFives} fives, and {numberOfOnes} ones.")
        elif destination == 2:
            amount = int(input("How much would you like to withdrawal from accountBalance2? "))
            if amount > accountBalance2:
                print("You are trying to withdrawal more money then you have in the bank account. Please try again.")
            elif amount <= accountBalance2:
                accountBalance2 = accountBalance2 - amount
                print(f"You have ${accountBalance2} in your bank account.")
        elif destination == 3:
            amount = int(input("How much would you like to withdrawal from accountBalance3? "))
            if amount > accountBalance3:
                print("You are trying to withdrawal more money then you have in the bank account. Please try again.")
            elif amount <= accountBalance3:
                accountBalance3 = accountBalance3 - amount
                print(f"You have ${accountBalance3} in your bank account.")
    elif userDecision == "t":
        destination1 = int(input("Which account would you be transfering from? Type 1 for accountBalance1, 2 for accountBalance2, or 3 for accountBalance3. "))
        if destination1 == 1:
            destination2 = int(input("Which account would you be transfering to? Type 2 for accountBalance2 or 3 for accountBalance3. "))
            if destination2 == 2:
                amount = int(input("How much would you like to transfer from accountBalance1 to accountBalance2? "))
                if amount > accountBalance1:
                    print("You are trying to transfer more money than you have in your account 2. Please try again.")
                elif amount <= accountBalance1:
                    accountBalance1 = accountBalance1 - amount
                    accountBalance2 = accountBalance2 + amount
                    print(f"You have ${accountBalance1} left in your account 1 and you now have ${accountBalance2} in your account 2.")
            elif destination2 == 3:
                amount = int(input("How much would you like to transfer from accountBalance1 to accountBalance3? "))
                if amount > accountBalance1:
                    print("You are trying to transfer more money than you have in your account 1. Please try again.")
                elif amount <= accountBalance1:
                    accountBalance1 = accountBalance1 - amount
                    accountBalance3 = accountBalance3 + amount
                    print(f"You have ${accountBalance1} left in your account 1 and you now have ${accountBalance3} in your account 3.")
        elif destination1 == 2:
            destination2 = int(input("Which account would you be transfering to? Type 1 for accountBalance1 or 3 for accountBalance3. "))
            if destination2 == 1:
                amount = int(input("How much would you like to transfer from accountBalance1 to accountBalance2? "))
                if amount > accountBalance2:
                    print("You are trying to transfer more money than you have in your account 2. Please try again.")
                elif amount <= accountBalance2:
                    accountBalance2 = accountBalance2 - amount
                    accountBalance1 = accountBalance1 + amount
                    print(f"You have ${accountBalance2} left in your account 2 and you now have ${accountBalance1} in your account 1.")
            elif destination2 == 3:
                amount = int(input("How much would you like to transfer from accountBalance2 to accountBalance3? "))
                if amount > accountBalance2:
                    print("You are trying to transfer more money than you have in your account 2. Please try again.")
                elif amount <= accountBalance2:
                    accountBalance2 = accountBalance2 - amount
                    accountBalance3 = accountBalance3 + amount
                    print(f"You have ${accountBalance2} left in your account 2 and you now have ${accountBalance3} in your account 3.")
        elif destination1 == 3:
            destination2 = int(input("Which account would you be transfering to? Type 1 for accountBalance1 or 2 for accountBalance2. "))
            if destination2 == 1:
                amount = int(input("How much would you like to transfer from accountBalance1 to accountBalance2? "))
                if amount > accountBalance3:
                    print("You are trying to transfer more money than you have in your account 3. Please try again.")
                elif amount <= accountBalance3:
                    accountBalance3 = accountBalance3 - amount
                    accountBalance1 = accountBalance1 + amount
                    print(f"You have ${accountBalance3} left in your account 3 and you now have ${accountBalance1} in your account 1.")
            elif destination2 == 2:
                amount = int(input("How much would you like to transfer from accountBalance3 to accountBalance2? "))
                if amount > accountBalance3:
                    print("You are trying to transfer more money than you have in your account 3. Please try again.")
                elif amount <= accountBalance1:
                    accountBalance3 = accountBalance3 - amount
                    accountBalance2 = accountBalance2 + amount
                    print(f"You have ${accountBalance3} left in your account 3 and you now have ${accountBalance2} in your account 2.")
    # Ask the user if they would like to end the session or continue
    
    
elif userPin != passcode:
    print("The pin you entered is not found in the database. Please try again.")
# do not loop back yet

print("Thank you for your business. We hope to see you again soon.")