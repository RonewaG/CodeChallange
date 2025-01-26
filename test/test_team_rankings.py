from test_utils import add_src_to_path
add_src_to_path()

import unittest
from team_rankings import TeamRankings
from team import Team

class TestTeamRankings(unittest.TestCase):

    def setUp(self):
        self.spider = Team("Spider")
        self.lions = Team("Lions")
        self.leopard = Team("Leopard")
        
        self.spider.add_points(10)
        self.lions.add_points(10)
        self.leopard.add_points(8)

        self.rankings = TeamRankings({
            "Spider": self.spider,
            "Lions": self.lions,
            "Leopard": self.leopard
        })

    def test_rank_teams(self):
        ranked_teams = self.rankings.rank_teams()
        
        self.assertEqual(ranked_teams[0].name, "Lions")
        self.assertEqual(ranked_teams[1].name, "Spider")
        self.assertEqual(ranked_teams[2].name, "Leopard")

if __name__ == '__main__':
    unittest.main()
