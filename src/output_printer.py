class OutputPrinter:
    @staticmethod
    def format(rankings):
        output = []
        last_rank = 0
        last_points = None
        for i, team in enumerate(rankings, start=1):
            if team.points != last_points:
                last_rank = i
            suffix = "pt" if team.points == 1 else "pts"
            output.append(f"{last_rank}. {team.name}, {team.points} {suffix}")
            last_points = team.points
        return "\n".join(output)
