"""
Developed by Sepehr Zohoori Rad
"""

import random
import itertools
import math


def quit_game():
    """
    Quit game after confirmation.
    """
    print("Are you sure you want ot quit? Type \"y\" to confirm: ", end="")
    player_choice = input()
    if player_choice == "y":
        exit()


def check_alive(character):
    """
    Check if character is alive.

    :param character: A dictionary that contains the character stats.
    :precondition: character dictionary must include 'HP'.
    :postcondition: Does not alter the character dictionary in any way.
    :return: True if character is alive. Else False.

    >>> test_character = {'HP': 5}
    >>> check_alive(test_character)
    True

    >>> test_character = {'HP': 0}
    >>> check_alive(test_character)
    False
    """
    return character["HP"] > 0


def clear_console():
    """
    Print 100 new lines to provide a clear console
    """
    print("\n" * 100)


def show_stats(character):
    """
    Print character stats.

    A function that prints the character stats nicely formatted for the player.

    :param character: A dictionary that contains the character stats.
    :precondition: Keys needed for this function to work: 'HP', 'Energy', 'Max HP, 'Max Energy'
                   'Name', 'Clan', 'XP', 'Max XP', 'Level', 'Special Ability', 'Damage',
                   'Special Ability Description', 'Enemies Slain'.
    :postcondition: Does not alter character in any way.
    """
    print(f"\nYour stats:\n"
          f"Health: {character['HP']} / {character['Max HP']}  |  "
          f"Energy: {character['Energy']} / {character['Max Energy']}  |  "
          f"Damage: {character['Damage']}\n"
          f"Name: {character['Name']}  |  Clan: {character['Clan']}\n\n"
          f"Experience: {character['XP']} / {character['Max XP']}  |  Level: {character['Level']}"
          f"  |  Enemies Slain: {character['Enemies Slain']}\n\n"
          f"Special Ability: {character['Special Ability']}\n"
          f"    Description: {character['Special Ability Description']}\n"
          f"    Energy Cost: 50\n")


def print_character_combat_stats(character):
    """
    Print character's combat-relevant stats.

    A function that prints the character's combat relevant stats nicely formatted for the player.
    :param character: A dictionary that contains the character stats.
    :precondition: Keys needed for this function to work: 'HP', 'Energy', 'Max HP, 'Max Energy'
                   'Name', 'Clan', 'XP', 'Max XP', 'Damage'
    :postcondition: Does not alter character in any way.
    """
    print(f"{character['Name']} --  HP: {character['HP']}/{character['Max HP']} | "
          f"Energy: {character['Energy']}/{character['Max Energy']} | Damage:"
          f" {character['Damage']}")


def print_enemy_combat_stats(enemy):
    """
    Print enemy's combat-relevant stats.

    A function that prints the enemy's combat relevant stats nicely formatted for the player.

    :param enemy: A dictionary that contains the enemy stats.
    :precondition: Keys needed for this function to work: 'HP', 'Max HP, 'Name', 'Damage'
    :postcondition: Does not alter enemy in any way
    """
    print(f"{enemy['Name']} -- HP: {enemy['HP']}/{enemy['Max HP']} | Damage: {enemy['Damage']}")


def initialize_game():
    """
    Initialize game

    A function that prints the start of game messages, and prompts the player to choose their
    character's name and clan.

    :return name: A string containing the character's chosen name
    :return clan: A string containing the character's chosen clan
    """
    print("After a long travel, you finally step up to the gates. A woman shouts at you:\n"
          "\"Welcome challenger! You have approached the Arena of Blood.\n"
          "Tell us which clan you are from if you wish to be granted entry.\"")
    clans = ("Warriors of Amazon", "Priests of Atlantis", "Shape Shifters of Narnia")
    clan = get_player_choice(clans)
    if clan == clans[0]:
        print("\"Ah! A warrior. I also used to be a part of the sisterhood once.\n"
              "What is your name warrior?\"")
    elif clan == clans[1]:
        print("\"A priest at the arena of blood? Have you lost your way father?\n"
              "Tell us your name priest!\"")
    else:
        print("\"A Shape Shifter! My sisters used to go crazy for your kind back in the Amazons.\n"
              "What is your name shape shifter?\"")
    name = input()
    print(f"\"{name} of the {clan}, welcome to the Arena of Blood!\"\n"
          f"The gates of the arena swing open with a loud screech.\n"
          f"\"The Goddess of The Red Moon is awaiting you on the other side of the arena.\n"
          f"Find you way through the halls to get to her.\n"
          f"On your way, you may come across other challengers that are in the arena.\"\n")
    input("Press Enter to step into the arena.")
    return name, clan


def make_character(name, clan):
    """
    Create the character.

    A function that generates a dictionary containing the character's stats. Stats are
    represented by key-value pairs. Stats that are generated in this function are:
    'HP', 'Energy', 'Max HP, 'Max Energy', 'Name', 'Clan', 'XP', 'Max XP', 'Level', 'Damage',
    'Special Ability', 'Special Ability Description', 'Enemies Slain', 'Position',
    'Previous Position'.

    :param name: A string containing the character's chosen name
    :param clan: A string containing the character's chosen clan
    :precondition: name must be a string.
    :precondition: clan must be one of the following strings
                   "Warriors of Amazon", "Priests of Atlantis", "Shape Shifters of Narnia"
    :postcondition: return character with class specific stats.
    :return: A dictionary containing the correct character stats

    >>> make_character("Test Name", "Warriors of Amazon")
    {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0), \
'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3, 'Enemies Slain': 0, 'HP': 125, \
'Energy': 100, 'Damage': 22, 'Special Ability': 'Execute', \
'Special Ability Description': 'You strike your opponent with the intent to kill. This deals 2x \
your damage and instantly kills them if they are below 15% HP.', \
'Max HP': 125, 'Max Energy': 100}
    """
    clans = ("Warriors of Amazon", "Priests of Atlantis", "Shape Shifters of Narnia")
    character = {"Name": name, "Clan": clan, "Position": (0, 0),
                 "Previous Position": (0, 0), "Level": 1, "XP": 0, "Max XP": 3,
                 "Enemies Slain": 0}

    if clan == clans[0]:  # Warrior
        character["HP"] = 125
        character["Energy"] = 100
        character["Damage"] = 22
        character["Special Ability"] = "Execute"
        character['Special Ability Description'] = "You strike your opponent with the intent to " \
                                                   "kill. This deals 2x your damage and instantly" \
                                                   " kills them if they are below 15% HP."
    elif clan == clans[1]:  # Priest
        character["HP"] = 125
        character["Energy"] = 120
        character["Damage"] = 18
        character["Special Ability"] = "Holy Fire"
        character['Special Ability Description'] = 'You purify your opponent with holy fire. This' \
                                                   'deals 1.75x your damage to them and heals you' \
                                                   ' for the same amount'
    else:  # Shape Shifter
        character["HP"] = 125
        character["Energy"] = 110
        character["Damage"] = 20
        character["Special Ability"] = "Bite"
        character['Special Ability Description'] = 'You shape shift into a wolf and bite a chunk ' \
                                                   'out of your opponent.This deals 3x your damage'
    character["Max HP"] = character["HP"]
    character["Max Energy"] = character["Energy"]
    return character


def make_board(rows, columns):
    """
    Generate game board

    A function that generates the game board inside a dictionary. This dictionary represents each
    location in the board as a key value pair, the key being a tuple that indicates the
    coordinates and the value is a dictionary that contains information about enemies and
    explored status of that location. Board dictionary also has a 'Dimensions' key that
    indicates the dimensions of the board in a tuple.

    :param rows: An integer indicating the number of rows in board.
    :param columns: An integer indicating the number of columns in board.
    :precondition: rows and columns must be integers that are bigger than 2
    :postcondition: Generates a board of the correct side with the dimensions stored inside.
    :return: A dictionary containing the game board.

    >>> make_board(3, 3)
    {(0, 0): {'Enemy': [], 'Explored': True}, (0, 1): {'Enemy': [], 'Explored': False}, \
(0, 2): {'Enemy': [], 'Explored': False}, (1, 0): {'Enemy': [], 'Explored': False}, \
(1, 1): {'Enemy': [], 'Explored': False}, (1, 2): {'Enemy': [], 'Explored': False}, \
(2, 0): {'Enemy': [], 'Explored': False}, (2, 1): {'Enemy': [], 'Explored': False}, \
(2, 2): {'Enemy': [], 'Explored': False}, 'Dimensions': (3, 3)}
    """
    board = {(row, column): {"Enemy": [], "Explored": False}
             for row in range(rows) for column in range(columns)}
    board[(0, 0)]["Explored"] = True
    board["Dimensions"] = (rows, columns)
    return board


def display_board(board, character):
    """
    Print the board.

    A function that prints the board using unicode characters. This function uses three different
    symbols indicating unexplored rooms, explored rooms, and the room that the character is in.

    :param board: A dictionary that contains the board.
    :param character: A dictionary that contains the character's stats.
    :precondition: character dictionary must include 'Position'.
    :precondition: board dictionary must include 'Dimensions'.
    :precondition: board dictionary must include 'Explored' for each location.
    :postcondition: Print the board with explored rooms and character's location indicated.

    >>> test_board = make_board(3, 3)
    >>> test_character = make_character("Test Name", "Warriors of Amazon")
    >>> display_board(test_board, test_character)
    ⏺ ⏹ ⏹ \n\
    ⏹ ⏹ ⏹ \n\
    ⏹ ⏹ ⏹ \n
    """
    rows, columns = (board["Dimensions"])
    player_location = tuple(character["Position"])
    # Draw the map
    for row, column in itertools.product(range(rows), range(columns)):
        location = (row, column)
        if not board[location]["Explored"]:
            print("⏹ ", end="")
        elif location == player_location:
            print("⏺ ", end="")
        else:
            print("▢ ", end="")
        if column == columns - 1:
            print()


def spawn_enemies(board):
    """
    Populate the board with enemies.

    A function that populates 25% of the locations on the board with one of three enemies. The
    enemy is represented with a dictionary containing it's stats. The enemies are scaled based on
    their distance from (0,0). The boss is also added to the board, in the farthest location from
    (0, 0). The enemy dictionary includes 'Name', 'HP', 'Max XP', 'Damage'.

    :param board: A dictionary that contains the board.
    :precondition: board dictionary must include 'Dimensions'.
    :precondition: board dictionary must include 'Enemy' for each location.
    :postcondition: Populates the board with enemies.
    :postcondition: Spawns boss in the correct location.
    :postcondition: Does not alter the board in any other way.
    """
    enemy1 = {"Name": "Samaritan Soldier", "HP": 100, "Damage": 20}
    enemy2 = {"Name": "Persian Monk", "HP": 105, "Damage": 18}
    enemy3 = {"Name": "Fire Worshiper", "HP": 95, "Damage": 22}
    enemy4 = {"Name": "Russian Blacksmith", "HP": 100, "Damage": 20}
    boss = {"Name": "Goddess of The Red Moon", "HP": 700, "Damage": 50, 'Max HP': 700}
    enemies = [enemy1, enemy2, enemy3, enemy4]
    rows = board["Dimensions"][0]
    columns = board["Dimensions"][1]
    for row, column in itertools.product(range(rows), range(columns)):
        if random.random() <= 0.25:
            enemy = random.choice(enemies).copy()
            scaling = math.sqrt(row * column) / 24
            enemy["HP"] += math.floor(enemy["HP"] * scaling)
            enemy["Max HP"] = enemy["HP"]
            enemy["Damage"] += math.floor(enemy["Damage"] * scaling)
            board[(row, column)]["Enemy"] = [enemy]
    board[(rows - 1, columns - 1)]['Enemy'] = [boss]


def describe_current_location(board, character):
    """
    Describe character's current location.

    A function that prints a random description for the room that character is in. If there is an
    enemy in that room a random description is also print for that enemy.

    :param board: A dictionary that contains the board.
    :param character: A dictionary that contains the character's stats.
    :precondition: character dictionary must include 'Position' and 'Name'.
    :precondition: board dictionary must include 'Enemy' for each location.
    :postcondition: Print the board with explored rooms and character's location indicated.
    """
    current_location = character["Position"]
    enemy = board[current_location]["Enemy"]

    location1 = "You enter a dimly lit hall with torches burning on the walls.\n" \
                "There are claw marks on the walls. Something big must have been kept captive here."
    location2 = "You enter a hall that has no ceiling. Sunlight brightens the whole room.\n" \
                "There are burnt paintings hanging on the walls."
    location3 = "You enter a hall with a chandelier hanging from the ceiling.\nYou might have " \
                "mistaken it for a banquet hall if it wasn't for all the blood on the walls."
    locations = [location1, location2, location3]

    enemy_description1 = "is hurriedly running across the hall. He might run into you if he " \
                         "keeps moving like that."
    enemy_description2 = "is standing in the corner. She gives you a nasty look and spits on " \
                         "the floor"
    enemy_description3 = "is sitting cross-legged in the middle of the room. You wouldn't want " \
                         "to disturb her, she might be meditating."
    enemy_descriptions = [enemy_description1, enemy_description2, enemy_description3]

    print("\n" + random.choice(locations) + "\n")

    if enemy:
        if enemy[0]["Name"].lower() in "aeoui":
            print("An ", end="")
        else:
            print("A ", end="")
        print(enemy[0]["Name"], random.choice(enemy_descriptions), "\n")
    return


def get_player_choice(options: tuple, input_map=None, quit_button="q") -> str:
    """
    Get player's choice

    A function that shows player a collection of options to choose from. Each option has key on
    the keyboard associated with it. It then takes the player's input and returns the option
    associated with that input. The items in options and characters in input_map are associated
    based on their index. This function always provides the player with the option to quit
    the game.

    :param options: A tuple of strings containing options that the player can choose from.
    :param input_map: A string that represents the characters that the player can input to choose
                      between the options. input_map is a string of ascending numbers starting
                      from 1 with the length of options by default.
    :param quit_button: The character that is used to quit the game. quit_button is q by default.
    :precondition: options and input_map must have the same length.
    :precondition: input_map cannot include '~'.
    :postcondition: Prompts the player for an input until they enter a character that exists in
                    input_map.
    :postcondition: Does not crash if the player enters a wrong input.
    :return: A string containing the option that the player selected.
    """
    # return_map is a string of numbers by default
    if input_map is None:
        input_map = ""
        for number, _ in enumerate(options):
            input_map += str(number + 1)
    prompt = ""
    for character, option, in zip(input_map, options):
        prompt += character + ". " + option + "   "
    prompt += quit_button + ". Quit"
    player_choice = ""
    while player_choice == "" or player_choice not in input_map:
        print(prompt)
        player_choice = input()
        if player_choice == quit_button:
            quit_game()
        elif player_choice == "" or player_choice not in input_map:
            print("That is not a correct option, please choose from the options provided below.")
    return options[input_map.find(player_choice)]


def move_character(board, character, direction):
    """
    Move character.

    A function that moves the character in certain direction if possible. If the move is not
    possible, it informs the player. When the character is moved to a new location, that location's
    'Explored' status is set to True.

    :param board: A dictionary that contains the board.
    :param character: A dictionary that contains the character's stats.
    :param direction: A string that indicates the movement direction
    :precondition: board must contain keys that indicate coordinates using a tuple as such (Y, X)
    :precondition: board dictionary must include 'Explored' for each location.
    :precondition: character dictionary must include 'Position' and 'Previous Position'.
    :precondition: direction must be one of the following: 'North', 'West', 'South', 'East'.
    :postcondition: Moves the character in the correct direction.
    :postcondition: Does not move character is the move is not valid.
    :postcondition: 'Explored' status is set to True for the location that the character moves into.
    :return: True if the move is possible and executed. Else, False.

    >>> test_board = make_board(3, 3)
    >>> test_character = make_character("Test Name", "Warriors of Amazon")
    >>> move_character(test_board, test_character, "North")
    There is no hall in that direction. This seems to be the edge of the arena.
    False
    >>> display_board(test_board, test_character)
    ⏺ ⏹ ⏹ \n\
    ⏹ ⏹ ⏹ \n\
    ⏹ ⏹ ⏹ \n
    >>> move_character(test_board, test_character, "South")
    True
    >>> display_board(test_board, test_character)
    ▢ ⏹ ⏹ \n\
    ⏺ ⏹ ⏹ \n\
    ⏹ ⏹ ⏹ \n
    """
    direction_vectors = {"North": (-1, 0), "West": (0, -1), "South": (1, 0), "East": (0, 1)}
    vector = direction_vectors[direction]
    row = (character["Position"][0] + vector[0])
    column = (character["Position"][1] + vector[1])
    if (row, column) in board:
        valid_input = True
        character["Previous Position"] = character["Position"]
        character["Position"] = (row, column)
        board[character["Position"]]["Explored"] = True
    else:
        print("There is no hall in that direction. This seems to be the edge of the arena.")
        valid_input = False
    return valid_input


def execute_player_action(board, character):
    """
    Execute player action.

    A function that displays all possible actions in a given room in the board to the player,
    and then executes the action that player has chosen. The possible actions in a room are
    movement, combat if there is an enemy in that room, and show stats.

    :param board: A dictionary that contains the board.
    :param character: A dictionary that contains the character's stats.
    :precondition: board must contain keys that indicate coordinates using a tuple as such (Y, X)
    :precondition: board dictionary must include 'Enemy' and 'Explored for each location.
    :precondition: character dictionary must include  'HP', 'Energy', 'Max HP, 'Max Energy',
                   'Name', 'Clan', 'XP', 'Max XP', 'Level', 'Damage', 'Special Ability', 'Special
                   Ability Description', 'Enemies Slain', 'Position', 'Previous Position'.
    :postcondition: Correctly executes movement, combat or show stats.
    :postcondition: Does not crash with invalid input.
    """
    if board[character["Position"]]["Enemy"]:
        options = ("North", "West", "South", "East", "Combat", "Stats")
        input_map = "wasder"
    else:
        options = ("North", "West", "South", "East", "Stats")
        input_map = "wasdr"
    valid_input = False
    while not valid_input:
        player_choice = get_player_choice(options, input_map)
        if player_choice == "Stats":
            show_stats(character)
        elif player_choice == "Combat":
            combat(board, character)
            return
        else:  # move character
            valid_input = move_character(board, character, player_choice)


def regeneration(character, heal=None, energy=None):
    """
    Restore health and energy to the character.

    A function that restores health and energy to the character. The amount of restoration can be
    passed through as arguments, if not it is calculated based on the character's level.

    :param character: A dictionary that contains the character's stats.
    :param heal: An integer indicating the amount of HP to be restored to the character
    :param energy: An integer indicating the amount of energy to be restored to the character.
    :precondition: character dictionary must include  'HP', 'Energy', 'Max HP, 'Max Energy', 'Level'
    :precondition: heal and energy are optional.
    :precondition: heal and energy must be positive integers.
    :postcondition: HP will not be restored to more than Max HP.
    :postcondition: Energy will not be restored to more than Max Energy.
    :postcondition: Does not alter the character in any other way.

    >>> test_character = {'HP': 50, 'Energy': 50, 'Max HP': 125, 'Max Energy': 100, 'Level': 2}
    >>> regeneration(test_character)
    >>> test_character
    {'HP': 55, 'Energy': 58, 'Max HP': 125, 'Max Energy': 100, 'Level': 2}
    >>> regeneration(test_character, heal=100, energy=100)
    >>> test_character
    {'HP': 125, 'Energy': 100, 'Max HP': 125, 'Max Energy': 100, 'Level': 2}
    """
    if heal is None:
        heal = 1 + character["Level"] * 2
    if energy is None:
        energy = 2 + character["Level"] * 3
    character["HP"] += heal
    if character["HP"] > character["Max HP"]:
        character["HP"] = character["Max HP"]
    character["Energy"] += energy
    if character["Energy"] > character["Max Energy"]:
        character["Energy"] = character["Max Energy"]


def level_up_if_possible(character):
    """
    Level-up the character if possible.

    A function that checks if the character has enough XP to level up, and if so, levels up the
    character. Character's Damage, Max HP and Max Energy are increased upon level up, and the
    character is restored to max hp and energy.

    :param character: A dictionary that contains the character's stats.
    :precondition: character dictionary must include  'HP', 'Energy', 'Max HP, 'Max Energy',
                   'Level', 'XP', 'Max XP'.
    :postcondition: Levels up character correctly.
    :postcondition: Sets character's 'XP' to 0.
    :postcondition: Increases character's 'Max XP' by 2.
    :postcondition: Increases character's 'Damage' by 60%.
    :postcondition: Increases character's 'Max XP' by 50%.
    :postcondition: Increases character's 'Max Energy' by 30%.
    :postcondition: Sets character to max HP and energy.
    :postcondition: Does not alter character in any other way.
    :postcondition: Prints level-up messages

    >>> test_character = {'XP': 0, 'Max XP': 3, 'Level': 1, 'HP': 55, 'Energy': 58, 'Max HP': 125, \
    'Max Energy': 100, 'Damage': 20}
    >>> level_up_if_possible(test_character)
    >>> test_character
    {'XP': 0, 'Max XP': 3, 'Level': 1, 'HP': 55, 'Energy': 58, 'Max HP': 125, 'Max Energy': 100, \
'Damage': 20}
    >>> test_character['XP'] = 3
    >>> level_up_if_possible(test_character)
    You feel yourself getting stronger.
    You are now level 2.
    Your health and energy have been replenished.
    >>> test_character
    {'XP': 0, 'Max XP': 5, 'Level': 2, 'HP': 187, 'Energy': 130, 'Max HP': 187, \
'Max Energy': 130, 'Damage': 32}

    """
    if character["XP"] >= character["Max XP"]:
        character["Level"] += 1
        print(f"You feel yourself getting stronger.\n"
              f"You are now level {character['Level']}.\n"
              f"Your health and energy have been replenished.")
        character["Max HP"] += math.floor(character["Max HP"] * 0.5)
        character['HP'] = character["Max HP"]
        character["Max Energy"] += math.floor(character["Max Energy"] * 0.3)
        character["Energy"] = character["Max Energy"]
        character['Damage'] += math.floor(character['Damage'] * 0.6)
        character['Max XP'] += 2
        character['XP'] = 0


def enemy_slain(board, character):
    """
    Slay enemy.

    A function that removes the enemy from character's current location in the board, gives the
    character 1 XP, and displays the appropriate messages.

    :param board: A dictionary that contains the board.
    :param character: A dictionary that contains the character's stats.
    :precondition: board must contain keys that indicate coordinates using a tuple as such (Y, X)
    :precondition: board dictionary must include 'Enemy' for each location.
    :precondition: character dictionary must include  'XP', 'Max XP', 'Enemies Slain'.
    :postcondition: Does not alter board and character in any way other than specified.


    """
    print("You have slain your enemy!")
    board[character["Position"]]["Enemy"] = []
    print_character_combat_stats(character)
    character['XP'] += 1
    character["Enemies Slain"] += 1
    print(f"You have gained 1 experience. | "
          f"Experience: ({character['XP']}/{character['Max XP']})")
    input("Press Enter to move on.")


def execute(character, enemy):
    """
    Use 'execute' special ability on enemy.

    This special ability deals twice character's damage to an enemy, and if they enemy falls below
    15% HP it instantly dies. This ability costs 50 energy.

    :param character: A dictionary that contains the character's stats.
    :param enemy: A dictionary that contains the enemy's stats.
    :precondition: character dictionary must include 'Energy' and 'Damage'.
    :precondition: enemy dictionary must include 'HP' and 'Max HP'.
    :postcondition: prints statements relevant to using this ability.
    :postcondition: Does not alter character and enemy in any way other than specified.

    >>> test_enemy = {'Damage': 20,'HP': 100,'Max HP': 100, 'Name': 'Samaritan Soldier'}
    >>> test_character = {'XP': 0, 'Max XP': 3, 'Level': 1, 'HP': 55, 'Energy': 58, 'Max HP': 125, \
    'Max Energy': 100, 'Damage': 20, 'Position': (0, 0), 'Enemies Slain': 0, 'Name': 'Test Name'}
    >>> execute(test_character, test_enemy)
    You have just attempted to execute your opponent. That dealt 40 damage.
    That wasn't quite enough to take them out.
    Your opponent takes a step back, you can see the fear in their eyes
    >>> execute(test_character, test_enemy)
    You don't have enough energy to execute your opponent.
    """
    if character["Energy"] < 50:
        print(f"You don't have enough energy to execute your opponent.")
        return
    else:
        character["Energy"] -= 50
    damage = character["Damage"] * 2
    enemy["HP"] -= damage
    print(F"You have just attempted to execute your opponent. "
          f"That dealt {damage} damage.")
    if enemy["HP"] / enemy["Max HP"] <= 0.15:
        print("They were too weak to withstand that blow.")
        enemy["HP"] = 0
    else:
        print("That wasn't quite enough to take them out.\n"
              "Your opponent takes a step back, you can see the fear in their eyes")


def holy_fire(character, enemy):
    """
    Use 'holy fire' special ability on enemy.

    This special ability deals 1.75x character's damage to an enemy, and heals the character for the
    same amount.

    :param character: A dictionary that contains the character's stats.
    :param enemy: A dictionary that contains the enemy's stats.
    :precondition: character dictionary must include 'Energy', 'HP' and 'Damage'.
    :precondition: enemy dictionary must include 'HP' and 'Max HP'.
    :postcondition: prints statements relevant to using this ability.
    :postcondition: Does not alter character and enemy in any way other than specified.
    >>> test_enemy = {'Damage': 20,'HP': 100,'Max HP': 100, 'Name': 'Samaritan Soldier'}
    >>> test_character = {'XP': 0, 'Max XP': 3, 'Level': 1, 'HP': 55, 'Energy': 58, 'Max HP': 125, \
    'Max Energy': 100, 'Damage': 20, 'Position': (0, 0), 'Enemies Slain': 0, 'Name': 'Test Name'}
    >>> holy_fire(test_character, test_enemy)
    You have just cast a spell of holy fire on your opponent.
    The fire burns them for 35 damage, and the light heals you for 35 hit points.
    >>> holy_fire(test_character, test_enemy)
    You don't have enough energy to cast holy fire.
    """
    if character["Energy"] < 50:
        print(f"You don't have enough energy to cast holy fire.")
        return
    else:
        character["Energy"] -= 50
    damage = int(character["Damage"] * 1.75)
    heal = damage
    enemy["HP"] -= damage
    regeneration(character, heal=heal, energy=0)
    print(f"You have just cast a spell of holy fire on your opponent.\n"
          f"The fire burns them for {damage} damage, and the light heals you for {heal} hit "
          f"points.")


def bite(character, enemy):
    """
    Use 'bite' special ability on enemy.

    This special ability deals 3x character's damage to the enemy.

    :param character: A dictionary that contains the character's stats.
    :param enemy: A dictionary that contains the enemy's stats.
    :precondition: character dictionary must include 'Energy' and 'Damage'.
    :precondition: enemy dictionary must include 'HP'.
    :postcondition: prints statements relevant to using this ability.
    :postcondition: Does not alter character and enemy in any way other than specified.
    >>> test_enemy = {'Damage': 20,'HP': 100,'Max HP': 100, 'Name': 'Samaritan Soldier'}
    >>> test_character = {'XP': 0, 'Max XP': 3, 'Level': 1, 'HP': 55, 'Energy': 58, 'Max HP': 125, \
    'Max Energy': 100, 'Damage': 20, 'Position': (0, 0), 'Enemies Slain': 0, 'Name': 'Test Name'}
    >>> bite(test_character, test_enemy)
    You shape shit into a wolf and bite your opponent.
    That took a chunk out of them, you dealt 60 damage
    >>> bite(test_character, test_enemy)
    You don't have enough energy to shape shift.
    """
    if character["Energy"] < 50:
        print(f"You don't have enough energy to shape shift.")
        return
    else:
        character["Energy"] -= 50
    damage = int(character["Damage"] * 3)
    enemy["HP"] -= damage
    print(f"You shape shit into a wolf and bite your opponent.\n"
          f"That took a chunk out of them, you dealt {damage} damage")


def cast_special_ability(character, enemy):
    """
    Cast special ability.

    A function that executes the function related to the character's special ability on an enemy.

    :param character: A dictionary that contains the character's stats.
    :param enemy: A dictionary that contains the enemy's stats.
    :precondition: character dictionary must include 'Energy', 'HP', 'Max HP' and 'Damage'.
    :precondition: enemy dictionary must include 'HP' and 'Max HP'.
    :postcondition: casts the special ability related to the character's clan.
    >>> test_enemy = {'Damage': 20,'HP': 100,'Max HP': 100, 'Name': 'Samaritan Soldier'}
    >>> test_character = {'XP': 0, 'Max XP': 3, 'Level': 1, 'HP': 55, 'Energy': 58, 'Max HP': 125, \
    'Max Energy': 100, 'Damage': 20, 'Position': (0, 0), 'Enemies Slain': 0, 'Name': 'Test Name', \
    'Special Ability': 'Bite'}
    >>> cast_special_ability(test_character, test_enemy)
    You shape shit into a wolf and bite your opponent.
    That took a chunk out of them, you dealt 60 damage
    >>> cast_special_ability(test_character, test_enemy)
    You don't have enough energy to shape shift.
    """
    special_ability = character["Special Ability"]
    if special_ability == "Execute":
        execute(character, enemy)
    elif special_ability == "Holy Fire":
        holy_fire(character, enemy)
    elif special_ability == "Bite":
        bite(character, enemy)


def flee_combat(character, enemy):
    """
    Flee from combat.

    A function that makes the character flee from combat. The character is returned to it's previous
    location, and takes some damage while fleeing. The character cannot flee from the final boss.

    :param character: A dictionary that contains the character's stats.
    :param enemy: A dictionary that contains the enemy's stats.
    :precondition: character dictionary must include 'HP', 'Position', 'Previous Position'.
    :precondition: enemy dictionary must include 'Name', 'Damage', 'HP' and 'Max HP'.
    :postcondition: casts the special ability related to the character's clan.
    :return: True if the character was able to flee. Else, False.
    """
    if enemy['Name'] != "Goddess of The Red Moon":
        print(f"You come to your senses and choose to flee from the fight.\n"
              f"The {enemy['Name']} throws a rock at you as you are running away.")
        character["HP"] -= int(enemy["Damage"] / 3)
        print_character_combat_stats(character)
        character["Position"] = character["Previous Position"]
        input("Press Enter to move on.")
        flee = True
    else:
        print("In fear you decide to flee from the fight.\n"
              "As you turn your back to The Goddess in an attempt to run away, you find her "
              "standing in front of you.\n"
              "She yells \"You stench of fear mortal. You can not run from your demise.\"\n"
              "She lands a direct strike into your face.")
        character["HP"] -= int(enemy["Damage"] * 2)
        print_character_combat_stats(character)
        flee = False
    return flee


def combat(board, character):
    """
    Engage combat.

    This function performs all the tasks needed for a complete combat session. It prints pre-combat
    messages, the lets the player choose between attacking their enemy, using their special
    ability or fleeing. The combat continues until one of the participants die or the players
    chooses to flee. The player gains an experience point if the enemy is slain.

    :param board: A dictionary that contains the board.
    :param character: A dictionary that contains the character's stats.
    :precondition: board must contain keys that indicate coordinates using a tuple as such (Y, X)
    :precondition: board dictionary must include 'Enemy' for each location.
    :precondition: There must be an enemy in the board location that the character is in.
    :precondition: character dictionary must include  'HP', 'Energy', 'Max HP, 'Max Energy', 'Name',
                   'Clan', 'XP', 'Max XP', 'Level', 'Damage', 'Special Ability', 'Special Ability
                   Description', 'Enemies Slain', 'Position', 'Previous Position'.
    :postcondition: Combat happens correctly
    """
    enemy = board[character["Position"]]["Enemy"][0]
    special_ability = character["Special Ability"]
    options = ("Attack", special_ability, "Flee")
    # pre-combat
    clear_console()
    print(f"You grab a rock and throw it at the {enemy['Name']}\'s head.\n"
          f"That's one way to start a fight...")
    # combat loop
    flee = False
    while check_alive(character) and check_alive(enemy) and not flee:
        print_character_combat_stats(character)
        print_enemy_combat_stats(enemy)
        choice = get_player_choice(options)
        if choice == special_ability:
            cast_special_ability(character, enemy)
        elif choice == "Flee":
            flee = flee_combat(character, enemy)
        else:
            print("You and your opponent strike at each other.")
            character["HP"] -= enemy["Damage"]
            enemy["HP"] -= character["Damage"]
            regeneration(character, heal=0)
    # post-combat
    if enemy["HP"] <= 0:
        enemy_slain(board, character)


def check_boss_event(board, character):
    """
    Check for boss.

    A function that checks if the final boss of the game is in character's current location.

    :param board: A dictionary that contains the board.
    :param character: A dictionary that contains the character's stats.
    :precondition: board must contain keys that indicate coordinates using a tuple as such (Y, X)
    :precondition: board dictionary must include 'Enemy' for each location.
    :precondition: character dictionary must include 'Position'
    :postcondition: Does not alter board and character in any way.
    :return: True if the boss in in character's location. Else, False.

    >>> test_board = {'Dimensions': (1, 2), (0, 0): {'Enemy': [{'Damage': 50, 'HP': 700, \
    'Max HP': 700, 'Name': 'Goddess of The Red Moon'}]}, (0, 1): {'Enemy': []}}
    >>> test_character = {'Position': (0, 0)}
    >>> check_boss_event(test_board, test_character)
    True
    >>> test_character = {'Position': (0, 1)}
    >>> check_boss_event(test_board, test_character)
    False
    """
    enemy = board[character["Position"]]["Enemy"]
    if enemy:
        return enemy[0]['Name'] == "Goddess of The Red Moon"
    else:
        return False


def boss_event(board, character):
    """
    Trigger boss event.

    A function that triggers the final boss event. There are two different forms of this event,
    the correct one is triggered based on character's Enemies Slain stat. This function prints the
    appropriate messages for the user and then engages the boss in combat if necessary.

    :param board: A dictionary that contains the board.
    :param character: A dictionary that contains the character's stats.
    :precondition: board must contain keys that indicate coordinates using a tuple as such (Y, X)
    :precondition: board dictionary must include 'Enemy' for each location.
    :precondition: character dictionary must include 'HP', 'Energy', 'Max HP, 'Max Energy', 'Name',
                   'Clan', 'XP', 'Max XP', 'Level', 'Damage', 'Special Ability', 'Special Ability
                   Description', 'Enemies Slain', 'Position', 'Previous Position'.
    :postcondition: Triggers the correct boss event which matches the game's ending.
    """
    if character['Enemies Slain'] == 0:
        print(f"You enter a hall with walls made of pure light.\n"
              f"The Goddess of the Red Moon is sitting on a chair in the middle of the hall.\n"
              f"There is an empty chair and a table besides her.\n"
              f"You notice a teapot and two tea cups on the table\n"
              f"The Goddess softly says \"Join with me for a cup of tea brave challenger.\"\n"
              f"You exclaim \"Aren't you going to fight me!?\"\n"
              f"The Goddess replies \"Only the noblest of souls can cross the arena without "
              f"shedding blood\n"
              f"A peaceful spirit like yours has a resting place besides me in eternity\"\n"
              f"You join The Goddess and sip from the tea cup.\n"
              f"You feel a warm, wholesome feeling fill you body.\n"
              f"You see heaven rise around you as the arena disappears.\n")
    else:
        print(f"You enter a hall with the walls glowing red.\n"
              f"You notice they are covered in blood as you walk further into the room.\n"
              f"The Goddess of The Red Moon appears behind you."
              f"Her eyes are glowing red, with tear drops made of blood rolling down her cheeks.\n"
              f"She screams \"YOU DARE CHALLENGE THE GODDESS IN HER OWN HOME?\"")
        input("Press Enter twice to stand your ground.")
        input()
        combat(board, character)


def display_ending_message(character):
    """
    Print appropriate ending messages.

    This function prints the appropriate ending messages based on whether the character has died, or
    the ending that has been unlocked.

    :param character: A dictionary that contains the character's stats.
    :precondition: character dictionary must include 'Enemies Slain'
    >>> test_character = {'HP': 50, 'Enemies Slain': 0}
    >>> display_ending_message(test_character)
     Ending 2 Unlocked
     >>> test_character = {'HP': 0, 'Enemies Slain': 3}
    >>> display_ending_message(test_character)
    You died!
    """
    if not check_alive(character):
        print("You died!")
    elif character['Enemies Slain'] == 0:
        print(" Ending 2 Unlocked")
    else:
        print("You have successfully defeated The Goddess of The Red Moon!\n"
              "Your turn your back, bloodied and tired, and start walking away from the hall.\n"
              "Suddenly you hear a noise coming from behind you. You look back and see the Goddess "
              "has risen from the dead.\n"
              "She says \"Did you really think you could kill a Goddess?\"\n"
              "She rises to the roof of the hall and disappears into the light.\n\n"
              " Ending 1 Unlocked")


def game():
    """
    Play the game.

    :precondition: Get ready!
    :postcondition: Have fun!
    """
    rows = 25
    columns = 25
    name, clan = initialize_game()
    board = make_board(rows, columns)
    character = make_character(name, clan)
    spawn_enemies(board)
    is_alive = True
    while is_alive:
        clear_console()
        if check_boss_event(board, character):
            boss_event(board, character)
            break
        display_board(board, character)
        describe_current_location(board, character)
        level_up_if_possible(character)
        execute_player_action(board, character)
        regeneration(character)
        is_alive = check_alive(character)
    display_ending_message(character)


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
