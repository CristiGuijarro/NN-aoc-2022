#!/usr/bin/env python3
"""
Advent of Code 2022 - Elf Crane Stack Rearrangement

Determine which crates in each of the stacks will be unpacked first
"""
import argparse
import re
from typing import List
import pandas as pd


def cleanup_stacks(stack_list: list) -> tuple:
    """Standardise the input data to single digit assignment ids as List[list]

    Args:
        stack_list: list of stacks as raw input split into a list in
            intial configuration:
                        [J]             [B] [W]
                        [T]     [W] [F] [R] [Z]
                    [Q] [M]     [J] [R] [W] [H]
                [F] [L] [P]     [R] [N] [Z] [G]
            [F] [M] [S] [Q]     [M] [P] [S] [C]
            [L] [V] [R] [V] [W] [P] [C] [P] [J]
            [M] [Z] [V] [S] [S] [V] [Q] [H] [M]
            [W] [B] [H] [F] [L] [F] [J] [V] [B]
             1   2   3   4   5   6   7   8   9

    Returns: table of transposed stacks
    """
    regex = re.compile(r"    ")
    full_stacks = [(re.sub(regex, " [] ", x)) for x in stack_list]
    index = full_stacks.pop().split()
    index_int = [str(x) for x in index]
    full_stacks.reverse()
    df_of_stacks = [x.split() for x in full_stacks]
    pd_df = pd.DataFrame(df_of_stacks)
    pd_df.columns = index_int
    pd_df.transpose()
    list_of_stacks = []

    for i in index_int:
        los = [re.sub(r"\W+", "", x) for x in pd_df[i] if re.search("[a-zA-Z]", x)]
        list_of_stacks.append(los)
    return list_of_stacks


def follow_instructions_9000(stacks: List[list], instructions: list) -> List[list]:
    """Take in instructions to follow for 9000 crane model

    Args:
        stacks: list of each stack as an ordered list
        instructions: list of [ "move x from y to z" ] instructions

    Returns: rearranged stacks list
    """
    for i in instructions:
        ins = i.split()
        crate_num = ins[1]
        stack_from = ins[3]
        stack_to = ins[5]
        for _ in range(int(crate_num)):
            moved_crate = stacks[int(stack_from) - 1].pop()
            stacks[int(stack_to) - 1].append(moved_crate)
    return stacks


def follow_instructions_9001(stacks: List[list], instructions: list) -> List[list]:
    """Take in instructions to follow for 9001 crane model

    Args:
        stacks: list of each stack as an ordered list
        instructions: list of [ "move x from y to z" ] instructions

    Returns: rearranged stacks list
    """
    for i in instructions:
        ins = i.split()
        crate_num = ins[1]
        stack_from = ins[3]
        stack_to = ins[5]
        moved_crates = []
        for _ in range(int(crate_num)):
            moved_crate = stacks[int(stack_from) - 1].pop()
            moved_crates.append(moved_crate)
        moved_crates.reverse()
        stacks[int(stack_to) - 1].extend(moved_crates)
    return stacks


# pylint: disable=R0914
def main() -> None:
    """Main function to ..."""
    parser = argparse.ArgumentParser("")
    parser.add_argument("--input_list", help="", type=str)
    parser.add_argument("--crane_model", help="9000|9001", type=str, default="9000")
    parser.parse_args()
    args = parser.parse_args()

    stacks = ""
    instructions = ""
    input_file = args.input_list
    with open(input_file, encoding="utf-8") as file:
        stacks_in = file.read()
        stacks, instructions = stacks_in.split("\n\n")

    instruction_list = instructions.splitlines()
    list_stacks = stacks.splitlines()
    stack_list = cleanup_stacks(list_stacks)
    sorted_list = (
        follow_instructions_9000(stack_list, instruction_list)
        if (args.crane_model == "9000")
        else follow_instructions_9001(stack_list, instruction_list)
    )
    final_list = []
    for crates in sorted_list:
        final_list.append(crates.pop())
    final_string = "".join(final_list)
    print(f"My final string is: {final_string}")


if __name__ == main():
    main()
