from Game.character_creation import player
from Game.temple_of_forgotten import journey_to_temple_of_forgotten


def proceed_to_wallechia():
    print("\nAfter a long and arduous journey, you find yourself at the edge of the great kingdom of Wallechia.")
    print("You have traversed treacherous lands, faced formidable foes, and completed numerous quests.")
    print("Your level of experience and skill have grown remarkably.")
    input("\nPress Enter to continue...")

    print("\nThe gates of Wallechia stand before you, towering and imposing.")
    print("The city within is a place of grandeur, filled with the hum of activity and the buzz of anticipation.")
    print("As you step through the gates, you feel a sense of both excitement and solemnity.")
    print("You have come a long way, and the final challenge awaits you.")
    input("\nPress Enter to continue...")

    print("\nThe weight of your journey and the gravity of the impending battle with Adrieth feel more real than ever.")
    print("The kingdom’s atmosphere is thick with tension, as if the very air is charged with the upcoming conflict.")
    print("Your heart races with the knowledge that your ultimate test is near.")
    input("\nPress Enter to enter the heart of Wallechia and prepare for confrontation with the king.")

    # Proceed to the final preparations or confrontation
    proceed_to_king()

def proceed_to_king():
    print(
        "\nThe grand halls of the palace are filled with the rich scent of incense and the murmur of courtly affairs.")
    print("You are led to the throne room where the king, a figure of great stature and wisdom, awaits you.")
    print(
        "He looks at you with a mix of respect and anticipation, having heard of your heroic deeds and successes across the land.")
    print("'What news do you bring?' the king inquires, his voice echoing in the hall.")

    print(
        "You step forward, ready to deliver the message, knowing this is your moment to make a difference for the kingdom.")

    input("\nPress Enter to reveal the truth to the king.")
    meet_king2()


def meet_king2():
    print("\nYou clear your throat, feeling the weight of the moment.")
    print("'Your Majesty, we come from the Village of Sarth, where tragedy has struck...'\n")

    print(
        "Kael interjects, 'We found survivors, but there is much more at stake. We learned of Adrieth's plans and the chaos he seeks to unleash.'")
    meet_theking()


def meet_theking():
    print("\nThe king addresses you, his voice resonating with authority and kindness.")
    print("He acknowledges the many trials you have faced and the valor you have shown.")
    print(
        "\nThe king speaks gravely: 'You have proven yourself through countless trials. Now, a final challenge awaits you.'")
    print(
        "He continues, 'Deep within the land lies the Void Realm, a dimension of pure darkness where Adrieth’s fortress resides.'")
    print(
        "The king explains, 'To enter the Void Realm, you must locate the Astral Gate, hidden in the depths of the Temple of the Forgotten.'")
    input("\nPress Enter to continue...")
    king_reward()


def king_reward():
    print("He offers you a choice to recruit a group of his best soldiers if your agility is sufficient.")

    if player['agility'] >= 17:
        print(
            "\n'Your agility allows you to command a group of elite soldiers to aid you in your quest,' says the king.")
        print("He provides you with the soldiers and a map leading to the Temple of the Forgotten.")
    else:
        print(
            "\n'You lack the agility to command my elite soldiers, but I will provide you with guidance and the map to the Temple of the Forgotten.'")

    input("\nPress Enter to receive the map and prepare for your journey...")
    map_and_prepare()


def map_and_prepare():
    # Provide the map and information about the next steps
    print("\nYou receive a detailed map marking the location of the Temple of the Forgotten.")
    print("The map also indicates the path to the Astral Gate within the temple.")
    print("You now know your journey will lead you to the Temple of the Forgotten before you can confront Adrieth.")
    input("\nPress Enter to begin your preparations for the journey to the Temple of the Forgotten.")
    journey_to_temple_of_forgotten()