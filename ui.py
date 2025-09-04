# This file contains functions for displaying text and interacting with the user via the terminal.

import textwrap
import time
from colorama import init, Fore, Style
from data import TRAVEL_DATA

# Initialize colorama
init(autoreset=True)

# --- STYLES ---
TITLE_STYLE = Fore.CYAN + Style.BRIGHT
HEADER_STYLE = Fore.YELLOW + Style.BRIGHT
DESTINATION_STYLE = Fore.GREEN + Style.BRIGHT
ERROR_STYLE = Fore.RED + Style.BRIGHT
INPUT_STYLE = Fore.MAGENTA

def print_welcome_message():
    """Prints a stylish welcome message for the user."""
    print(TITLE_STYLE + "=" * 60)
    print(TITLE_STYLE + "✈️  Welcome to the Terminal Travel Booking Assistant! ✈️")
    print(TITLE_STYLE + "=" * 60)
    print("\nLet's plan your next adventure together. Just tell me where you'd like to go!")
    time.sleep(1)

def display_destinations():
    """Displays the list of available destinations."""
    print(HEADER_STYLE + "\nHere are the destinations we can explore:")
    
    dest_list = sorted(list(TRAVEL_DATA.keys()))
    
    col_width = max(len(d) for d in dest_list) + 4
    cols = 3
    for i in range(0, len(dest_list), cols):
        line = dest_list[i:i+cols]
        print("".join(d.title().ljust(col_width) for d in line))

def get_user_input():
    """Gets travel preferences from the user."""
    display_destinations()

    while True:
        try:
            destination_input = input(INPUT_STYLE + "\n➡️  Enter your preferred destination: ").lower().strip()
            if destination_input:
                break
            else:
                print(ERROR_STYLE + "Destination cannot be empty.")
        except (KeyboardInterrupt, EOFError):
            print(ERROR_STYLE + "\n\nExiting the assistant. Goodbye!")
            exit()

    while True:
        try:
            budget = input(INPUT_STYLE + "➡️  Enter your budget category (low, mid, luxury): ").lower().strip()
            if budget in ['low', 'mid', 'luxury']:
                break
            else:
                print(ERROR_STYLE + "Invalid budget. Please choose from 'low', 'mid', or 'luxury'.")
        except (KeyboardInterrupt, EOFError):
            print(ERROR_STYLE + "\n\nExiting the assistant. Goodbye!")
            exit()

    while True:
        try:
            days_input = input(INPUT_STYLE + "➡️  Enter the number of days for your trip: ").strip()
            days = int(days_input)
            if days > 0:
                break
            else:
                print(ERROR_STYLE + "Number of days must be a positive number.")
        except ValueError:
            print(ERROR_STYLE + "Invalid input. Please enter a number for the days.")
        except (KeyboardInterrupt, EOFError):
            print(ERROR_STYLE + "\n\nExiting the assistant. Goodbye!")
            exit()

    return destination_input, budget, days

def generate_itinerary(data, days):
    """Generates a simple day-wise itinerary."""
    print("\n" + TITLE_STYLE + "=" * 60)
    print("🗓️  Suggested Day-wise Itinerary  🗓️".center(60))
    print(TITLE_STYLE + "=" * 60)

    plan_items = data['attractions'] + data['activities']
    
    if not plan_items:
        print(ERROR_STYLE + "No specific itinerary items available for this destination.")
        return

    for day in range(1, days + 1):
        item1 = plan_items[(day - 1) * 2 % len(plan_items)]
        item2 = plan_items[((day - 1) * 2 + 1) % len(plan_items)]
        print(f"\n{HEADER_STYLE}Day {day}:")
        print(textwrap.indent(f"Morning: Explore {item1}", "   "))
        print(textwrap.indent(f"Afternoon: Enjoy {item2}", "   "))
        print(textwrap.indent("Evening: Relax or explore local markets.", "   "))

def display_plan(destination_key, budget, days):
    """Displays the complete travel plan for the selected destination."""
    data = TRAVEL_DATA[destination_key]
    
    print("\n" + TITLE_STYLE + "=" * 60)
    print(f"🌍 Your Trip Plan for {destination_key.title()} 🌍".center(60))
    print(TITLE_STYLE + "=" * 60)

    print(f"\n{HEADER_STYLE}📅 Best Time to Visit:")
    print(f"   {data['best_time']}")
    
    print(f"\n{HEADER_STYLE}💰 Approximate Cost (for {days} days, {budget} budget):")
    print(f"   {data['cost'][budget]}")

    print(f"\n{HEADER_STYLE}🏨 Recommended Stays ({budget} budget):")
    print(f"   {data['hotels'][budget]}")

    # --- NEW SECTION FOR TRANSPORTATION ---
    if 'how_to_reach' in data:
        print(f"\n{HEADER_STYLE}🚖 How to Reach:")
        reach_info = data['how_to_reach']
        if 'air' in reach_info:
            print(textwrap.indent(f"By Air ✈️: {reach_info['air']}", "   - "))
        if 'train' in reach_info:
            print(textwrap.indent(f"By Train 🚂: {reach_info['train']}", "   - "))
        if 'bus' in reach_info:
            print(textwrap.indent(f"By Bus 🚌: {reach_info['bus']}", "   - "))
        if 'sea' in reach_info:
            print(textwrap.indent(f"By Sea 🚢: {reach_info['sea']}", "   - "))

    if 'currency' in data:
        print(f"\n{HEADER_STYLE}💱 Currency Info:")
        print(f"   {data['currency']}")
    
    if 'visa' in data:
        print(f"\n{HEADER_STYLE}🛂 Visa Info:")
        print(f"   {data['visa']}")
    
    print(f"\n{HEADER_STYLE}📍 Top Tourist Attractions:")
    for item in data['attractions']:
        print(f"   - {item}")
    
    print(f"\n{HEADER_STYLE}🏄 Suggested Activities:")
    for item in data['activities']:
        print(f"   - {item}")

    print(f"\n{HEADER_STYLE}🍔 Famous Local Food:")
    for item in data['food']:
        print(f"   - {item}")

    generate_itinerary(data, days)