"""
Client side, "Requests" goes here.
This will also be where your marker starts from
and where your main program should start from
"""
import requests
import json


def get_all_cards_front_end():
    endpoint = "http://127.0.0.1:5000/cards"
    result = requests.get(endpoint).json()
    return result


def add_new_card_front_end(new_card_dict):
    endpoint = "http://127.0.0.1:5000/cards/add"
    result = requests.post(
        endpoint,
        headers={'content-type': 'application/json'},
        data=json.dumps(new_card_dict)
    )
    return result.json()


def delete_card_by_id(card_id):
    endpoint = f"http://127.0.0.1:5000/cards/remove/{card_id}"
    result = requests.delete(endpoint).json()
    return result


def collect_card_data():
    # Prompt the user for input with appropriate questions
    name = input("Enter the Pokémon card's name: ").strip()

    # Prompt for card type (e.g., Fire, Water)
    card_type = input("Enter the card's type (e.g., Fire, Water): ").strip()

    # Prompt for PSA rating of the card
    psa = input("Enter the card's PSA rating (e.g., Mint, Near Mint): ").strip()

    # Return the collected data as a dictionary
    new_card_dict = {
        "name": name,
        "type": card_type,
        "PSA": psa
    }

    return new_card_dict


def run():
    # NOTE - I've added more splash here for the Front End example.
    print("\nWelcome to the Pokémon Trading Card Registry!")
    print("---------------------------------")
    print("Choose an option:")
    print("A: View all Pokémon card records")
    print("B: Remove a card by ID")
    print("C: Add a NEW Pokémon card")
    print("---------------------------------")

    answer = input("What would you like to do? (A, B or C): ").strip().upper()

    if answer == "A":
        cards = get_all_cards_front_end()
        if cards is None:
            print("Failed to retrieve records.")
        else:
            print("Pokémon Card Registry:")
            print(cards)

    elif answer == "B":
        cards = get_all_cards_front_end()
        print("Here is the Pokémon card registry: \n")
        print(cards)
        if cards is not None:
            card_id_to_remove = input("\nEnter the ID of the card you would like to remove: ").strip()
            print("Card removed from registry:")
            print(delete_card_by_id(card_id_to_remove))
        else:
            print("Could not load cards for deletion.")

    elif answer == "C":
        new_card_dict = collect_card_data()
        print("Updated Pokémon Card Registry:")
        print(add_new_card_front_end(new_card_dict))

    else:
        print("Invalid option. Please select either A, B, or C.")


if __name__ == "__main__":
    run()

