from unittest import TestCase
from unittest.mock import patch
from game import spawn_enemies


class TestSpawnEnemies(TestCase):
    @patch('random.choice', return_value={"Name": "Samaritan Soldier", "HP": 100, "Damage": 20})
    @patch('random.random', return_value=0.2)
    def test_spawn_enemies_same_enemy_in_all_rooms(self, _, __):
        board = {'Dimensions': (2, 2),
                 (0, 0): {'Enemy': [], 'Explored': True},
                 (0, 1): {'Enemy': [], 'Explored': False},
                 (1, 0): {'Enemy': [], 'Explored': False},
                 (1, 1): {'Enemy': [], 'Explored': False}}
        expected = {'Dimensions': (2, 2),
                    (0, 0): {'Enemy': [{'Damage': 20,
                                        'HP': 100,
                                        'Max HP': 100,
                                        'Name': 'Samaritan Soldier'}],
                             'Explored': True},
                    (0, 1): {'Enemy': [{'Damage': 20,
                                        'HP': 100,
                                        'Max HP': 100,
                                        'Name': 'Samaritan Soldier'}],
                             'Explored': False},
                    (1, 0): {'Enemy': [{'Damage': 20,
                                        'HP': 100,
                                        'Max HP': 100,
                                        'Name': 'Samaritan Soldier'}],
                             'Explored': False},
                    (1, 1): {'Enemy': [{'Damage': 50,
                                        'HP': 700,
                                        'Max HP': 700,
                                        'Name': 'Goddess of The Red Moon'}],
                             'Explored': False}}
        spawn_enemies(board)
        actual = board
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[{"Name": "Samaritan Soldier", "HP": 100, "Damage": 20},
                                         {"Name": "Persian Monk", "HP": 105, "Damage": 18},
                                         {"Name": "Fire Worshiper", "HP": 95, "Damage": 22},
                                         {"Name": "Russian Blacksmith", "HP": 100, "Damage": 20},
                                         {"Name": "Samaritan Soldier", "HP": 100, "Damage": 20},
                                         {"Name": "Persian Monk", "HP": 105, "Damage": 18}])
    @patch('random.random', return_value=0.2)
    def test_spawn_enemies_different_enemy_in_all_rooms(self, _, __):
        board = {'Dimensions': (2, 3),
                 (0, 0): {'Enemy': [], 'Explored': True},
                 (0, 1): {'Enemy': [], 'Explored': False},
                 (0, 2): {'Enemy': [], 'Explored': False},
                 (1, 0): {'Enemy': [], 'Explored': False},
                 (1, 1): {'Enemy': [], 'Explored': False},
                 (1, 2): {'Enemy': [], 'Explored': False}}
        expected = {'Dimensions': (2, 3),
                    (0, 0): {'Enemy': [{'Damage': 20,
                                        'HP': 100,
                                        'Max HP': 100,
                                        'Name': 'Samaritan Soldier'}],
                             'Explored': True},
                    (0, 1): {'Enemy': [{'Damage': 18,
                                        'HP': 105,
                                        'Max HP': 105,
                                        'Name': 'Persian Monk'}],
                             'Explored': False},
                    (0, 2): {'Enemy': [{'Damage': 22,
                                        'HP': 95,
                                        'Max HP': 95,
                                        'Name': 'Fire Worshiper'}],
                             'Explored': False},
                    (1, 0): {'Enemy': [{'Damage': 20,
                                        'HP': 100,
                                        'Max HP': 100,
                                        'Name': 'Russian Blacksmith'}],
                             'Explored': False},
                    (1, 1): {'Enemy': [{'Damage': 20,
                                        'HP': 104,
                                        'Max HP': 104,
                                        'Name': 'Samaritan Soldier'}],
                             'Explored': False},
                    (1, 2): {'Enemy': [{'Damage': 50,
                                        'HP': 700,
                                        'Max HP': 700,
                                        'Name': 'Goddess of The Red Moon'}],
                             'Explored': False}}
        spawn_enemies(board)
        actual = board
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=[{"Name": "Samaritan Soldier", "HP": 100, "Damage": 20},
                                         {"Name": "Fire Worshiper", "HP": 95, "Damage": 22}])
    @patch('random.random', side_effect=[0.2, 0.5, 0.1, 0.4])
    def test_spawn_enemies_different_enemy_in_some_rooms(self, _, __):
        board = {'Dimensions': (2, 2),
                 (0, 0): {'Enemy': [], 'Explored': True},
                 (0, 1): {'Enemy': [], 'Explored': False},
                 (1, 0): {'Enemy': [], 'Explored': False},
                 (1, 1): {'Enemy': [], 'Explored': False}}
        expected = {'Dimensions': (2, 2),
                    (0, 0): {'Enemy': [{'Damage': 20,
                                        'HP': 100,
                                        'Max HP': 100,
                                        'Name': 'Samaritan Soldier'}],
                             'Explored': True},
                    (0, 1): {'Enemy': [], 'Explored': False},
                    (1, 0): {'Enemy': [{'Damage': 22,
                                        'HP': 95,
                                        'Max HP': 95,
                                        'Name': 'Fire Worshiper'}],
                             'Explored': False},
                    (1, 1): {'Enemy': [{'Damage': 50,
                                        'HP': 700,
                                        'Max HP': 700,
                                        'Name': 'Goddess of The Red Moon'}],
                             'Explored': False}}
        spawn_enemies(board)
        actual = board
        self.assertEqual(expected, actual)
