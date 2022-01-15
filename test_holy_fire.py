from unittest import TestCase
from unittest.mock import patch
from game import holy_fire
import io


class TestHolyFire(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_holy_fire_enough_energy(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 70, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        enemy = {"Name": "Samaritan Soldier", "HP": 100, "Damage": 20, 'Max HP': 100}
        expected_1 = ("You have just cast a spell of holy fire on your opponent.\n"
                      "The fire burns them for 38 damage, and the light heals you for 38 hit"
                      " points.\n")
        expected_2 = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                      'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                      'Enemies Slain': 0, 'HP': 88, 'Energy': 20, 'Damage': 22,
                      'Special Ability': 'Execute', 'Special Ability Description':
                          'You strike your opponent with the intent to kill. This deals 2x your '
                          'damage and instantly kills them if they are below 15% HP.',
                      'Max HP': 125, 'Max Energy': 100}
        expected_3 = {"Name": "Samaritan Soldier", "HP": 62, "Damage": 20, 'Max HP': 100}
        holy_fire(character, enemy)
        actual_1 = output_string.getvalue()
        actual_2 = character
        actual_3 = enemy
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_holy_fire_not_enough_energy(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 40, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        enemy = {"Name": "Samaritan Soldier", "HP": 100, "Damage": 20, 'Max HP': 100}
        expected_1 = "You don't have enough energy to cast holy fire.\n"
        expected_2 = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                      'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                      'Enemies Slain': 0, 'HP': 50, 'Energy': 40, 'Damage': 22,
                      'Special Ability': 'Execute', 'Special Ability Description':
                          'You strike your opponent with the intent to kill. This deals 2x your '
                          'damage and instantly kills them if they are below 15% HP.',
                      'Max HP': 125, 'Max Energy': 100}
        expected_3 = {"Name": "Samaritan Soldier", "HP": 100, "Damage": 20, 'Max HP': 100}
        holy_fire(character, enemy)
        actual_1 = output_string.getvalue()
        actual_2 = character
        actual_3 = enemy
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)
