from unittest import TestCase
from unittest.mock import patch
from game import move_character
import io


class TestMoveCharacter(TestCase):
    def test_move_character_north(self):
        board = {'Dimensions': (2, 2),
                 (0, 0): {'Enemy': [], 'Explored': False},
                 (0, 1): {'Enemy': [], 'Explored': False},
                 (1, 0): {'Enemy': [], 'Explored': True},
                 (1, 1): {'Enemy': [], 'Explored': True}}
        character = {'Position': (1, 0), 'Previous Position': (1, 1)}
        expected_1 = {'Position': (0, 0), 'Previous Position': (1, 0)}
        expected_2 = True
        expected_3 = {'Dimensions': (2, 2),
                      (0, 0): {'Enemy': [], 'Explored': True},
                      (0, 1): {'Enemy': [], 'Explored': False},
                      (1, 0): {'Enemy': [], 'Explored': True},
                      (1, 1): {'Enemy': [], 'Explored': True}}
        actual_2 = move_character(board, character, 'North')
        actual_1 = character
        actual_3 = board
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    def test_move_character_west(self):
        board = {'Dimensions': (2, 2),
                 (0, 0): {'Enemy': [], 'Explored': False},
                 (0, 1): {'Enemy': [], 'Explored': True},
                 (1, 0): {'Enemy': [], 'Explored': False},
                 (1, 1): {'Enemy': [], 'Explored': True}}
        character = {'Position': (0, 1), 'Previous Position': (1, 1)}
        expected_1 = {'Position': (0, 0), 'Previous Position': (0, 1)}
        expected_2 = True
        expected_3 = {'Dimensions': (2, 2),
                      (0, 0): {'Enemy': [], 'Explored': True},
                      (0, 1): {'Enemy': [], 'Explored': True},
                      (1, 0): {'Enemy': [], 'Explored': False},
                      (1, 1): {'Enemy': [], 'Explored': True}}
        actual_2 = move_character(board, character, 'West')
        actual_1 = character
        actual_3 = board
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    def test_move_character_south(self):
        board = {'Dimensions': (2, 2),
                 (0, 0): {'Enemy': [], 'Explored': True},
                 (0, 1): {'Enemy': [], 'Explored': True},
                 (1, 0): {'Enemy': [], 'Explored': False},
                 (1, 1): {'Enemy': [], 'Explored': False}}
        character = {'Position': (0, 0), 'Previous Position': (0, 1)}
        expected_1 = {'Position': (1, 0), 'Previous Position': (0, 0)}
        expected_2 = True
        expected_3 = {'Dimensions': (2, 2),
                      (0, 0): {'Enemy': [], 'Explored': True},
                      (0, 1): {'Enemy': [], 'Explored': True},
                      (1, 0): {'Enemy': [], 'Explored': True},
                      (1, 1): {'Enemy': [], 'Explored': False}}
        actual_2 = move_character(board, character, 'South')
        actual_1 = character
        actual_3 = board
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    def test_move_character_east(self):
        board = {'Dimensions': (2, 2),
                 (0, 0): {'Enemy': [], 'Explored': True},
                 (0, 1): {'Enemy': [], 'Explored': False},
                 (1, 0): {'Enemy': [], 'Explored': True},
                 (1, 1): {'Enemy': [], 'Explored': False}}
        character = {'Position': (0, 0), 'Previous Position': (1, 0)}
        expected_1 = {'Position': (0, 1), 'Previous Position': (0, 0)}
        expected_2 = True
        expected_3 = {'Dimensions': (2, 2),
                      (0, 0): {'Enemy': [], 'Explored': True},
                      (0, 1): {'Enemy': [], 'Explored': True},
                      (1, 0): {'Enemy': [], 'Explored': True},
                      (1, 1): {'Enemy': [], 'Explored': False}}
        actual_2 = move_character(board, character, 'East')
        actual_1 = character
        actual_3 = board
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_character_invalid_move(self, output_string):
        board = {'Dimensions': (2, 2),
                 (0, 0): {'Enemy': [], 'Explored': True},
                 (0, 1): {'Enemy': [], 'Explored': False},
                 (1, 0): {'Enemy': [], 'Explored': True},
                 (1, 1): {'Enemy': [], 'Explored': False}}
        character = {'Position': (0, 0), 'Previous Position': (1, 0)}
        expected_1 = {'Position': (0, 0), 'Previous Position': (1, 0)}
        expected_2 = False
        expected_3 = {'Dimensions': (2, 2),
                      (0, 0): {'Enemy': [], 'Explored': True},
                      (0, 1): {'Enemy': [], 'Explored': False},
                      (1, 0): {'Enemy': [], 'Explored': True},
                      (1, 1): {'Enemy': [], 'Explored': False}}
        expected_4 = "There is no hall in that direction. This seems to be the edge of the arena.\n"
        actual_2 = move_character(board, character, 'West')
        actual_1 = character
        actual_3 = board
        actual_4 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)
        self.assertEqual(expected_4, actual_4)
