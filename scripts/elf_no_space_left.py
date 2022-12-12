#!/usr/bin/env python3
"""
Advent of Code 2022 - Elf Out Of Space Issue

Calculate the total sum of all files in all directories with size =< 10000
The total disk space available to the filesystem is 70000000
The update needs unused space of at least 30000000
"""
import argparse


def add_path_to_directories(path: str, directories: dict) -> dict:
    """Function to add a directory if not an existing directory path

    Args:
        path: current path of directory/subdirectory
        directories: directory/subdirectory path as keys

    Returns: Updated directory structure/path
    """
    if path not in directories.keys():
        directories[path] = 0
    return directories


# pylint: disable=R0914,R0915
def main() -> None:
    """Main function to calculate and return the total sum of all files"""
    parser = argparse.ArgumentParser("")
    parser.add_argument("--input_list", help="", type=str)
    parser.parse_args()
    args = parser.parse_args()

    objects_oi = []
    input_file = args.input_list
    with open(input_file, encoding="utf-8") as file:
        objects_in = file.read()
        objects_oi = objects_in.splitlines()

    directories_size = {}
    curr_struct = []
    curr_path = ""
    all_file_sizes = 0
    for cmd in objects_oi:
        if cmd.startswith("$ cd"):
            if not cmd.startswith("$ cd ..") and not cmd.startswith("$ cd /"):
                curr_path += (
                    f"/{cmd.split()[-1]}" if curr_path != "/" else cmd.split()[-1]
                )
                curr_struct.append(curr_path)
                directories_size = add_path_to_directories(curr_path, directories_size)

            elif cmd.strip() == "$ cd /":
                curr_path = "/"
                curr_struct = ["/"]
                directories_size = add_path_to_directories(curr_path, directories_size)

            elif cmd.strip() == "$ cd ..":
                curr_path = "/".join(curr_path.split("/")[:-1])
                curr_struct.pop()

        if cmd[0].isdigit():
            file_size = int(cmd.split()[0])
            all_file_sizes += file_size
            for directory in curr_struct:
                directories_size[directory] += file_size

    total_size = [x for x in directories_size.values() if x <= 100000]
    print(f"Total size of dirs < 100,000: {sum(total_size)}")

    total_system_size = list(directories_size.values())
    sort_total_size = sorted(total_system_size)
    target_size = all_file_sizes - 40000000
    size_to_remove = int()
    for bites in sort_total_size:
        if bites >= target_size:
            size_to_remove = bites
            break

    print(f"Size of directory to remove ~ {target_size}: {size_to_remove}")


if __name__ == main():
    main()
