from unittest import TestCase
from unittest.mock import patch
from game import display_ending_message
import io


class TestDisplayEndingMessages(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_ending_messages_character_hp_negative(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 0, 'Energy': 50, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        expected = "You died!\n"
        display_ending_message(character)
        actual = output_string.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_ending_messages_character_hp_zero(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': -15, 'Energy': 50, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        expected = "You died!\n"
        display_ending_message(character)
        actual = output_string.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_ending_messages_ending_1(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 7, 'HP': 30, 'Energy': 50, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        expected = ("You have successfully defeated The Goddess of The Red Moon!\n"
                    "Your turn your back, bloodied and tired, and start walking away from the hall."
                    "\n"
                    "Suddenly you hear a noise coming from behind you. You look back and see the "
                    "Goddess has risen from the dead.\n"
                    "She says \"Did you really think you could kill a Goddess?\"\n"
                    "She rises to the roof of the hall and disappears into the light.\n"
                    "\n"
                    " Ending 1 Unlocked\n")
        display_ending_message(character)
        actual = output_string.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_ending_messages_ending_2(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 50, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        expected = " Ending 2 Unlocked\n"
        display_ending_message(character)
        actual = output_string.getvalue()
        self.assertEqual(expected, actual)
