from unittest import TestCase
from unittest.mock import patch
from game import show_stats
import io


class TestShowStats(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_stats(self, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 2),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 100, 'Energy': 80, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        expected_1 = ('\n'
                      'Your stats:\n'
                      'Health: 100 / 125  |  Energy: 80 / 100  |  Damage: 22\n'
                      'Name: Test Name  |  Clan: Warriors of Amazon\n'
                      '\n'
                      'Experience: 0 / 3  |  Level: 1  |  Enemies Slain: 0\n'
                      '\n'
                      'Special Ability: Execute\n'
                      '    Description: You strike your opponent with the intent to kill. This '
                      'deals 2x your damage and instantly kills them if they are below 15% HP.\n'
                      '    Energy Cost: 50\n'
                      '\n')
        expected_2 = character.copy()
        show_stats(character)
        actual_1 = output_string.getvalue()
        actual_2 = character
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
