from unittest import TestCase
from unittest.mock import patch
from game import cast_special_ability
import io


class TestCastSpecialAbility(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cast_special_ability_execute(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (1, 2),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 100, 'Energy': 80, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        enemy = {"Name": "Samaritan Soldier", "HP": 100, "Damage": 20, 'Max HP': 100}
        expected_1 = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (1, 2),
                      'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                      'Enemies Slain': 0, 'HP': 100, 'Energy': 30, 'Damage': 22,
                      'Special Ability': 'Execute', 'Special Ability Description':
                          'You strike your opponent with the intent to kill. This deals 2x your '
                          'damage and instantly kills them if they are below 15% HP.',
                      'Max HP': 125, 'Max Energy': 100}
        expected_2 = {"Name": "Samaritan Soldier", "HP": 56, "Damage": 20, 'Max HP': 100}
        expected_3 = ("You have just attempted to execute your opponent. That dealt 44 damage.\n"
                      "That wasn't quite enough to take them out.\n"
                      "Your opponent takes a step back, you can see the fear in their eyes\n")
        cast_special_ability(character, enemy)
        actual_1 = character
        actual_2 = enemy
        actual_3 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cast_special_ability_holy_fire(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Priests of Atlantis', 'Position': (1, 2),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 80, 'Damage': 22,
                     'Special Ability': 'Holy Fire', 'Special Ability Description':
                         'You purify your opponent with holy fire. This'
                         'deals 1.75x your damage to them and heals you'
                         ' for the same amount',
                     'Max HP': 125, 'Max Energy': 100}
        enemy = {"Name": "Samaritan Soldier", "HP": 100, "Damage": 20, 'Max HP': 100}
        expected_1 = {'Name': 'Test Name', 'Clan': 'Priests of Atlantis', 'Position': (1, 2),
                      'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                      'Enemies Slain': 0, 'HP': 88, 'Energy': 30, 'Damage': 22,
                      'Special Ability': 'Holy Fire', 'Special Ability Description':
                          'You purify your opponent with holy fire. This'
                          'deals 1.75x your damage to them and heals you'
                          ' for the same amount',
                      'Max HP': 125, 'Max Energy': 100}
        expected_2 = {"Name": "Samaritan Soldier", "HP": 62, "Damage": 20, 'Max HP': 100}
        expected_3 = ("You have just cast a spell of holy fire on your opponent.\n"
                      "The fire burns them for 38 damage, and the light heals you for 38 hit "
                      "points.\n")
        cast_special_ability(character, enemy)
        actual_1 = character
        actual_2 = enemy
        actual_3 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cast_special_ability_bite(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Shape Shifters of Narnia', 'Position': (1, 2),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 50, 'Energy': 80, 'Damage': 22,
                     'Special Ability': 'Bite', 'Special Ability Description':
                         'You shape shift into a wolf and bite a chunk '
                         'out of your opponent.This deals 3x your damage',
                     'Max HP': 125, 'Max Energy': 100}
        enemy = {"Name": "Samaritan Soldier", "HP": 100, "Damage": 20, 'Max HP': 100}
        expected_1 = {'Name': 'Test Name', 'Clan': 'Shape Shifters of Narnia', 'Position': (1, 2),
                      'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                      'Enemies Slain': 0, 'HP': 50, 'Energy': 30, 'Damage': 22,
                      'Special Ability': 'Bite', 'Special Ability Description':
                          'You shape shift into a wolf and bite a chunk '
                          'out of your opponent.This deals 3x your damage',
                      'Max HP': 125, 'Max Energy': 100}
        expected_2 = {'Damage': 20, 'HP': 34, 'Max HP': 100, 'Name': 'Samaritan Soldier'}
        expected_3 = ("You shape shit into a wolf and bite your opponent.\n"
                      "That took a chunk out of them, you dealt 66 damage\n")
        cast_special_ability(character, enemy)
        actual_1 = character
        actual_2 = enemy
        actual_3 = output_string.getvalue()
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
        self.assertEqual(expected_3, actual_3)
