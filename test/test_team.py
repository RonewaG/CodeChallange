from test_utils import add_src_to_path
add_src_to_path()

import unittest
from team import Team


class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team = Team("Lion Club")

    def test_initial_points(self):
        self.assertEqual(self.team.points, 0)
    
    def test_team_name(self):
        self.assertEqual(self.team.name, "Lion Club")

    def test_add_points(self):
        self.team.add_points(3)
        self.assertEqual(self.team.points, 3)

if __name__ == '__main__':
    unittest.main()