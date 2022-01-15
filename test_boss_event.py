from unittest import TestCase
from unittest.mock import patch
from game import boss_event
import io


class TestBossEvent(TestCase):
    @patch('builtins.input', side_effect="\n")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_event_no_enemies_killed(self, output_string, _):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (1, 2),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 0, 'HP': 0, 'Energy': 50, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        board = {'Dimensions': (2, 3),
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
        expected = ("You enter a hall with walls made of pure light.\n"
                    "The Goddess of the Red Moon is sitting on a chair in the middle of the hall.\n"
                    "There is an empty chair and a table besides her.\n"
                    "You notice a teapot and two tea cups on the table\n"
                    "The Goddess softly says \"Join with me for a cup of tea brave challenger.\"\n"
                    "You exclaim \"Aren't you going to fight me!?\"\n"
                    "The Goddess replies \"Only the noblest of souls can cross the arena without "
                    "shedding blood\n"
                    "A peaceful spirit like yours has a resting place besides me in eternity\"\n"
                    "You join The Goddess and sip from the tea cup.\n"
                    "You feel a warm, wholesome feeling fill you body.\n"
                    "You see heaven rise around you as the arena disappears.\n"
                    "\n")
        boss_event(board, character)
        actual = output_string.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["\n", "\n", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_event_normal(self, output_string, _):
        character = {'Name': 'Test Name', 'Clan': 'Warriors of Amazon', 'Position': (1, 2),
                     'Previous Position': (0, 0), 'Level': 1, 'XP': 0, 'Max XP': 3,
                     'Enemies Slain': 1, 'HP': 10, 'Energy': 50, 'Damage': 22,
                     'Special Ability': 'Execute', 'Special Ability Description':
                         'You strike your opponent with the intent to kill. This deals 2x your '
                         'damage and instantly kills them if they are below 15% HP.',
                     'Max HP': 125, 'Max Energy': 100}
        board = {'Dimensions': (2, 3),
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
        expected = ("You enter a hall with the walls glowing red.\n"
                    "You notice they are covered in blood as you walk further into the room.\n"
                    "The Goddess of The Red Moon appears behind you.Her eyes are glowing red, "
                    "with tear drops made of blood rolling down her cheeks.\n"
                    "She screams \"YOU DARE CHALLENGE THE GODDESS IN HER OWN HOME?\"\n" +
                    "\n" * 100 +
                    "\nYou grab a rock and throw it at the Goddess of The Red Moon's head.\n"
                    "That's one way to start a fight...\n"
                    "Test Name --  HP: 10/125 | Energy: 50/100 | Damage: 22\n"
                    "Goddess of The Red Moon -- HP: 700/700 | Damage: 50\n"
                    "1. Attack   2. Execute   3. Flee   q. Quit\n"
                    "You and your opponent strike at each other.\n")
        boss_event(board, character)
        actual = output_string.getvalue()
        self.assertEqual(expected, actual)
