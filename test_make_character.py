from unittest import TestCase
from game import make_character


class TestMakeCharacter(TestCase):
    def test_make_character_warrior(self):
        expected = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                    'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                    'Enemies Slain': 0, 'HP': 125, 'Energy': 100, 'Damage': 22,
                    'Special Ability': 'Execute', 'Special Ability Description':
                        'You strike your opponent with the intent to kill. This deals 2x your '
                        'damage and instantly kills them if they are below 15% HP.',
                    'Max HP': 125, 'Max Energy': 100}
        actual = make_character("Test Name", 'Warriors of Amazon')
        self.assertEqual(expected, actual)

    def test_make_character_priest(self):
        expected = {'Clan': 'Priests of Atlantis',
                    'Damage': 18,
                    'Enemies Slain': 0,
                    'Energy': 120,
                    'HP': 125,
                    'Level': 1,
                    'Max Energy': 120,
                    'Max HP': 125,
                    'Max XP': 3,
                    'Name': 'Test Name',
                    'Position': (0, 0),
                    'Previous Position': (0, 0),
                    'Special Ability': 'Holy Fire',
                    'Special Ability Description': 'You purify your opponent with holy fire. '
                                                   'Thisdeals 1.75x your damage to them and heals '
                                                   'you for the same amount',
                    'XP': 0}
        actual = make_character("Test Name", 'Priests of Atlantis')
        self.assertEqual(expected, actual)

    def test_make_character_shape_shifter(self):
        expected = {'Clan': 'Shape Shifters of Narnia',
                    'Damage': 20,
                    'Enemies Slain': 0,
                    'Energy': 110,
                    'HP': 125,
                    'Level': 1,
                    'Max Energy': 110,
                    'Max HP': 125,
                    'Max XP': 3,
                    'Name': 'Test Name',
                    'Position': (0, 0),
                    'Previous Position': (0, 0),
                    'Special Ability': 'Bite',
                    'Special Ability Description': 'You shape shift into a wolf and bite a chunk '
                                                   'out of your opponent.This deals 3x your '
                                                   'damage',
                    'XP': 0}
        actual = make_character("Test Name", 'Shape Shifters of Narnia')
        self.assertEqual(expected, actual)
