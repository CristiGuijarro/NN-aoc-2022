#!/usr/bin/env python3
"""
Advent of Code 2022 - Move the rope
"""
import argparse


def reposition_head(pos: tuple, direction: str) -> None:
    """Return new position of Head

    Arg:
        pos: current position of Head
    """
    if direction == "R":
        pos[0] += 1
    if direction == "L":
        pos[0] -= 1
    if direction == "D":
        pos[1] += 1
    if direction == "U":
        pos[1] -= 1


def follow_tail(hpos: tuple, tpos: tuple) -> None:
    """Check closeness of Head and Tail and return new Tail position

    Args:
        hpos: position of Head
        tpos: position of Tail
    """
    xdiff = hpos[0] - tpos[0]
    ydiff = hpos[1] - tpos[1]
    if abs(xdiff) > 1 or abs(ydiff) > 1:
        tpos[0] += (xdiff > 0) - (xdiff < 0)
        tpos[1] += (ydiff > 0) - (ydiff < 0)


def move_rope_on_bridge(rope_pos: tuple, direction: str) -> tuple:
    """Function to move the rope along the bridge

    Args:
        rope_pos: current rope position
        direction: direction to move in
    """
    reposition_head(rope_pos[0], direction)

    for i in range(1, len(rope_pos)):
        follow_tail(rope_pos[i - 1], rope_pos[i])

    return tuple(rope_pos[-1])


# pylint: disable=R0914
def main() -> None:
    """Main function to follow the rope from Head to Tail"""
    parser = argparse.ArgumentParser("")
    parser.add_argument("--input_list", help="", type=str)
    parser.parse_args()
    args = parser.parse_args()

    input_file = args.input_list
    with open(input_file, encoding="utf-8") as file:
        dir_in = file.read()
        moves = dir_in.splitlines()

    rope_position = [[0, 0] for n in range(2)]

    all_pos = []
    for move in moves:
        direction, distance = move.split()
        for _ in range(int(distance)):
            move_rope_on_bridge(rope_position, direction)
            all_pos.append(f"{rope_position[1]}")

    print(f"Number of distinct Tail positions with whole rope: {len(list(set(all_pos)))}")

    broken_rope = [[0, 0] for n in range(10)]
    for i in range(10):
        all_knot_pos = []
        for move in moves:
            direction, distance = move.split()
            for _ in range(int(distance)):
                move_rope_on_bridge(broken_rope, direction)
                all_knot_pos.append(f"{broken_rope[i]}")
    # pylint: disable=C0301
    print(f"Number of distinct Tail positions for last knot of broken rope: {len(list(set(all_knot_pos)))}")


if __name__ == main():
    main()
