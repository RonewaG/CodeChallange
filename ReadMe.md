# Project: CodeChallenge

## Description
This project is a Python-based solution for managing and ranking teams based on match results. The application uses an object-oriented design with clear separation of responsibilities for parsing, score calculation, and ranking.

## Features
- Parse input match data in a human-readable format (e.g., "Lions 3, Spider 3").
- Calculate scores based on match outcomes:
  - Win: 3 points
  - Draw: 1 point for each team
  - Loss: 0 points
- Rank teams based on points, with tie-breaking based on alphabetical order.
- Display team rankings with sequential numbering.

---

## Project Structure
```plaintext
CodeChallenge/src/
* main.py              
* input_parser.py       
* score_calculator.py   
* team_rankings.py     
* team.py               

CodeChallenge/test/
* test_main.py          
* test_input_parser.py  
* test_score_calculator.py  
* test_team_rankings.py     
* test_team.py          
README.md 
```

## How to run


```
python3 main.py < input.txt
```

input file example
```
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
```