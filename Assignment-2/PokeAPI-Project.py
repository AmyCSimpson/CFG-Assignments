# Trying to understand code for API game

import requests  # Module to make HTTP requests

import random  # Used for generating random numbers

import time  # This additional module is used for creating delays between clues - it does not need installed.

# This script uses the free PokeAPI.
# No API key is required for access.
# The PokeAPI provides a wealth of information on Pokémon, including their stats, species data, evolution chain, and more.
# We use the API to get random Pokémon data from Generation 1 (Pokémon IDs 1-151)

# Function to get a random Pokémon from the PokeAPI (Gen 1 Pokémon)
# We use the `requests` module to send an HTTP GET request to the PokeAPI server. A GET request asks the server to
# send back specific data (like Pokémon details) based on the URL we provide.
#    - For example, the URL `https://pokeapi.co/api/v2/pokemon/1` requests data for the Pokémon with ID 1 (Bulbasaur).
def get_random_pokemon():
    pokemon_id = random.randint(1, 151)  # Random Pokémon ID (Gen 1 only)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    return response.json()  # Return Pokémon data as a dictionary


# Function to fetch Pokémon species data (like color and evolution chain)
#    - PyCharm, through the `requests` module, receives the API's response.
#    - We extract the data by calling `response.json()`. This converts the JSON data from the API into a Python dictionary,
#    making it easy to work with in the script.
#    - The dictionary allows us to access specific pieces of information, like color and evolution chain, by using
#    dictionary keys.
def get_pokemon_species(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}"
    response = requests.get(url)
    return response.json()  # Return species data as a dictionary



# Function to fetch the evolution chain data
def get_evolution_chain(evolution_url):
    response = requests.get(evolution_url)
    return response.json()


# Function to extract the Pokémon evolution chain
def extract_evolution_chain(chain):
    evolutions = []
    current = chain["chain"]

    while current:
        evolutions.append(current["species"]["name"])
        if current["evolves_to"]:
            current = current["evolves_to"][0]
        else:
            break
    return evolutions


# Helper function to write game result to a file
# Used for loop to write game result to file, accounting for if user plays more than one round
def write_to_file(data):
    with open("pokemon_trivia_result.txt", "w") as file:
        for individual_result in data:
            file.write(individual_result + "\n\n")


# Function to handle guessing logic and return whether the guess is correct
def check_guess(pokemon_name, guess):
    return guess.lower() == pokemon_name.lower()

# Main trivia game function
def play_trivia_game():
    pokemon_data = get_random_pokemon()  # Get random Pokémon data
    if not pokemon_data:
        print("Failed to retrieve Pokémon data.")
        return

    pokemon_name = pokemon_data["name"]  # Pokémon's name
    print("Welcome to 'Who's That Pokémon?' \nLet's start the game! You will need to guess the Pokémon after each clue.")

    # Get Pokémon's types (list)
    types = [t['type']['name'] for t in pokemon_data['types']]
    clues = [f"This Pokémon's type is {', '.join(types)}."]

    # Get species info to get Pokémon's color and evolution chain
    species_data = get_pokemon_species(pokemon_name)
    if not species_data:
        print("Failed to retrieve Pokémon species data.")
        return

    # Give color clue
    color = species_data['color']['name']
    clues.append(f"This Pokémon's color is {color}.")

    # String slicing: First 3 letters of the name
    clues.append(f"The first 3 letters of the Pokémon's name are: {pokemon_name[:3].capitalize()}")

    # Get a few random attack moves
    moves = [move['move']['name'] for move in pokemon_data['moves']]
    random_moves = random.sample(moves, min(3, len(moves)))
    clues.append(f"Some of this Pokémon's moves are {', '.join(random_moves)}.")

    # Check evolution chain
    # Utilised for loop to make sure Pokémon being guessed was not spoiled
    evolution_chain_url = species_data['evolution_chain']['url']
    evolution_data = get_evolution_chain(evolution_chain_url)
    evolutions = extract_evolution_chain(evolution_data) if evolution_data else []
    for i in range(0,len(evolutions)):
        if evolutions[i] == pokemon_name:
            evolutions[i] = "***"

    # Boolean logic: Check if Pokémon is legendary
    is_legendary = species_data["is_legendary"]
    clues.append(f"This Pokémon is{' ' if is_legendary else ' not '}a legendary Pokémon.")

    # Determine evolution status using if else statement
    if len(evolutions) > 1:
        clues.append(f"This Pokémon evolves in this order: {', '.join(evolutions)}.")
    else:
        clues.append("This Pokémon does not evolve.")

    # Loop through clues and ask the user to guess after each clue
    for i, clue in enumerate(clues):
        print(f"Clue {i + 1}: {clue}")
        guess = input("Enter your guess: ").strip()

        if check_guess(pokemon_name, guess):
            result = f"Correct! The Pokémon is {pokemon_name.capitalize()}!"
            print(result)
            all_results.append(result)
            return
        else:
            print("Incorrect! Here's another clue...")
            time.sleep(1)  # Short delay before the next clue

    # If the player reaches the end without guessing correctly
    result = f"Oh no, you've run out of clues! The correct answer was {pokemon_name.capitalize()}.\nBetter luck next time!"
    print(result)
    all_results.append(result)

# Start the trivia game
if __name__ == "__main__":
    play_again = True
    all_results = []
    result_string = ""
    while play_again:
        play_trivia_game()
        if input("Do you want to play again? (Y/N)") == "N":
            play_again=False
            write_to_file(all_results)