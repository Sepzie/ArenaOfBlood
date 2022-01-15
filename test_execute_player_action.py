from unittest import TestCase
from unittest.mock import patch
from game import execute_player_action
import io


class TestExecutePlayerAction(TestCase):
    @patch('builtins.input', side_effect=["e", "1", "1", "2", "\n"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_player_action_combat(self, output_string, _):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 1), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 100, 'Energy': 80, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        board = {'Dimensions': (2, 3),
                 (0, 0): {'Enemy': [{'Damage': 20,
                                     'HP': 100,
                                     'Max HP': 100,
                                     'Name': 'Samaritan Soldier'}],
                          'Explored': True},
                 (0, 1): {'Enemy': [{'Damage': 18,
                                     'HP': 105,
                                     'Max HP': 105,
                                     'Name': 'Persian Monk'}],
                          'Explored': True},
                 (0, 2): {'Enemy': [{'Damage': 22,
                                     'HP': 95,
                                     'Max HP': 95,
                                     'Name': 'Fire Worshiper'}],
                          'Explored': True},
                 (1, 0): {'Enemy': [{'Damage': 20,
                                     'HP': 100,
                                     'Max HP': 100,
                                     'Name': 'Russian Blacksmith'}],
                          'Explored': False},
                 (1, 1): {'Enemy': [{'Damage': 20,
                                     'HP': 104,
                                     'Max HP': 104,
                                     'Name': 'Samaritan Soldier'}],
                          'Explored': False},
                 (1, 2): {'Enemy': [{'Damage': 50,
                                     'HP': 700,
                                     'Max HP': 700,
                                     'Name': 'Goddess of The Red Moon'}],
                          'Explored': False}}
        expected_1 = {'Dimensions': (2, 3),
                      (0, 0): {'Enemy': [], 'Explored': True},
                      (0, 1): {'Enemy': [{'Damage': 18,
                                          'HP': 105,
                                          'Max HP': 105,
                                          'Name': 'Persian Monk'}],
                               'Explored': True},
                      (0, 2): {'Enemy': [{'Damage': 22,
                                          'HP': 95,
                                          'Max HP': 95,
                                          'Name': 'Fire Worshiper'}],
                               'Explored': True},
                      (1, 0): {'Enemy': [{'Damage': 20,
                                          'HP': 100,
                                          'Max HP': 100,
                                          'Name': 'Russian Blacksmith'}],
                               'Explored': False},
                      (1, 1): {'Enemy': [{'Damage': 20,
                                          'HP': 104,
                                          'Max HP': 104,
                                          'Name': 'Samaritan Soldier'}],
                               'Explored': False},
                      (1, 2): {'Enemy': [{'Damage': 50,
                                          'HP': 700,
                                          'Max HP': 700,
                                          'Name': 'Goddess of The Red Moon'}],
                               'Explored': False}}
        expected_2 = {'Clan': 'Warriors of Amazon',
                      'Damage': 22,
                      'Enemies Slain': 1,
                      'Energy': 40,
                      'HP': 60,
                      'Level': 1,
                      'Max Energy': 100,
                      'Max HP': 125,
                      'Max XP': 3,
                      'Name': 'Test Name',
                      'Position': (0, 0),
                      'Previous Position': (0, 1),
                      'Special Ability': 'Execute',
                      'Special Ability Description':
                          'You strike your opponent with the intent to '
                          'kill. This deals 2x your damage and instantly '
                          'kills them if they are below 15% HP.',
                      'XP': 1}
        expected_3 = ("w. North   a. West   s. South   d. East   e. Combat   r. Stats   q. Quit" +
                      "\n" * 102 +
                      ("You grab a rock and throw it at the Samaritan Soldier's head.\n"
                       "That's one way to start a fight...\n"
                       "Test Name --  HP: 100/125 | Energy: 80/100 | Damage: 22\n"
                       "Samaritan Soldier -- HP: 100/100 | Damage: 20\n"
                       "1. Attack   2. Execute   3. Flee   q. Quit\n"
                       "You and your opponent strike at each other.\n"
                       "Test Name --  HP: 80/125 | Energy: 85/100 | Damage: 22\n"
                       "Samaritan Soldier -- HP: 78/100 | Damage: 20\n"
                       "1. Attack   2. Execute   3. Flee   q. Quit\n"
                       "You and your opponent strike at each other.\n"
                       "Test Name --  HP: 60/125 | Energy: 90/100 | Damage: 22\n"
                       "Samaritan Soldier -- HP: 56/100 | Damage: 20\n"
                       "1. Attack   2. Execute   3. Flee   q. Quit\n"
                       "You have just attempted to execute your opponent. That dealt 44 damage.\n"
                       "They were too weak to withstand that blow.\n"
                       "You have slain your enemy!\n"
                       "Test Name --  HP: 60/125 | Energy: 40/100 | Damage: 22\n"
                       "You have gained 1 experience. | Experience: (1/3)\n"))
        execute_player_action(board, character)
        actual_1 = board
        actual_2 = character
        actual_3 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('builtins.input', side_effect=["r", "s"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_player_show_stats_then_move_south(self, output_string, _):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 1), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 100, 'Energy': 80, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        board = {'Dimensions': (2, 3),
                 (0, 0): {'Enemy': [{'Damage': 20,
                                     'HP': 100,
                                     'Max HP': 100,
                                     'Name': 'Samaritan Soldier'}],
                          'Explored': True},
                 (0, 1): {'Enemy': [{'Damage': 18,
                                     'HP': 105,
                                     'Max HP': 105,
                                     'Name': 'Persian Monk'}],
                          'Explored': True},
                 (0, 2): {'Enemy': [{'Damage': 22,
                                     'HP': 95,
                                     'Max HP': 95,
                                     'Name': 'Fire Worshiper'}],
                          'Explored': True},
                 (1, 0): {'Enemy': [{'Damage': 20,
                                     'HP': 100,
                                     'Max HP': 100,
                                     'Name': 'Russian Blacksmith'}],
                          'Explored': False},
                 (1, 1): {'Enemy': [{'Damage': 20,
                                     'HP': 104,
                                     'Max HP': 104,
                                     'Name': 'Samaritan Soldier'}],
                          'Explored': False},
                 (1, 2): {'Enemy': [{'Damage': 50,
                                     'HP': 700,
                                     'Max HP': 700,
                                     'Name': 'Goddess of The Red Moon'}],
                          'Explored': False}}
        expected_1 = {'Dimensions': (2, 3),
                      (0, 0): {'Enemy': [{'Damage': 20,
                                          'HP': 100,
                                          'Max HP': 100,
                                          'Name': 'Samaritan Soldier'}],
                               'Explored': True},
                      (0, 1): {'Enemy': [{'Damage': 18,
                                          'HP': 105,
                                          'Max HP': 105,
                                          'Name': 'Persian Monk'}],
                               'Explored': True},
                      (0, 2): {'Enemy': [{'Damage': 22,
                                          'HP': 95,
                                          'Max HP': 95,
                                          'Name': 'Fire Worshiper'}],
                               'Explored': True},
                      (1, 0): {'Enemy': [{'Damage': 20,
                                          'HP': 100,
                                          'Max HP': 100,
                                          'Name': 'Russian Blacksmith'}],
                               'Explored': True},
                      (1, 1): {'Enemy': [{'Damage': 20,
                                          'HP': 104,
                                          'Max HP': 104,
                                          'Name': 'Samaritan Soldier'}],
                               'Explored': False},
                      (1, 2): {'Enemy': [{'Damage': 50,
                                          'HP': 700,
                                          'Max HP': 700,
                                          'Name': 'Goddess of The Red Moon'}],
                               'Explored': False}}
        expected_2 = {'Clan': 'Warriors of Amazon',
                      'Damage': 22,
                      'Enemies Slain': 0,
                      'Energy': 80,
                      'HP': 100,
                      'Level': 1,
                      'Max Energy': 100,
                      'Max HP': 125,
                      'Max XP': 3,
                      'Name': 'Test Name',
                      'Position': (1, 0),
                      'Previous Position': (0, 0),
                      'Special Ability': 'Execute',
                      'Special Ability Description':
                          'You strike your opponent with the intent to '
                          'kill. This deals 2x your damage and instantly '
                          'kills them if they are below 15% HP.',
                      'XP': 0}
        expected_3 = ("w. North   a. West   s. South   d. East   e. Combat   r. Stats   q. Quit\n"
                      "\n"
                      "Your stats:\n"
                      "Health: 100 / 125  |  Energy: 80 / 100  |  Damage: 22\n"
                      "Name: Test Name  |  Clan: Warriors of Amazon\n"
                      "\n"
                      "Experience: 0 / 3  |  Level: 1  |  Enemies Slain: 0\n"
                      "\n"
                      "Special Ability: Execute\n"
                      "    Description: You strike your opponent with the intent to kill. This "
                      "deals 2x your damage and instantly kills them if they are below 15% HP.\n"
                      "    Energy Cost: 50\n"
                      "\n"
                      "w. North   a. West   s. South   d. East   e. Combat   r. Stats   q. Quit\n")
        execute_player_action(board, character)
        actual_1 = board
        actual_2 = character
        actual_3 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)
