def basic_actions:

# prompt the user with possible
while True:
    basic_action = input("Do you want to:\n A) Attack\n B) Runaway \n C) Negotiate?\n [A/B/C]: ")
    if basic_action in ['A', 'B', 'C']:
        break
if basic_action == "A":
    print("You choose to attack!")
if basic_action == "B":
    print("You attempt to runaway!")
elif basic_action == "C":
    print("You attempt to negotiate.")

# create functions for each basic action
# Attack power =  strength_points * weapon_points