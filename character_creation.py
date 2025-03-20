# Define global variables for character customization and stats

player = {
    'name': '',
    'class': '',
    'level': 1,
    'xp': 0,
    'strength': 0,
    'magic': 0,
    'agility': 0,
    'charisma': 0
}


def start_game():
    print(
        "The lands of Wallachia are shrouded in darkness, and the world trembles beneath the iron grip of Adrieth, the cursed knight of Apixori.")
    print(
        "But before you begin your quest, you must define who you are. The choices you make now will echo throughout your journey.")

    print("\nChoose your background:")
    print("[1] A peasant, hardened by the toils of the earth, with hands accustomed to the weight of a plow rather than a sword.")
    print("[2] A noble, trained in the art of war, but unaccustomed to the harsh realities of the common folk.")
    print("[3] A mystic from the ancient forests, wielding magic drawn from nature itself.")

    background_choice = input("Enter 1, 2, or 3: ")

    if background_choice == "1":
        player['background'] = "Peasant"
        player['strength'] = 6
        player['agility'] = 5
        player['magic'] = 3
        player['charisma'] = 2
        print(
            "\nYou are a peasant, once a humble farmer who now finds yourself embroiled in a quest far beyond your old life.")
        print("Your body is strong from years of labor, but your knowledge of the arcane is weak.")
    elif background_choice == "2":
        player['background'] = "Noble"
        player['strength'] = 5
        player['agility'] = 4
        player['magic'] = 4
        player['charisma'] = 6
        print(
            "\nYou are a noble, born into privilege and trained in the art of combat. But your silver spoon has not prepared you for the cruel world beyond the castle walls.")
    elif background_choice == "3":
        player['background'] = "Mystic"
        player['strength'] = 3
        player['agility'] = 5
        player['magic'] = 6
        player['charisma'] = 4
        print(
            "\nYou are a mystic, a keeper of ancient secrets and a wielder of powers beyond the comprehension of mortals.")
    else:
        print("Invalid choice. Try again.")
        start_game()

    input("\n[Press Enter to continue]")

    customize_appearance()


def customize_appearance():
    print("\nNow, let’s shape your appearance.")
    print("How does your character look?")

    print("\nChoose your physique:")
    print("[1] Sturdy and imposing, with a physique forged for combat.")
    print("[2] Sleek and swift, adept at weaving through dangers with remarkable agility.")
    print("[3] Graceful and refined, with a magical presence that radiates both charm and power.")

    physique_choice = input("Enter 1, 2, or 3: ")

    if physique_choice == "1":
        player['physique'] = "Tall and muscular"
        player['strength'] += 2
        print("\nYour physique adds to your strength, making you a formidable opponent in combat.")
    elif physique_choice == "2":
        player['physique'] = "Lean and quick"
        player['agility'] += 2
        print("\nYour lean frame enhances your agility, making you a difficult target to hit.")
    elif physique_choice == "3":
        player['physique'] = "Slight and delicate"
        player['magic'] += 2
        print("\nThough physically slight, your presence is charged with mystical energy, enhancing your magic.")
    else:
        print("Invalid choice. Try again.")
        customize_appearance()
    where_are_you_from()
def where_are_you_from():
    print("\nWhere are you from?")
    print("1. Apixori – A kingdom known for its relentless warriors.")
    print("2. Wallechia – The center of a powerful and vast empire.")
    print("3. Hallowed Marsh – A land of mystery and ancient magic.")
    print("4. The Veiled Vale – A secluded village, hidden and forgotten by most, where time moves slowly.")

    location_choice = input("Enter 1, 2, 3, or 4: ")

    if location_choice == "1":
        player['location'] = "Apixori"
        print("\nYou hail from the kingdom of Apixori, a land of disciplined warriors and great conquests.")
    elif location_choice == "2":
        player['location'] = "Wallechia"
        print("\nYou come from the powerful empire of Wallechia, where the influence of the empire stretches far and wide.")
    elif location_choice == "3":
        player['location'] = "Hallowed Marsh"
        print("\nYou emerge from the Hallowed Marsh, a mysterious and mystical place, where ancient magics stir the land.")
    elif location_choice == "4":
        player['location'] = "The Veiled Vale"
        print("\nYou come from the Veiled Vale, a hidden village few know about. Its quiet existence has kept it safe from the troubles of the world.")
    else:
        print("Invalid choice. Try again.")
        where_are_you_from()
    name_character()
def name_character():
    print("\nFinally, what is your name?")
    player['name'] = input("\nEnter your character's name: ")
    print(f"\nWelcome, {player['name']}, to the dark and perilous lands of Wallachia.")
    input("\n[Press Enter to continue]")
    ready_to_start()

def ready_to_start():
        print(f"\nYou are now {player['name']}, a {player['background']} with a {player['physique']} phyisque,from the lands of {player['location']}.")
        print(
            f"Your current stats are:\nStrength: {player['strength']}, Agility: {player['agility']}, Magic: {player['magic']}")

        print("\nAre you ready to begin your adventure?")
        print("(Note: Once you start, you cannot change your character's background, appearance, or stats.)")
        print("\n ( your choices will affect the rest of the game.)")
        print("1. Yes, I am ready.")
        print("2. No, I would like to redo something.")

        choice = input("Enter 1 or 2: ")

        if choice == "1":
            print("\nThe road ahead is uncertain, but with courage in your heart,you embark on a journey like no other...")
            input("\n[Press Enter to continue]")
            begin_story()
        elif choice == "2":
            redo_customization()
        else:
            print("Invalid choice. Try again.")
            ready_to_start()

def redo_customization():
        print("\nWhat would you like to redo?")
        print("[1] Change your name.")
        print("[2] Change your background and appearance.")

        choice = input("Enter 1/2: ")

        if choice == "1":
            player['name'] = input("\nEnter your new character's name: ")
            print(f"\nYour name is now {player['name']}.")
            ready_to_start()
        elif choice == "2":
            start_game()
        elif choice == "3":
            glitch_spot()
        else:
            print("Invalid choice. Try again.")
            redo_customization()
def begin_story():
    print(f"\nWelcome, {player['name']} the {player['background']}!")
    print(f"Starting stats: Strength = {player['strength']}, Magic = {player['magic']}, Agility = {player['agility']}.")
    input("\n[Press Enter to continue]")
    # Start the story
    from story_start import begin_story2
    begin_story2()


