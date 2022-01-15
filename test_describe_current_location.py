from unittest import TestCase
from unittest.mock import patch
from game import describe_current_location
import io


class TestDescribeCurrentLocation(TestCase):
    location1 = "You enter a dimly lit hall with torches burning on the walls.\n" \
                "There are claw marks on the walls. Something big must have been kept captive here."
    location2 = "You enter a hall that has no ceiling. Sunlight brightens the whole room.\n" \
                "There are burnt paintings hanging on the walls."
    location3 = "You enter a hall with a chandelier hanging from the ceiling.\nYou might have " \
                "mistaken it for a banquet hall if it wasn't for all the blood on the walls."

    enemy_description1 = "is hurriedly running across the hall. He might run into you if he " \
                         "keeps moving like that."
    enemy_description2 = "is standing in the corner. She gives you a nasty look and spits on " \
                         "the floor"
    enemy_description3 = "is sitting cross-legged in the middle of the room. You wouldn't want " \
                         "to disturb her, she might be meditating."

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.choice', side_effect=[location1, enemy_description1])
    def test_describe_current_location_location_1_enemy_1(self, _, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 125, 'Energy': 100, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        board = {'Dimensions': (2, 2),
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
        describe_current_location(board, character)
        actual = output_string.getvalue()
        expected = ("\n"
                    "You enter a dimly lit hall with torches burning on the walls.\n"
                    "There are claw marks on the walls. Something big must have been kept captive "
                    "here.\n"
                    "\n"
                    "A Samaritan Soldier is hurriedly running across the hall. He might run into "
                    "you if he keeps moving like that. \n"
                    "\n")
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.choice', side_effect=[location2, enemy_description2])
    def test_describe_current_location_location_2_enemy_2(self, _, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (1, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 125, 'Energy': 100, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        board = {'Dimensions': (2, 2),
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
                          'Explored': True},
                 (1, 1): {'Enemy': [{'Damage': 50,
                                     'HP': 700,
                                     'Max HP': 700,
                                     'Name': 'Goddess of The Red Moon'}],
                          'Explored': False}}
        describe_current_location(board, character)
        actual = output_string.getvalue()
        expected = ("\n"
                    "You enter a hall that has no ceiling. Sunlight brightens the whole room.\n"
                    "There are burnt paintings hanging on the walls.\n"
                    "\n"
                    "A Fire Worshiper is standing in the corner. She gives you a nasty look and "
                    "spits on the floor \n"
                    "\n")
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.choice', side_effect=[location3, enemy_description3])
    def test_describe_current_location_location_3_enemy_3(self, _, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 0),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 125, 'Energy': 100, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        board = {'Dimensions': (2, 2),
                 (0, 0): {'Enemy': [{'Damage': 20,
                                     'HP': 100,
                                     'Max HP': 100,
                                     'Name': 'Persian Monk'}],
                          'Explored': True},
                 (0, 1): {'Enemy': [], 'Explored': False},
                 (1, 0): {'Enemy': [{'Damage': 22,
                                     'HP': 95,
                                     'Max HP': 95,
                                     'Name': 'Fire Worshiper'}],
                          'Explored': True},
                 (1, 1): {'Enemy': [{'Damage': 50,
                                     'HP': 700,
                                     'Max HP': 700,
                                     'Name': 'Goddess of The Red Moon'}],
                          'Explored': False}}
        describe_current_location(board, character)
        actual = output_string.getvalue()
        expected = ("\n"
                    "You enter a hall with a chandelier hanging from the ceiling.\n"
                    "You might have mistaken it for a banquet hall if it wasn't for all the blood "
                    "on the walls.\n"
                    "\n"
                    "A Persian Monk is sitting cross-legged in the middle of the room. You "
                    "wouldn't want to disturb her, she might be meditating. \n"
                    "\n")
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.choice', return_value=location2)
    def test_describe_current_location_location_2_no_enemy(self, _, output_string):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (0, 1),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 125, 'Energy': 100, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        board = {'Dimensions': (2, 2),
                 (0, 0): {'Enemy': [{'Damage': 20,
                                     'HP': 100,
                                     'Max HP': 100,
                                     'Name': 'Persian Monk'}],
                          'Explored': True},
                 (0, 1): {'Enemy': [], 'Explored': False},
                 (1, 0): {'Enemy': [{'Damage': 22,
                                     'HP': 95,
                                     'Max HP': 95,
                                     'Name': 'Fire Worshiper'}],
                          'Explored': True},
                 (1, 1): {'Enemy': [{'Damage': 50,
                                     'HP': 700,
                                     'Max HP': 700,
                                     'Name': 'Goddess of The Red Moon'}],
                          'Explored': False}}
        describe_current_location(board, character)
        actual = output_string.getvalue()
        expected = ("\n"
                    "You enter a hall that has no ceiling. Sunlight brightens the whole room.\n"
                    "There are burnt paintings hanging on the walls.\n"
                    "\n")
        self.assertEqual(expected, actual)
