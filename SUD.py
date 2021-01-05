"""
Team member: Sean Yang & Vincent Wang
"""
import random
import sys
import doctest


def intro():

    print(
        'You are a hardworking student in the prestigious BCIT CST program. It is the time of the year for midterm exam week again... \n \n Tonight is a Thursday night. You finished most of your midterms for other courses, leaving only one python midterm hackathon left to do on Friday. \n \n While you were studying hard for this last python midterm in your room, a mysterious voice, coming from nowhere, hypnotized you. \n \n When you finally regained your consciousness, you found out that you had been trapped inside a mysterious space with invisible walls around you. \n \n'
    )

    print(
        'Suddenly, you see a very handsome man with a long beard. As this man approaches you, he begins to talk: "Greeting. I am Chris. I am here to assist you, Programmer." \n \n As Handsome Chris introduces himself, he begins to explain your situation with you. \n \n'
    )

    print(
        '"Unfortunately, you have been trapped inside your own nightmare in perpetuity by a mysterious evil force. \n \n In order to wake up from your nightmare and make it to your midterm hackathon on time, you must follow my instructions." \n \n'
    )

    print(
        '"I want to play a game." \n \n Says Handsome Chris, "In this game, you are trapped inside a 5*5, 25-cell mysterious space. \n \n Here you can enter [1, 2, 3, 4] to represent the north, south, east, and west to walk around in this space. \n \n However, when you reach the edge of the space, you will be blocked by an invisible wall. \n \n You have a starting 10 health points and 1d6 attack power. \n \n Each time you take a step, you will have a 25% chance of encountering a monster named Bug that looks like a bug, smells like a bug, and buzz like a bug. \n \n The monsters have 5 health points and 1d6 attack power. \n \n When you encounter a monster, you can choose to escape or fight until one party dies. \n \n If you choose to flee, the monster has a 10% chance to stab you back and deal 1d4 damage. If you choose to fight, it will be combat to the death. \n \n Before the start of each round of the battle, a 1d20 first strike decision will be made, and the party with the larger roll will strike first. \n \n The battle is over when either one of you dies. \n \n When you are not in battle, you can get 2 points of health regeneration if you move a step without encountering any monsters. \n \n If you successfully  survive without dying, you win! \n \n Another version of you will pass the midterm Hackathon in a parallel universe. \n \n If you die, you will lose and fall into a 72-hour sleep, thus missing your hackathon and weekend in this universe."'
    )


def get_user_name():
    """Prompt users to enter their name.

    :precondition: users input must not be "quit"
    :postcondition: return users' input as string
    :return: a string of users' input
    """
    return exit_the_game(input('Tell me your name, programmer.\n').upper())


def get_user_choice():
    """Prompt users to enter the direction they wish to go.

    :precondition: users input must be one of range(1, 4) that represent north, south, west, east and not be "quit"
    :postcondition: adjust player's coordinate base on their directional input.
    :return: a list representing player's updated coordinate.
    """
    return exit_the_game(
        input(
            'Tell me a number that represent the direction you want to go, programmer.\n [1 = north, 2 = south, 3 = west, 4 = east]\n'
        ))


def flee_or_not():
    """Prompt users to enter Y or N to represent their wish to flee or fight.

    :precondition: users input must be Y/N and not "quit"
    :postcondition: return "Y" or "N" as string
    :return: a string of "Y" or "N" to represent users' input
    """
    return exit_the_game(
        input("You want to flee like a coward? [Y/N]\n").upper())


def exit_the_game(play_input):
    """Quit the game if user enter "quit".
    
    :parameter play_input: a string
    :precondition: user must input "quit" to quit the game.
    :postcondition: quit the game if user input "quit". Otherwise return user input.
    :param play_input: user input strings.
    :return: user input string.
    """
    if play_input.lower() == 'quit':
        print("You quit the game.")
        sys.exit()
    else:
        return play_input


def make_board():
    """create a 2D list as the board of the game.

    :precondition: no precondition; function will always execute
    :postcondition: create a 5*5 2D list 
    :return: A 2D list act as the board of the game.
    """
    board = []
    (BOARD_ROW, BOARD_COLUMN) = (5, 5)
    for column in range(1, BOARD_COLUMN + 1):
        rows = []
        for row in range(1, BOARD_ROW + 1):
            rows.append(row)
        board.append(rows)
    return board


def make_character(player_name, board):
    """Create a new character

    Create new character profile for new player_name
    
    :param player_name: a string representing the player's name
    :param board: a two dimensional list representing the whole dungeon
    :precondition: board has to be a list which contains five [1,2,3,4,5] as its element.
    :postcondition: generate character profile with correct information
    :return: a list which contain the player's name, its health, start x position and y position within board.
    
    """
    position_x = random.randint(1, len(board[0]))
    position_y = random.randint(1, len(board))
    health = 10
    return [position_x, position_y, health, player_name]


def move_character(character, direction):
    """Move character towards given direction

    Move character's current position by 1 towards given direction

    :param character: a one dimensional list containing the character's current status
    :param direction: a string which contains an integer representing a specific direction, '1' = north, '2' = south, '3' = west, '4' = east
    :precondition: character list must contains character's current x and y position, its heal and name in order;
    direction must be one of 1, 2, 3, 4
    :postcondition: move character's position by one towards correct direction
    :return: None

    >>> test_character = [2, 3, 6, 'test_player']
    >>> move_character(test_character, '1')
    >>> print(test_character)
    [2, 4, 6, 'test_player']

    >>> test_character = [2, 3, 6, 'test_player']
    >>> move_character(test_character, '2')
    >>> print(test_character)
    [2, 2, 6, 'test_player']

    >>> test_character = [2, 3, 6, 'test_player']
    >>> move_character(test_character, '3')
    >>> print(test_character)
    [1, 3, 6, 'test_player']

    >>> test_character = [2, 3, 6, 'test_player']
    >>> move_character(test_character, '4')
    >>> print(test_character)
    [3, 3, 6, 'test_player']
    """
    if direction == '1':
        character[1] += 1
    elif direction == '2':
        character[1] -= 1
    elif direction == '3':
        character[0] -= 1
    elif direction == '4':
        character[0] += 1


def validate_and_move(character, direction, board):
    """Validate a move and move a character

    Validate if a move is valid, perform the move if it is valid

    :param character: a one dimensional list containing the character's current status
    :param direction: a string which contains an integer representing a specific direction, '1' = north, '2' = south, '3' = west, '4' = east
    :param board: a two dimensional list representing the whole dungeon
    :precondition: character list must contains character's current x and y position, its heal and name in order;
    direction must be one of 1, 2, 3, 4; board has to be a list which contains five [1,2,3,4,5] as its element.
    :postcondition: Correctly validate a move; perform the corresponding move if it is valid
    :return: True if the move is valid; Otherwise reture False and print error message if needed

    >>> test_board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    >>> test_player = [3,5,3,'Peter']
    >>> validate_and_move(test_player, "1", test_board)
    Ah, you can't go that way.
    False
    >>> test_board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    >>> test_player = [3,5,3,'Peter']
    >>> validate_and_move(test_player, "2", test_board)
    True
    >>> test_board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    >>> test_player = [1,5,3,'Peter']
    >>> validate_and_move(test_player, "3", test_board)
    Ah, you can't go that way.
    False
    >>> test_board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    >>> test_player = [1,5,3,'Peter']
    >>> validate_and_move(test_player, "4", test_board)
    True
    >>> test_board = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    >>> test_player = [3,5,3,'Peter']
    >>> validate_and_move(test_player, 'wasd', test_board)
    Sorry, I can't understand you.
    False
    """
    directions = ("1", "2", "3", "4")
    if direction in directions:
        initial_position_x = character[0]
        initial_position_y = character[1]
        move_character(character, direction)
        if character[0] not in range(1, len(board[0]) + 1):
            character[0] = initial_position_x
            print("Ah, you can't go that way.")
            return False
        elif character[1] not in range(1, len(board) + 1):
            character[1] = initial_position_y
            print("Ah, you can't go that way.")
            return False
        else:
            return True
    else:
        print("Sorry, I can't understand you.")
        return False


def check_back_stab():
    """Check if player got back stabbed

    Check if the player got back stabbed by the monster, which has 10% chance to happen

    :precondition: no precondition, the function will always execute successfully
    :postcondition: return 10 in randint(1, 10) representing a 10% chance of backstabbing, otherwise it return nothing to represent false
    :return: a integer 10 if random.randint(1, 10) == 10
    """
    return random.randint(1, 10) == 10


def health_regen(character):
    """Regenerate Player's health points if they are in range(1, 9).
    
    :param character: a 1D list representing player's status
    :precondition: character[2], aka player's health, must be in range(1, 9)
    :postcondition: player's HP will +2 if they are in range(1, 8),+1 if they are 9
    :return: None
    >>> test_character = [2, 3, 6, 'test_player']   
    >>> health_regen(test_character)
    >>> print(test_character[2])
    8
    >>> test_character = [2, 3, 9, 'test_player']   
    >>> health_regen(test_character)
    >>> print(test_character[2])
    10
    >>> test_character = [2, 3, 10, 'test_player']   
    >>> health_regen(test_character)
    >>> print(test_character[2])
    10
    """
    if 1 <= character[2] <= 8:
        character[2] += 2
    elif character[2] == 9:
        character[2] = 10


def check_for_monsters():
    """check if player encounter monsters when they move.

    Check if the player encounter monsters when they move, which has 25% chance to happen.

    :precondition: no precondition, the function will always execute successfully
    :postcondition: return 4 in randint(1, 4) representing a 25% chance of encounter, otherwise it return nothing to represent false
    :return: a integer 4 if random.randint(1, 4) == 4
    """
    return random.randint(1, 4) == 4


def flee(player_health):
    """check if player take damage from backstabbing when fleeing.

    check if player take damage from backstabbing when fleeing. If they do, minus the damage from player's HP.
    
    :parameter player_health: a integer in the list representing player's HP
    :precondition: must be a positive integer
    :postcondition: player_health - random.randint(1, 4) if they got back-stabbed
    :return: a integer representing player's updated health points
    """
    if check_back_stab():
        damage = random.randint(1, 4)
        player_health -= damage
        print(
            f"While you are busy fleeing the scene, your enemy back-stabs you and deal {damage} damage!"
        )
    else:
        print("You successfully escape! Live to fight another day!")
    return player_health


def dead(health):
    """check if player is dead.

    chec if target's health is less than or equal to zero

    :precondition: health must be an integer
    :postcondition: tell if the target is dead or not correctly
    :return: True if target health is below 0; otherwise return False
    
    >>> dead(-2)
    True
    >>> dead(0)
    True
    >>> dead(2)
    False
    """
    return health <= 0


def get_initiative():
    """Create initiative value in a combat

    Create initiative value for both player and monster
    
    :precondition: no precondition, the function will always execute successfully
    :postcondition: correctly create two initiative value for both player and monster
    :return: a list which first element representing the player's initiative value and the second representing the monster's initiative value
    """
    return [random.randint(1, 20), random.randint(1, 20)]


def deal_random_damage(health):
    """Deal random damage to given health
    
    Reduce health value by a random damage integer from 1 to 6

    :param health: an integer representing the target's health
    :precondition: health must be a integer
    :postcondition: reduced health by correct amount with in 1 to 6 inclusive
    :return: an integer damaged health; print out damage information
    """
    damage = random.randint(1, 6)
    health -= damage
    print(f"The strike deal {damage} damage!")
    return health


def player_initiative_combat(character_health, monster_health, initiative):
    """Create fight result for a player initiative combat

    Create the result health for both player and monster after a player initiative combat

    :param character_health: an integer representing the player's health
    :param monster_health: an integer representing the monster's health
    :param initiative: a list contain initiative values for both the player and monster
    :precondition: player's health must be a integer between 1 to 10 inclusive; monster's health must be a integer between 1 to 5 inclusive, initiative must be a list contain initiative values between 1 to 20 inclusive for both the player and monster
    :postcondition: create correct health result for both player and monster
    :return: a list contains damaged character_health and damaged monster_health; and print statements about battle result
    """
    print(
        f"You roll {initiative[0]} and your silly opponent roll {initiative[1]}, "
        f"now it's your turn to punish the bug!")
    monster_health = deal_random_damage(monster_health)
    if not dead(monster_health):
        print(
            f"The bug is still alive with {monster_health} remaining! It is about to strike you back!"
        )
        character_health = deal_random_damage(character_health)
        if not dead(character_health):
            print(
                f"You still have {character_health} health! Let's revenge in the next round of fight!"
            )
        else:
            print(f"You run out of HP. You are defeated by a runtime error.")
    else:
        print(f"The bug's HP is now 0. You killed the bug!")
    return [character_health, monster_health]


def monster_initiative_combat(character_health, monster_health, initiative):
    """Create fight result for a monster initiative combat

    Create the result health for both player and monster after a monster initiative combat

    :param character_health: an integer representing the player's health
    :param monster_health: an integer representing the monster's health
    :param initiative: a list contain initiative values for both the player and monster
    :precondition: player's health must be a integer between 1 to 10 inclusive; monster's health must be a integer between 1 to 5 inclusive, initiative must be a list contain initiative values between 1 to 20 inclusive for both the player and monster
    :postcondition: create correct health result for both player and monster
    :return: a list contains damaged character_health and damaged monster_health, or a list contain the original health result if initiative roll is draw; and print statements about battle result
    """
    if initiative[0] == initiative[1]:
        print(
            f"You roll {initiative[0]} and your silly opponent roll {initiative[1]}, no one is hurt!"
        )
    else:
        print(
            f"You roll {initiative[0]} and your silly opponent roll {initiative[1]}, "
            f"hang in there, the bug is about to strike you!")
        character_health = deal_random_damage(character_health)
        if not dead(character_health):
            print(
                f"Brave warrior! You are still alive with {character_health} HP. Now it's your time to fight back!"
            )
            monster_health = deal_random_damage(monster_health)
            if not dead(monster_health):
                print(
                    f"The bug still have {monster_health} health left! It seems angry!"
                )
            else:
                print(f"The bug's HP is now 0. You killed the bug!")
        else:
            print(f"You run out of HP. You are defeated by a runtime error.")
    return [character_health, monster_health]


def combat_single_round(character_health, monster_health):
    """Determine if player or monster can attack first each combat round.

    Determine whose initiative roll is larger and can attack first.

    :param character_health: an integer representing the player's health
    :param monster_health: an integer representing the monster's health
    :precondition: both parameter must be positive integers
    :postcondition: whoever rolls is larger initiates the combat
    :return: a list consists of 2 integer representing the updated health of player and monster, and a nested list representing who attack first.   
    """
    initiative = get_initiative()
    if initiative[0] > initiative[1]:
        combat_single_round_result = player_initiative_combat(
            character_health, monster_health, initiative)
    else:
        combat_single_round_result = monster_initiative_combat(
            character_health, monster_health, initiative)
    return combat_single_round_result


def combat_result(player_health):
    """Update and return player's health after the combat.

    :param player_health: an integer representing the target's health
    :precondition: health must be a integer
    :postcondition: update the health by correct amount after the combat deductions
    :return: an integer representing player's updated health points
    """
    print("A wild runtime error jumps out from the bush! Let the fight begin!")
    monster_health = 5
    if flee_or_not() == 'Y':
        player_health = flee(player_health)
    else:
        while player_health > 0 and monster_health > 0:
            combat_result_single_round = combat_single_round(
                player_health, monster_health)
            player_health = combat_result_single_round[0]
            monster_health = combat_result_single_round[1]
    return player_health


def main():
    """
    
    Drive the program
    
    """
    doctest.testmod()
    intro()
    board = make_board()
    character = make_character(get_user_name(), board)
    while not dead(character[2]):
        print(
            f'{character[-1]}, you are now standing on ({character[0]},{character[1]}) with {character[2]} health.'
        )
        direction = get_user_choice()
        if validate_and_move(character, direction, board):
            if check_for_monsters():
                character[2] = combat_result(character[2])
            else:
                health_regen(character)
                print("You are safe and immersed in a healing breeze.")
    print(f"You health bar is empty and you are dead. End of game.")


if __name__ == '__main__':
    main()
