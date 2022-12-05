#!/usr/bin/env python3
"""
Advent of Code 2022 - Elf Game Scores

#A for Rock, B for Paper, and C for Scissors
#X for Rock, Y for Paper, and Z for Scissors

# Your total score is the sum of your scores for each round. The score for a single round is
# the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the
# score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you
# won)
"""
import argparse
import pandas as pd

def sum_shape_scores(games: list) -> int:
    """Function to count shape specific scores

    Args:
        games: list of games outcomes

    Returns: count of game scores based on specific shape
    """
    shape_dict = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    shape_map = [ shape_dict[x] for x in games ]
    return sum(shape_map)

def count_wins(games: list) -> int:
    """Function to count number of wins

    Args:
        games: list of games outcomes

    Returns: count of winning occurrances
    """
    win_list = [ "A Y", "B Z", "C X" ]
    count_occ = [ games.count(x) for x in win_list ]
    return sum(count_occ)

def count_losses(games: list) -> int:
    """Function to count the number of losses

    Args:
        games: list of games outcomes

    Returns: count of losing occurrances
    """
    lose_list = [ "A Z", "B X", "C Y" ]
    count_occ = [ games.count(x) for x in lose_list ]
    return sum(count_occ)

def count_draws(games: list) -> int:
    """Function to count the number of draws

    Args:
        games: list of games outcomes

    Returns: count of drawing occurrances
    """
    draw_list = [ "A X", "B Y", "C Z" ]
    count_occ = [ games.count(x) for x in draw_list ]
    return sum(count_occ)

# pylint: disable=R0914
def main() -> None:
    """Main function to generate total score of elven rock, paper, scissors
    """
    parser = argparse.ArgumentParser("Input list to work out the elf game outcomes")
    parser.add_argument("--input_list", help="Input mini-game combo list as txt file", type=str)
    parser.parse_args()
    args = parser.parse_args()

    input_file = args.input_list
    games = []
    # pylint: disable=C0103
    me = []
    opponent = []
    with open (input_file, encoding="utf-8") as file:
        infile = file.read()
        games = infile.splitlines()
    # pylint: disable=W1401
    dframe = pd.read_csv(input_file, sep="\s+", header=None)
    dframe.rename(columns={dframe.columns[0]:'opponent'}, inplace=True)
    dframe.rename(columns={dframe.columns[1]:'me'}, inplace=True)
    opponent = list(dframe["opponent"])
    me = list(dframe["me"])

    my_shape_scores = sum_shape_scores(me)
    print(f"My shape score: {my_shape_scores}\n")
    op_shape_scores = sum_shape_scores(opponent)
    print(f"Op shape score: {op_shape_scores}\n")
    win_count = count_wins(games)
    print(f"My win count: {win_count}\n")
    draw_count = count_draws(games)
    print(f"My draw count: {draw_count}\n")
    lose_count = count_losses(games)
    print(f"My lose count : {lose_count}\n")

    my_score = my_shape_scores + (win_count * 6) + (draw_count * 3)
    op_score = op_shape_scores + (lose_count * 6) + (draw_count * 3)

    print(f"My score: {my_score}\n")
    print(f"Opponent score: {op_score}\n")

if __name__ == main():
    main()
