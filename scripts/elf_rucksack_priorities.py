#!/usr/bin/env python3
"""
Advent of Code 2022 - Elf Rucksack Reorganization

A given rucksack always has the same number of items in each of its two compartments

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.

Find the item type that appears in both compartments of each rucksack.
What is the sum of the priorities of those item types?

"""
import argparse
from typing import List


def get_priority(letter: str) -> dict:
    """Assigns the priority to each item passed in

    Args:
        letter: single alphabetical letter in upper or lower case

    Returns: conversion of character to expected int
    """
    # ord "a" = 97
    # ord "A" = 65
    if letter.isupper() is False:
        return ord(letter) - 96
    return ord(letter) - 38

def compare_comparts(compartment1: str, compartment2: str) -> str:
    """Returns the priority of item in common between compartments

    Args:
        compartment1: string of letters representing items
        compartment2: string of letters representing items

    Returns: string of single letter shared between compartment[1|2]
    """
    item_in_common = list(set(compartment1).intersection(compartment2))
    return get_priority(item_in_common[0])

def elf_grouping(rucksacks: list, group_size: int) -> list:
    """Returns list of elf groups of specified size

    Args:
        rucksacks: list of all the rucksacks in camp
        group_size: number of elves in a rucksack priority group

    Returns: list of organised elf groups by group_size
    """
    return [rucksacks[x:x+group_size] for x in range(0, len(rucksacks), group_size)]

def fetch_badge(group_of_bags: List[list]) -> int:
    """Returns the priority of item in common for an elf grouping

    Args:
        group_of_bags: A list containing the list of elf rucksacks in a group

    Returns: the shared badge priority for the group of elves
    """
    badge = list(set.intersection(*map(set, group_of_bags)))
    return get_priority(badge[0])

# pylint: disable=R0914
def main() -> None:
    """Main function to generate total score of elven rock, paper, scissors
    """
    parser = argparse.ArgumentParser("Input list to work out the elf game outcomes")
    parser.add_argument("--input_list", help="Input rucksack list as txt file", type=str)
    parser.parse_args()
    args = parser.parse_args()

    rucksacks = []
    input_file = args.input_list
    with open (input_file, encoding="utf-8") as file:
        rucksack_in = file.read()
        rucksacks = rucksack_in.splitlines()

    item_dups = []
    for rucksack in rucksacks:
        rucksack_objs = list(rucksack)
        rucksack_size = len(rucksack_objs)
        compartment_size = int(rucksack_size / 2)
        comp1 = slice(0, compartment_size)
        comp2 = slice(compartment_size, int(len(rucksack_objs)))
        item_dups.append(compare_comparts(rucksack_objs[comp1], rucksack_objs[comp2]))
    sum_of_priorities = sum(item_dups)
    print(f"Sum of priorities in duplicates: {sum_of_priorities}\n")
    rucksack_list = [ list(x) for x in rucksacks ]
    rucksack_groups = elf_grouping(rucksack_list, 3)
    badge_priorities = [ fetch_badge(x) for x in rucksack_groups ]
    sum_badge_priors = sum(badge_priorities)
    print(f"Sum of badge priorities: {sum_badge_priors}\n")


if __name__ == main():
    main()
