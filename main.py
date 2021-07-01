import time
import random
import sys

player_next_turn = [
    "Your turn...",
    "Go...",
    "Please proceed...",
    "Lets win this...",
    "Are you ready?  ",
    "",
]

snakes = {
    27:5,
    40:3,
    43:18,
    54:31,
    66:45,
    76:58,
    89:53,
    99:41
}

ladders = {
    4:25,
    13:46,
    33:49,
    42:63,
    50:69,
    62:81,
    74:92
}

def welcome():
    print('\nWelcome to Snakes and Ladders game.\n'+
    'Developed by: Konda Jayant Reddy\n'+
    '\n'+
    'Rules:\n'+
    '   1. The players will move their pieces starting at 0, following the numbers on the board. If a player rolls a 4, then the player would move their piece four places.\n'+
    '   2. The first player to get to the final position i.e., 100 will be the winner.\n'+
    '   3. When a player lands on a top of a snake, their playing piece will slide down to the bottom of the snake.\n'+
    '   4. When a player lands at the base of a ladder, it immediately climbs to the top of the ladder.\n'+
    '   5. Hit ENTER to roll the dice.\n'
    )

def roll_dice():
    time.sleep(1)

    value = random.randint(1,6)
    print('The dice value is '+str(value))
    
    return value

def snake_slide(name,prev,current):
    print('\nDang!')
    print(name + ' has been bit by the snake from ' + str(prev) + ' to ' + str(current) + '\n')

def ladder_jump(name,prev,current):
    print('\nYaayyyy!!!')
    print(name + ' climbed the ladder from ' + str(prev) + ' to ' + str(current) + '\n') 

def game_counter(name, current, dice):
    time.sleep(1)

    prev = current
    current = current + dice
    if current<101:
        print('\n'+ name + ' moved from ' + str(prev) + ' to ' + str(current) + '\n')
    else:
        print("Can't move further...")

    if current > 100:
        print(name + ' needs more ' + str(100 - prev) + ' to win the game.\n')
        return prev
    
    if current in snakes:
        final = snakes[current]
        snake_slide(name, current, final)

    elif current in ladders:
        final = ladders[current]
        ladder_jump(name,current,final)

    else:
        final = current

    return final

def winner(name,position):
    time.sleep(1)

    if position == 100:
        if name == 'Computer':
            print('You have lost the game :(')
            print('Better Luck Next Time.....\n')

        else:
            print('Congratulations ' + name + '!!!')
            print('You have won the game.....\n')
            print('\nThank You for playing the game.\n')

        sys.exit(1)
    
welcome()
time.sleep(1)

player = None
while not player:
    player = input("Please enter a valid name for the player: ").strip()

comp = 'Computer'

player_pos = 0
comp_pos = 0

while(1):
    time.sleep(1)

    input_ = input('\n' + player + ', ' + random.choice(player_next_turn) + ' Hit ENTER to roll the dice: ')
    print('Rolling the dice....')
    value = roll_dice()
    while value%6 == 0:
        value+=roll_dice()

    print(player + ' is moving.....')
    player_pos = game_counter(player,player_pos,value)

    winner(player,player_pos)

    time.sleep(1)

    print('\nComputer is rolling the dice.....')
    value = roll_dice()
    while value%6 == 0:
        value+=roll_dice()

    print(comp + ' is moving.....')
    comp_pos = game_counter(comp,comp_pos,value)

    winner(comp,comp_pos)
