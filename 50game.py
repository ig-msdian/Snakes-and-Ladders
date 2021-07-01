import random

roll_again = 'yes'

P1pos = 0
P2pos = 0

while P1pos < 50 and P2pos < 50:
    while roll_again.lower() == "yes" or roll_again == "y":
        print("Rolling the dice...")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print('P1, You rolled a ' + str(dice1))
        P1pos = P1pos + dice1
        if (P1pos) > 50:
            print("Oopsie! You couldn't hit the right one! Try again!")
            P1pos = P1pos - dice1
        print('P1, You are in the positon ' + str(P1pos))

        if P1pos == 6:
            P1pos = 14
            print('Yay! You caught a ladder!\n')
            print('P1: You are standing on ' + str(P1pos))

        if P1pos == 11:
            P1pos = 29
            print('Yay! You caught a ladder!\n')
            print('P1: You are standing on ' + str(P1pos))

        if P1pos == 17:
            P1pos = 36
            print('Yay! You caught a ladder!\n')
            print('P1: You are standing on ' + str(P1pos))

        if P1pos == 18:
            P1pos = 39
            print('Yay! You caught a ladder!\n')
            print('P1: You are standing on ' + str(P1pos))

        if P1pos == 27:
            P1pos = 33
            print('Yay! You caught a ladder!\n')
            print('P1: You are standing on ' + str(P1pos))

        if P1pos == 37:
            P1pos = 43
            print('Yay! You caught a ladder!\n')
            print('P1: You are standing on ' + str(P1pos))

        if P1pos == 16:
            P1pos = 3
            print('Oh, drat! A snake caught you!')
            print('P1: You are standing on ' + str(P1pos))

        if P1pos == 22:
            P1pos = 20
            print('Oh, drat! A snake caught you!')
            print('P1: You are standing on ' + str(P1pos))

        if P1pos == 34:
            P1pos = 26
            print('Oh, drat! A snake caught you!')
            print('P1: You are standing on ' + str(P1pos))

        if P1pos == 47:
            P1pos = 35
            print('Oh, drat! A snake caught you!')
            print('P1: You are standing on ' + str(P1pos))

        if P1pos == 50 and P2pos != 50:
            print('P1: Congrats! You have won!')
            break

        print('P2 rolled a ' + str(dice2))
        P2pos = P2pos + dice2
        if (P2pos) > 50:
            print("Oopsie! You couldn't hit the right one, P2! Try again!")
            P2pos = P1pos - dice2
        print('P2, You are in the positon ' + str(P2pos))

        if P2pos == 6:
            P2pos = 14
            print('Yay! P2 caught a ladder!\n')
            print('P2 is standing on ' + str(P2pos))

        if P2pos == 11:
            P2pos = 29
            print('Yay! P2 caught a ladder!\n')
            print('P2 is standing on ' + str(P2pos))

        if P2pos == 17:
            P2pos = 36
            print('Yay! P2 caught a ladder!\n')
            print('P2 is standing on ' + str(P2pos))

        if P2pos == 18:
            P2pos = 39
            print('Yay! P2 caught a ladder!\n')
            print('P2 is standing on ' + str(P2pos))

        if P2pos == 27:
            P2pos = 33
            print('Yay! P2 caught a ladder!\n')
            print('P2 is standing on ' + str(P2pos))

        if P2pos == 37:
            P2pos = 43
            print('Yay! P2 caught a ladder!\n')
            print('P2 is standing on ' + str(P2pos))

        if P2pos == 16:
            P2pos = 3
            print('Oh, drat! A snake caught P2!')
            print('P2 is standing on ' + str(P2pos))

        if P2pos == 22:
            P2pos = 20
            print('Oh, drat! A snake caught P2!')
            print('P2 is standing on ' + str(P2pos))

        if P2pos == 34:
            P2pos = 26
            print('Oh, drat! A snake caught P2!')
            print('P2 is standing on ' + str(P2pos))

        if P2pos == 47:
            P2pos = 35
            print('Oh, drat! A snake caught P2!')
            print('P2 is standing on ' + str(P2pos))

        if P2pos == 50 and P1pos != 50:
            print(
                'P2: Congrats! You have won! And P1, a computer beat you. Suck on that!'
            )
            break
        roll_again = input("Do you want to continue? Press yes or y.\n")
