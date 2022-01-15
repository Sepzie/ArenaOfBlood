from unittest import TestCase
from game import regeneration


class TestRegeneration(TestCase):
    def test_regeneration_default(self):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 100, 'Energy': 50, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        expected = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                    'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                    'Enemies Slain': 0, 'HP': 103, 'Energy': 55, 'Damage': 22,
                    'Special Ability': 'Execute', 'Special Ability Description':
                        'You strike your opponent with the intent to kill. This deals 2x your '
                        'damage and instantly kills them if they are below 15% HP.',
                    'Max HP': 125, 'Max Energy': 100}
        regeneration(character)
        actual = character
        self.assertEqual(expected, actual)

    def test_regeneration_character_level_3(self):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 3, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 50, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        expected = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                    'Previous Position': (0, 0), 'Level': 3, 'XP': 0, 'Max XP': 3,
                    'Enemies Slain': 0, 'HP': 57, 'Energy': 61, 'Damage': 22,
                    'Special Ability': 'Execute', 'Special Ability Description':
                        'You strike your opponent with the intent to kill. This deals 2x your '
                        'damage and instantly kills them if they are below 15% HP.',
                    'Max HP': 125, 'Max Energy': 100}
        regeneration(character)
        actual = character
        self.assertEqual(expected, actual)

    def test_regeneration_with_heal_value(self):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 50, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        expected = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                    'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                    'Enemies Slain': 0, 'HP': 100, 'Energy': 55, 'Damage': 22,
                    'Special Ability': 'Execute', 'Special Ability Description':
                        'You strike your opponent with the intent to kill. This deals 2x your '
                        'damage and instantly kills them if they are below 15% HP.',
                    'Max HP': 125, 'Max Energy': 100}
        regeneration(character, heal=50)
        actual = character
        self.assertEqual(expected, actual)

    def test_regeneration_with_energy_value(self):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 50, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        expected = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                    'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                    'Enemies Slain': 0, 'HP': 53, 'Energy': 80, 'Damage': 22,
                    'Special Ability': 'Execute', 'Special Ability Description':
                        'You strike your opponent with the intent to kill. This deals 2x your '
                        'damage and instantly kills them if they are below 15% HP.',
                    'Max HP': 125, 'Max Energy': 100}
        regeneration(character, energy=30)
        actual = character
        self.assertEqual(expected, actual)

    def test_regeneration_to_max(self):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 50, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        expected = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                    'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                    'Enemies Slain': 0, 'HP': 125, 'Energy': 100, 'Damage': 22,
                    'Special Ability': 'Execute', 'Special Ability Description':
                        'You strike your opponent with the intent to kill. This deals 2x your '
                        'damage and instantly kills them if they are below 15% HP.',
                    'Max HP': 125, 'Max Energy': 100}
        regeneration(character, heal=200, energy=200)
        actual = character
        self.assertEqual(expected, actual)
