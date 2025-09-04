import time
import difflib

# Import functions and data from other files
from data import TRAVEL_DATA
from ui import (
    print_welcome_message, 
    get_user_input, 
    display_plan, 
    DESTINATION_STYLE, 
    ERROR_STYLE, 
    INPUT_STYLE, 
    TITLE_STYLE
)

def find_destination(user_destination):
    """Finds the destination in the data, suggests alternatives if not found."""
    if user_destination in TRAVEL_DATA:
        return user_destination

    close_matches = difflib.get_close_matches(user_destination, TRAVEL_DATA.keys())
    if close_matches:
        suggestion = close_matches[0]
        while True:
            try:
                choice = input(
                    f"\nDid you mean '{suggestion.title()}'? (yes/no): "
                ).lower().strip()
                if choice in ['yes', 'y']:
                    return suggestion
                elif choice in ['no', 'n']:
                    print(ERROR_STYLE + "Okay, please try entering the destination again.")
                    return None
                else:
                    print(ERROR_STYLE + "Invalid input. Please enter 'yes' or 'no'.")
            except (KeyboardInterrupt, EOFError):
                print(ERROR_STYLE + "\n\nExiting the assistant. Goodbye!")
                exit()
    else:
        print(ERROR_STYLE + f"Sorry, we couldn't find any information for '{user_destination}'.")
        return None

def main():
    """Main function to run the chatbot."""
    print_welcome_message()
    
    while True:
        destination_input, budget, days = get_user_input()
        
        destination_key = find_destination(destination_input)

        if destination_key:
            print("\n" + DESTINATION_STYLE + "Awesome! Generating your personalized travel plan... ✨")
            time.sleep(1.5)
            display_plan(destination_key, budget, days)

        while True:
            try:
                another_trip = input(
                    INPUT_STYLE + "\n\nWould you like to plan another trip? (yes/no): "
                ).lower().strip()
                if another_trip in ['yes', 'y', 'no', 'n']:
                    break
                else:
                    print(ERROR_STYLE + "Invalid input. Please enter 'yes' or 'no'.")
            except (KeyboardInterrupt, EOFError):
                print(ERROR_STYLE + "\n\nExiting the assistant. Goodbye!")
                exit()
        
        if another_trip in ['no', 'n']:
            print(TITLE_STYLE + "\nHappy travels! Goodbye! 👋")
            break
        else:
            print("\n" + DESTINATION_STYLE + "Let's plan your next adventure!")

if __name__ == "__main__":
    main()
