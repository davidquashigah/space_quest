import random
# below is a demonstration of the runaway scenario

min = 1  # minimum roll
max = 10 # maximum roll

roll_die = ['Y', 'y']

while roll_die == 'y' or 'Y':
    print("Rolling the dice . . .")
    print("You rolled a . . . ")
    roll_result = (random.randint(min, max)) # the roll_result determines the User's attack power, runaway success, and negotative effectiveness.
    print(roll_result)
    break

dex_points = 5 # dexterity  points
monster_lvl = 4 # monster level

# below is a demonstration of the attack scenario, using a 10-sided die.
runaway_chance = (roll_result * dex_points) / (monster_lvl)

if runaway_chance >= 10:
    print("You successfully ran away!")
else :
    roll_die = input("You need to roll a number up to " + str(int(runaway_chance)) + " to successfully runaway. Are you ready to roll [Y/N]? ")

while roll_die == 'y' or 'Y':
    print("Rolling the dice . . .")
    roll_result = (random.randint(min, max)) # the roll_result determines the User's attack power, runaway success, and negotative effectiveness.
    print("You rolled a . . . " + str(roll_result) + "!")
    break

if roll_result <= runaway_chance:
    print("You successfully ran away!")
else:
    print("You did not run away.")


