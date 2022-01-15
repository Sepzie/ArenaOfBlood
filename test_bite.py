from unittest import TestCase
from unittest.mock import patch
from game import bite
import io


class TestBite(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bite_enough_energy(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 70, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        enemy = {"Name": "Samaritan Soldier", "HP": 100, "Damage": 20, 'Max HP': 100}
        expected_1 = ("You shape shit into a wolf and bite your opponent.\n"
                      "That took a chunk out of them, you dealt 66 damage\n")
        expected_2 = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                      'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                      'Enemies Slain': 0, 'HP': 50, 'Energy': 20, 'Damage': 22,
                      'Special Ability': 'Execute', 'Special Ability Description':
                          'You strike your opponent with the intent to kill. This deals 2x your '
                          'damage and instantly kills them if they are below 15% HP.',
                      'Max HP': 125, 'Max Energy': 100}
        expected_3 = {"Name": "Samaritan Soldier", "HP": 34, "Damage": 20, 'Max HP': 100}
        bite(character, enemy)
        actual_1 = output_string.getvalue()
        actual_2 = character
        actual_3 = enemy
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bite_not_enough_energy(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 40, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        enemy = {"Name": "Samaritan Soldier", "HP": 100, "Damage": 20, 'Max HP': 100}
        expected_1 = "You don't have enough energy to shape shift.\n"
        expected_2 = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                      'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                      'Enemies Slain': 0, 'HP': 50, 'Energy': 40, 'Damage': 22,
                      'Special Ability': 'Execute', 'Special Ability Description':
                          'You strike your opponent with the intent to kill. This deals 2x your '
                          'damage and instantly kills them if they are below 15% HP.',
                      'Max HP': 125, 'Max Energy': 100}
        expected_3 = {"Name": "Samaritan Soldier", "HP": 100, "Damage": 20, 'Max HP': 100}
        bite(character, enemy)
        actual_1 = output_string.getvalue()
        actual_2 = character
        actual_3 = enemy
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)
