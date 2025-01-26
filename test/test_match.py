from test_utils import add_src_to_path
add_src_to_path()

import unittest
from match import Match

class TestMatch(unittest.TestCase):

    def setUp(self):
        self.match = Match("Lions", 3, "Spiders", 2)

    def test_initialization(self):
        self.assertEqual(self.match.home_name, "Lions")
        self.assertEqual(self.match.home_score, 3)
        self.assertEqual(self.match.away_name, "Spiders")
        self.assertEqual(self.match.away_score, 2)

if __name__ == '__main__':
    unittest.main()
