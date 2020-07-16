def intro():

    print("Welcome to Space Quest, a text-based sci-fi game!")
    print("Before you can start, you need to choose your character name and class.")

    character_name = input("What is the name of your explorer? ")
    print("Are you sure you want your character name to be " + character_name +"?")

    name_check = input("Type 'y', 'Y', 'yes', 'Yes', or 'YES' to keep this character name: ")

    if name_check in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print("Okay, welcome to the Universe " + character_name + "!")
    else:
        character_name = input("What is the name of your explorer? ")
        print("Welcome to Space Quest, " + character_name + "!")

    print("Next, it is time to choose your explorer.")
    print("Each explorer has their own strengths, weakness, and skills.")

    print("There are three types of explorers: Marines, Teeps, and Rangers.")

    print("Which explorer would you like to read about?")

    marine_description = input("Press 'm' or 'M' to read about a short description on the Marines: ")
    if marine_description in ['m', 'M']:
        print("The marines are hard-nosed veterans of the Chrysalis war. "
              "They are comfortable in close-quarters combat. "
              "Their primary weapons include shotgun-axes, dual-swords, and "
              "proton-cannons.  Although they have the highest durability, "
              "their range is limited and so is their agility. You will find "
              "marines behind enemy lines. Are you ready to join the Marines?")

    teep_description = input("Press 't' or 'T' to read about a short description on the Teeps: ")
    if teep_description in ['t', 'T']:
        print("Teeps (or telepaths) are seldom found within the Space "
              "Exploration Foundation (SEF). Teep civil rights have grown "
              "steadily as Alien Space Federations use teeps for alien-alien "
              "communication. While low-level teeps can determine the colour "
              "in a person’s mind, high-level teeps can perform brain "
              "surgery, read the future, and mind-control. Are you mindful?")

    ranger_description = input("Press 'r' or 'R' to read about a short description on the Rangers: ")
    if ranger_description in ['r', 'R']:
        print("Rangers are never seen, heard, but felt. From miles away, "
              "rangers are excellent in long-range battle. Their greatest "
              "weapon is their sniper, and cover. Rangers and Marines are "
              "always in competition to see which is the dominant military "
              "class. Rangers are the only class that use animals to aid "
              "them in their quests.")

    print("Did you get all that?")

    print("So which space explorer will you be? A Marine, a Teep, or a Ranger?")

# Work on choosings hero class

    class_choice = input("Press 'm' or 'M' to enroll in the Marine Academy: "
    "press 't' or 'T' to join the Intergalactic Teep Alliance: "
    "press 'r' or 'R' to unite with your animal friends among the Rangers: ")

    class_choice = ()
    if class_choice in ['m', 'M']:
        print("You are enrolled in Marine Academy " + character_name + "!")
    if class_choice in ['t', 'T']:
        print("You joined the Intergalactic Teep Alliance " + character_name + "!")
    if class_choice in ['r', 'R']:
        print("Your are now among animals as a Ranger " + character_name + "!")
    else:
        input("Press 'm' or 'M' to enroll in the Marine Academy: "
    "press 't' or 'T' to join the Intergalactic Teep Alliance: "
    "press 'r' or 'R' to unite with your animal friends among the Rangers: ")



intro()