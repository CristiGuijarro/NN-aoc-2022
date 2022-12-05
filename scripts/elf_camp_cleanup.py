#!/usr/bin/env python3
"""
Advent of Code 2022 - Elf Camp Cleanup

Highlight the number of encapsulated chore pairs
"""
import argparse
import pandas as pd

def standardise_data(duties_str: str) -> list:
    """Standardise the input data to range list

    Args:
        duties_str: the range of duties given to an elf

    Returns: Standardised duties listed in order min-max
    """
    dmin, dmax = duties_str.split("-")
    elf_list = []
    if dmin == dmax:
        elf_list = [ int(dmin), int(dmax) ]
    if not elf_list:
        elf_list = list(range(int(dmin), int(dmax) + 1))
    return elf_list

def data_encapsulation(duty_combo: tuple[int, int]) -> int:
    """Return True if one data encapsulates the other

    Args:
        duty_combo: a dataframe containing the standardised
            duties of both elves

    Returns: 1 if the the duties of one elf encapsulate the other
             0 if the duties are not totally redundant
    """
    elf1_max = int(max(duty_combo[0]))
    elf1_min = int(min(duty_combo[0]))
    elf2_max = int(max(duty_combo[1]))
    elf2_min = int(min(duty_combo[1]))
    if (elf1_max >= elf2_max and elf1_min <= elf2_min):
        return 1
    if (elf2_max >= elf1_max and elf2_min <= elf1_min):
        return 1
    return 0

def data_intersection(duty_combo: tuple[int, int]) -> int:
    """Return 1 if one data overlaps the other

    Args:
        duty_combo: a dataframe containing the standardised
        duties of both elves

    Returns: 1 if the the duties of one elf overlaps the other
             0 if there is no duty redundancy
    """
    matching = list(set(duty_combo[0]).intersection(duty_combo[1]))
    return 1 if (len(matching) >= 1) else 0

# pylint: disable=R0914
def main() -> None:
    """Main function to collect the assigned camp cleanup data redundancy
    """
    parser = argparse.ArgumentParser("Input csv list to work out the elf game outcomes")
    parser.add_argument("--input_list", help="Input chores list as csv file", type=str)
    parser.parse_args()
    args = parser.parse_args()

    input_file = args.input_list

    dframe = pd.read_csv(input_file, header=None)
    dframe.rename(columns={dframe.columns[0]:'elf1', dframe.columns[1]:'elf2'}, inplace=True)
    elf1_list = [ standardise_data(x) for x in list(dframe["elf1"]) ]
    elf2_list = [ standardise_data(x) for x in list(dframe["elf2"]) ]
    duties_std = list(zip(elf1_list,elf2_list))
    bool_list = [ data_encapsulation(x) for x in duties_std ]
    redundancy_num = sum(bool_list)
    print(f"Wrong number of redundant duties: {redundancy_num}\n")
    overlap_list = [ data_intersection(x) for x in duties_std ]
    overlap_num = sum(overlap_list)
    print(f"Number of overlapped duties: {overlap_num}\n")

if __name__ == main():
    main()
