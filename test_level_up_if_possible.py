from unittest import TestCase
from unittest.mock import patch
from game import level_up_if_possible
import io


class TestLevelUpIfPossible(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_if_possible_not_possible(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 100, 'Energy': 50, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        expected_1 = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                      'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                      'Enemies Slain': 0, 'HP': 100, 'Energy': 50, 'Damage': 22,
                      'Special Ability': 'Execute', 'Special Ability Description':
                          'You strike your opponent with the intent to kill. This deals 2x your '
                          'damage and instantly kills them if they are below 15% HP.',
                      'Max HP': 125, 'Max Energy': 100}
        expected_2 = ""
        level_up_if_possible(character)
        actual_1 = character
        actual_2 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_if_possible_possible(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 3, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 100, 'Energy': 50, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        expected_1 = {'Clan': 'Warriors of Amazon',
                      'Damage': 35,
                      'Enemies Slain': 0,
                      'Energy': 130,
                      'HP': 187,
                      'Level': 2,
                      'Max Energy': 130,
                      'Max HP': 187,
                      'Max XP': 5,
                      'Name': 'Test Name',
                      'Position': (0, 0),
                      'Previous Position': (0, 0),
                      'Special Ability': 'Execute',
                      'Special Ability Description':
                          'You strike your opponent with the intent to '
                          'kill. This deals 2x your damage and instantly '
                          'kills them if they are below 15% HP.',
                      'XP': 0}
        expected_2 = ("You feel yourself getting stronger.\n"
                      "You are now level 2.\n"
                      "Your health and energy have been replenished.\n")
        level_up_if_possible(character)
        actual_1 = character
        actual_2 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
