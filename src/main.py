from input_parser import Parser
from score_calculator import ScoreCalculator
from team_rankings import TeamRankings

import sys

def main():
    import sys
    input_lines = sys.stdin.read().strip().split("\n")

    matches =Parser.parse_input(input_lines)

    # Calculate scores
    calculator = ScoreCalculator()
    for match in matches:
        calculator.calculate(match)

    # Get rankings and print
    rankings = TeamRankings(calculator.teams)
    print(rankings)

if __name__ == "__main__":
    main()
