from unittest import TestCase
from unittest.mock import patch
from game import print_enemy_combat_stats
import io


class TestPrintEnemyCombatStats(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_enemy_combat_stats(self, output_string):
        enemy = {"Name": "Samaritan Soldier", "HP": 100, "Damage": 20, 'Max HP': 100}
        expected_1 = "Samaritan Soldier -- HP: 100/100 | Damage: 20\n"
        expected_2 = enemy.copy()
        print_enemy_combat_stats(enemy)
        actual_1 = output_string.getvalue()
        actual_2 = enemy
        self.assertEqual(expected_1, actual_1)
        self.assertEqual(expected_2, actual_2)
