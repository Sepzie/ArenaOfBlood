from unittest import TestCase
from unittest.mock import patch
from game import flee_combat
import io


class TestFleeCombat(TestCase):
    @patch('builtins.input', side_effect="\n")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_combat_successful(self, output_string, _):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (1, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 70, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        enemy = {"Name": "Samaritan Soldier", "HP": 100, "Damage": 20, 'Max HP': 100}
        expected_1 = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                      'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                      'Enemies Slain': 0, 'HP': 44, 'Energy': 70, 'Damage': 22,
                      'Special Ability': 'Execute', 'Special Ability Description':
                          'You strike your opponent with the intent to kill. This deals 2x your '
                          'damage and instantly kills them if they are below 15% HP.',
                      'Max HP': 125, 'Max Energy': 100}
        expected_2 = True
        expected_3 = ("You come to your senses and choose to flee from the fight.\n"
                      "The Samaritan Soldier throws a rock at you as you are running away.\n"
                      "Test Name --  HP: 44/125 | Energy: 70/100 | Damage: 22\n")
        actual_2 = flee_combat(character, enemy)
        actual_1 = character
        actual_3 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_combat_unsuccessful(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (1, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 100, 'Energy': 70, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        enemy = {"Name": "Goddess of The Red Moon", "HP": 100, "Damage": 20, 'Max HP': 100}
        expected_1 = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (1, 0),
                      'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                      'Enemies Slain': 0, 'HP': 60, 'Energy': 70, 'Damage': 22,
                      'Special Ability': 'Execute', 'Special Ability Description':
                          'You strike your opponent with the intent to kill. This deals 2x your '
                          'damage and instantly kills them if they are below 15% HP.',
                      'Max HP': 125, 'Max Energy': 100}
        expected_2 = False
        expected_3 = ("In fear you decide to flee from the fight.\n"
                      "As you turn your back to The Goddess in an attempt to run away, you find "
                      "her standing in front of you.\n"
                      "She yells \"You stench of fear mortal. You can not run from your demise.\"\n"
                      "She lands a direct strike into your face.\n"
                      "Test Name --  HP: 60/125 | Energy: 70/100 | Damage: 22\n")
        actual_2 = flee_combat(character, enemy)
        actual_1 = character
        actual_3 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)
