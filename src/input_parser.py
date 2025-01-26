from match import Match

class Parser:
    @staticmethod
    def parse_input(input):
        matches = []
        for line in input:
            parts = line.split(",")
            home, home_score = Parser._parse_scores(parts[0])
            away, away_score = Parser._parse_scores(parts[1])
            matches.append(Match(home, home_score, away, away_score))
        return matches

    @staticmethod
    def _parse_scores(part):
        parts = part.strip().rsplit(" ", 1)
        team = parts[0]
        score = int(parts[1])
        return team, score
