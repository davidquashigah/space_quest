# this is a demonstration of the multiple choice questionnaire

while True:
    basic_action = input("Do you want to:\n "
                         "A) Attack \n "
                         "B) Runaway \n "
                         "C) Negotiate\n "
                         "[A/B/C]: ")
    if basic_action in ['A', 'a', 'b', 'B', 'c', 'C']:
        break

if basic_action == "a" or "A":
    print("You choose to attack!")

elif basic_action == "b" or "B":
    print("You attempt to runaway!")

else:
    print("You attempt to negotiate.")
