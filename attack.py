import random
# below is a demonstration of the attack scenario

min = 1  # minimum roll
max = 10 # maximum roll

roll_die = ['Y', 'y']

def attack(str_points, wpn_atk):
    while roll_die == 'y' or 'Y':
        print("Rolling the dice . . .")
        print("You rolled a . . . ")
        roll_result = (random.randint(1, 10)) # the roll_result determines the User's attack power, runaway success, and negotative effectiveness.
        print(roll_result)
        break

    max_atk_dmg = str_points * wpn_atk
    print(max_atk_dmg)
    atk_dmg = max_atk_dmg * int(roll_result) / 10
    print("You did " + str(int(atk_dmg)) + " points of damage!")

attack(10,2)
