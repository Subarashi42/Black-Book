from Wallechia import proceed_to_wallechia
from character_creation import player
from dragon_keep import journey_to_dragons_keep
from temple_of_forgotten import journey_to_temple_of_forgotten
from travel_menu import travel_menu, player_destination
from village_sarth import journey_to_village_of_sarth


def leave_village_no_info():
    print("\nYou decide to leave the village, still in the dark about the rumors circulating.")
    print(
        "But the air is thick with tension, and whispers of a growing threat to the kingdom of Wallechia fill the streets.")
    print("You overhear travelers and villagers speaking in hushed tones about disturbances in distant lands.")
    print("\nDriven by curiosity, you feel compelled to learn more about the growing danger.")
    print("Perhaps the road ahead holds the answers you seek.")
    input("\nPress Enter to continue.")

    # Present the travel menu for exploration
    travel_menu()


# Global variable to track the player's chosen destination



# Travel menu where the player picks a destination
# Leads to the lieutenant encounter


# Continue journey after the lieutenant encounter
def continue_journey():
    if player_destination == "dragons_keep":
        journey_to_dragons_keep()
    elif player_destination == "mountain_of_echoes":
        journey_to_mountain_of_echoes()
    elif player_destination == "village_of_sarth":
        journey_to_village_of_sarth()
    elif player_destination == "temple_of_forgotten":
        journey_to_temple_of_forgotten()
    elif player_destination == "wallechia":
        proceed_to_wallechia()


# Specific journey functions for each destination


def journey_to_mountain_of_echoes():
    print("\nYou climb the winding path toward the Mountain of Echoes, where every sound is magnified.")
    print("The wind howls, and your footsteps echo eerily through the mountain range.")
    input("\nPress Enter to continue your journey to the Mountain of Echoes.")
    journey_to_mountain_of_echoes2()


def journey_to_mountain_of_echoes2():
    print("\nYou approach the Mountain of Echoes, its towering peaks shrouded in mist. The air is thick with tension.")
    print(
        "As you ascend, the echoing winds carry whispers of an ancient conflict. The mountain is not as serene as it seems.")

    input("\nPress Enter to continue...")
    moutain_of_echoes_encounter()
    # Initial interaction and exploration


def moutain_of_echoes_encounter():
    print(
        "\nUpon reaching a small base camp, you encounter three figures: a weary ranger, a nervous merchant, and a stoic soldier.")
    print(
        "They seem to be dealing with various issues related to the mountain. You have a few options on how to proceed:")
    print("1. Speak with the ranger about the disturbances on the mountain.")
    print("2. Talk to the merchant about what they are selling.")
    print("3. Approach the soldier to learn about any recent conflicts.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        ranger_interaction()
    elif choice == "2":
        print("\nThe merchant eyes you warily as you approach.")
        print("The merchant seems hesitant to speak with you as he doesn't trust you.")
        print("He advises you to assist the soldier first before he can trust you.")
        input("\n[Press Enter to continue]")
        moutain_of_echoes_encounter()
    elif choice == "3":
        soldier_interaction()
    else:
        print("Invalid choice, please select 1, 2, or 3.")
        moutain_of_echoes_encounter()


def ranger_interaction():
    print(
        "\nThe ranger introduces himself as Eirik and explains that he's searching for a formidable beast in these mountains.")
    print("He offers to team up with you if you're willing to help.")

    print("\n1. Agree to help Eirik with his quest.")
    print("2. Decline and explore the mountain on your own.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        help_ranger()
    elif choice == "2":
        explore_on_own()
    else:
        print("Invalid choice, please select 1 or 2.")
        ranger_interaction()


def explore_on_own():
    print("\nYou decide to explore the treacherous paths of the Mountain of Echoes on your own.")
    print(
        "The air grows colder, and the mist thickens as you venture deeper into the mountain. Strange noises echo all around you.")

    print(
        "\nSuddenly, you hear the sound of heavy footsteps approaching. A group of mountain trolls emerges from the fog, blocking your path.")
    print("1. Engage the trolls in a fierce battle head-on. (Strength required: 10)")
    print("2. Attempt to outmaneuver them and flee into the shadows. (Agility required: 10)")
    print("3. Use your magic to cast a powerful spell to distract or disable them. (Magic required: 9)")

    choice = input("\nWhat do you do? (1/2/3): ")

    if choice == "1" and player['strength'] >= 10:
        print(
            "\nYou charge at the trolls, swinging your weapon with all your might. After a grueling fight, you manage to overpower them!")
        reward_xp(950)
        print("You gain 950 XP for defeating the trolls!")
        next_encounter()
    elif choice == "1":
        print("\nYour strength isn’t enough. The trolls overpower you, and you barely escape with your life.")
        print("- You lose 10 XP for the failed battle.")
        player['xp'] -= 10
        retreat_to_base_camp()

    elif choice == "2" and player['agility'] >= 10:
        print(
            "\nYou swiftly dodge the trolls' attacks, slipping through their defenses and disappearing into the shadows.")
        reward_xp(900)
        print("You gain 900 XP for evading the trolls!")
        next_encounter()
    elif choice == "2":
        print(
            "\nYou try to flee, but the trolls are too fast, catching you off guard. You manage to escape but are wounded.")
        print("- You lose 5 XP for the failed escape.")
        player['xp'] -= 5
        retreat_to_base_camp()

    elif choice == "3" and player['magic'] >= 9:
        print("\nYou conjure an illusion spell, confusing the trolls long enough for you to slip past them.")
        reward_xp(950)
        print("You gain 950 XP for outwitting the trolls!")
        next_encounter()
    elif choice == "3":
        print(
            "\nYour spell fizzles out, leaving you vulnerable. The trolls attack, and you barely escape with a few injuries.")
        print("- You lose 8 XP for the failed spell.")
        player['xp'] -= 8
        retreat_to_base_camp()

    else:
        print("\nInvalid choice or insufficient attributes. You hesitate, and the trolls attack!")
        print("- You lose 10 XP and are forced to retreat.")
        player['xp'] -= 10
        retreat_to_base_camp()


def next_encounter():
    print(
        "\nAfter dealing with the trolls, you push forward, determined to uncover the secrets of the Mountain of Echoes.")
    print(
        "The path becomes steeper and narrower. As you move cautiously, you sense something watching you from the shadows.")

    print("\nSuddenly, a ferocious beast leaps out from behind the rocks!")
    print(
        "This is no ordinary creature; its eyes glow with a malevolent light, and its claws seem to shimmer with dark energy.")

    print("\n1. Stand your ground and engage the beast in direct combat. (Strength required: 18)")
    print("2. Use the environment to your advantage, setting a trap. (Agility required: 16)")
    print("3. Cast a binding spell to immobilize the beast. (Magic required: 17)")

    choice = input("\nWhat do you do? (1/2/3): ")

    if choice == "1" and player['strength'] >= 18:
        print("\nYou brace yourself and meet the beast’s charge head-on. With immense effort, you bring it down!")
        reward_xp(1200)
        print("You gain 1200 XP for defeating the beast!")
        find_treasure()
    elif choice == "1":
        print(
            "\nThe beast is too strong, and you are overwhelmed. You barely escape with your life, injured but alive.")
        print("- You lose 12 XP for the failed battle.")
        player['xp'] -= 12
        retreat_to_base_camp()

    elif choice == "2" and player['agility'] >= 16:
        print(
            "\nYou use your surroundings cleverly, leading the beast into a trap. It snarls as it becomes trapped, allowing you to escape.")
        reward_xp(1150)
        print("You gain 1150 XP for outwitting the beast!")
        find_treasure()
    elif choice == "2":
        print("\nYour attempt to set a trap fails. The beast is faster than you expected, and you barely escape.")
        print("- You lose 10 XP for the failed escape.")
        player['xp'] -= 10
        retreat_to_base_camp()

    elif choice == "3" and player['magic'] >= 17:
        print(
            "\nYou quickly cast a binding spell, wrapping the beast in magical chains. It struggles, but you hold it long enough to escape.")
        reward_xp(1200)
        print("You gain 1200 XP for using your magic!")
        find_treasure()
    elif choice == "3":
        print(
            "\nYour spell flickers out before you can bind the beast, and it lunges at you. You narrowly escape, but not without injury.")
        print("- You lose 8 XP for the failed spell.")
        player['xp'] -= 8
        retreat_to_base_camp()

    else:
        print("\nInvalid choice or insufficient attributes. The beast attacks ferociously!")
        print("- You lose 12 XP and are forced to retreat.")
        player['xp'] -= 12
        retreat_to_base_camp()


def retreat_to_base_camp():
    print("\nYou retreat back to the base camp, nursing your wounds and catching your breath.")
    print("The beast’s roars echo through the mountain, a reminder of the dangers that lurk in the shadows.")
    print("You decide to rest and recover before deciding your next move.")
    input("\n[Press Enter to continue]")
    moutain_of_echoes_encounter()


def find_treasure():
    print(
        "\nAs you catch your breath, you notice something glittering nearby. Upon closer inspection, you find a hidden cache of treasures left behind by previous adventurers.")
    print("You gain a rare item and an additional 100 XP!")
    reward_xp(100)
    player['inventory'].append("Rare Item")  # You can later define what kind of item it is.
    print("You return to the base camp with the knowledge of your success.")
    return_to_base_camp()


def return_to_base_camp():
    print(
        "\nYou make your way back to the base camp, exhausted but victorious. As you approach, a strange silence fills the air.")
    print(
        "The campfire is still burning, but something is wrong... both the ranger and the soldier are nowhere to be seen.")
    print("The only one remaining is the merchant, who sits quietly, looking uneasy.")

    print(
        "\nMerchant: 'You're back... but the others... they disappeared. I haven't seen them since you left. I don't know what's going on, but something terrible must've happened.'")

    print("You can now:")
    print("1. Question the merchant about what happened.")
    print("2. Inspect the camp for clues.")
    print("3. Prepare to leave the mountain.")

    choice = input("\nWhat will you do? (1/2/3): ")

    if choice == "1":
        question_merchant()
    elif choice == "2":
        inspect_camp()
    elif choice == "3":
        prepare_to_leave()
    else:
        print("Invalid choice, please select 1, 2, or 3.")
        return_to_base_camp()


def question_merchant():
    print("\nYou approach the merchant and ask what he saw.")
    print(
        "Merchant: 'I heard some noises in the night, strange ones. I thought the ranger and the soldier went to check it out, but they never came back.'")
    print(
        "Merchant: 'I didn't dare follow them, not in this cursed place. I swear, this mountain has eyes... watching, waiting.'")
    print("You feel a chill run down your spine as you realize something darker might be at play here.")
    print("You decide it's best to keep moving before whatever took them returns.")

    proceed_to_next_stage()


def inspect_camp():
    print("\nYou carefully search the camp for any signs of the ranger and the soldier.")
    print("You find the ranger's bow, discarded hastily, and a few footprints leading away into the wilderness.")
    print("The soldier’s sword, however, is missing altogether. You find no other clues, just an eerie silence.")
    print("With the unsettling realization that they might not have simply left, you decide it’s best to press on.")
    input("\n[Press Enter to continue]")
    proceed_to_next_stage()


def prepare_to_leave():
    print(
        "\nYou decide not to waste any more time and gather your belongings. The longer you stay, the more dangerous the mountain seems to become.")
    print(
        "The merchant eyes you nervously as you prepare to leave, clearly too afraid to say more about what’s happened.")
    input("\n[Press Enter to continue]")
    proceed_to_next_stage()


def proceed_to_next_stage():
    print("\nYou take one last look at the deserted camp before turning your back to it.")
    print(
        "The ranger and the soldier are gone, and you have no time to search further if you wish to survive the Mountain of Echoes.")
    print("The merchant follows quietly, a shadow of fear on his face as he too senses the danger that lurks.")
    print("\nYou continue your journey, but the mystery of their disappearance weighs heavily on your mind.")
    reward_xp(50)
    print("You gain 50 XP for surviving this unsettling encounter.")


def help_ranger():
    print(
        "\nEirik leads you deeper into the mountain, explaining that the beast has been terrorizing the local wildlife and villagers.")
    print("You encounter a group of bandits along the way.")

    print("\n1. Fight the bandits.")
    print("2. Attempt to negotiate with the bandits.(Charisma required)")
    print("3. Avoid the bandits and continue with Eirik.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        bandit_encounter()
    elif choice == "2":
        negotiate_bandits()
    elif choice == "3":
        avoid_bandits()
    else:
        print("Invalid choice, please select 1, 2, or 3.")
        help_ranger()


def bandit_encounter():
    print("\nYou decide to fight the bandits. It’s a tough battle, but you manage to defeat them.")
    reward_xp(150)  # Reward XP for defeating bandits
    print("Eirik thanks you for your bravery and you continue the journey.")
    print("You and Eirik press on, determined to find the beast terrorizing the mountain.")
    print("You gain 150 XP for your efforts.")
    input("\n[Press Enter to continue]")
    find_beast()


def negotiate_bandits():
    print("\nYou try to negotiate with the bandits. They seem open to the idea, but require something in return.")
    print("You must decide if you have enough Charisma to sway them.")

    if player['charisma'] >= 7:
        print("\nYour negotiation skills pay off. The bandits let you pass and you avoid a fight.")
        reward_xp(230)  # Reward XP for successful negotiation
        print("Eirik is impressed with your skills and you continue the journey.")
        find_beast()
    else:
        print("\nThe bandits are not convinced and attack you.")
        bandit_encounter()


def avoid_bandits():
    print("\nYou decide to avoid the bandits. While you don't engage them directly, it slows you down.")
    print("You lose some time but eventually catch up with Eirik.")
    reward_xp(120)  # Reward XP for avoiding bandits
    print("Eirik is relieved and you continue the journey.")
    input("\n[Press Enter to continue]")
    find_beast()


def find_beast():
    print("\nYou and Eirik finally track down the beast to a dark cave.")
    print("The cave is eerie, with strange noises echoing around.")

    print("\n1. Enter the cave cautiously.")
    print("2. Prepare for battle outside the cave.")
    print("3. Look for an alternate way into the cave.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        enter_cave()
    elif choice == "2":
        prepare_battle()
    elif choice == "3":
        find_alternate_path()
    else:
        print("Invalid choice, please select 1, 2, or 3.")
        find_beast()


def enter_cave():
    print("\nYou enter the cave cautiously. The beast is waiting for you inside.")
    print("You must use your attributes to defeat the beast.")

    print("\n1. Use Strength to overpower the beast.")
    print("2. Use Agility to dodge the beast’s attacks.")
    print("3. Use Magic to cast a spell and defeat the beast.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1" and player['strength'] >= 8:
        print("\nYou use your strength to overpower the beast. It’s a fierce fight, but you emerge victorious.")
        reward_xp(300)  # Reward XP for defeating the beast
    elif choice == "2" and player['agility'] >= 8:
        print(
            "\nYou use your agility to dodge the beast’s attacks and strike when the moment is right. The beast falls.")
        reward_xp(300)  # Reward XP for defeating the beast
    elif choice == "3" and player['magic'] >= 8:
        print("\nYou use your magic to cast a powerful spell. The beast is overwhelmed and defeated.")
        reward_xp(300)  # Reward XP for defeating the beast
    else:
        print("\nYour attempt to defeat the beast fails. You retreat and Eirik decides to help.")
        print("Eirik uses his skills to defeat the beast. You gain partial XP for your effort.")
        reward_xp(150)  # Partial XP for effort

    print("Eirik thanks you for your help and you both head back down the mountains base camp.")
    mountain_base_camp_soldier_missing()


def prepare_battle():
    print("\nYou prepare for battle outside the cave. The beast eventually emerges and you face it.")
    print("You must use your attributes to defeat the beast.")

    print("\n1. Use Strength to overpower the beast.")
    print("2. Use Agility to dodge the beast’s attacks.")
    print("3. Use Magic to cast a spell and defeat the beast.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1" and player['strength'] >= 8:
        print("\nYou use your strength to overpower the beast. It’s a fierce fight, but you emerge victorious.")
        reward_xp(100)  # Reward XP for defeating the beast
    elif choice == "2" and player['agility'] >= 8:
        print(
            "\nYou use your agility to dodge the beast’s attacks and strike when the moment is right. The beast falls.")
        reward_xp(100)  # Reward XP for defeating the beast
    elif choice == "3" and player['magic'] >= 8:
        print("\nYou use your magic to cast a powerful spell. The beast is overwhelmed and defeated.")
        reward_xp(100)  # Reward XP for defeating the beast
    else:
        print("\nYour attempt to defeat the beast fails. You retreat and Eirik decides to help.")
        print("Eirik uses his skills to defeat the beast. You gain partial XP for your effort.")
        reward_xp(50)  # Partial XP for effort

    print("Eirik thanks you for your help and you both head back down the mountain base camp.")
    mountain_base_camp_soldier_missing()


def find_alternate_path():
    print("\nYou search for an alternate way into the cave and find a narrow tunnel.")
    print("It’s dark and treacherous, but it leads to a different part of the cave.")

    print("\n1. Continue through the tunnel.")
    print("2. Go back and try another approach.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        print("\nYou continue through the tunnel and find the beast unprepared.")
        print("You must use your attributes to defeat the beast.")

        print("\n1. Use Strength to overpower the beast.")
        print("2. Use Agility to dodge the beast’s attacks.")
        print("3. Use Magic to cast a spell and defeat the beast.")

        choice = input("What do you do? (1/2/3): ")

        if choice == "1" and player['strength'] >= 10:
            print("\nYou use your strength to overpower the beast. It’s a fierce fight, but you emerge victorious.")
            reward_xp(350)  # Reward XP for defeating the beast
        elif choice == "2" and player['agility'] >= 10:
            print(
                "\nYou use your agility to dodge the beast’s attacks and strike when the moment is right. The beast falls.")
            reward_xp(350)  # Reward XP for defeating the beast
        elif choice == "3" and player['magic'] >= 10:
            print("\nYou use your magic to cast a powerful spell. The beast is overwhelmed and defeated.")
            reward_xp(350)  # Reward XP for defeating the beast
        else:
            print("\nYour attempt to defeat the beast fails. Due to being unprepared")
            print("You and Eirik are forced to retreat, wounded and bleeding you sit aside the cave entrance.")
            print("Eirik uses his skills to defeat the beast. You gain partial XP for your effort.")
            reward_xp(50)  # Partial XP for effort

        print("Eirik thanks you for your help and you both head back down the mountain base.")
        mountain_base_camp_soldier_missing()
    elif choice == "2":
        find_beast()
    else:
        print("Invalid choice, please select 1 or 2.")
        find_alternate_path()


def mountain_base_camp_soldier_missing():
    print("\nYou return to the base camp, but the soldier is gone.")
    print("Pieces of his armor are scattered on the ground, with bloodstains leading away into the woods.")
    print("His sword lies broken nearby, and it’s clear something terrible happened.")

    print("\nThe merchant remains at the camp, offering his goods as if nothing has changed.")
    input("\n[Press Enter to continue]")
    merchant_interaction()


def mountain_base_camp_ranger_missing():
    print("\nYou return to the base camp, but something feels off.")
    print("The ranger, who had been with you earlier, is nowhere to be found.")
    print("Upon closer inspection, you notice signs of a struggle. It seems the ranger met a grim fate.")
    print("\nThe merchant is still here, though. You can talk to the merchant for any goods or information.")
    input("\n[Press Enter to continue]")
    merchant_interaction()


def merchant_interaction():
    print("\nYou approach the merchant, who is setting up a stall with various goods.")
    print(
        "Merchant: 'I have items that might be of interest to adventurers like you. Some of them are rare and valuable.'")
    print("1. Browse the merchant’s goods.")
    print("2. Ask the merchant if they know anything about recent events on the mountain.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        print(
            "\nYou browse through the goods and find a magical map that shows hidden paths on the mountain. It costs 50 gold.")
        print("1. Buy the magical map.")
        print("2. Decline and move on.")

        choice = input("What do you do? (1/2): ")

        if choice == "1":
            print("\nYou purchase the map, gaining a new advantage in navigating the mountain’s hidden paths.")
            print("This map also reveals shortcuts that save time and help you avoid dangers, granting you 30 XP.")
            input("\nPress Enter to continue...")
            inspect_camp()
        elif choice == "2":
            print("\nYou decide not to buy the map and continue your journey.")
            input("\nPress Enter to continue...")
            inspect_camp()
        else:
            print("Invalid choice, please select 1 or 2.")
            merchant_interaction()
    elif choice == "2":
        print(
            "\nThe merchant shares that there have been increased reports of attacks and disappearances, particularly near the mountain’s summit.")
        input("\nPress Enter to continue...")
        inspect_camp()
    else:
        print("Invalid choice, please select 1 or 2.")
        merchant_interaction()


def soldier_interaction():
    print("\nAs you explore the rugged terrain of the Mountain of Echoes, you come across a weary soldier.")
    print("His armor is dented, and his face is etched with worry. He seems to be searching for something.")

    if player['location'] == 'Apixoria':
        print("\nThe soldier looks up, recognizing your background.")
        print(
            "‘Ah, a fellow Apixorian!’ he says. ‘The king of Apixoria has been slain by a dark knight. The kingdom is in turmoil.’")
    else:
        print("\nThe soldier greets you with a nod.")
        print(
            "‘Greetings, traveler. I am a soldier from Apixoria. The king has been slain by a dark knight, and the kingdom is in disarray.’")

    print("\nThe soldier offers you two choices:")
    print("1. Ask about the ancient ruins.")
    print("2. Offer to help deal with the insurgents.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        ask_about_ancient_ruins()
    elif choice == "2":
        offer_help_with_insurgents()
    else:
        print("Invalid choice, please select 1 or 2.")
        soldier_interaction()


def ask_about_ancient_ruins():
    print("\nYou ask the soldier about the ancient ruins in the mountains.")

    if player["location"] == "Apixori":
        print(
            'The soldier eyes you for a moment, then sighs. "Since you’re from Apixori, I guess I can trust you with this," he says.')
        print(
            '"The ruins are said to hold ancient powers, but they’re dangerous. Many have entered and never returned."')
        print('"I wouldn’t go looking for them unless you’re ready for a real challenge."')
        reward_xp(150)  # Reward XP for gaining the information
        print("You have gained some valuable knowledge about the ancient ruins.")
        print(f"{player['name']} gains 150 XP!")
        input("\n[Press Enter to continue]")
        print("\nThe soldier offers you two choices:")
        print("1. Ask about the ancient ruins.")
        print("2. Offer to help deal with the insurgents.")

        choice = input("What do you do? (1/2): ")

        if choice == "1":
            ask_about_ancient_ruins()
        elif choice == "2":
            offer_help_with_insurgents()
        else:
            print("Invalid choice, please select 1 or 2.")
            soldier_interaction()
    else:
        print('The soldier looks uneasy, clearly reluctant to reveal anything.')
        print(
            '"I’ve heard about them, but I’m not about to share that kind of information with a stranger," he says firmly.')
        print('"Help me deal with these insurgents first, and maybe then we’ll talk about those ruins."')
        input("\n[Press Enter to continue]")
        print("\nThe soldier offers you two choices:")
        print("1. Ask about the ancient ruins.")
        print("2. Offer to help deal with the insurgents.")

        choice = input("What do you do? (1/2): ")

        if choice == "1":
            ask_about_ancient_ruins()
        elif choice == "2":
            offer_help_with_insurgents()
        else:
            print("Invalid choice, please select 1 or 2.")
            soldier_interaction()

    # Add further quest or options here if needed


def offer_help_with_insurgents():
    print("\nThe soldier looks relieved.")
    print(
        "‘Thank you for offering your help,’ he says. ‘There are insurgents disrupting the peace in these mountains. We need to push them back.’")
    print("‘Follow me, and we’ll deal with them together.’")

    # Simulate a multi-stage fight with insurgents
    print("\nYou and the soldier move through the mountains and encounter a group of insurgents.")

    if multi_stage_fight():
        print("\nWith the insurgents defeated, the soldier thanks you for your bravery.")
        print("‘You’ve done a great service today. We’ve secured this area for now.’")
        reward_xp(100)  # Reward 100 XP for successfully completing the multi-stage fight
        print(f"{player['name']} gains 100 XP!")
    else:
        print("\nDespite your efforts, the insurgents manage to escape.")
        print("The soldier looks disappointed but thanks you for your attempt.")


def multi_stage_fight():
    # Stage 1: Initial Skirmish
    print("You face a small group of insurgents. You need to decide how to handle the situation.")

    choice = input("How will you approach the fight? (1. Fight head-on / 2. Use agility / 3. Cast spells): ")

    if choice == "1":
        if player['strength'] >= 8:
            print("\nYou overpower the initial group with your strength.")
            print("You move on to face a more dangerous faction of insurgents.")
            return stage_2_fight()
        else:
            print("\nYour strength is not sufficient. The initial group overpowers you.")
            return False
    elif choice == "2":
        if player['agility'] >= 7:
            print("\nYou outmaneuver the initial group, avoiding their attacks and striking swiftly.")
            print("You move on to face a more dangerous faction of insurgents.")
            return stage_2_fight()
        else:
            print("\nYour agility is not enough. The insurgents catch you off guard.")
            return False
    elif choice == "3":
        if player['magic'] >= 6:
            print("\nYou use powerful spells to control the battlefield and defeat the initial group.")
            print("You move on to face a more dangerous faction of insurgents.")
            return stage_2_fight()
        else:
            print("\nYour magic is too weak. The insurgents overpower you.")
            return False
    else:
        print("Invalid choice. The fight continues.")
        return multi_stage_fight()


def stage_2_fight():
    # Stage 2: Reinforcements Arrive
    print("Reinforcements Arrive")
    print("After defeating the initial group, reinforcements arrive. This is a more challenging fight.")
    print("The soldier looks to you for guidance on how to approach the situation.")

    choice = input("How will you approach the reinforcements? (1. Fight head-on / 2. Use agility / 3. Cast spells): ")

    if choice == "1":
        if player['strength'] >= 10:
            print("\nYou use your strength to hold off the reinforcements and defeat them.")
            return True
        else:
            print("\nThe reinforcements are too strong for you. You struggle to hold your ground.")
            return False
    elif choice == "2":
        if player['agility'] >= 9:
            print("\nYou dodge the attacks of the reinforcements and strike with precision.")
            return True
        else:
            print("\nThe reinforcements overwhelm you despite your attempts to evade them.")
            return False
    elif choice == "3":
        if player['magic'] >= 8:
            print("\nYou use advanced spells to control and defeat the reinforcements.")
            return True
        else:
            print("\nThe reinforcements resist your magic and continue to fight fiercely.")
            return False
    else:
        print("Invalid choice. The fight continues.")
        return stage_2_fight()


def battlefield_encounter():
    print("\nShortly after deciding where to go next, you encounter a fort on the outskirts of the village.")
    print(
        "\nYou arrive at the fort, where the clash between the royal army and Adrieth’s forces has left devastation in its wake.")
    print("\nThe battlefield is a wasteland of bodies and broken weapons.")
    print("In the chaos, you spot an lieutenant of Adreith's army, kneeling next to a terrified child.")
    print(
        "His bloodied hands rest gently on the child's shoulder making sure the child is safe, his eyes tired and full of regret.")
    input("\nPress Enter to continue.")

    print("\n'Go, you’re safe now,' the lieutenant says quietly, his voice heavy.")
    print(
        "The child in shock,runs past you back towards the village, a royal guard charges, sword raised to strike the lieutenant down.")
    print("The lieutenant doesn’t move, as if resigned to his fate.")
    input("\nPress Enter to continue.")

    print("\nWhat do you do?")
    print("1. Intervene and save the lieutenant.")
    print("2. Let the guard kill the lieutenant.")

    choice = input("Choose your action (1/2): ")

    if choice == "1":
        spare_lieutenant()
    elif choice == "2":
        kill_lieutenant()
    else:
        print("Invalid choice, please select 1 or 2.")
        battlefield_encounter()


def proceed_to_next_stage():
    print(
        "\nYou push deeper into the heart of the Mountain of Echoes. The air grows colder, and the shadows seem to watch your every step.")
    print(
        "The path ahead becomes narrow and treacherous, with steep cliffs and strange ancient symbols carved into the walls.")

    print("\nAs you move forward, you begin to hear whispers in the wind. The mountain is alive with an eerie energy.")
    print("1. Examine the ancient carvings.")
    print("2. Continue forward, ignoring the whispers.")
    print("3. Set up camp to rest.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        examine_carvings()
    elif choice == "2":
        continue_forward()
    elif choice == "3":
        set_up_camp()
    else:
        print("Invalid choice, please select 1, 2, or 3.")
        proceed_to_next_stage()


def examine_carvings():
    print(
        "\nYou approach the ancient carvings, running your fingers over the strange symbols. They seem to depict a great battle long ago.")
    print(
        "You decipher a message: 'The Beast of Echoes was sealed here by the elders. Only the worthy shall break the seal.'")

    if player['magic'] >= 12:
        print(
            "With your knowledge of magic, you recognize this as an ancient sealing spell. You can feel its power weakening.")
        reward_xp(50)
        proceed_to_boss_encounter()
    else:
        print(
            "Without the proper understanding of magic, the carvings remain a mystery to you. You move on, feeling uneasy.")
        continue_forward()


def continue_forward():
    print("\nYou decide to press on, feeling the weight of the mountain’s secrets closing in around you.")
    print("As you move deeper, the ground suddenly shakes, and rocks begin to fall from the ceiling!")

    print("1. Use your agility to dodge the falling rocks.")
    print("2. Use your strength to push through and shield yourself.")
    print("3. Use magic to create a protective barrier.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        if player['agility'] >= 10:
            print(
                "\nYou dart through the falling rocks, narrowly avoiding disaster. You make it to the other side unscathed.")
            reward_xp(1175)
            proceed_to_boss_encounter()
        else:
            print("\nYou try to dodge, but you're not quick enough. A boulder crashes down, injuring you.")
            proceed_to_boss_encounter()
    elif choice == "2":
        if player['strength'] >= 10:
            print("\nYou brace yourself and push through, using your strength to shield yourself from the debris.")
            reward_xp(1175)
            proceed_to_boss_encounter()
        else:
            print("\nYou attempt to push through, but the rocks are too heavy. You are knocked to the ground, wounded.")
            proceed_to_boss_encounter()
    elif choice == "3":
        if player['magic'] >= 10:
            print("\nYou conjure a magical barrier just in time, protecting yourself from the falling rocks.")
            reward_xp(1175)
            proceed_to_boss_encounter()
        else:
            print(
                "\nYou try to summon magic, but it’s too weak. The rocks crush through your barrier, leaving you injured.")
            proceed_to_boss_encounter()
    else:
        print("Invalid choice, please select 1, 2, or 3.")
        continue_forward()


def set_up_camp():
    print("\nYou decide to set up camp and rest before continuing deeper into the mountain.")
    print(
        "As you rest, strange dreams fill your mind—visions of an ancient battle and a powerful beast bound by magic.")
    print("You awaken, feeling uneasy but more focused. You gain some energy back.")
    reward_xp(1000)
    input("\n[Press Enter to continue]")
    proceed_to_boss_encounter()


def proceed_to_boss_encounter():
    print(
        "\nAfter surviving the trials of the mountain, you finally arrive at a massive cavern, the heart of the Mountain of Echoes.")
    print("A towering creature emerges from the shadows—it is the Beast of Echoes, the one spoken of in the carvings.")

    print("\nThis will be the final challenge.")

    print("1. Attack the beast head-on.")
    print("2. Look for weaknesses in the environment.")
    print("3. Summon a spell to weaken the beast.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        if player['strength'] >= 12:
            print("\nWith immense strength, you charge at the beast and strike it with all your might, staggering it.")
            reward_xp(1150)
            defeat_beast()
        else:
            print("\nYou try to attack head-on, but the beast is too powerful. It swipes at you, knocking you back.")
            survive_beast_encounter()
    elif choice == "2":
        if player['agility'] >= 12:
            print(
                "\nYou notice a weak spot in the cavern—if you strike the right place, the ceiling will collapse onto the beast.")
            reward_xp(1150)
            defeat_beast()
        else:
            print("\nYou search for weaknesses, but the beast is too fast. It attacks you while you hesitate.")
            survive_beast_encounter()
    elif choice == "3":
        if player['magic'] >= 12:
            print("\nYou summon a powerful spell, binding the beast in magical chains, rendering it helpless.")
            reward_xp(1150)
            defeat_beast()
        else:
            print(
                "\nYou try to summon magic, but the beast interrupts you with a brutal strike, knocking you to the ground.")
            survive_beast_encounter()
    else:
        print("Invalid choice, please select 1, 2, or 3.")
        proceed_to_boss_encounter()


def defeat_beast():
    print("\nWith a final strike, the Beast of Echoes lets out a deafening roar and falls to the ground, defeated.")
    print("The cavern shakes as the beast’s body dissolves into a dark mist, leaving behind a glowing essence.")
    print("You have overcome the greatest challenge of the mountain, and with it, the dark magic begins to lift.")
    reward_xp(2000)
    print("You feel a surge of power as you absorb the beast's remaining essence. You have gained valuable knowledge.")
    print("You now possess the information you need to proceed to Wallechia.")
    input("\n[Press Enter to continue]")
    print("Thank you for playing version0.03 of this game!")
    input("\n[Press Enter to continue the game for one last option before the game stops running!]")
    travel_menu2()


def survive_beast_encounter():
    print(
        "\nYou manage to escape the beast's clutches, but you're badly injured. It seems too powerful for you right now.")
    print(
        "You retreat from the battle, but you know you'll need to return if you wish to unlock the secrets of the mountain.")
    print("You can hear the beast's roar echoing behind you as you make your way back to the mountain's entrance.")
    input("\n[Press Enter to continue]")
    # player dies here
    print("The beast chases after you, its roars echoing through the caverns.")
    print("You try to escape, but the beast is too fast. It catches up to you and strikes you down.")
    print("\nYour journey ends here.")
    print("GAME OVER")
    input("\n[Press Enter to exit the game]")
    exit()


def continue_journey2():
    if player_destination == "dragons_keep":
        journey_to_dragons_keep()
    elif player_destination == "mountain_of_echoes":
        journey_to_mountain_of_echoes()
    elif player_destination == "village_of_sarth":
        journey_to_village_of_sarth()
    elif player_destination == "temple_of_forgotten":
        journey_to_temple_of_forgotten()
    elif player_destination == "wallechia":
        proceed_to_wallechia()


def spare_lieutenant():
    print("\nYou step in, stopping the guard’s blade from striking the lieutenant.")
    print("The guard looks at you, uncertain, as you shield the lieutenant from harm.")
    print("The lieutenant looks up at you, clearly shocked. 'Why would you spare me?' he asks, voice shaky.")
    print("'I've done terrible things... followed Adrieth blindly... but I couldn’t let this child die.'")
    input("\nPress Enter to continue.")

    print("\nThe lieutenant rises to his feet, his body trembling, as if weighed down by guilt.")
    print("'You’re chasing a path that will lead you to him, aren’t you?' he says, his eyes weary.")
    print("You have a choice to make:")
    print("1. Ask him about Adrieth.")
    print("2. Leave him to his fate and continue your journey.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        ask_about_adrieth()
    elif choice == "2":
        print("\nYou choose not to press further, leaving the lieutenant to deal with his own demons.")
        reward_xp(50)  # Small XP reward for sparing him, but no crucial information gained.
        input("\nPress Enter to continue your journey.")
        continue_journey()
    else:
        print("Invalid choice, please select 1 or 2.")
        spare_lieutenant()


def ask_about_adrieth():
    print(
        "\n'If you want to face Adrieth, there’s something you need to know,' the lieutenant says, his voice lowering.")
    print("'He’s not just strong—there’s something dark, ancient that fuels him.'")
    print("He pauses, eyes filled with regret. 'The relic... destroy it, and his power will crumble.'")
    print("'Without it, Adrieth is just a man, not the invincible knight people fear.'")
    player['magic'] += 2  # Bonus for getting key information about Adrieth.
    reward_xp(100)  # Reward extra XP for gaining vital information.
    input("\nPress Enter to continue your journey.")
    continue_journey()


def kill_lieutenant():
    print("\nYou step back as the guard's sword strikes true.")
    print("The lieutenant gasps, reaching for the child, but his strength fades.")
    print("His last words are faint: 'I... tried.'")
    reward_xp(150)  # Quick XP reward, but player misses out on the information
    input("\nPress Enter to continue your journey.")
    continue_journey()


# Reward XP and check for level up
def reward_xp(amount):
    player['xp'] += amount
    level_up()


# Level up system
def level_up():
    xp_to_next_level = player['level'] * 100
    if player['xp'] >= xp_to_next_level:
        player['level'] += 1
        player['xp'] = 0  # Reset XP after leveling up
        player['strength'] += 2
        player['magic'] += 2
        player['agility'] += 2
        print(f"\nCongratulations! {player['name']} has leveled up to Level {player['level']}!")
        print(f"New stats: Strength = {player['strength']}, Magic = {player['magic']}, Agility = {player['agility']}.")
    else:
        print(f"\n{player['name']} needs {xp_to_next_level - player['xp']} more XP to reach the next level.")


# After any village action, the player is taken to the Kingdom of Wallachia
def taken_to_wallachia():
    print("\nDespite your efforts to escape or fight, you are eventually caught by the royal guards.")
    print("You are taken to the great kingdom of Wallachia, known for its powerful rulers and strict laws.")
    print("After a long journey in chains, you stand before King Vlad of Wallachia.")
    input("\nPress Enter to continue...")
    present_to_king()


def present_to_king():
    print("\nYou kneel in the grand hall, surrounded by the court. King Vlad gazes down at you from his throne.")
    print(f"'You stand accused of causing chaos in our lands, {player['name']}.'")
    input("\nPress Enter to continue...")
    present_to_king_options()


def present_to_king_options():
    print("'However, I believe that you might serve a greater purpose...'")
    print("'A powerful knight, Adrieth, has slain the King of Apixori, plunging that kingdom into darkness.'")
    print("'Adrieth now rules with a dark dominion and threatens all of Wallachia and beyond.'")
    print("'I need someone capable of ending this reign of terror.'")
    print("'Will you accept this task, or will you face the consequences of your crimes?'")

    print("\n1. Accept the quest to kill Adrieth.")
    print("2. Refuse the quest and face the king's wrath.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        accept_quest_to_kill_adrieth()
    elif choice == "2":
        refuse_quest()
    else:
        print("Invalid choice, please select 1 or 2.")
        present_to_king()


# Option 1: Accept the quest to kill Adrieth
def accept_quest_to_kill_adrieth():
    print("\nYou accept the king's offer and agree to take on the quest to kill Adrieth.")
    print("King Vlad nods approvingly and leans forward.")
    print(
        "'Good,' he says. 'This will not be an easy task. Adrieth is a powerful knight who wields dark magic and commands an army of loyal followers.'")
    print("'You must journey to his fortress in the dark lands and put an end to him once and for all.'")
    print("'Succeed, and you will be pardoned of all your crimes and granted wealth and glory.'")
    print("'Fail... and the consequences will be dire, not just for you, but for all of us.'")
    print("\nYour quest to kill Adrieth begins...")
    quest_to_kill_adrieth()


# Option 2: Refuse the quest
def refuse_quest():
    print("\nYou refuse the king's quest, and his expression darkens.")
    print("'Foolish,' he says. 'You have sealed your fate.'")
    print("The guards seize you, and you are taken to the dungeons.")
    input("\nPress Enter to continue...")
    game_over()


def game_over():
    print("As the dungeon gates close behind you, you realize this is the end.")
    print("A few months pass before you awake from screams of the terrorization being caused above.")
    print("You realize that the kingdom has fallen to Adrieth, and the dungeons are now your tomb.")
    print("Game Over...")


# Start the quest to kill Adrieth
def quest_to_kill_adrieth():
    print("\nYou gather your gear and begin your journey to the dark lands where Adrieth's fortress lies.")
    print("The road ahead is long and treacherous, and you know that many dangers await you.")
    print("But the fate of kingdoms depends on your success.")
    reward_xp(100)  # Reward XP for accepting the quest
    # Continue with the next part of the story, building up the journey to confront Adrieth
    journey_to_adrieth()


def journey_to_adrieth():
    print(
        "\nYou travel through forests, mountains, and desolate wastelands, avoiding patrols of Adrieth's dark soldiers.")
    print(
        "The journey is perilous, but you are determined to reach your goal. The void realm a desolate place where Adrieth's fortress lies.")
    print(
        "Eventually, you arrive at the outskirts of Adrieth's fortress, a towering black castle surrounded by dark magic.")
    print("What do you do?")

    print("1. Sneak into the fortress and try to assassinate Adrieth quietly.")
    print("2. Challenge Adrieth and his forces head-on in battle.")
    print("3. Search for allies who may be willing to help you fight Adrieth.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        sneak_into_fortress()
    elif choice == "2":
        challenge_adrieth()
    elif choice == "3":
        search_for_allies()
    else:
        print("Invalid choice, please select 1, 2, or 3.")
        journey_to_adrieth()


# Option 1: Sneak into Adrieth's fortress
def sneak_into_fortress():
    if player['agility'] >= 8:
        print("\nYou manage to sneak into the fortress undetected, moving through the shadows.")
        print("You find Adrieth in his throne room, and you prepare for a surprise attack...")
        face_adrieth()
    else:
        print("\nYou attempt to sneak in, but you are spotted by the guards!")
        print("You are captured and brought before Adrieth himself.")
        face_adrieth()


# Option 2: Challenge Adrieth and his forces head-on
def challenge_adrieth():
    print("\nYou decide to take a more direct approach, storming the gates of Adrieth's fortress.")
    if player['strength'] >= 8:
        print("With your immense strength, you fight your way through his forces, finally reaching Adrieth.")
        face_adrieth()
    else:
        print("Despite your best efforts, Adrieth's forces overwhelm you, and you are captured.")
        face_adrieth()


# Option 3: Search for allies
def search_for_allies():
    print("\nYou search for local resistance groups or old allies of the fallen King of Apixori.")
    if player['charisma'] >= 7:
        print("Using your charisma, you convince a group of resistance fighters to join your cause.")
        print("With their help, you plan a coordinated attack on Adrieth's fortress.")
        face_adrieth_with_allies()
    else:
        print("Unfortunately, you fail to find anyone willing to help you, and you must face Adrieth alone.")
        face_adrieth()


# Confront Adrieth directly
def face_adrieth():
    print("\nAs you step into Adrieth's dark fortress, a chill grips your heart.")
    print("The air is thick with the stench of decay, and the walls seem to pulse with a life of their own.")
    print("The shadows whisper to you, reminding you of every mistake, every crime, every regret.")
    print("It’s as though the weight of your sins crawls back from the past, clawing at your soul as you walk further.")
    input("\nPress Enter to continue...")
    face_adrieth3()


def face_adrieth3():
    print("\nYou descend a long, narrow corridor, the walls lined with the twisted faces of those who came before you.")
    print("The flickering torchlight dances off their empty eyes, and you swear you can hear faint screams.")
    print("Ahead, a massive door, carved with ancient runes and soaked in blood, looms ominously.")
    input("\nPress Enter to continue...")
    face_adrieth4()


def face_adrieth4():
    print("Behind it, you know, is Adrieth.")

    input("\nPress Enter to continue...")
    face_adrieth2()


def face_adrieth2():
    print(
        "\nYou push open the door and enter a massive, darkened chamber. In the center of the room, Adrieth sits upon a throne of blackened bones, his armor gleaming with a dark, malevolent energy.")
    print("His eyes, glowing red like the fires of hell, lock onto you, and a cold smile spreads across his face.")
    print(
        "'So, another fool has come to challenge me,' he says, his voice a guttural growl that echoes through the chamber.")
    print("'I will enjoy watching you fall into the abyss.'")

    print("\nYour heart pounds in your chest as you draw your weapon. The final battle has begun.")

    print("\n1. Use your strength to overpower Adrieth.")
    print("2. Outmaneuver him with agility.")
    print("3. Use magic to counter his dark powers.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        fight_adrieth_strength_phase_one()
    elif choice == "2":
        fight_adrieth_agility_phase_one()
    elif choice == "3":
        fight_adrieth_magic_phase_one()
    else:
        print("Invalid choice, please select 1, 2, or 3.")
        face_adrieth()


# Phase one: Strength option
def fight_adrieth_strength_phase_one():
    print("\nYou charge at Adrieth, your weapon raised high, determined to end this battle with raw power.")
    if player['strength'] >= 9:
        print(
            "With a powerful swing, you strike Adrieth's armor, sending sparks flying. He staggers back, momentarily surprised by your strength.")
        print("But as you press forward, he recovers quickly, parrying your strikes with ease.")
        print(
            "His eyes gleam with dark energy, and he summons a wave of black flames that scorch the floor as they race toward you.")
        next_battle_phase_strength()
    else:
        print(
            "\nYou swing with all your might, but Adrieth’s dark power is too strong. He blocks your attacks effortlessly, toying with you.")
        print("With a cruel grin, he slams his gauntlet into your chest, sending you crashing into the ground.")
        print("Before you can recover, he steps forward and plunges his sword into your heart.")
        print("You fought bravely, but it wasn’t enough. The darkness consumes you.")
        print("Game over.")


# Phase one: Agility option
def fight_adrieth_agility_phase_one():
    print(
        "\nYou dart forward, relying on your speed to outmaneuver Adrieth. Each step echoes in the dark chamber as you weave through his attacks.")
    if player['agility'] >= 9:
        print("Adrieth swings his massive sword, but you’re too fast, dodging his strikes by mere inches.")
        print(
            "With a quick lunge, you manage to land a blow on his side, but the impact barely dents his cursed armor.")
        print(
            "As you pull back, Adrieth’s laughter echoes in the chamber. 'Is that the best you can do?' he sneers, as dark energy crackles around him.")
        next_battle_phase_agility()
    else:
        print("\nYou try to dodge Adrieth’s attacks, but he moves with unnatural speed, matching your agility.")
        print(
            "Before you can react, he swings his sword, catching you in the side and sending you sprawling to the ground.")
        print("The last thing you see is his boot coming down on your face.")
        final_death_sequence()


# Phase one: Magic option
def fight_adrieth_magic_phase_one():
    print(
        "\nYou raise your hands, summoning your magic to counter Adrieth's dark powers. The air around you hums with arcane energy.")
    if player['magic'] >= 9:
        print(
            "With a flick of your wrist, you send a bolt of pure magic toward Adrieth. It crashes into him, and for the first time, you see a flicker of pain in his eyes.")
        print(
            "But he quickly recovers, his armor shimmering with a dark shield as he conjures a storm of black lightning in retaliation.")
        next_battle_phase_magic()
    else:
        print(
            "\nYou try to summon your magic, but Adrieth’s dark power is overwhelming. His magic warps the very fabric of reality around you, and your spell fizzles out before it reaches him.")
        print(
            "With a cruel laugh, Adrieth unleashes a blast of dark energy, and your body is torn apart by the force of his magic.")
        print("Game over.")


# Next phase of the battle (regardless of choice, if successful)
def next_battle_phase_strength():
    print(
        "\nAdrieth stumbles, and you press your advantage. But the room seems to darken further, as if the shadows themselves are alive.")
    print("You hear whispers in your mind, telling you to give up, to embrace the darkness.")
    print(
        "But you shake them off and charge at Adrieth again. His dark powers surge around him, but you force your way through, landing another strike.")

    final_phase()


def next_battle_phase_agility():
    print(
        "\nYou continue to dodge Adrieth’s strikes, finding small openings to land hits. The whispers grow louder, as if the fortress itself is trying to break your will.")
    print(
        "Adrieth swings at you with renewed fury, but you manage to avoid the worst of his attacks. You land a swift strike, but it’s clear that this battle is far from over.")

    final_phase()


def next_battle_phase_magic():
    print(
        "\nYour magic collides with Adrieth’s, the room filled with the sound of crackling energy and shattering spells.")
    print(
        "The whispers in the air grow louder, and you realize that Adrieth is trying to break your concentration with his dark influence.")
    print("But you hold firm, launching another spell that briefly weakens his defenses.")

    final_phase()


# Final phase of the battle
def final_phase():
    print(
        "\nAdrieth roars in fury, his armor cracking under the weight of your attacks. But his eyes glow brighter, and you can feel the dark energy in the room intensify.")
    print("The shadows on the walls twist and writhe, as if alive, and the whispers in your mind grow deafening.")

    print("'You cannot defeat me!' Adrieth snarls, raising his sword high. 'I am darkness incarnate!'")

    print(
        "\nBut you know this is your moment. With one final effort, you gather all your strength and prepare to end this once and for all.")

    print("\n1. Finish Adrieth with a powerful blow.")
    print("2. Use the last of your agility to outmaneuver him and strike.")
    print("3. Summon a final surge of magic to destroy Adrieth.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        final_blow_strength()
    elif choice == "2":
        final_blow_agility()
    elif choice == "3":
        final_blow_magic()
    else:
        print("Invalid choice, please select 1, 2, or 3.")
        final_phase()


# Final blow: Strength option
def final_blow_strength():
    if player['strength'] >= 20:
        print("\nWith a mighty roar, you bring your weapon down with all your strength, shattering Adrieth’s defenses.")
        print(
            "His eyes widen in shock as your weapon strikes true, cleaving through his armor and sinking deep into his chest.")
        print(
            "Adrieth lets out a final, terrible scream as dark energy erupts from his body, and he falls to the ground, lifeless.")
        end_game_victory()
    else:
        print("\nYou swing with all your might, but Adrieth catches your weapon in midair, his strength overwhelming.")
        final_death_sequence()


# Final blow: Agility option
def final_blow_agility():
    if player['agility'] >= 20:
        print(
            "\nYou move faster than ever before, darting around Adrieth’s final attack and slipping past his defenses.")
        print("With a quick, precise strike, you plunge your weapon into his chest, ending his reign of darkness.")
        print("Adrieth's body collapses, his dark energy dissipating into the air.")
        end_game_victory()
    else:
        print("\nYou attempt to outmaneuver Adrieth, but his dark power warps the very space around you.")
        final_death_sequence()


# Final blow: Magic option
def final_blow_magic():
    if player['magic'] >= 20:
        print(
            "\nYou summon the last of your magical energy, casting a spell so powerful that the very air crackles with arcane power.")
        print(
            "Adrieth tries to resist, but your magic is too strong. His body is consumed in a torrent of light, and his dark essence is obliterated.")
        end_game_victory()
    else:
        print(
            "\nYou attempt to cast a final spell, but Adrieth’s dark magic overwhelms you, and you are consumed by his power.")
        input("\nPress Enter to continue...")
        final_death_sequence()


def final_death_sequence():
    print(
        "\nThe battle with Adrieth reaches its horrifying climax. Despite your valor, his dark power proves insurmountable.")
    input("\nPress Enter to continue...")

    print(
        "Adrieth's relentless assault breaks through your defenses. You feel every bone in your body ache as if being crushed under a mountain.")
    print(
        "His laughter echoes through the battlefield, mingling with your cries of agony. Darkness seeps into your vision as your strength wanes.")
    input("\nPress Enter to continue...")

    print(
        "With a final, brutal strike, Adrieth's sword pierces through you. The cold steel chills your very soul, and you collapse to the ground, your life force draining away.")
    print(
        "As the darkness engulfs you, the weight of your failure presses down, and you see haunting visions of the kingdom's despair and suffering.")
    input("\nPress Enter to continue...")

    print(
        "You awaken in a bleak, shadowy realm. The remnants of the battle and your shattered hopes are all around you.")
    print(
        "The crushing defeat and the specter of failure leave a scar on your spirit. Yet, the glimmer of hope still remains, as another chance might be within reach.")

    # Offer options to restart from checkpoint, restart the game, or exit
    print("\nWhat would you like to do?")
    print("1. Restart from checkpoint.")
    print("2. Restart the game.")
    print("3. Exit to the main menu.")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        restart_from_checkpoint()
    elif choice == "2":
        restart_game()
    elif choice == "3":
        exit_game()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        final_death_sequence()


def restart_from_checkpoint():
    print(
        "\nYou have chosen to restart from the checkpoint. The darkness fades, and you find yourself back at a critical juncture in your journey.")
    # Reset player stats and position to the checkpoint
    player['strength'] = 12
    player['agility'] = 12
    player['magic'] = 12
    player['xp'] = 0
    player['level'] = 14
    input("\nPress Enter to continue...")
    take_to_wallechia()


def restart_game():
    print("\nYou have chosen to restart the game. All progress will be lost, but a new adventure awaits.")
    # Reset player stats and start the game again
    player['strength'] = 0
    player['agility'] = 0
    player['magic'] = 0
    player['xp'] = 0
    player['level'] = 1
    print("Restarting game...")
    input("\nPress Enter to continue...")
    # Call the initial game start function or character customization
    start_game()


def exit_game():
    print("\nYou have chosen to exit. Thank you for playing!")
    # Handle exiting the game or returning to the main menu
    # For example:
    # return_to_main_menu()
    exit()


def take_to_wallechia():
    print("\nYou find yourself once again at the village's edge, with the road to Wallachia ahead of you.")
    input("\nPress Enter to continue...")
    # Continue with the path to Wallachia
    travel_menu()
