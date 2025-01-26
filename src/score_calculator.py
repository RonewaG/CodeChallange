from team import Team

class ScoreCalculator:
    def __init__(self):
        self.teams = {}

    def get_team(self, team_name):
        if team_name not in self.teams:
            self.teams[team_name] = Team(team_name)
        return self.teams[team_name]

    def calculate(self, match):
        home_team = self.get_team(match.home_name)
        away_team = self.get_team(match.away_name)

        if match.home_score > match.away_score:
            home_team.add_points(3)
        elif match.home_score < match.away_score:
            away_team.add_points(3)
        else:
            home_team.add_points(1)
            away_team.add_points(1)
