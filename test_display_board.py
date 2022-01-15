from unittest import TestCase
from unittest.mock import patch
from game import display_board
import io


class TestDisplayBoard(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_some_explored(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 2),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
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
        expected = ("▢ ▢ ⏺ \n"
                    "⏹ ⏹ ⏹ \n")
        display_board(board, character)
        actual = output_string.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_none_explored(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
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
                          'Explored': False},
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
        expected = ("⏹ ⏹ ⏹ \n"
                    "⏹ ⏹ ⏹ \n")
        display_board(board, character)
        actual = output_string.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_board_all_explored(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (1, 2),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
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
                          'Explored': True},
                 (1, 1): {'Enemy': [{'Damage': 20,
                                     'HP': 104,
                                     'Max HP': 104,
                                     'Name': 'Samaritan Soldier'}],
                          'Explored': True},
                 (1, 2): {'Enemy': [{'Damage': 50,
                                     'HP': 700,
                                     'Max HP': 700,
                                     'Name': 'Goddess of The Red Moon'}],
                          'Explored': True}}
        expected = ("▢ ▢ ▢ \n"
                    "▢ ▢ ⏺ \n")
        display_board(board, character)
        actual = output_string.getvalue()
        self.assertEqual(expected, actual)
