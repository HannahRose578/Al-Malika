import json
import requests

# To install the 'requests' library, run 'pip install requests' in your terminal.
# This program uses the Star Wars API (SWAPI) to fetch character details.
# No API key is needed to access this API.
# This program also uses the 'json' module from Python's standard library to
# pretty-print alliance stats. No installation is required for this module.

# API Usage Explanation:
# ----------------------
# SWAPI is being used in three main ways in this program:
#
# 1. Fetching Character Details
#    This function sends a GET request to `https://swapi.dev/api/people/?search={name}`
#    to search for a Star Wars character by name and fetches their details
#
# 2. Fetching Additional Information (in `fetch_additional_info` function):
#    This function takes a URL (for films, starships, or planets from the SWAPI API) and fetches extra
#    information from the API, returning either the name
#
# 3. Populating Films in `write_alliance_to_file` and `analyze` methods:
#    These methods indirectly use the API to resolve URLs of films related to alliance
#    members into actual film titles using `fetch_additional_info` method
#

def write_alliance_to_file(alliance):
    """
    Write alliance statistics to a JSON file.
    
    Parameters:
    alliance (list): List of dictionaries containing member details.
    """
    with open("alliance_stats.json", "w") as f:
        stats = {
            "Alliance Members": len(alliance),
            "Members": [member['name'] for member in alliance],
            "Total Starships": sum(len(char['starships']) for char in alliance),
            "Films": list(set(url for char in alliance for url in char['films']))
        }
        
        # Populate 'Films' with actual film titles instead of URLs
        stats["Films"] = [fetch_additional_info(url) for url in stats["Films"]]
        
        json.dump(stats, f, indent=4)

def fetch_character_details(name):
    """
    Fetch a Star Wars character's details by their name.
    
    Parameters:
    name (str): The name of the character.
    
    Returns:
    dict: A dictionary containing character details.
    """
    url = f"https://swapi.dev/api/people/?search={name[:20]}" # Added slicing to limit to 20 characters
    response = requests.get(url)
    data = response.json()
    
    return data['results'][0] if len(data['results']) > 0 else None

def fetch_additional_info(url):
    """
    Fetch additional information based on a URL. Used for resolving film or planet names.
    
    Parameters:
    url (str): The URL pointing to the additional info.
    
    Returns:
    str: The title or name associated with the URL.
    """
    response = requests.get(url)
    data = response.json()
    
    return data.get('title', data.get('name'))

def analyze_alliance(alliance):
    """
    Analyze alliance to provide a summary.
    
    Parameters:
    alliance (list): List of dictionaries containing member details.
    """
    total_members = len(alliance)
    total_starships = sum(len(char['starships']) for char in alliance)
    
    # Extract unique film URLs and resolve to actual film titles
    unique_films = set(url for char in alliance for url in char['films'])
    film_names = [fetch_additional_info(url) for url in unique_films]
    
    print(f"\nAlliance Stats:")
    print(f"  Total Members: {total_members}")
    print(f"  Total Starships: {total_starships}")
    print(f"  Films: {', '.join(film_names)}")

def main():
    """
    Main function to drive the program. Provides a menu to interact with Star Wars API.
    """
    alliance = []  # List to store characters added to the alliance
    member_added = False  # Flag to check if any member has been added to the alliance
    
    while True:
        # Main menu options
        print("\nStar Wars Universe Explorer")
        print("1. Search for a character")
        print("2. Show alliance stats")
        print("3. Quit")
        main_choice = input("Choose an option (1/2/3): ")

        if main_choice == '1':
            # Search for a character by name
            character_name = input("\nEnter the Star Wars character's name: ").strip()
            character_data = fetch_character_details(character_name)

            if not character_data:
                print("Character not found.")
                continue
            
            # Display basic character information
            print(f"\nInfo for {character_data['name']}:")
            print(f"  Height: {character_data['height']} cm")
            print(f"  Mass: {character_data['mass']} kg")
            print(f"  Homeworld: {fetch_additional_info(character_data['homeworld'])}")

            while True:
                # Sub-menu for character-related actions
                print("\nWhat would you like to do next?")
                print("1. Add to alliance")
                print("2. Explore more about this character")
                print("3. Go back to main menu")
                choice = input("Choose an option (1/2/3): ")

                if choice == '1':
                    # Add the current character to the alliance list. Allows duplicates for the same character for greater freedom.
                    alliance.append(character_data)
                    print(f"Added {character_data['name']} to the alliance!")
                    member_added = True
                elif choice == '2':
                    # Show additional details like films and starships
                    films = [fetch_additional_info(url) for url in character_data['films']]
                    starships = [fetch_additional_info(url) for url in character_data['starships']]
                    print(f"\nFilms: {', '.join(films)}")
                    print(f"Starships: {', '.join(starships) if starships else 'None'}")
                elif choice == '3':
                    break
                else:
                    print("Invalid option.")

        elif main_choice == '2':
            # Show alliance statistics
            if member_added:
                analyze_alliance(alliance)
                print("\nWould you like to save these stats to a file? (y/n)")
                save_choice = input().strip().lower()
                if save_choice == 'y':
                    write_alliance_to_file(alliance)
                    print("Alliance stats saved to 'alliance_stats.json'.")
            else:
                print("No members in the alliance yet.")

        elif main_choice == '3':
            break  # Exit the program
        else:
            print("Invalid option.")

# Run the program if this file is executed as a script
if __name__ == "__main__":
    main()
