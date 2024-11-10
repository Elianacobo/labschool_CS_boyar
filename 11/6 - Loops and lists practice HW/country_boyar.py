# Define lists with city names for each state (use abbreviations for state lists)
ny = ["Buffalo", "Rochester", "Syracuse", "Albany", "New York City", "Ithaca"]
ca = ["Los Angeles", "San Francisco", "San Diego", "Sacramento", "San Jose", "Oakland"]
tx = ["Houston", "Dallas", "Austin", "San Antonio", "Fort Worth", "El Paso"]
fl = ["Miami", "Orlando", "Tampa", "Jacksonville", "Tallahassee", "Boca Raton"]
md = ["Bethesda", "Rockville", "Baltimore", "Annapolis", "Potomac", "Silver Spring"]

# Create a "nation" list to hold all state-city lists
country = [ny, ca, tx, fl, md]

# Create a list of state names that correspond to the lists in "country"
state_names = ["New York", "California", "Texas", "Florida", "Maryland"]

# Ask the user for a state name 
user_state = input("Enter a state name: ")

# Check if the user's input matches a state in "state_names"
if user_state in state_names:
    # Find the index of the user's state in "state_names"
    index = state_names.index(user_state)
    
    # Access the corresponding list of cities in "country" using the index
    city_list = country[index]
    
    # Print each city name from the selected state list
    for city in city_list:
        print(city)
        
# If the state is not found in the list, display a message to the user
else:
    print("State not found.")