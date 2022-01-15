from unittest import TestCase
from unittest.mock import patch
from game import get_player_choice
import io


class TestGetPlayerChoice(TestCase):
    @patch('builtins.input', side_effect=["1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_player_choice_normal_1(self, output_string, _):
        options = ('Option 1', 'Option 2', 'Option 3')
        expected_1 = 'Option 1'
        actual_1 = get_player_choice(options)
        expected_2 = "1. Option 1   2. Option 2   3. Option 3   q. Quit\n"
        actual_2 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)

    @patch('builtins.input', side_effect="5")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_player_choice_normal_2(self, output_string, _):
        options = ('Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5')
        expected_1 = 'Option 5'
        actual_1 = get_player_choice(options)
        expected_2 = "1. Option 1   2. Option 2   3. Option 3   4. Option 4   5. Option 5   " \
                     "q. Quit\n"
        actual_2 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)

    @patch('builtins.input', side_effect="a")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_player_choice_input_map(self, output_string, _):
        options = ('Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5')
        input_map = "abcde"
        expected_1 = 'Option 1'
        actual_1 = get_player_choice(options, input_map)
        expected_2 = (
            "a. Option 1   b. Option 2   c. Option 3   d. Option 4   e. Option 5   q. Quit\n")
        actual_2 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)

    @patch('builtins.input', side_effect="d")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_player_choice_input_map_quit_button(self, output_string, _):
        options = ('Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5')
        input_map = "wasdr"
        quit_button = "0"
        expected_1 = 'Option 4'
        actual_1 = get_player_choice(options, input_map, quit_button)
        expected_2 = (
            "w. Option 1   a. Option 2   s. Option 3   d. Option 4   r. Option 5   0. Quit\n")
        actual_2 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)

    @patch('builtins.input', side_effect=['0', '', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_player_choice_quit_button(self, output_string, _):
        options = ('Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5')
        quit_button = "0"
        expected_1 = 'Option 1'
        actual_1 = get_player_choice(options, quit_button=quit_button)
        expected_2 = (
            "1. Option 1   2. Option 2   3. Option 3   4. Option 4   5. Option 5   0. Quit\n"
            "Are you sure you want ot quit? Type \"y\" to confirm: 1. Option 1   2. Option 2   "
            "3. Option 3   4. Option 4   5. Option 5   0. Quit\n")
        actual_2 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)

    @patch('builtins.input', side_effect=['', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_player_choice_incorrect_input(self, output_string, _):
        options = ('Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5')
        quit_button = "0"
        expected_1 = 'Option 1'
        actual_1 = get_player_choice(options, quit_button=quit_button)
        expected_2 = (
            "1. Option 1   2. Option 2   3. Option 3   4. Option 4   5. Option 5   0. Quit\n"
            "That is not a correct option, please choose from the options provided below.\n"
            "1. Option 1   2. Option 2   3. Option 3   4. Option 4   5. Option 5   0. Quit\n")
        actual_2 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
