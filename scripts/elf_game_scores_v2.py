#!/usr/bin/env python3
"""
Advent of Code 2022 - Elf Game Strategy

#A for Rock, B for Paper, and C for Scissors
#X for Lose, Y for Draw, and Z for win

# Your total score is the sum of your scores for each round. The score for a single round is
# the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the
# score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you
# won)
"""
import argparse
import pandas as pd

def count_outcomes(games: list) -> int:
    """Function to count number of wins
    """
    #X for Lose, Y for Draw, and Z for win
    outcome_dict = {"X": 0, "Y": 3, "Z": 6 }
    count_occ = [ outcome_dict[x] for x in games ]
    return sum(count_occ)

def sum_shapes_scores(games: list) -> int:
    """Function to return list of played shapes
    """
    rock_list = [ "A Y", "B X", "C Z" ]
    paper_list = [ "A Z", "B Y", "C X" ]
    sciss_list = [ "A X", "B Z", "C Y" ]
    num_rock = [ games.count(x) for x in rock_list ]
    num_paper = [ games.count(x) for x in paper_list ]
    num_sciss = [ games.count(x) for x in sciss_list ]
    return ((sum(num_rock) * 1) + (sum(num_paper) * 2) + (sum(num_sciss) * 3))


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
    with open (input_file, encoding="utf-8") as file:
        infile = file.read()
        games = infile.splitlines()
    # pylint: disable=W1401
    dframe = pd.read_csv(input_file, sep="\s+", header=None)
    dframe.rename(columns={dframe.columns[1]:'me'}, inplace=True)
    me = list(dframe["me"])

    outcomes_score = count_outcomes(me)
    sum_shapes = sum_shapes_scores(games)

    my_score = outcomes_score + sum_shapes

    print(f"My score: {my_score}\n")

if __name__ == main():
    main()
