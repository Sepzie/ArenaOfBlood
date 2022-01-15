from unittest import TestCase
from unittest.mock import patch
from game import initialize_game
import io


class TestInitializeGame(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["1", "Test Name", ""])
    def test_initialize_game_clan_1(self, _, output_string):
        expected_1 = (
            "After a long travel, you finally step up to the gates. A woman shouts at you:\n"
            "\"Welcome challenger! You have approached the Arena of Blood.\n"
            "Tell us which clan you are from if you wish to be granted entry.\"\n"
            "1. Warriors of Amazon   2. Priests of Atlantis   3. Shape Shifters of Narnia   "
            "q. Quit\n"
            "\"Ah! A warrior. I also used to be a part of the sisterhood once.\n"
            "What is your name warrior?\"\n"
            "\"Test Name of the Warriors of Amazon, welcome to the Arena of Blood!\"\n"
            "The gates of the arena swing open with a loud screech.\n"
            "\"The Goddess of The Red Moon is awaiting you on the other side of the arena.\n"
            "Find you way through the halls to get to her.\n"
            "On your way, you may come across other challengers that are in the arena.\"\n"
            "\n")
        expected_2 = "Test Name"
        expected_3 = "Warriors of Amazon"
        actual_2, actual_3 = initialize_game()
        actual_1 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["2", "Test Name", ""])
    def test_initialize_game_clan_2(self, _, output_string):
        expected_1 = (
            "After a long travel, you finally step up to the gates. A woman shouts at you:\n"
            "\"Welcome challenger! You have approached the Arena of Blood.\n"
            "Tell us which clan you are from if you wish to be granted entry.\"\n"
            "1. Warriors of Amazon   2. Priests of Atlantis   3. Shape Shifters of Narnia   "
            "q. Quit\n"
            "\"A priest at the arena of blood? Have you lost your way father?\n"
            "Tell us your name priest!\"\n"
            "\"Test Name of the Priests of Atlantis, welcome to the Arena of Blood!\"\n"
            "The gates of the arena swing open with a loud screech.\n"
            "\"The Goddess of The Red Moon is awaiting you on the other side of the arena.\n"
            "Find you way through the halls to get to her.\n"
            "On your way, you may come across other challengers that are in the arena.\"\n"
            "\n")
        expected_2 = "Test Name"
        expected_3 = "Priests of Atlantis"
        actual_2, actual_3 = initialize_game()
        actual_1 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["3", "Test Name", ""])
    def test_initialize_game_clan_3(self, _, output_string):
        expected_1 = (
            "After a long travel, you finally step up to the gates. A woman shouts at you:\n"
            "\"Welcome challenger! You have approached the Arena of Blood.\n"
            "Tell us which clan you are from if you wish to be granted entry.\"\n"
            "1. Warriors of Amazon   2. Priests of Atlantis   3. Shape Shifters of Narnia   "
            "q. Quit\n"
            "\"A Shape Shifter! My sisters used to go crazy for your kind back in the Amazons.\n"
            "What is your name shape shifter?\"\n"
            "\"Test Name of the Shape Shifters of Narnia, welcome to the Arena of Blood!\"\n"
            "The gates of the arena swing open with a loud screech.\n"
            "\"The Goddess of The Red Moon is awaiting you on the other side of the arena.\n"
            "Find you way through the halls to get to her.\n"
            "On your way, you may come across other challengers that are in the arena.\"\n"
            "\n")
        expected_2 = "Test Name"
        expected_3 = "Shape Shifters of Narnia"
        actual_2, actual_3 = initialize_game()
        actual_1 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)
