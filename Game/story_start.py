from Game.Mountains import leave_village_no_info
from Game.character_creation import player


def begin_story2():
    if player['background'] == "Peasant":
        print(f"\n{player['name']}, the fields you once tilled are barren, and the village elder spoke of a curse spreading through the land. No one knows the cause, only that the darkness is spreading.")
        print( "With little choice, you’ve set out to find answers, leaving your village behind as the road stretches before you.")

    elif player['background'] == "Noble":
        print(f"\n{player['name']}, the halls of your estate echo with fear. Whispers speak of a shadow consuming kingdoms, though no one dares name the one behind it.")
        print("With your family's honor at stake, you venture out to uncover the truth behind the growing threat.")

    elif player['background'] == "Mystic":
        print(f"\n{player['name']}, the signs of nature have turned dire. The spirits whisper of a great darkness, though they do not name it. The balance of the world is faltering.")
        print("Guided by these warnings, you leave your sanctuary and begin your journey into the unknown.")

    print(
        "\nThe road ahead seems endless, while a twisted forest looms to your right. The air feels heavy, as if something dark lingers just beyond your understanding.")

    input("\n[Press Enter to continue]")
    choice1()
def choice1():
    print("\nYou see two paths before you:")
    print("1. Enter the forest.")
    print("2. Continue along the road.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        enter_forest()
    elif choice == "2":
        continue_road()
    else:
        print("Invalid choice, please select 1 or 2.")
        choice1()


def enter_forest():
    print("\nYou step into the dark, shadowy forest. The trees seem to whisper around you.")
    print("Suddenly, you hear rustling in the bushes.")
    print("[1] Investigate the noise.")
    print("[2] Ignore it and move deeper into the forest.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        investigate_noise()
    elif choice == "2":
        deeper_forest()
    else:
        print("Invalid choice, please select 1 or 2.")
        enter_forest()


def continue_road():
    print("\nYou continue walking along the road. The sun is shining and the day seems peaceful.")
    print("After a few miles, you come across a small village.")
    print("[1] Visit the village inn.")
    print("[2] Speak to the local blacksmith.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        visit_inn()
    elif choice == "2":
        speak_blacksmith()
    else:
        print("Invalid choice, please select 1 or 2.")
        continue_road()


def investigate_noise():
    print(
        "\nThe forest grows darker as you enter, the trees seeming to close in around you. A strange silence hangs in the air, broken only by the occasional rustle of leaves.")
    print(
        "Suddenly, you spot something lying on the ground—it's a soldier, badly wounded, his armor torn and bloodied. His breath is shallow as he tries to speak.")
    input("\n[Press Enter to continue]")
    wounded_soldier()
def wounded_soldier():

    print(
        f"\nWounded Soldier: 'Please... help me... a beast... it attacked us. My comrades... they went ahead to slay it, but none returned. The creature is too strong... please, if you can... help.'")

    print(
        "The soldier winces in pain, struggling to stay conscious. His hand clutches a deep wound in his side, the blood flowing freely.")

    # Present the player with the choice to help the soldier or leave him behind
    forest_choice()


def forest_choice():
    print("\nWhat will you do?")
    print("[1] Help the soldier.")
    print("[2] Leave the soldier and continue into the forest.")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        help_soldier()
    elif choice == "2":
        leave_soldier()
    else:
        print("Invalid choice. Try again.")
        forest_choice()


def help_soldier():
    # Reward player with XP and provide quest
    xp_gain = 100
    player['xp'] += xp_gain
    player['charisma'] += 2
    print(
        f"\nYou kneel down beside the soldier and do your best to tend to his wounds with the limited supplies you have. He winces, but seems grateful.")
    print(
        f"\nWounded Soldier: 'Thank you... I don’t know if I’ll make it, but you might stand a chance against the beast. Beware... it’s stronger than anything I’ve ever seen.'")
    print(f"\nYou have gained {xp_gain} XP for your efforts!")

    # Provide quest to defeat the beast
    print("The soldier tells you the direction where the beast is lurking, should you choose to confront it.")
    print("You have been given a new quest: Defeat the formidable beast that attacked the soldier and his comrades.")

    # Continue the story or quest based on the player's choice here
    quest_choice()


def leave_soldier():
    print("\nYou glance at the soldier, hearing his shallow breaths, but your decision is made.")
    input("\n[Press Enter to continue]")

    print(
        "Without a word, you walk away, leaving him to his fate. The forest grows eerily silent around you, the weight of your choice pressing in.")
    input("\n[Press Enter to continue]")
    beast_appears()
def beast_appears():
    print(
        "Suddenly, out of nowhere, a beast emerges from the underbrush, its eyes glowing with malice. You were unprepared, lacking the vital information the soldier could have provided.")
    print("The beast strikes, slashing at you before vanishing back into the shadows.")
    print("\nYou lose 5 XP from the unexpected attack!")
    player['xp'] -= 5  # Deduct 5 XP from the player for the attack
    print(f"Current XP: {player['xp']}")
    input("\n[Press Enter to continue]")

    print("The encounter has shaken you, but you press on. The path ahead splits once more.")

    print("\nWhat will you do next?")
    print("1. Delve deeper into the forest.")
    print("2. Seek the beast directly.")

    choice = input("What do you choose? (1/2): ")

    if choice == "1":
        deeper_forest()
    elif choice == "2":
        seek_the_beast()
    else:
        print("Invalid choice, please select 1 or 2.")
        leave_soldier()


def quest_choice():
    print("\nDo you wish to seek out the beast, or continue on your way?")
    print("[1] Seek out the beast.")
    print("[2] Continue your exploration.")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        seek_beast()
    elif choice == "2":
        deeper_forest()
    else:
        print("Invalid choice. Try again.")
        quest_choice()

def seek_the_beast():
    print("\nSteeling yourself, you decide to seek the beast directly, hoping to end its reign of terror.")
    print(
        "\nWith determination, you set your sights on the beast's lair. The forest around you feels alive, as if it is aware of your intent.")
    input("\n[Press Enter to continue]")
    encounter_beast()
def seek_beast():
    print(
        "\nYou follow the soldier's directions, venturing deeper into the forest. The air grows colder, and the trees seem to close in around you.")
    input("\n[Press Enter to continue]")
    encounter_beast()
def encounter_beast():
    print(
        "The forest becomes darker and more foreboding as you approach a cave with strange, ancient markings on its entrance. The faint sound of growling can be heard from within.")

    print(
        "\nAs you enter the cave, you see the beast's lair—dark and damp, with the remnants of previous battles scattered around. The growling grows louder, more intense.")
    print(
        "At the back of the cave, partially obscured by shadows, you see the beast. It is a formidable creature, towering and covered in thick, black fur. Its eyes glow with a fierce, malevolent light.")

    # Prompt the player for their approach to the battle
    battle_choice()


def battle_choice():
    print("\nWhat will you do?")
    print("[1] Approach the beast cautiously.")
    print("[2] Charge at the beast aggressively.")
    print("[3] Try to find a way to outsmart the beast from a distance.")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        approach_cautiously()
    elif choice == "2":
        charge_aggressively()
    elif choice == "3":
        outsmart_beast()
    else:
        print("Invalid choice. Try again.")
        battle_choice()


def approach_cautiously():
    print(
        "\nYou move carefully, keeping to the shadows and observing the beast’s movements. The creature seems to be less aware of your presence.")
    print(
        "You find a strategic position where you can attack from a distance. With a well-aimed shot or spell, you manage to strike the beast, causing it to roar in anger.")
    input("\nPress Enter to continue...")
    # Battle with the beast
    battle_with_beast()


def charge_aggressively():
    print(
        "\nYou decide to charge at the beast, weapon drawn. The beast roars and lunges at you, its massive claws swiping through the air.")
    print(
        "You engage in a fierce battle, dodging its attacks and striking back with all your might. The fight is brutal and intense, the cave echoing with the sounds of combat.")
    input("\nPress Enter to continue...")
    # Battle with the beast
    battle_with_beast()


def outsmart_beast():
    print(
        "\nYou attempt to outsmart the beast by using the environment to your advantage. You set traps and use the cave's layout to avoid direct confrontation.")
    print(
        "The beast is initially confused by your tactics, but it soon becomes enraged and more aggressive. You'll need to be quick and clever to succeed.")
    input("\nPress Enter to continue...")
    # Battle with the beast
    battle_with_beast()


def battle_with_beast():
    # Simulate the battle with the beast
    player_stat = player['strength']  # Replace 'stat' with the appropriate attribute representing player's combat skill
    beast_stat = 10

    # Battle outcome
    if player_stat >= beast_stat:
        print(
            "\nYou manage to defeat the beast after a grueling battle. Its body collapses, and the cave falls silent.")
        print("You have succeeded in your quest and can now return to the wounded soldier or continue your journey.")
        # Reward player with XP or items
        player['xp'] += 200
        print("You gain 200 XP for defeating the beast.")
        # Option to return to the soldier or continue exploring
        post_battle_choice()
    else:
        print(
            "\nDespite your best efforts, the beast overpowers you. You are forced to retreat, wounded and exhausted.")
        print(
            "You barely manage to escape the cave and find a safe place to rest. The quest remains unfinished, and the beast still lurks in the forest.")
        # Option to recover and attempt again or change direction
        recovery_choice()


def post_battle_choice():
    print("\nWhat would you like to do next?")
    print("[1] Return to the wounded soldier.")
    print("[2] Continue exploring the forest.")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        return_to_soldier()
    elif choice == "2":
        deeper_forest()
    else:
        print("Invalid choice. Try again.")
        post_battle_choice()


def return_to_soldier():
    print(
        "\nYou make your way back to the soldier, informing him of your victory. He thanks you with his last ounce of strength.")
    print("He gives you a token of gratitude, a small, valuable item from his supplies.")
    # Reward player with an item or additional XP
    player['xp'] += 1050
    print("You gain an additional 1050 XP for your dedication.")
    input("\nPress Enter to continue...")
    deeper_forest()
    # Option to continue the main quest or explore further


def recovery_choice():
    print("\nWhat will you do now?")
    print("1. Rest and recover, then attempt the quest again.")
    print("2. Leave the forest and seek other paths.")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        # Recover and retry
        print("\nYou take time to heal your wounds and regain your strength, preparing for another attempt.")
        # Reattempt the quest or return to where you left off
        seek_beast()
    elif choice == "2":
        # Leave forest and explore other paths
        print("\nYou decide to leave the forest behind, seeking new paths and adventures.")
        continue_road()
    else:
        print("Invalid choice. Try again.")
        recovery_choice()


def deeper_forest():
    print(
        "\nYou delve deeper into the forest, the dense canopy above casting eerie shadows. The air grows cooler, and the silence is occasionally broken by distant, unsettling sounds.")
    # Provide options for further exploration
    exploration_choice()


def exploration_choice():
    print("\nWhat will you do?")
    print("[1] Investigate a mysterious glow in the distance.")
    print("[2] Follow the sound of running water.")
    print("[3] Examine an ancient ruin partially hidden by foliage.")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        investigate_glow()
    elif choice == "2":
        follow_water()
    elif choice == "3":
        explore_ruins()
    else:
        print("Invalid choice. Try again.")
        exploration_choice()


def investigate_glow():
    print(
        "\nYou follow the mysterious glow through the underbrush, pushing aside branches and foliage. The light grows brighter, revealing an otherworldly, ethereal radiance emanating from a clearing.")
    print(
        "In the center of the clearing stands a majestic, ancient tree with glowing runes carved into its bark. The tree seems alive with magic, and a gentle hum fills the air.")

    # Interaction with the magical tree
    print("You can:")
    print("[1] Touch the tree and investigate the runes.")
    print("[2] Collect some of the glowing leaves.")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        touch_tree()
    elif choice == "2":
        collect_leaves()
    else:
        print("Invalid choice. Try again.")
        investigate_glow()


def touch_tree():
    print(
        "\nYou reach out and touch the tree, feeling a surge of magical energy flow through you. The runes on the tree begin to glow brighter, and a voice echoes in your mind, offering knowledge about the forest's secrets.")
    print(
        "You gain insight into hidden paths and ancient lore about the forest. This knowledge may aid you in future quests.")
    # Option to continue exploring or return to the main path
    post_interaction_choice()


def collect_leaves():
    print(
        "\nYou carefully gather some of the glowing leaves, which seem to pulse with a soft light. These leaves could have magical properties or be used as a valuable item.")
    print("You gain a special item: Glowing Leaves, which may have unique effects or be used in future quests.")
    # Option to continue exploring or return to the main path
    post_interaction_choice()


def follow_water():
    print(
        "\nYou follow the sound of running water through the forest, eventually arriving at a serene, crystal-clear stream. The water flows gently over smooth stones, and the surrounding area is peaceful and untouched.")
    print("Next to the stream, you find a hidden alcove with a small, ornate chest partially buried in the sand.")

    # Interaction with the chest
    print("You can:")
    print("[1] Open the chest and investigate its contents.")
    print("[2] Drink from the stream and rest.")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        open_chest()
    elif choice == "2":
        drink_stream()
    else:
        print("Invalid choice. Try again.")
        follow_water()


def open_chest():
    print(
        "\nYou carefully open the chest, revealing its contents: a collection of old, but valuable items including a few pieces of gold, a map with mysterious markings, and a potion of unknown origin.")
    print("You gain some gold and a mysterious map which may lead to hidden treasures or secrets.")
    # Option to continue exploring or return to the main path
    post_interaction_choice()


def drink_stream():
    print(
        "\nYou take a refreshing drink from the stream and rest for a while. The cool water revitalizes you, and you feel more energized for your journey ahead.")
    # Resting here can provide a temporary boost to the player's stats
    player['xp'] += 20
    print("You gain a small xp boost.")
    # Option to continue exploring or return to the main path
    post_interaction_choice()


def explore_ruins():
    print(
        "\nYou make your way to the ancient ruin, the crumbling stone walls covered in moss and ivy. The ruins are shrouded in mystery, and the air is thick with a sense of forgotten history.")
    print("Among the ruins, you discover a hidden chamber with strange symbols and relics from a bygone era.")

    # Interaction with the relics
    print("You can:")
    print("[1] Examine the symbols and attempt to decipher their meaning.")
    print("[2] Search the chamber for any hidden artifacts.")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        examine_symbols()
    elif choice == "2":
        search_artifacts()
    else:
        print("Invalid choice. Try again.")
        explore_ruins()


def examine_symbols():
    print(
        "\nYou study the symbols on the walls, and through careful observation and intuition, you manage to decipher some of their meanings. The symbols speak of ancient magic and forgotten rituals.")
    print("You gain knowledge about ancient magic, which might be useful in future encounters or quests.")
    # Option to continue exploring or return to the main path
    post_interaction_choice()


def search_artifacts():
    print(
        "\nYou search the chamber and find several ancient artifacts, including a scroll with magical inscriptions and a rare gem.")
    player['xp'] += 150
    print("You gain a scroll that could be used to learn new spells or abilities and a rare gem that might be of value.")


    # Option to continue exploring or return to the main path
    post_interaction_choice()


def post_interaction_choice():
    print("\nWhat would you like to do next?")
    print("[1] Continue exploring the forest.")
    print("[2] Return to the main path.")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        deeper_forest()
    elif choice == "2":
        # Option to leave the forest or continue with another aspect of the main quest
        main_path()
    else:
        print("Invalid choice. Try again.")
        post_interaction_choice()


def main_path():
    print("\nYou decide to return to the main path, leaving the forest’s mysteries behind for now. The road ahead is filled with new possibilities and adventures.")
    input("\nPress Enter to continue...")
    continue_road()


def visit_inn():
    print("\nYou enter the inn, a warm and bustling place filled with laughter and the clinking of mugs.")
    print("The air is thick with the smell of roasted meat and ale. You notice a group of travelers huddled in a corner.")
    print("One of them looks particularly suspicious, eyeing everyone around them.")
    print("[1] Talk to the suspicious traveler.")
    print("[2] Avoid them and get a drink.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        talk_to_suspicious_traveler()
    elif choice == "2":
        get_drink()
    else:
        print("Invalid choice, please select 1 or 2.")
        visit_inn()

def talk_to_suspicious_traveler():
    print("\nYou approach the suspicious traveler. They seem nervous but try to hide it behind a forced smile.")
    print("Traveler: 'Good evening! What brings you here?'")
    print("[1] Ask them about their strange behavior.")
    print("[2] Accuse them of being up to no good.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        investigate_traveler()
    elif choice == "2":
        bar_fight()
    else:
        print("Invalid choice, please select 1 or 2.")
        talk_to_suspicious_traveler()

def investigate_traveler():
    print("\nYou ask the traveler about their odd behavior. They start sweating and seem increasingly uncomfortable.")
    print("Traveler: 'I... I'm just a simple wanderer. Please, leave me be.'")
    print("As you press further, they suddenly stand up and try to flee.")
    print("[1] Stop them from leaving.")
    print("[2] Let them go and return to your seat.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        bar_fight()
    elif choice == "2":
        print("\nYou decide to let the traveler go. They slip out of the inn, leaving a sense of unease behind.")
        print("You return to your seat and enjoy the rest of your evening.")
        input("\nPress Enter to continue.")
    else:
        print("Invalid choice, please select 1 or 2.")
        investigate_traveler()

def get_drink():
    print("\nYou walk up to the bar and order a drink. The bartender hands you a mug of frothy ale.")
    print("You find a seat and relax, enjoying the atmosphere. After a while, you overhear some locals talking about recent troubles in the area.")
    print("[1] Eavesdrop more on the conversation.")
    print("[2] Finish your drink and leave the inn.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        gather_information()
    elif choice == "2":
        print("\nYou finish your drink and leave the inn, heading back to your journey.")
        input("\nPress Enter to continue.")
        speak_blacksmith2()
    else:
        print("Invalid choice, please select 1 or 2.")
        get_drink()


def gather_information():
    print("\nYou find a quiet corner in the inn and begin to eavesdrop on the travelers.")
    print("As the murmur of conversations fills the room, you catch fragments of interesting gossip.")
    print(
        "One group is talking about recent attacks near the Mountain of Echoes, while another mentions a mysterious figure in The Village of Sarth.")

    print("\nWhat do you do?")
    print("[1] Focus on the conversation about the attacks near the Mountain of Echoes.")
    print("[2] Listen closer to the discussion about the mysterious figure in The Village of Sarth.")
    print("[3] Pretend you didn’t hear anything and move on.")

    choice = input("\nChoose your action (1/2/3): ")

    if choice == "1":
        print("\nYou lean in closer to hear more about the Mountain of Echoes...")
        input("\nPress Enter to continue.")
        print(
            "The travelers mention that the attacks have been growing more frequent, and that they seem to be coming from some sort of strange beast.")
        print("Rumors suggest that only someone with great strength can withstand the creature’s attacks.")
        input("\nPress Enter to continue.")
        print("You gain valuable information about the dangers near the Mountain of Echoes.")
        reward_xp(50)  # Reward XP for gathering useful information
        print(f"{player['name']} gains 50 XP!")
        speak_blacksmith2()
    elif choice == "2":
        print("\nYou listen carefully to the group discussing The Village of Sarth...")
        input("\nPress Enter to continue.")
        print( "They mention a shadowy figure who’s been seen moving through the village at night, speaking with local criminals and stirring unrest.")
        print("It’s unclear what their motives are, but the group suspects something sinister is at play.")
        input("\nPress Enter to continue.")
        print("You gain valuable information about a potential threat in The Village of Sarth.")
        reward_xp(50)  # Reward XP for gathering useful information
        print(f"{player['name']} gains 50 XP!")
        speak_blacksmith2()
    elif choice == "3":
        print("\nYou decide it's best not to get involved and move on.")
        input("\nPress Enter to continue.")
        speak_blacksmith2()
    else:
        print("\nInvalid choice, please select 1, 2, or 3.")
        gather_information()


def bar_fight():
    print("\nA scuffle breaks out as the suspicious traveler draws a knife and attacks you!")
    print("The bar erupts into chaos. Patrons scatter, and furniture is overturned.")
    print("You have to make quick decisions to win this fight.")

    # Choices based on player attributes
    if player['strength'] >= 10:
        print("\n1. Use your strength to overpower the traveler.")
    else:
        print("\n1. Try to use your strength to overpower the traveler (requires Strength 10).")

    if player['agility'] >= 7:
        print("2. Dodge and counterattack with agility.")
    else:
        print("2. Try to dodge and counterattack (requires Agility 7).")

    if player['magic'] >= 5:
        print("3. Use a magical spell to disarm the traveler.")
    else:
        print("3. Try to use magic to disarm the traveler (requires Magic 5).")

    print("4. Attempt to disarm the traveler without using attributes.")

    choice = input("What do you do? (1/2/3/4): ")

    if choice == "1":
        if player['strength'] >= 10:
            win_fight()
        else:
            lose_fight()
    elif choice == "2":
        if player['agility'] >= 7:
            win_fight()
        else:
            lose_fight()
    elif choice == "3":
        if player['magic'] >= 5:
            win_fight()
        else:
            lose_fight()
    elif choice == "4":
        lose_fight()
    else:
        print("Invalid choice, please select 1, 2, 3, or 4.")
        bar_fight()


def win_fight():
    print(
        "\nWith a decisive move, you subdue the traveler. The fight ends, and the innkeeper thanks you for your help.")
    print("You gain 200 XP for your victory.")
    reward_xp(200)  # Reward 100 XP for winning the fight
    print(f"{player['name']} gains 200 XP!")
    input("\nPress Enter to continue.")
    chase_sequence()


def lose_fight():
    print("\nYou struggle against the traveler, and despite your best efforts, they manage to escape.")
    print(
        "The traveler flees into the night, leaving you with a sense of frustration and a warning from the innkeeper.")
    print("You lose 10 XP for failing to stop the traveler.")
    reward_xp(-10)  # Penalize 10 XP for losing the fight
    print(f"{player['name']} loses 10 XP.")
    input("\nPress Enter to continue.")
    chase_sequence()


def chase_sequence():
    print(
        "\nAs you leave the inn, you hear the sound of local guards approaching. They have been alerted by the commotion.")
    print("You need to out-run them before they catch up with you!")

    # Choices for the chase sequence
    if player['agility'] >= 8:
        print("\n[1] Use your agility to quickly escape through a narrow alley.")
    else:
        print("\n[1] Try to escape through a narrow alley (requires Agility 8).")

    if player['strength'] >= 6:
        print("[2] Find a way to barricade a path and slow the guards down.")
    else:
        print("[2] Try to barricade a path (requires Strength 6).")

    if player['magic'] >= 4:
        print("[3] Use a magical spell to create an illusion and mislead the guards.")
    else:
        print("[3] Try to use magic to mislead the guards (requires Magic 4).")

    print("[4] Attempt to blend in with the crowd and hope the guards don’t notice you.")

    choice = input("What do you do? (1/2/3/4): ")

    if choice == "1":
        if player['agility'] >= 8:
            escape_success()
        else:
            escape_fail()
    elif choice == "2":
        if player['strength'] >= 6:
            escape_success()
        else:
            escape_fail()
    elif choice == "3":
        if player['magic'] >= 4:
            escape_success()
        else:
            escape_fail()
    elif choice == "4":
        escape_fail()
    else:
        print("Invalid choice, please select 1, 2, 3, or 4.")
        chase_sequence()


def escape_success():
    print("\nYou successfully out-run the guards and make your way out of town without further trouble.")
    print("You gain 50 XP for your clever escape.")
    reward_xp(550)  # Reward 50 XP for a successful escape````````````````````````````````
    print(f"{player['name']} gains 550 XP!")
    input("\nPress Enter to continue.")
    leave_village_no_info()

def escape_fail():
    print("\nThe guards spot you as you attempt to flee. They manage to catch up and detain you.")
    print("You are given a warning and are forced to leave town immediately.")
    print("You lose 20 XP for failing to escape.")
    reward_xp(-10)  # Penalize 20 XP for failing to escape
    print(f"{player['name']} loses 10 XP.")
    input("\nPress Enter to continue.")
    leave_village_no_info()
def speak_blacksmith2():
    print('\nYou return back outside to the blacksmith, who greets you with a nod.')
    print("[1] Buy the sword (Agility required).")
    print("[2] Decline and leave the village.")
    print("[3] Ask the blacksmith for information about recent events.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        buy_sword2()
    elif choice == "2":
        decline_sword()
    elif choice == "3":
        ask_information()
    else:
        print("Invalid choice, please select 1, 2, or 3.")
        speak_blacksmith2()

def buy_sword2():
    print('The blacksmith explains that your late arrival the sword had actually been sold to another traveler.')
    print("He offers you a different weapon instead.")
    print("[1] Accept the new weapon.")
    print("[2] Decline and leave the village.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        accept_weapon()
    elif choice == "2":
        decline_sword()
    else:
        print("Invalid choice, please select 1 or 2.")
        buy_sword2()

def accept_weapon():
    print("You accept the blacksmith's offer and receive a new weapon. It may not be as powerful as the magical sword, but it will serve you well.")
    reward_xp(250)  # Reward 50 XP for accepting the weapon
    print(f"{player['name']} gains 250 XP!")
    input("\nPress Enter to continue...")
    leave_village_no_info()
def speak_blacksmith():
    print(
        "\nYou enter the blacksmith's shop, where the air is filled with the clanging of metal and the smell of molten iron. The blacksmith, a burly man with a friendly demeanor, greets you with a nod.")
    input("\nPress Enter to continue...")

    print(
        "\nThe blacksmith says, 'Welcome, traveler. I have a fine magical sword for sale, but it requires a certain level of agility to wield effectively. Interested?'")
    print("[1] Buy the sword (Agility 7 required).")
    print("[2] Decline and leave the village.")
    print("[3] Ask the blacksmith for information about recent events.")
    print("[4] Go back and enter the inn.")

    choice = input("What do you do? (1/2/3/4): ")

    if choice == "1":
        buy_sword()
    elif choice == "2":
        decline_sword()
    elif choice == "3":
        ask_information()
    elif choice == "4":
        enter_inn()
    else:
        print("Invalid choice, please select 1, 2, 3, or 4.")
        speak_blacksmith()


def buy_sword():
    print(
        "\nYou express your interest in buying the sword. The blacksmith shows you a gleaming blade with intricate runes etched into the hilt.")
    input("\nPress Enter to continue...")

    if player['agility'] >= 7:
        print("You purchase the sword of mael!, which greatly enhances your agility.")
        player['agility'] += 5  # Increase agility as a reward for buying the sword
        reward_xp(170)  # Reward 170 XP for buying the sword
        print(f"{player['name']} gains 170 XP!")
        print("With your new weapon, you feel more confident and prepared.")
    else:
        print(
            "You attempt to buy the sword, but the blacksmith notices that you lack the agility to handle it properly.")
        print("He politely declines to sell it to you, but he offers you some advice.")
        print(
            "'Be careful in your travels,' he says. 'The roads are dangerous, and there are rumors of a great threat in the kingdom.'")

    input("\nPress Enter to continue...")
    leave_village_no_info()


def decline_sword():
    print(
        "\nYou thank the blacksmith and decline the offer. As you leave the shop, you hear the blacksmith's voice calling after you.")
    input("\nPress Enter to continue...")

    print(
        "'Even if you don't need the sword now, keep your wits about you. The kingdom has its troubles, and it's always good to be prepared.'")
    input("\nPress Enter to continue...")
    speak_blacksmith2()


def ask_information():
    print("\nYou ask the blacksmith about recent events. He wipes his hands on his apron and begins to speak.")
    input("\nPress Enter to continue...")

    print(
        "'There have been strange happenings lately,' he says. 'Some say a great threat looms over the kingdom. Many brave souls have gone to investigate, but few return.'")
    print(
        "He pauses and looks at you with a knowing glance. 'I wouldn't be surprised if this is a problem for the king himself.'")

    input("\nPress Enter to continue...")
    speak_blacksmith2()


def enter_inn():
    print(
        "\nYou decide to go back and enter the inn. The innkeeper greets you warmly as you step inside. The inn is bustling with activity, and you find a cozy corner to relax.")
    input("\nPress Enter to continue...")
    visit_inn()
