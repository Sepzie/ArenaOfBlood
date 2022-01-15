from unittest import TestCase
from game import make_board


class TestMakeBoard(TestCase):
    def test_make_board_two_by_two(self):
        expected = {'Dimensions': (2, 2),
                    (0, 0): {'Enemy': [], 'Explored': True},
                    (0, 1): {'Enemy': [], 'Explored': False},
                    (1, 0): {'Enemy': [], 'Explored': False},
                    (1, 1): {'Enemy': [], 'Explored': False}}
        actual = make_board(2, 2)
        self.assertEqual(expected, actual)

    def test_make_board_three_by_two(self):
        expected = {'Dimensions': (3, 2),
                    (0, 0): {'Enemy': [], 'Explored': True},
                    (0, 1): {'Enemy': [], 'Explored': False},
                    (1, 0): {'Enemy': [], 'Explored': False},
                    (1, 1): {'Enemy': [], 'Explored': False},
                    (2, 0): {'Enemy': [], 'Explored': False},
                    (2, 1): {'Enemy': [], 'Explored': False}}
        actual = make_board(3, 2)
        self.assertEqual(expected, actual)

    def test_make_board_two_by_three(self):
        expected = {'Dimensions': (2, 3),
                    (0, 0): {'Enemy': [], 'Explored': True},
                    (0, 1): {'Enemy': [], 'Explored': False},
                    (0, 2): {'Enemy': [], 'Explored': False},
                    (1, 0): {'Enemy': [], 'Explored': False},
                    (1, 1): {'Enemy': [], 'Explored': False},
                    (1, 2): {'Enemy': [], 'Explored': False}}
        actual = make_board(2, 3)
        self.assertEqual(expected, actual)
