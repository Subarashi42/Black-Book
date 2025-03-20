from Mountains import battlefield_encounter, continue_journey2
from character_creation import player

# Travel menu 1
player_destination = ""


def travel_menu():
    global player_destination
    print("\nYou stand at a crossroads, pulling out your map, deciding your next destination.")
    print("[1] The Dragons Keep")
    print("[2] The Mountain of Echoes")
    print("[3] The Village of Sarth")
    print("[4] The Temple of the Forgotten")
    print("[5] Proceed to Wallechia")

    choice = input("Choose your destination (1/2/3/4/5): ")

    if choice == "1":
        if player['level'] >= 15:
            player_destination = "dragons_keep"
            print("\nYou decide to venture to the Dragons Keep, where legends of ancient dragons still linger.")
        else:
            print("\nYou must reach level 15 before you can proceed to the Dragons Keep.")
            player_destination = ""
            travel_menu()
    elif choice == "2":
        player_destination = "mountain_of_echoes"
        print("\nYou choose to travel to the Mountain of Echoes, where your voice is said to carry for miles.")
    elif choice == "3":
        player_destination = "village_of_sarth"
        print("\nYou decide to head to the Village of Sarth, where whispers of a mysterious figure have been heard.")
    elif choice == "4":
        print(
            "\nYou attempt to look at the map for the Temple of the Forgotten, but it appears to be burned or missing.")
        print("You cannot proceed without the necessary information.")
        player_destination = ""
        travel_menu()
        return
    elif choice == "5":
        if player['level'] >= 20:
            player_destination = "wallechia"
            print("\nYou decide to proceed to Wallechia, the heart of the kingdom and where your fate may be sealed.")
        else:
            print("\nYou must reach level 20 before you can proceed to Wallechia.")
            player_destination = ""  # Reset player_destination if Wallechia is not allowed
            travel_menu()  # Prompt again if the player tries to proceed to Wallechia prematurely
            return
    else:
        print("Invalid choice, please select 1, 2, 3, 4, or 5.")
        travel_menu()

    input("\nPress Enter to continue.")
    battlefield_encounter()  # Proceed to the battlefield encounter based on the player's choice


def travel_menu2():
    global player_destination
    print("\n After lifting the dark magic from the mountain, you pull open your map to decide where to go next.")
    print("1. The Dragons Keep")
    print("2. The Village of Sarth")
    print("3. The Temple of the Forgotten")
    print("4. Proceed to Wallechia")

    choice = input("Choose your destination (1/2/3/4/5): ")

    if choice == "1":
        player_destination = "dragons_keep"
        print("\nYou decide to venture to the Dragons Keep, where legends of ancient dragons still linger.")
    elif choice == "2":
        print("\nYou glance at the map, looking at a marked location.")
        print("named The village of sarth, although it seems you have no reason.")
        print("to go there, you decide to glance back over the map.")
        player_destination = ""
        travel_menu2()
    elif choice == "3":
        print(
            "\nYou attempt to look at the map for the Temple of the Forgotten, but it appears to be burned or missing.")
        print("You cannot proceed without the necessary information.")
        player_destination = ""
        travel_menu2()
        return
    elif choice == "4":
        if player['level'] >= 20:
            player_destination = "wallechia"
            print(
                "\nYou decide to proceed to Wallechia, the heart of the kingdom and where your fate may be sealed.")
        else:
            print("\nYou must reach level 20 before you can proceed to Wallechia.")
            player_destination = ""  # Reset player_destination if Wallechia is not allowed
            travel_menu2()  # Prompt again if the player tries to proceed to Wallechia prematurely
            return
    else:
        print("Invalid choice, please select 1, 2, 3, 4, or 5.")
        travel_menu2()

    input("\nPress Enter to continue.")
    continue_journey2()