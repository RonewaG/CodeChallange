from test_utils import add_src_to_path
add_src_to_path()

import unittest
from score_calculator import ScoreCalculator
from team import Team
from match import Match

class TestScoreCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = ScoreCalculator()


    def test_calculate_home_win(self):
        match = Match("Spider", 3, "Lions", 1)
        self.calculator.calculate(match)

        home_team = self.calculator.get_team("Spider")
        away_team = self.calculator.get_team("Lions")
        
        self.assertEqual(home_team.points, 3)
        self.assertEqual(away_team.points, 0)

    def test_calculate_away_win(self):
        match = Match("Spider", 1, "Lions", 2)
        self.calculator.calculate(match)

        home_team = self.calculator.get_team("Spider")
        away_team = self.calculator.get_team("Lions")
        
        self.assertEqual(home_team.points, 0) 
        self.assertEqual(away_team.points, 3)  

    def test_calculate_draw(self):
        """Test that calculate assigns points correctly for a draw."""
        match = Match("Spider", 2, "Lions", 2)
        self.calculator.calculate(match)

        home_team = self.calculator.get_team("Spider")
        away_team = self.calculator.get_team("Lions")
        
        self.assertEqual(home_team.points, 1) 
        self.assertEqual(away_team.points, 1)

if __name__ == '__main__':
    unittest.main()
