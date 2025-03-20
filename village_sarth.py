from character_creation import player
from to_the_castle import return_to_castle


def journey_to_village_of_sarth():
    print("\nThe rain pours relentlessly as you approach the Village of Sarth.")
    print("A dense mist cloaks the surroundings, shrouding the village in foreboding.")
    print("Whispers of lost souls echo through the darkness, hinting at secrets buried deep.")
    print("You sense an ominous presence lurking just beyond your sight.\n")
    input("\nPress Enter to continue your journey in the Village of Sarth.")
    village_of_sarth2()


def village_of_sarth2():
    print("\nAs you enter the village, your heart sinks.")
    print("Homes lie in ruins, smoke rises from the remnants of what were once safe havens.")
    print("The streets are quiet, yet you feel eyes watching you from the shadows.\n")

    print("Suddenly, a figure emerges from an alleyway. It's a villager named Kael.")
    print("'You! You look capable! We need help!' Kael pleads.")

    print("\nYou can see that Kael is frantic but determined.")
    print("'If you help me find the remaining villagers, I might know where Adrieth has gone.'\n")

    input("\nPress Enter to team up with Kael.")

    kael_quests()


def kael_quests():
    print("\nKael leads you through the village, and you start looking for survivors.")

    quest_options = [
        "Search for the healer in the eastern part of the village.",
        "Investigate the marketplace for clues.",
        "Check the old tavern for any survivors."
    ]

    print("\nQuest Options:")
    for idx, option in enumerate(quest_options, 1):
        print(f"[{idx}] {option}")

    choice = input("\nChoose a quest: ")

    if choice == '1':
        search_for_healer()
    elif choice == '2':
        investigate_marketplace()
    elif choice == '3':
        check_old_tavern()
    else:
        print("\nInvalid choice. Please try again.")
        kael_quests()


def search_for_healer():
    print("\nYou and Kael rush to the healer's house.")
    print("Inside, you find the healer injured but alive, cradling a broken arm.")

    print("'I can help you if you fetch my herbs from the garden,' the healer instructs.")

    print("\nChoices:\n")
    print("[1] Use Agility to sneak past any lurking soldiers.")
    print("[2] Use Strength to clear a path through the debris.")

    choice = input("Choose an action: ")

    if choice == '1':
        if player['agility'] >= 10:
            print("\nYou dart through the shadows, successfully retrieving the herbs!")
            player['xp'] += 20
            print("You gain 20 XP!")
        else:
            print("\nYou trip and attract attention, but you manage to grab the herbs.")
            player['xp'] += 10
            print("You gain 10 XP!")
    elif choice == '2':
        if player['strength'] >= 12:
            print("\nYou clear a path effortlessly and retrieve the herbs.")
            player['xp'] += 30
            print("You gain 30 XP!")
        else:
            print("\nYou struggle, but you manage to retrieve the herbs with some effort.")
            player['xp'] += 15
            print("You gain 15 XP!")

    print("\nReturning to the healer, you help her bandage her arm.")
    print("She expresses her gratitude and gives you information about a hidden cache of supplies nearby.")
    player['xp'] += 20
    print("You gain 20 XP!")

    print("\nAs you leave, the healer warns you about soldiers patrolling the area.")
    print("You need to be cautious.\n")

    kael_quests()


def investigate_marketplace():
    print("\nYou head to the marketplace, scanning for clues.")
    print("You find signs of a struggle but no villagers.")

    print("\nChoices:\n")
    print("[1] Use Perception to examine the scene closely.")
    print("[2] Use Magic to sense any residual energies.")

    choice = input("Choose an action: ")

    if choice == '1':
        if player['perception'] >= 10:
            print("\nYou spot a hidden message etched into the ground.")
            print("It points toward Adrieth's camp!")
            player['xp'] += 20
            print("You gain 20 XP!")
        else:
            print("\nYou find nothing of note but gain a feeling of dread.")
            player['xp'] += 5
            print("You gain 5 XP.")
    elif choice == '2':
        if player['magic'] >= 12:
            print("\nYou sense the dark magic left behind by Adrieth's soldiers.")
            print("You gain insight into their next move.")
            player['xp'] += 30
            print("You gain 30 XP!")
        else:
            print("\nYour attempt fails, and you gain no useful information.")
            player['xp'] -= 5
            print("You lose 5 XP.")

    print("\nAs you leave the marketplace, a soldier spots you!")
    print("You must act quickly!")

    print("\nChoices:\n")
    print("[1] Use Agility to dodge and escape.")
    print("[2] Use Strength to confront the soldier.")

    action_choice = input("Choose an action: ")

    if action_choice == '1':
        if player['agility'] >= 10:
            print("\nYou dodge skillfully, escaping the soldier's grasp!")
            player['xp'] += 20
            print("You gain 20 XP!")
        else:
            print("\nYou stumble, but manage to escape.")
            player['xp'] += 10
            print("You gain 10 XP.")
    elif action_choice == '2':
        if player['strength'] >= 12:
            print("\nYou confront the soldier and intimidate him.")
            print("He backs off, allowing you to escape.")
            player['xp'] += 30
            print("You gain 30 XP!")
        else:
            print("\nYou try to fight but are overpowered.")
            print("You barely manage to escape with your life.")
            player['xp'] -= 10
            print("You lose 10 XP.")

    kael_quests()


def check_old_tavern():
    print("\nYou enter the old tavern, the air thick with dust and despair.")
    print("You hear a muffled sound coming from the back room.")

    print("\nChoices:\n")
    print("[1] Use Agility to sneak in quietly.")
    print("[2] Use Strength to kick the door down.")

    choice = input("Choose an action: ")

    if choice == '1':
        if player['agility'] >= 10:
            print("\nYou sneak in and find a group of terrified villagers.")
            print("They are hiding from the soldiers that ransacked the tavern.")
            player['xp'] += 20
            print("You gain 20 XP!")
        else:
            print("\nYou make noise and alert the soldiers outside!")
            player['xp'] -= 10
            print("You lose 10 XP.")
    elif choice == '2':
        if player['strength'] >= 12:
            print("\nYou kick the door down, startling everyone inside.")
            print("The villagers are grateful for your boldness.")
            player['xp'] += 30
            print("You gain 30 XP!")
        else:
            print("\nThe door won't budge, but you eventually get it open.")
            player['xp'] += 10
            print("You gain 10 XP.")

    print("\nThe villagers tell you of Adrieth's merciless raid and mention a potential hideout.")
    print("They offer you some supplies as gratitude.")
    player['xp'] += 20
    print("You gain 20 XP.")

    kael_quests()


def return_to_ruins():
    print("\nAfter completing your quests, you and Kael return to the village center.")
    print("But what you see stops you in your tracks.")
    print("The once-bustling center is now a battlefield, with smoke rising and fires burning.")
    print("You realize you are surrounded by Adrieth's soldiers!\n")

    mysterious_character()


def mysterious_character():
    print("Suddenly, a tall figure steps out from the shadows, cloaked in dark, flowing attire.")
    print("His face is obscured by a hood, but his piercing blue eyes shine with intensity.")
    print("He moves with an air of confidence, and you feel both intrigued and uneasy.\n")

    print("'I can help you escape,' he says, his voice smooth yet enigmatic.")
    print("'But we must be swift. Time is of the essence.'")

    print("You feel a mixture of trust and suspicion towards him.")

    print("\nChoices:\n")
    print("[1] Accept his help and follow him.")
    print("[2] Distrust him and try to escape on your own.")

    choice = input("Choose an action: ")

    if choice == '1':
        print("\nYou choose to trust the mysterious figure.")
        print("He leads you through hidden passages, skillfully avoiding the soldiers.")
        player['xp'] += 30
        print("You gain 30 XP!")

        sabotaging_escape()

    elif choice == '2':
        print("\nYou decide to escape on your own.")
        print("But as you turn, he whispers, 'You won’t make it alone.'")
        print("His voice echoes in your mind, causing hesitation.")
        print("Adrieth's soldiers close in, and you must think fast!\n")

        sabotaging_escape()


def sabotaging_escape():
    print("\nYou now find yourself faced with a choice.")
    print("The mysterious figure's assistance comes with unexpected consequences.")

    print("\nChoices:\n")
    print("[1] Use Agility to slip past the soldiers while he distracts them.")
    print("[2] Use Strength to fight your way through, but the figure seems to vanish for a moment.")

    choice = input("Choose an action: ")

    if choice == '1':
        if player['agility'] >= 12:
            print("\nYou expertly maneuver through the chaos, the figure drawing the soldiers' attention.")
            print("You escape just in time, but wonder about his true intentions.")
            player['xp'] += 40
            print("You gain 40 XP!")
        else:
            print("\nYou slip but stumble, alerting the soldiers.")
            print("The figure appears just in time to help you back on your feet.")
            player['xp'] += 20
            print("You gain 20 XP.")

    elif choice == '2':
        if player['strength'] >= 15:
            print("\nYou fight through, but the figure reappears, causing some soldiers to falter.")
            print("While you push through, you feel a pang of mistrust toward his motives.")
            player['xp'] += 50
            print("You gain 50 XP!")
        else:
            print("\nYou try to fight, but he vanishes again, leaving you exposed.")
            print("You manage to escape, but not without injury.")
            player['xp'] -= 15
            print("You lose 15 XP.")

    print("\nYou and Kael regroup outside the village, the horrors of the day weighing heavily on your hearts.")
    print(
        "But you also feel the mystery surrounding the figure, wondering if he will help or hinder you in the future.")
    return_to_castle()