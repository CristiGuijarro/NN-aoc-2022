#!/usr/bin/env python3
"""
Advent of Code 2022 - Elf Calories
"""


import argparse

def group_elf_calories(input_file: str) -> list:
    """Function to return the elf calorie groups as list of totals

    Args:
        input_file: file containing newline seperated integers
            with double newline between elves

    Returns:
        list of integers (elf_totals)
    """
    with open (input_file, encoding="utf-8") as file:
        calorie_str = file.read()
        elves = calorie_str.split('\n\n')
        elf_counts = [ list(x.splitlines()) for x in elves ]
        elf_totals = []
        for mini_list in elf_counts:
            elf_total = [ int(x) for x in mini_list ]
            elf_totals.append(sum(elf_total))
        return elf_totals

def top_elves(elf_cals: list, top_n: int) -> int:
    """Function to return the `top_n` maximum calories of elves in list

    Args:
        elf_cals: list of summed elf calories (as integers)
        top_n: number of top elves to total

    Returns:
        sum of top_n elf calories
    """
    sorted_elves = sorted(elf_cals, reverse=True)
    sum_top_n = sum(sorted_elves[0:top_n])
    return sum_top_n

def main() -> None:
    """Main function to run the elf calories counting script
    """
    parser = argparse.ArgumentParser("Input list to work out the elf with the most calories")
    parser.add_argument("--input_list", help="Input calorie list with spaces", type=str)
    parser.parse_args()
    args = parser.parse_args()

    calories_input = args.input_list

    summed_elf_cals = group_elf_calories(calories_input)

    maxcalories = max(summed_elf_cals)
    print(f"Largest elf load: {maxcalories}\n")
    top_three = top_elves(summed_elf_cals, 3)
    print(f"Top three elf load: {top_three}")


if __name__ == '__main__':
    main()
