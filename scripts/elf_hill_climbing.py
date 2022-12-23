#!/usr/bin/env python3
"""
Advent of Code 2022 - Find the shortest route
"""
import argparse

# pylint: disable=R0914, C0200
def get_height(letter: str) -> int:
    """Assigns the priority to each item passed in

    Args:
        letter: single alphabetical letter in upper or lower case

    Returns: conversion of character to expected int
    """
    # ord "a" = 97
    if isinstance(letter, list):
        letter = str(letter[0])
    if letter == "E":
        return ord("z")
    if letter == "S":
        return ord("a") - 96
    return ord(letter) - 96


def find_start(contours: list) -> set:
    """Function to return the coordinate in which is Start point"""
    for xrow in range(len(contours)):
        for ycol in range(len(contours[xrow])):
            if contours[xrow][ycol] == "S":
                return (ycol, xrow)
    return None


def find_end(contours: list) -> set:
    """Function to return the coordinate in which is End point"""
    for xrow in range(len(contours)):
        for ycol in range(len(contours[xrow])):
            if contours[xrow][ycol] == "E":
                return (ycol, xrow)
    return None


def bfs_v1(start_point: set, end_point: set, grid: list) -> list:
    """Function to breadth first search the hill"""
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    row = len(grid)
    col = len(grid[0])
    seen = set()
    queue = set()
    queue.add(start_point)
    attempts = [[0 for i in range(col)] for _ in range(row)]

    while queue:
        path = queue.pop()
        if path == end_point:
            return attempts[end_point[0]][end_point[1]]

        for i in range(4):
            edge_a = path[0] + directions[i][0]
            edge_b = path[1] + directions[i][1]
            if ( row > edge_a >= 0 and col > edge_b >= 0 and (
                    grid[edge_a][edge_b] >= grid[path[0]][path[1]]
                    or grid[edge_a][edge_b] + 1 == grid[path[0]][path[1]]
                    ) and (edge_a, edge_b) not in seen ):
                queue.add((edge_a, edge_b))
                seen.add((edge_a, edge_b))
                attempts[edge_a][edge_b] = attempts[path[0]][path[1]] + 1

    return None

def bfs_v2(start_point: set, grid: list) -> list:
    """Function to breadth first search the hill"""
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    row = len(grid)
    col = len(grid[0])
    seen = set()
    queue = set()
    queue.add(start_point)
    attempts = [[0 for i in range(col)] for _ in range(row)]

    while queue:
        path = queue.pop()
        if grid[path[0]][path[1]] == 1:
            return attempts[path[0]][path[1]]
        for i in range(4):
            edge_a = path[0] + directions[i][0]
            edge_b = path[1] + directions[i][1]
            if ( row > edge_a >= 0 and col > edge_b >= 0 and (
                    grid[edge_a][edge_b] >= grid[path[0]][path[1]]
                    or grid[edge_a][edge_b] + 1 == grid[path[0]][path[1]]
                    ) and (edge_a, edge_b) not in seen ):
                queue.add((edge_a, edge_b))
                seen.add((edge_a, edge_b))
                attempts[edge_a][edge_b] = attempts[path[0]][path[1]] + 1

    return None

def main() -> None:
    """Main function to ..."""
    parser = argparse.ArgumentParser("")
    parser.add_argument("--input_matrix", help="", type=str)
    parser.parse_args()
    args = parser.parse_args()

    matrix_file = args.input_matrix
    with open(matrix_file, encoding="utf-8") as file:
        forest = [ line.strip() for line in file.readlines() ]
        matrix = [ list(list(line)) for line in forest ]

        start_coord = find_start(matrix)
        end_coord = find_end(matrix)
        print(f"Start point: {start_coord}")
        print(f"End point:   {end_coord}")

        for xrow in range(len(matrix)):
            for xcol in range(len(matrix[xrow])):
                matrix[xrow][xcol] = get_height(matrix[xrow][xcol])

        shortest_path = bfs_v1(start_coord, end_coord, matrix)
        print(f"Shortest and safest path {shortest_path}")
        shortest_route = bfs_v2(start_coord, matrix)
        print(f"Other route {shortest_route}")


if __name__ == main():
    main()
