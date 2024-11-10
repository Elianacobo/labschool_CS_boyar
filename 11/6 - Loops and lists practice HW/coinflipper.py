# Import the random module for generating random values
import random

# Define the coin_flipper function
def coin_flipper():
    # Ask the user to input the number of coin flips they want and convert it to an integer
    num_flips = int(input("Enter the number of times to flip the coin: "))
    
    # Create a list to represent the coin with "Head" and "Tail" as options
    coin_sides = ["Head", "Tail"]
    
    # Create a list to keep track of the results of each flip
    flip_results = []
    
    # Create counters for heads and tails
    heads_count = 0
    tails_count = 0
    
    # Create a loop counter for tracking the number of flips
    flip_counter = 0
    
    # Start a while loop that continues until the flip_counter reaches num_flips
    while flip_counter < num_flips:
        # Randomly select a side from the coin_sides list
        flip = random.choice(coin_sides)
        
        # Append the flip result to the flip_results list
        flip_results.append(flip)
        
        # Check if the flip result was "Head" and increment the heads_count if so
        if flip == "Head":
            heads_count += 1
        else:
            # If the flip result was "Tail", increment the tails_count
            tails_count += 1
            
        # Increment the flip_counter to keep track of the number of flips
        flip_counter += 1
    
    # Calculate the percentage of heads and tails
    heads_percentage = (heads_count / num_flips) * 100
    tails_percentage = (tails_count / num_flips) * 100

    # Display the final percentages
    print("Heads Percentage: ", heads_percentage)
    print("Tails Percentage: ", tails_percentage)

# Call the function to execute the coin flipper
coin_flipper()
