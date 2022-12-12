#!/usr/bin/env python3
"""
Advent of Code 2022 - Elf Tree Viewage

"""
import argparse
from typing import List
from itertools import takewhile


def tree_visibility(matrix: List[list], xrow: int, xcol: int) -> int:
    """Function to return whether a tree is visible

    Args:
        matrix: matrix of all the trees in forest
        xrow: row of tree position in matrix
        xcol: col of tree position in matrix

    Returns: visibility of tree
    """
    if xrow in (0, len(matrix) - 1):
        return True
    if xcol in (0, len(matrix[xrow]) - 1):
        return True

    height = matrix[xrow][xcol]
    row = matrix[xrow]
    col = [matrix[xrow][xcol] for xrow in range(len(matrix))]

    left = all(x < height for x in row[:xcol])
    right = all(x < height for x in row[xcol + 1 :])
    top = all(x < height for x in col[:xrow])
    bottom = all(x < height for x in col[xrow + 1 :])

    return top * left * bottom * right

def sum_up_until(depth_list: list) -> int:
    """Function to return the length of tree visibility

    Args:
        depth_list: list of true and false for a tree

    Returns:
        Total number of visible trees from tree view
    """
    if depth_list:
        tree_stop = list(takewhile(lambda x: x != 0, depth_list))
        return sum(tree_stop) if sum(tree_stop) != 0 else 1
    return 1

def tree_scenic_score(matrix: List[list], xrow: int, xcol: int) -> int:
    """Function to return whether a tree is visible

    Args:
        matrix: matrix of all the trees in forest
        xrow: row of tree position in matrix
        xcol: col of tree position in matrix

    Returns: visibility of tree
    """
    height = matrix[xrow][xcol]
    row = matrix[xrow]
    col = [matrix[xrow][xcol] for xrow in range(len(matrix))]

    left = [ 1 if x < height else 0 for x in row[:xcol - 1] ]
    right = [ 1 if x < height else 0 for x in row[xcol :] ]
    top = [ 1 if x < height else 0 for x in col[:xrow - 1] ]
    bottom = [ 1 if x < height else 0 for x in col[xrow :] ]

    # left.reverse()
    # top.reverse()

    left_sum = sum_up_until(left) if left else 1
    right_sum = sum_up_until(right) if right else 1
    top_sum = sum_up_until(top) if top else 1
    bottom_sum = sum_up_until(bottom) if bottom else 1

    if xrow in (0, len(matrix) - 1):
        return 0
    if xcol in (0, len(matrix[xrow]) - 1):
        return 0

    # print(f"height: {height} row:{xrow} col:{xcol}")
    # print(f"left:{left_sum} * right:{right_sum} * top:{top_sum} * bottom:{bottom_sum}")
    # print(left_sum * right_sum * top_sum * bottom_sum)
    # print("\n")
    return left_sum * right_sum * top_sum * bottom_sum

def main() -> None:
    """Main function to determine number of visible trees"""
    parser = argparse.ArgumentParser("")
    parser.add_argument("--input_matrix", help="", type=str)
    parser.parse_args()
    args = parser.parse_args()

    matrix_file = args.input_matrix
    with open(matrix_file, encoding="utf-8") as file:
        forest = [ line.strip() for line in file.readlines() ]
        matrix = [ [int(x) for x in list(line)] for line in forest ]

        visibility = [
            tree_visibility(matrix, xrow, xcol)
            for xrow in range(len(matrix))
            for xcol in range(len(matrix[xrow]))
        ]
        print(f"Number of visible trees: {sum(visibility)}")

        scenic_score = [
            tree_scenic_score(matrix, xrow, xcol)
            for xrow in range(len(matrix))
            for xcol in range(len(matrix[xrow]))
        ]
        print(f"Top scenic view: {max(scenic_score)}")


if __name__ == main():
    main()
