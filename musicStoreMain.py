import sys

from music_store_inventory.services import (
    add_music_record_service,
    change_music_records_service,
    search_music_records_service,
    view_music_records_service,
)

def main():
    print("Welcome to the Music Store Inventory")
    main_menu()

def main_menu():
    print("***Main Menu***")
    print("1. Search for Music Records")
    print("2. Add new Music Records")
    print("3. Change Music Record information")
    print("4. View All Music Records")
    print("5. Exit Main Menu")

    try:
        menu_selection_input = int(input("Enter a choice (1-5): "))
    except ValueError:
        print("Please enter a valid number.")
        main_menu()
        return

    if menu_selection_input == 1:
        search_music_records_service()
        print()
        main_menu()
    elif menu_selection_input == 2:
        add_music_record_service()
        main_menu()
    elif menu_selection_input == 3:
        change_music_records_service()
        main_menu()
    elif menu_selection_input == 4:
        view_music_records_service()
        main_menu()
    elif menu_selection_input == 5:
        sys.exit("Thank you for using the Music Inventory application. Goodbye!")
    else:
        main_menu()

if __name__ == "__main__":
    main()
