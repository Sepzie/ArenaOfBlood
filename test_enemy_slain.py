from unittest import TestCase
from unittest.mock import patch
from game import enemy_slain
import io


class TestEnemySlain(TestCase):
    @patch('builtins.input', side_effect="\n")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_slain(self, output_string, _):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 100, 'Energy': 50, 'Damage': 22,
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
                          'Explored': False},
                 (0, 2): {'Enemy': [{'Damage': 22,
                                     'HP': 95,
                                     'Max HP': 95,
                                     'Name': 'Fire Worshiper'}],
                          'Explored': False},
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
        expected_1 = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                      'Previous Position': (0, 0), 'Level': 1, 'XP': 1, 'Max XP': 3,
                      'Enemies Slain': 1, 'HP': 100, 'Energy': 50, 'Damage': 22,
                      'Special Ability': 'Execute', 'Special Ability Description':
                          'You strike your opponent with the intent to kill. This deals 2x your '
                          'damage and instantly kills them if they are below 15% HP.',
                      'Max HP': 125, 'Max Energy': 100}
        expected_2 = {'Dimensions': (2, 3),
                      (0, 0): {'Enemy': [],
                               'Explored': True},
                      (0, 1): {'Enemy': [{'Damage': 18,
                                          'HP': 105,
                                          'Max HP': 105,
                                          'Name': 'Persian Monk'}],
                               'Explored': False},
                      (0, 2): {'Enemy': [{'Damage': 22,
                                          'HP': 95,
                                          'Max HP': 95,
                                          'Name': 'Fire Worshiper'}],
                               'Explored': False},
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
        expected_3 = ("You have slain your enemy!\n"
                      "Test Name --  HP: 100/125 | Energy: 50/100 | Damage: 22\n"
                      "You have gained 1 experience. | Experience: (1/3)\n")
        enemy_slain(board, character)
        actual_1 = character
        actual_2 = board
        actual_3 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)
