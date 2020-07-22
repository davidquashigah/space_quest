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

    print("Next, it is time to choose your explorer. \n"
          "Each explorer has their own strengths, weakness, and skills. \n"
          "There are three types of explorers: Marines, Teeps, and Rangers. \n"
          "Which explorer would you like to read about?")

    marine_description = input("Press 'm' or 'M' to read about a short description on the Marines: ")
    if marine_description in ['m', 'M']:
        print("The marines are hard-nosed veterans of the Chrysalis war. \n"
              "They are comfortable in close-quarters combat. \n"
              "Their primary weapons include shotgun-axes, dual-swords, and proton-cannons. \n"
              "Although they have the highest durability, their range is limited and so is their agility. \n"
              "You will find marines behind enemy lines. \n"
              "Are you ready to join the Marines?")

    teep_description = input("Press 't' or 'T' to read about a short description on the Teeps: ")
    if teep_description in ['t', 'T']:
        print("Teeps (or telepaths) are seldom found within the Space xploration Foundation (SEF). \n"
              "Teep civil rights have grown as Alien Space Federations use Teeps for alien-to-alien communication. \n"
              "While low-level Teeps can determine what a person is thinking, high-level teeps can perform brain surgery, read the future, and mind-control. \n"
              "Are you mindful enough to join the Teeps?")

    ranger_description = input("Press 'r' or 'R' to read about a short description on the Rangers: ")
    if ranger_description in ['r', 'R']:
        print("Rangers are never seen, heard, but felt. \n"
              "From miles away, rangers are excellent in long-range battle. \n"
              "Their greatest weapon is their sniper rifle, cover, and beast. \n"
              "Rangers and Marines are always in competition to see which is the dominant military class. \n"
              "Rangers are the only class that use beast to aid them in their quests. \n"
              "Are you prepared to leave the bush, and join the Rangers?")
              "them in their quests.")
            
    while True:
        class_choice = input("So which space explorer will you be? A Marine, a Teep, or a Ranger? [M/T/R] ")

        if class_choice in ['M', 'm', 'T', 't', 'R', 'r']:
            break

    if class_choice in ['m', 'M']:
        print("You are enrolled in Marine Academy " + character_name + "!")
    elif class_choice in ['t', 'T']:
        print("You joined the Intergalactic Teep Alliance, " + character_name + "!")
    elif class_choice in ['r', 'R']:
        print("Your are now among animals as a Ranger, " + character_name + "!")

intro()
