from unittest import TestCase
from game import check_alive


class TestCheckAlive(TestCase):
    def test_check_alive_hp_positive(self):
        character = {'Name': 'ASD', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 125, 'Energy': 100, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}

        expected_1 = character.copy()
        expected_2 = True
        actual_1 = character
        actual_2 = check_alive(character)
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)

    def test_check_alive_hp_zero(self):
        character = {'Name': 'ASD', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 0, 'Energy': 100, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}

        expected_1 = character.copy()
        expected_2 = False
        actual_1 = character
        actual_2 = check_alive(character)
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)

    def test_check_alive_hp_negative(self):
        character = {'Name': 'ASD', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': -10, 'Energy': 100, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}

        expected_1 = character.copy()
        expected_2 = False
        actual_1 = character
        actual_2 = check_alive(character)
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
