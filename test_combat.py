from unittest import TestCase
from unittest.mock import patch
from game import combat
import io


class TestCombat(TestCase):
    @patch('builtins.input', side_effect=["1", "1", "1", "1", "1", "\n"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_attack_kill_enemy(self, output_string, _):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 2),
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
                      (0, 2): {'Enemy': [], 'Explored': True},
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
                      'Energy': 100,
                      'HP': -10,
                      'Level': 1,
                      'Max Energy': 100,
                      'Max HP': 125,
                      'Max XP': 3,
                      'Name': 'Test Name',
                      'Position': (0, 2),
                      'Previous Position': (0, 1),
                      'Special Ability': 'Execute',
                      'Special Ability Description':
                          'You strike your opponent with the intent to '
                          'kill. This deals 2x your damage and instantly '
                          'kills them if they are below 15% HP.',
                      'XP': 1}
        expected_3 = ("\n" * 101 +
                      "You grab a rock and throw it at the Fire Worshiper's head.\n"
                      "That's one way to start a fight...\n"
                      "Test Name --  HP: 100/125 | Energy: 80/100 | Damage: 22\n"
                      "Fire Worshiper -- HP: 95/95 | Damage: 22\n"
                      "1. Attack   2. Execute   3. Flee   q. Quit\n"
                      "You and your opponent strike at each other.\n"
                      "Test Name --  HP: 78/125 | Energy: 85/100 | Damage: 22\n"
                      "Fire Worshiper -- HP: 73/95 | Damage: 22\n"
                      "1. Attack   2. Execute   3. Flee   q. Quit\n"
                      "You and your opponent strike at each other.\n"
                      "Test Name --  HP: 56/125 | Energy: 90/100 | Damage: 22\n"
                      "Fire Worshiper -- HP: 51/95 | Damage: 22\n"
                      "1. Attack   2. Execute   3. Flee   q. Quit\n"
                      "You and your opponent strike at each other.\n"
                      "Test Name --  HP: 34/125 | Energy: 95/100 | Damage: 22\n"
                      "Fire Worshiper -- HP: 29/95 | Damage: 22\n"
                      "1. Attack   2. Execute   3. Flee   q. Quit\n"
                      "You and your opponent strike at each other.\n"
                      "Test Name --  HP: 12/125 | Energy: 100/100 | Damage: 22\n"
                      "Fire Worshiper -- HP: 7/95 | Damage: 22\n"
                      "1. Attack   2. Execute   3. Flee   q. Quit\n"
                      "You and your opponent strike at each other.\n"
                      "You have slain your enemy!\n"
                      "Test Name --  HP: -10/125 | Energy: 100/100 | Damage: 22\n"
                      "You have gained 1 experience. | Experience: (1/3)\n")
        combat(board, character)
        actual_1 = board
        actual_2 = character
        actual_3 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('builtins.input', side_effect=["1", "1", "1", "1", "1", "\n"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_attack_character_death(self, output_string, _):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 2),
                     'Previous Position': (0, 1), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 80, 'Damage': 22,
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
                                          'HP': 29,
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
                      'Enemies Slain': 0,
                      'Energy': 95,
                      'HP': -16,
                      'Level': 1,
                      'Max Energy': 100,
                      'Max HP': 125,
                      'Max XP': 3,
                      'Name': 'Test Name',
                      'Position': (0, 2),
                      'Previous Position': (0, 1),
                      'Special Ability': 'Execute',
                      'Special Ability Description':
                          'You strike your opponent with the intent to '
                          'kill. This deals 2x your damage and instantly '
                          'kills them if they are below 15% HP.',
                      'XP': 0}
        expected_3 = ("\n" * 101 +
                      ("You grab a rock and throw it at the Fire Worshiper's head.\n"
                       "That's one way to start a fight...\n"
                       "Test Name --  HP: 50/125 | Energy: 80/100 | Damage: 22\n"
                       "Fire Worshiper -- HP: 95/95 | Damage: 22\n"
                       "1. Attack   2. Execute   3. Flee   q. Quit\n"
                       "You and your opponent strike at each other.\n"
                       "Test Name --  HP: 28/125 | Energy: 85/100 | Damage: 22\n"
                       "Fire Worshiper -- HP: 73/95 | Damage: 22\n"
                       "1. Attack   2. Execute   3. Flee   q. Quit\n"
                       "You and your opponent strike at each other.\n"
                       "Test Name --  HP: 6/125 | Energy: 90/100 | Damage: 22\n"
                       "Fire Worshiper -- HP: 51/95 | Damage: 22\n"
                       "1. Attack   2. Execute   3. Flee   q. Quit\n"
                       "You and your opponent strike at each other.\n"))
        combat(board, character)
        actual_1 = board
        actual_2 = character
        actual_3 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('builtins.input', side_effect=["1", "3", "\n"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_flee(self, output_string, _):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 2),
                     'Previous Position': (0, 1), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 80, 'Damage': 22,
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
                                          'HP': 73,
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
                      'Enemies Slain': 0,
                      'Energy': 85,
                      'HP': 21,
                      'Level': 1,
                      'Max Energy': 100,
                      'Max HP': 125,
                      'Max XP': 3,
                      'Name': 'Test Name',
                      'Position': (0, 1),
                      'Previous Position': (0, 1),
                      'Special Ability': 'Execute',
                      'Special Ability Description':
                          'You strike your opponent with the intent to '
                          'kill. This deals 2x your damage and instantly '
                          'kills them if they are below 15% HP.',
                      'XP': 0}
        expected_3 = ("\n" * 101 +
                      "You grab a rock and throw it at the Fire Worshiper's head.\n"
                      "That's one way to start a fight...\n"
                      "Test Name --  HP: 50/125 | Energy: 80/100 | Damage: 22\n"
                      "Fire Worshiper -- HP: 95/95 | Damage: 22\n"
                      "1. Attack   2. Execute   3. Flee   q. Quit\n"
                      "You and your opponent strike at each other.\n"
                      "Test Name --  HP: 28/125 | Energy: 85/100 | Damage: 22\n"
                      "Fire Worshiper -- HP: 73/95 | Damage: 22\n"
                      "1. Attack   2. Execute   3. Flee   q. Quit\n"
                      "You come to your senses and choose to flee from the fight.\n"
                      "The Fire Worshiper throws a rock at you as you are running away.\n"
                      "Test Name --  HP: 21/125 | Energy: 85/100 | Damage: 22\n")
        combat(board, character)
        actual_1 = board
        actual_2 = character
        actual_3 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('builtins.input', side_effect=["3", "3", "\n"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_final_boss_flee(self, output_string, _):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (1, 2),
                     'Previous Position': (0, 1), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 80, 'Damage': 22,
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
                      'Enemies Slain': 0,
                      'Energy': 80,
                      'HP': -50,
                      'Level': 1,
                      'Max Energy': 100,
                      'Max HP': 125,
                      'Max XP': 3,
                      'Name': 'Test Name',
                      'Position': (1, 2),
                      'Previous Position': (0, 1),
                      'Special Ability': 'Execute',
                      'Special Ability Description':
                          'You strike your opponent with the intent to '
                          'kill. This deals 2x your damage and instantly '
                          'kills them if they are below 15% HP.',
                      'XP': 0}
        expected_3 = ("\n" * 101 +
                      ("You grab a rock and throw it at the Goddess of The Red Moon's head.\n"
                       "That's one way to start a fight...\n"
                       "Test Name --  HP: 50/125 | Energy: 80/100 | Damage: 22\n"
                       "Goddess of The Red Moon -- HP: 700/700 | Damage: 50\n"
                       "1. Attack   2. Execute   3. Flee   q. Quit\n"
                       "In fear you decide to flee from the fight.\n"
                       "As you turn your back to The Goddess in an attempt to run away, you find "
                       "her standing in front of you.\n"
                       "She yells \"You stench of fear mortal. You can not run from your "
                       "demise.\"\n"
                       "She lands a direct strike into your face.\n"
                       "Test Name --  HP: -50/125 | Energy: 80/100 | Damage: 22\n"))
        combat(board, character)
        actual_1 = board
        actual_2 = character
        actual_3 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('builtins.input', side_effect=["1", "1", "2", "\n"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_special_ability(self, output_string, _):
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
        expected_3 = ("\n" * 101 +
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
        combat(board, character)
        actual_1 = board
        actual_2 = character
        actual_3 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)
