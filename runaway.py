import random
# below is a demonstration of the attack scenario

min = 1  # minimum roll
max = 10 # maximum roll

roll_die = ['Y', 'y']

while roll_die == 'y' or 'Y':
    print("Rolling the dice . . .")
    print("You rolled a . . . ")
    roll_result = (random.randint(min, max)) # the roll_result determines the User's attack power, runaway success, and negotative effectiveness.
    print(roll_result)
    break

dex_points = 30 # dexterity  points

# below is a demonstration of the attack scenario, using a 10-sided die.
runaway_chance = roll_result * dex_points / 10
print(runaway_chance)


