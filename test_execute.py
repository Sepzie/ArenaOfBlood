from unittest import TestCase
from unittest.mock import patch
from game import execute
import io


class TestExecute(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_unsuccessful(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 100, 'Energy': 70, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        enemy = {"Name": "Samaritan Soldier", "HP": 100, "Damage": 20, 'Max HP': 100}
        expected_1 = ("You have just attempted to execute your opponent. That dealt 44 damage.\n"
                      "That wasn't quite enough to take them out.\n"
                      "Your opponent takes a step back, you can see the fear in their eyes\n")
        expected_2 = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                      'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                      'Enemies Slain': 0, 'HP': 100, 'Energy': 20, 'Damage': 22,
                      'Special Ability': 'Execute', 'Special Ability Description':
                          'You strike your opponent with the intent to kill. This deals 2x your '
                          'damage and instantly kills them if they are below 15% HP.',
                      'Max HP': 125, 'Max Energy': 100}
        expected_3 = {"Name": "Samaritan Soldier", "HP": 56, "Damage": 20, 'Max HP': 100}
        execute(character, enemy)
        actual_1 = output_string.getvalue()
        actual_2 = character
        actual_3 = enemy
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_successful(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 100, 'Energy': 70, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        enemy = {"Name": "Samaritan Soldier", "HP": 59, "Damage": 20, 'Max HP': 100}
        expected_1 = ("You have just attempted to execute your opponent. That dealt 44 damage.\n"
                      "They were too weak to withstand that blow.\n")
        expected_2 = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                      'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                      'Enemies Slain': 0, 'HP': 100, 'Energy': 20, 'Damage': 22,
                      'Special Ability': 'Execute', 'Special Ability Description':
                          'You strike your opponent with the intent to kill. This deals 2x your '
                          'damage and instantly kills them if they are below 15% HP.',
                      'Max HP': 125, 'Max Energy': 100}
        expected_3 = {"Name": "Samaritan Soldier", "HP": 0, "Damage": 20, 'Max HP': 100}
        execute(character, enemy)
        actual_1 = output_string.getvalue()
        actual_2 = character
        actual_3 = enemy
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_low_energy(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 100, 'Energy': 45, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        enemy = {"Name": "Samaritan Soldier", "HP": 59, "Damage": 20, 'Max HP': 100}
        expected_1 = (
            "You don't have enough energy to execute your opponent.\n")
        expected_2 = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                      'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                      'Enemies Slain': 0, 'HP': 100, 'Energy': 45, 'Damage': 22,
                      'Special Ability': 'Execute', 'Special Ability Description':
                          'You strike your opponent with the intent to kill. This deals 2x your '
                          'damage and instantly kills them if they are below 15% HP.',
                      'Max HP': 125, 'Max Energy': 100}
        expected_3 = {"Name": "Samaritan Soldier", "HP": 59, "Damage": 20, 'Max HP': 100}
        execute(character, enemy)
        actual_1 = output_string.getvalue()
        actual_2 = character
        actual_3 = enemy
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)
