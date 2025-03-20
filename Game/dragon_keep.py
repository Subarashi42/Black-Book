from Game.character_creation import player
from Game.village_sarth import journey_to_village_of_sarth


def journey_to_dragons_keep():
    print("\nYou journey to the Dragons Keep, a towering fortress rumored to hold ancient power.")
    print("The air grows heavy with the scent of sulfur, and the skies darken as you approach the keep.")
    input("\nPress Enter to continue your journey to the Dragons Keep.")
    journey_to_dragons_keep2()


def journey_to_dragons_keep2():
    print(
        "\nYou arrive at Dragons Keep, a massive, fortress-like structure with towering walls and warriors clad in dragon scale armor.")
    print(
        "The atmosphere is tense, and there are whispers of an imminent threat tied to Adrieth. The keep is preparing for a full-scale battle.")
    print("\nAs you approach the main gate, you're greeted by Commander Eryx, the leader of the Keep’s elite forces.")

    input("\n[Press Enter to continue]")
    meet_commander()


def meet_commander():
    print("\nCommander Eryx: 'You must be the warrior we've heard about. News of your feats has reached us.'")
    print("He eyes you up and down, then speaks gravely.")
    print(
        "\nCommander Eryx: 'A great threat looms on the horizon. We’ve heard rumors that Adrieth’s forces march towards us. We could use someone of your skill to help in the defense.'")

    print("\nOptions:")
    print("[1] 'Tell me what I can do to help.'")
    print("[2] 'What can you tell me about Adrieth’s forces?'")
    print("[3] 'I’ll fight with you. Let’s just get to it.'")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        help_with_defenses()
    elif choice == "2":
        ask_about_adrieth_forces()
    elif choice == "3":
        start_battle_prep()
    else:
        print("Invalid choice, try again.")
        meet_commander()


def help_with_defenses():
    print(
        "\nCommander Eryx: 'We’re reinforcing the walls and bolstering our forces. Your strength will be invaluable.'")
    print(
        "You spend the next few hours helping the warriors prepare for the coming battle, adding to the fortifications and ensuring the soldiers are ready.")
    input("\n[Press Enter to continue]")
    start_battle_prep()


def ask_about_adrieth_forces():
    print(
        "\nCommander Eryx: 'Adrieth’s forces are unlike anything we’ve faced before. Dark magic, beasts that are more nightmare than reality, and soldiers who have no fear of death.'")
    print("He pauses, his face grim.")
    print("\nCommander Eryx: 'We’ve defeated dragons before, but this... this will be the hardest fight of our lives.'")
    input("\n[Press Enter to continue]")
    start_battle_prep()


def start_battle_prep():
    print("\nThe sun begins to set as the Keep prepares for war.")
    print("The soldiers line the walls, archers ready their bows, and ballistas are loaded. The tension is palpable.")
    print(
        "\nSuddenly, the horns sound. Adrieth’s forces have been spotted on the horizon, and a massive army marches toward the Keep.")

    input("\n[Press Enter to continue]")
    start_battle()


def start_battle():
    print("\nThe battle erupts as Adrieth's forces slam into the walls of Dragons Keep.")
    print("Dark beasts claw at the walls, and Adrieth's soldiers, clad in black armor, surge forward.")

    print("\nOptions:")
    print("[1] Fight on the front lines alongside the strongest warriors.")
    print("[2] Defend the gates with the archers.")
    print("[3] Help with magical defenses against the dark beasts.")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        fight_on_front_lines()
    elif choice == "2":
        defend_the_gates()
    elif choice == "3":
        magical_defenses()
    else:
        print("Invalid choice, try again.")
        start_battle()


def fight_on_front_lines():
    print("\nYou charge into battle, fighting alongside the elite warriors of Dragons Keep.")
    print("The battle is brutal, with the sound of steel clashing and the roars of dark beasts filling the air.")
    if player['strength'] > 8:
        print(
            "\nYour strength allows you to cut through Adrieth’s soldiers with ease, but the battle is far from over.")
    else:
        print(
            "\nThe fight is difficult, and you're struggling to keep up with the elite warriors. You take damage but manage to hold your own.")
    input("\n[Press Enter to continue]")
    next_battle_phase()


def defend_the_gates():
    print("\nYou rush to the gates, where the archers are fending off a relentless assault.")
    print("You help the defenders push back Adrieth’s forces, taking down enemy soldiers with precision.")
    if player['agility'] > 7:
        print("\nYour agility allows you to dodge attacks and take down enemies swiftly.")
    else:
        print(
            "\nYou struggle to keep up with the pace of the battle, and the gates are on the verge of being breached.")
    input("\n[Press Enter to continue]")
    next_battle_phase()


def magical_defenses():
    print("\nYou join the Keep’s mystics in creating magical barriers to hold off the dark beasts attacking the walls.")
    print("The beasts are ferocious, but with your help, the barriers hold strong.")
    if player['magic'] > 7:
        print(
            "\nYour magical abilities are crucial in keeping the beasts at bay, and you gain the respect of the Keep’s mystics.")
    else:
        print(
            "\nYou struggle to maintain the barrier, and some of the dark beasts break through, causing havoc inside the walls.")
    input("\n[Press Enter to continue]")
    next_battle_phase()


def next_battle_phase():
    print("\nThe battle rages on as both sides suffer heavy losses.")
    print("Adrieth’s forces continue to press the attack, but Dragons Keep’s warriors hold strong.")
    print("\nCommander Eryx calls out to you:")
    print(
        "'We're about to make our final stand. Will you rally the troops with me, or do you have another plan in mind?'")

    print("\nOptions:")
    print("1. 'I’ll fight with you to the end. Let’s rally the remaining soldiers!'")
    print("2. 'I have a different plan. I'll try to take down Adrieth himself.'")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        final_battle_stand()
    elif choice == "2":
        sneak_attack_adrieth()
    else:
        print("Invalid choice, try again.")
        next_battle_phase()


def final_battle_stand():
    print(
        "\nYou stand with Commander Eryx and the remaining forces of Dragons Keep as they prepare for the final assault.")
    print("With a mighty cry, you rally the soldiers for one last stand.")
    print(
        "\nThe ground shakes as a massive shadow appears on the horizon. Adrieth himself is coming to finish the fight.")
    print("Commander Eryx: 'This is it. The final battle for Dragons Keep.'")

    print("\nOptions:")
    print("1. Lead the charge with Commander Eryx.")
    print("2. Defend the walls from Adrieth’s beasts and soldiers.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        lead_charge_with_commander()
    elif choice == "2":
        defend_the_walls()
    else:
        print("Invalid choice, try again.")
        final_battle_stand()


def defend_the_walls():
    print("\nYou rush to the walls, where the defenders are holding back a relentless assault.")
    print("Adrieth’s dark beasts and soldiers are overwhelming the defenders, and the walls are starting to crumble.")
    if player['strength'] > 8:
        print("\nYour strength allows you to hold the line, but the situation is dire.")
    else:
        print("\nYou fight valiantly, but the dark forces are too strong. The defenders are being pushed back.")
    input("\n[Press Enter to continue]")
    battle_dragons_keep()


def sneak_attack_adrieth():
    print("\nYou decide to slip through the chaos of the battlefield and target Adrieth directly.")
    print("You stealthily make your way through the dark beasts and soldiers, trying to avoid detection.")

    if player['agility'] >= 8:
        print("\nYour agility allows you to move undetected through the battlefield, getting closer to Adrieth.")
    else:
        print(
            "\nYou struggle to stay hidden, and a few of Adrieth's soldiers notice you. You take some damage but press on.")

    print("\nYou spot Adrieth, surrounded by his dark soldiers and beasts. It's time to make your move.")

    print("\nOptions:")
    print("1. Confront Adrieth in direct combat.")
    print("2. Use a sneak attack to strike him from the shadows.")

    choice = input("What do you do? (1/2): ")

    if choice == "1":
        battle_dragons_keep()
    elif choice == "2":
        print("\nYou launch a surprise attack on Adrieth, attempting to catch him off guard.")
        print("As you go to strike him, a dark energy surrounds him, and he turns to face you.")
        print("Adrieth turns your attack back on you, and you're thrown back by a powerful force.")
        print("You take damage and are left vulnerable on the battlefield.")
        input("\n[Press Enter to continue]")
        battle_dragons_keep()
    else:
        print("Invalid choice, try again.")
        sneak_attack_adrieth()


def lead_charge_with_commander():
    print("\nYou and Commander Eryx lead the remaining soldiers into the heart of the battlefield.")
    print(
        "With a fierce cry, the elite warriors of Dragons Keep clash with Adrieth’s forces in a final, desperate charge.")

    if player['strength'] >= 9:
        print(
            "\nYour immense strength allows you to cut through Adrieth's forces like a whirlwind. The tide of battle begins to turn.")
        print("The soldiers rally behind you, and the Keep’s forces gain the upper hand.")
    else:
        print(
            "\nYou fight valiantly, but Adrieth's forces are overwhelming. Many fall, and the Keep’s forces begin to falter.")

    input("\n[Press Enter to continue]")
    battle_dragons_keep()


import random


def battle_dragons_keep():
    print(
        "\nThe battle rages around you. The strongest warriors of the Keep, clad in dragon scale armor, fight valiantly against Adrieth’s forces.")
    print(
        "The Commander is nearby, giving orders and holding off enemies. Suddenly, Adrieth appears, cloaked in dark energy.")
    input("\n[Press Enter to approach Adrieth]")

    approach_adrieth()


def approach_adrieth():
    print("\nAdrieth's presence is overwhelming, a dark aura radiating from him.")
    print("You can barely hear the battle around you as you lock eyes with him.")
    input("\n[Press Enter to face Adrieth]")

    player_attack_options()


def player_attack_options():
    print("\nAdrieth stands before you, unmoving, seemingly untouchable.")
    print("1. Slash with your sword.")
    print("2. Use a magic attack.")
    print("3. Attempt a tactical move (try to weaken his footing).")
    print("4. Call the Commander for assistance.")

    choice = input("\nWhat do you do? (1/2/3/4): ")

    if choice == "1":
        sword_attack()
    elif choice == "2":
        magic_attack()
    elif choice == "3":
        tactical_move()
    elif choice == "4":
        call_commander()
    else:
        print("Invalid choice. Try again.")
        player_attack_options()


def sword_attack():
    print("\nYou charge at Adrieth with all your might, swinging your sword with precision.")
    if random.choice([True, False]):
        print(
            "Your blade clashes against his armor, but to your horror, it doesn’t even leave a mark. Adrieth doesn’t flinch.")
    else:
        print("You strike, but an invisible force pushes you back before your sword can even touch him!")

    adrieth_reacts()


def magic_attack():
    print("\nYou summon your magical energy and unleash a powerful blast toward Adrieth.")
    if random.choice([True, False]):
        print(
            "The magic hits him square in the chest, but it dissipates like smoke, the dark aura around him swallowing it whole.")
    else:
        print("Your spell fizzles in the air, and you feel a dark energy pushing back at you!")

    adrieth_reacts()


def tactical_move():
    print(
        "\nYou try a different approach, aiming to destabilize Adrieth by targeting his footing or a weakness in his stance.")
    if random.choice([True, False]):
        print(
            "You rush forward, trying to throw him off balance, but it’s like hitting a mountain. He doesn’t even budge.")
    else:
        print("You attempt a clever strike at his legs, but a force field stops your attack cold.")

    adrieth_reacts()


def call_commander():
    print("\nYou shout for the Commander to assist you.")
    print("The Commander rushes in, swinging his mighty sword, but Adrieth doesn’t even acknowledge him.")
    print("With one swift motion, Adrieth bats the Commander aside, sending him flying into the rubble.")
    print("You hear the Commander’s painful groan as he struggles to get up.")

    adrieth_reacts()


def adrieth_reacts():
    print("\nAdrieth remains completely unaffected by your attacks. His dark aura grows stronger.")
    print(
        "A sense of dread fills you as you realize that no matter what you do, he’s untouchable. Something dark and magical is protecting him.")
    input("\n[Press Enter to decide your next move]")

    player_new_choices()


def player_new_choices():
    print("\nWhat do you do next?")
    print("[1] Keep attacking, hoping to find a weakness.")
    print("[2] Try to retreat and regroup with the other warriors.")
    print("[3] Attempt to find a way around Adrieth’s dark magic.")

    choice = input("\nWhat do you do? (1/2/3): ")

    if choice == "1":
        keep_attacking()
    elif choice == "2":
        retreat()
    elif choice == "3":
        search_for_weakness()
    else:
        print("Invalid choice. Try again.")
        player_new_choices()


def keep_attacking():
    print("\nYou decide to keep fighting, hoping that you’ll find a crack in Adrieth’s defenses.")
    print("You swing again, harder this time. But it’s no use. Adrieth stands like a statue, untouchable.")
    print(
        "As you struggle to keep up the attack, Adrieth suddenly raises his sword, and side swipes you knocking you back and to the ground.")

    player_stunned()


def retreat():
    print("\nRealizing that this fight is impossible to win, you decide to retreat.")
    print("You run back toward the Keep’s inner walls where the warriors are regrouping.")
    print("Adrieth’s forces continue to press the attack, but for now, you’ve escaped immediate danger.")
    input("\n[Press Enter to continue]")
    regroup_with_warriors()


def search_for_weakness():
    print(
        "\nYou take a moment to look around, thinking that there must be something that can explain Adrieth's unnatural power.")
    print(
        "Your eyes catch a glimpse of the dark aura surrounding him. It seems to pulse, as though tied to something... magical.")
    print("Though you don’t understand it, you’re certain now that there’s some magical force protecting him.")

    print("\nAdrieth notices your hesitation and strides toward you, dark energy swirling ominously.")
    input("\n[Press Enter to react]")

    adrieth_final_move()


def adrieth_final_move():
    print("\nAdrieth raises his hand, and with a flick of his wrist, a wave of dark energy surges toward you.")
    print(
        "It hits you full force, sending you crashing to the ground. As your vision blurs, you realize that this battle cannot be won.")
    print("Something more powerful than anything you've ever seen protects Adrieth.")

    input("\n[Press Enter to retreat]")
    regroup_with_warriors()


def player_stunned():
    print("\nDazed from the impact, you struggle to get back on your feet.")
    print("Adrieth turns away, clearly no longer considering you a threat.")

    print("\nWhat do you do?")
    print("[1] Try to get up and keep fighting.")
    print("[2] Retreat to safety and regroup.")

    choice = input("\nWhat do you do? (1/2): ")

    if choice == "1":
        keep_attacking()
    elif choice == "2":
        retreat()
    else:
        print("Invalid choice. Try again.")
        player_stunned()


def regroup_with_warriors():
    print(
        "\nThe clash of metal and screams of the dying fill the air as you and the remaining soldiers scramble to regroup inside the Keep.")
    print(
        "\nYou manage to retreat back to the Keep’s inner walls. The remaining warriors look to you and the wounded Commander for guidance.")
    print("Two warriors stagger toward you, one clutching a deep wound to his side.")
    input("\n[Press Enter to continue]")

    print("\nWarrior 1: 'It's hopeless... the inner walls won’t hold much longer!'")
    print("Warrior 2 wipes blood from his face, looking at you desperately.")
    input("\n[Press Enter to continue]")

    print("\nWarrior 2: 'There’s one last thing we could try.'")
    print(
        "'Legend says a dragon is sealed below the Keep. Releasing it might give us a chance, but it’s uncontrollable.'")
    input("\n[Press Enter to continue]")

    print("\nBefore you can respond, the wounded Commander stumbles in, blood covering his armor.")
    print(
        "Commander: 'What are you talking about?' His voice is stern. 'That dragon is real, but it's a suicide mission! It would kill us all!'")
    input("\n[Press Enter to continue]")

    print("\nYou can see the fear in the eyes of the soldiers. The choice weighs heavily.")

    print("\n[1] Venture below the Keep to release the dragon.")
    print("[2] Stay and help reinforce the inner walls.")

    choice = input("\nWhat will you do? (1/2): ")

    if choice == "1":
        print("\nYou decide to venture below the Keep, against the Commander’s warnings.")
        input("\n[Press Enter to continue]")
        # Continue dragon questline
        venture_to_dragon()

    elif choice == "2":
        print("\nYou stay and help reinforce the inner walls, preparing for the inevitable final stand.")
        input("\n[Press Enter to continue]")
        # Continue battle sequence
        reinforce_inner_walls()

    else:
        print("Invalid choice. Try again.")
        regroup_with_warriors()


def venture_to_dragon():
    print(
        "\nWith a handful of soldiers, you descend into the dark depths of the Keep, the air growing colder with each step.")
    input("\n[Press Enter to continue]")
    enter_dragon_keep_event()


def enter_dragon_keep_event():
    print("You descend into the dark, ancient chamber beneath the Keep.")
    print("The air is thick, and the walls are covered in ancient runes.")
    print("Suddenly, the ground shakes, and a large stone door slams shut behind you, locking you in.")
    print("[Press Enter to continue]")
    input()

    # First event: The Trap
    print("You hear mechanical gears turning in the darkness. A trap is about to be sprung.")
    print("[1] Use Agility to dodge the trap(Requires Agility 18)")
    print("[2] Use Magic to detect enchantments and disable the mechanism(Requires Magic 13)")
    print("[3] Brace for impact using Strength(Requires Strength 15)")
    choice = input("Choose an option: ")

    if choice == '1':
        if player['agility'] >= 18:
            print("You quickly leap to the side, evading a hail of arrows from hidden mechanisms.")
        else:
            print("You attempt to dodge, but you're too slow. Arrows graze your shoulder.(You lose 5 xp)")
            player['xp'] -= 5
    elif choice == '2':
        if player['magic'] >= 13:
            print("You detect a faint magical aura and use a spell to disable the trap.")
        else:
            print("The spell fizzles. The trap triggers and arrows shoot towards you.(-5 xp)")
            player['xp'] -= 5
    elif choice == '3':
        if player['strength'] >= 15:
            print("You brace yourself as the arrows harmlessly bounce off your armor.")
        else:
            print("The arrows are too strong. They pierce through your defenses.(You lose 10 xp)")
            player['xp'] -= 10

    input("[Press Enter to continue]")
    dragons_voice()


def dragons_voice():
    # Second event: The Dragon's Voice
    print("As you survive the trap, a deep, ancient voice echoes through the chamber.")
    print("'Who dares awaken me?' it speaks. The dragon senses your arrival.")
    print("[1] Speak boldly and try to convince the voice you are here to help (Charisma 10 required)")
    print("[2] Investigate the area for clues (Magic 16 required)")
    choice = input("Choose an option: ")

    if choice == '1':
        if player['charisma'] >= 10:
            print("The voice grows softer, intrigued by your confidence.")
            print("'Very well, mortal. Prove your worth.'")
        else:
            print("The voice roars in anger. 'You are nothing to me.'")
    elif choice == '2':
        if player['magic'] >= 16:
            print("You discover an ancient rune etched into the floor. Activating it opens a hidden path.")
        else:
            print("You search, but find nothing. The voice grows impatient.")
    else:
        print("Invalid choice. Try again.")
    input("[Press Enter to continue]")
    path_split_event()


def path_split_event():
    # Third event: Path Split
    print("\nYou reach a fork in the tunnels. One path leads deeper toward the dragon, the other to a secret passage.")
    print("[1] Proceed deeper into the dragon's lair (Strength/Agility)")
    print("[2] Explore the secret passage for hidden knowledge (Magic/Charisma)")
    print("[3] Retreat to the surface (Optional)")
    choice = input("Choose an option: ")

    if choice == '1':
        if player['strength'] >= 10 or player['agility'] >= 10:
            print("You head deeper into the lair, bracing yourself for what's to come.")
        else:
            print("You struggle as the path becomes more perilous. It's dangerous, but you press on.")
    elif choice == '2':
        if player['magic'] >= 8 or player['charisma'] >= 8:
            print("You discover a hidden cache of items that may aid you in the coming fight.")
        else:
            print("The passage is empty, offering no help.")
    elif choice == '3':
        print("You decide to retreat, leaving the depths for another day.")
        input("[Press Enter to continue]")
        reinforce_inner_walls()
    else:
        print("Invalid choice. Try again.")
        path_split_event()
    input("[Press Enter to continue]")
    guardian_event()
    # Handle consequences of retreating here


def guardian_event():
    print(
        "\nAs you traverse the path, you hear the sound of grinding stone. A massive Ancient Guardian stands before you, its stone body crackling with arcane energy.")
    print("[1] Use Agility to dodge its attacks and find a weak spot(Requires Agility 16)")
    print("[2] Use Magic to disable the Guardian’s enchantments(Requires Magic 15)")
    print("[3] Try to overpower the Guardian with Strength(Requires Strength 17)")
    choice = input("Choose an option: ")

    if choice == '1':
        if player['agility'] >= 16:
            print(
                "\nYou nimbly dodge the Guardian's heavy swings, and with a quick strike, you shatter one of its enchanted joints, disabling it.")
        else:
            print(
                "\nYou try to dodge, but the Guardian's attacks are swift. You're hit and sent flying across the room.")
            player['xp'] -= 10
            guardian_event()
    elif choice == '2':
        if player['magic'] >= 15:
            print(
                "\nYou concentrate and channel a spell, disrupting the enchantments binding the Guardian. It collapses into rubble.")
        else:
            print("\nYour magic is not strong enough. The Guardian's energy overwhelms your spell, and it strikes you.")
            player['xp'] -= 10
            guardian_event()
    elif choice == '3':
        if player['strength'] >= 17:
            print(
                "\nYou grapple with the Guardian, using your immense strength to pull apart its stone limbs. It crumbles into pieces.")
        else:
            print("\nThe Guardian's strength is too great. You are struck hard and knocked back.")
            player['xp'] -= 10
            guardian_event()
    input("[Press Enter to continue]")
    runes_event()


def runes_event():
    print(
        "\nAfter defeating the Guardian, you notice glowing runes lining the walls. The runes seem to be part of an ancient binding ritual.")
    print("[1] Investigate the runes (Magic 18 required)")
    print("[2] Ignore the runes and continue on your path")
    choice = input("Choose an option: ")

    if choice == '1':
        if player['magic'] >= 18:
            print(
                "\nYou carefully examine the runes. They seem to be part of a binding ritual meant to keep a powerful creature sealed within the depths.")
            print("You also detect a weak point in the binding. If you choose to, you could break the seal.")
            player['xp'] += 2000
        else:
            print("You try to understand the runes, but their magic is too complex for you to decipher.")
    elif choice == '2':
        print("You decide not to meddle with the ancient magic and move forward, keeping your focus on the mission.")

    input("[Press Enter to continue]")
    dragon_encounter_event()


def dragon_encounter_event():
    print("As you approach the dragon's chamber, you feel a wave of heat and raw power.")
    print("The dragon, its scales black as night, stares at you with burning, ancient eyes.")
    input("[Press Enter to continue]")

    print(
        "The dragon roars, shaking the very foundation of the Keep. 'Why do you come, mortal? I am no ally to your kind.'")
    print("[1] Tell the dragon you wish to unleash it on Adrieth’s forces.")
    print("[2] Stay silent, watching the dragon's reaction.")
    choice = input("Choose an option: ")

    if choice == '1':
        print("You tell the dragon about the battle above, about Adrieth, and your desperate need for its strength.")
        print(
            "The dragon huffs, amused but not convinced. 'You think I will help? Fool. I care not for your wars, only my freedom.'")
        print("[Press Enter to continue]")
        input()

        print(
            "The dragon eyes you, its interest piqued. 'Why do you wish to free me, knowing that I will bring ruin upon your people?'")
        print("[1] Convince the dragon that you have no other choice (Requires 10 Charisma)")
        print("[2] Admit that you only want to cause chaos and weaken Adrieth (Requires 17 Strength)")
        choice = input("Choose an option: ")

        if choice == '1':
            if player['charisma'] >= 10:
                print(
                    "'You think I care about your reasoning?' the dragon growls, but its tone softens. 'Very well, I shall not kill you... yet.'")
            else:
                print(
                    "The dragon laughs darkly. 'Pathetic. You think words will bind me? I’ll destroy everything in my path, including you.'")
                player['xp'] -= 10  # Loses XP for failing charisma
        elif choice == '2':
            if player['strength'] >= 17:
                print("You stand tall, meeting the dragon's gaze. 'I want destruction. I don't care who it hurts.'")
                print(
                    "The dragon snorts, approving. 'At least you're honest, mortal. Perhaps I will spare you in the chaos.'")
            else:
                print(
                    "The dragon doesn't buy it. 'Weak. I could crush you with a thought.' The threat hangs in the air.")
                player['xp'] -= 10  # Loses XP for failing strength
    elif choice == '2':
        print("You stay silent, studying the dragon.")
        print("'Nothing to say? Typical of mortals. Still, you interest me. I will break free, and chaos will follow.'")
        input("[Press Enter to continue]")

    # The dragon breaks free
    print(
        "With a sudden surge of power, the dragon slams its massive claws against the stone, breaking the magical seals.")
    print(
        "'I am free!' it roars, flames erupting from its mouth as it charges toward the surface, intent on wreaking havoc.")

    print("[1] Follow the dragon to the surface and witness the destruction.")
    print("[2] Return to the inner walls and try to regroup with the remaining soldiers.")
    choice = input("Choose an option: ")

    if choice == '1':
        print("\nYou follow the dragon, witnessing its wrath as it tears through the soldiers, both friend and foe.")
        print("Adrieth’s forces are forced to push back in the face of the dragon’s fury.")
        input("[Press Enter to continue]")

        # You can add more events or consequences from here, depending on how the player wants to handle the destruction.
    elif choice == '2':
        print("\nYou decide to return to the inner walls, leaving the dragon to its chaos.")
        print("The sounds of the battle above grow louder as the dragon’s roars fill the sky.")
        input("[Press Enter to continue]")
    return_to_inner_walls()


def return_to_inner_walls():
    print("\nYou return to the inner walls, but the scene is grim. Adrieth's forces have pushed back.\n")
    print(
        "The Keep lies in ruins. Most of the soldiers are dead, and a few survivors are desperately trying to repair the walls.\n")
    input("[Press Enter to continue]")

    print("Amidst the carnage, you see the Commander—his body slumped against the wall, bleeding out.\n")
    print("He looks up at you with a fading gaze, barely able to speak.")
    input("[Press Enter to continue]")

    # Commander gives the player a note with vital information
    print("Commander: 'You... You need to take this note... to the king... of Wallechia...'\n")
    print("With trembling hands, he pulls out a bloodstained note and hands it to you.")
    input("[Press Enter to continue]")

    # Player receives the note
    print("You take the note, the weight of its importance heavy in your hand.\n")
    print("Commander: 'This is... vital... Don't let Adrieth... gain... more power...'\n")
    input("[Press Enter to continue]")

    # Commander urges the player to chase Adrieth
    print("The Commander's voice becomes even weaker as his life fades. His last words are strained and desperate.\n")
    print("Commander: 'You must... chase... after Adrieth... he's heading... toward... Sarth...'")
    input("[Press Enter to continue]")

    print(
        "With those final words, the Commander takes his last breath. You stand in the ruins, holding the note that may hold the key to stopping Adrieth.\n")
    input("[Press Enter to continue]")

    # Player's next objective
    print("Your objective is clear: travel to the Village of Sarth and pursue Adrieth.\n")
    input("[Press Enter to continue]")

    # Next step in the story: Travel to the Village of Sarth
    travel_to_sarth()


# Assuming we continue from the last point, call the return event

def reinforce_inner_walls():
    print(
        "\nYou and the remaining soldiers prepare for the final onslaught, barricading the inner walls and bracing for the enemy forces.")
    print(
        "As you and the remaining warriors hurriedly work to strengthen your defenses, you hear the sounds of battle intensifying outside.\n")
    input("[Press Enter to continue]")

    # First phase: Battle begins
    print("Adrieth's forces surge forward, overwhelming the defenders with sheer numbers.\n")
    print("You grab your weapon and prepare to fight alongside your comrades.\n")
    input("[Press Enter to continue]")

    # Choices during the first phase of battle
    print("As the enemy breaches the outer gates, you have to make a quick decision:\n")
    print("[1] Use Strength to charge into the fray and hold back the attackers.\n")
    print("[2] Use Agility to maneuver around the chaos and flank the enemy.\n")
    choice = input("Choose an option: ")

    if choice == '1':
        if player['strength'] >= 12:
            print("You charge forward, pushing back several foes with brute force.\n")
        else:
            print(
                "You attempt to hold your ground, but the enemy is too strong. You struggle to maintain your position.\n")
            player['xp'] -= 5
    elif choice == '2':
        if player['agility'] >= 10:
            print("You deftly weave through the battle, taking down enemies from the sides.\n")
        else:
            print("You try to maneuver, but your footing slips, and you find yourself overwhelmed.\n")
            player['xp'] -= 5

    input("[Press Enter to continue]")

    # Second phase: The battle escalates
    print("The situation grows dire as more of Adrieth's forces break through. You see your fellow warriors falling.\n")
    print("You hear cries for help and the clash of steel echoing around you.\n")
    input("[Press Enter to continue]")

    print("You have another chance to act:\n")
    print("[1] Rally the troops with a strong voice (Charisma).\n")
    print("[2] Attempt to block the entrance with fallen debris (Strength).\n")
    choice = input("Choose an option: ")

    if choice == '1':
        if player['charisma'] >= 10:
            print("Your voice carries over the chaos, inspiring the remaining soldiers to fight with renewed vigor.\n")
        else:
            print("Your words are lost in the chaos, and the troops falter even more.\n")
            player['xp'] -= 5
    elif choice == '2':
        if player['strength'] >= 15:
            print("With a great effort, you push heavy debris against the entrance, slowing down the enemy advance.\n")
        else:
            print("You struggle to move the debris; it doesn’t hold the entrance as effectively as you hoped.\n")
            player['xp'] -= 10

    input("[Press Enter to continue]")

    # New action: Desperate Defense
    print("As the enemy closes in, you spot a group of soldiers surrounded and outnumbered.\n")
    print("You have a choice:\n")
    print("[1] Rush in to aid your comrades (Strength).\n")
    print("[2] Set a trap to ambush the attackers (Agility).\n")
    choice = input("Choose an option: ")

    if choice == '1':
        if player['strength'] >= 10:
            print("You charge in, using your strength to push back the attackers and save your fellow soldiers.\n")
        else:
            print("You fight bravely, but there are too many foes, and you struggle to save them.\n")
            player['xp'] -= 5
    elif choice == '2':
        if player['agility'] >= 10:
            print("You swiftly set a trap that catches several enemies off guard, buying time for your comrades.\n")
        else:
            print("You attempt to set a trap, but it fails, and you find yourself in danger.\n")
            player['xp'] -= 5

    input("[Press Enter to continue]")

    # Third phase: Knocked out
    print("Just as you think you're turning the tide, Adrieth charges at you, knocking you to the ground.\n")
    print("The world spins as darkness envelops you, and you feel yourself losing consciousness.\n")
    input("[Press Enter to continue]")

    # Player wakes up
    print("You awaken moments later in the inner walls, the sounds of battle still echoing, but it's quieter now.\n")
    print("You struggle to your feet, realizing the grim fate that has befallen your comrades.\n")
    input("[Press Enter to continue]")

    return_to_inner_walls()


def travel_to_sarth():
    print("\nYou gather your remaining strength, taking one last look at the devastated Keep.")
    print("With the note safely tucked away, you begin your journey toward the Village of Sarth.")
    print("The road ahead is uncertain, but the fate of Wallechia depends on what you do next.\n")
    input("[Press Enter to continue]")
    journey_to_village_of_sarth()
