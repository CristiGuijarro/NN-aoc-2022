#!/usr/bin/env python3
"""
Advent of Code 2022 - Elf lava cubes
"""

import argparse
from collections import deque
# pylint: disable=R0914, C0103


def cube_nextto(cube: set) -> set:
    """Function to look next to cube in 3D
    """
    x, y, z = cube
    all_sets = []
    all_sets.append((x + 1, y, z))
    all_sets.append((x - 1, y, z))
    all_sets.append((x, y + 1, z))
    all_sets.append((x, y - 1, z))
    all_sets.append((x, y, z + 1))
    all_sets.append((x, y, z - 1))
    return all_sets

def get_surface_area(cube: set, all_cubes: list) -> int:
    """Function to determine surfae area of each cube
    """
    all_adj_cubes = cube_nextto(cube)
    area = len(list(set(all_adj_cubes).difference(all_cubes)))
    return area

def get_max_coords(all_cubes: list) -> set:
    """Function to return maximum and minimum coords
    """
    max_x = 0
    max_y = 0
    max_z = 0
    for x, y, z in all_cubes:
        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y
        max_z = z if z > max_z else max_z
    return (max_x, max_y, max_z)

def outer_space(x: int, y: int, z: int, maxxyz: set) -> bool:
    """Function to return whether inside or outside the droplet
    """
    max_x, max_y, max_z = maxxyz
    return x<0 or y<0 or z<0 or x>=max_x or y>=max_y or z>=max_z

def bfs(start_point: set, cubes: list) -> bool:
    """Function to breadth first search the fill space
    """
    max_xyz = get_max_coords(cubes)
    seen = {start_point}
    queue = deque([start_point])
    while queue:
        possible = queue.popleft()
        if possible == (0,0,0):
            return True
        for side in cube_nextto(possible):
            if side in seen:
                continue
            if outer_space(*side, max_xyz):
                return True
            if side not in cubes:
                seen.add(side)
                queue.append(side)
    return False

def main() -> None:
    """Main function to get the stats on those lava droplets
    """
    parser = argparse.ArgumentParser("")
    parser.add_argument("--input_list", help="", type=str)
    parser.parse_args()
    args = parser.parse_args()

    objects_oi = []
    input_file = args.input_list
    cubes = []
    with open (input_file, encoding="utf-8") as file:
        objects_in = file.read()
        objects_oi = objects_in.splitlines()
        for cube in objects_oi:
            x, y, z = map(int, cube.split(','))
            cubes.append((x, y, z))

    surface_area = [ get_surface_area(x, cubes) for x in cubes ]

    print(f"Total surface area: {sum(surface_area)}")

    total_sa = 0
    for cube in cubes:
        for side in cube_nextto(cube):
            if ( side not in cubes and bfs(side, cubes) ):
                total_sa += 1

    print(f"Total surface area with bubbles: {total_sa}")

if __name__ == main():
    main()
