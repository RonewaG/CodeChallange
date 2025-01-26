class TeamRankings:
    def __init__(self, teams):
        self.teams = teams

    def rank_teams(self):
        return sorted(self.teams.values(), key=lambda t: (-t.points, t.name))

    def __str__(self):
        output = []
        ranked_teams = self.rank_teams()
        rank = 1

        for i, team in enumerate(ranked_teams):
            suffix = "pt" if team.points == 1 else "pts"
            output.append(f"{rank}. {team.name}, {team.points} {suffix}")
            rank += 1

        return "\n".join(output)

