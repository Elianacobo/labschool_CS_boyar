
population = 25000
for i in range (0,26):
    population = population + 3500*i
    print(f"Your population is {population}.")
    
size = 8

strength = 9
defense = 9
fortification = 10
attacked = True

for i in range (0,5):
    if attacked == True:
        defense = defense - 1
        strength = strength - 1
        fortification = fortification - 1
        print(f"You have been attacked! Your size is still {size}, your strength is now {strength}, your defense is now {defense}, and your fortification is now {fortification}. STAY SAFE!!")
    else:
        print("You are safe and your military has not changed.")

