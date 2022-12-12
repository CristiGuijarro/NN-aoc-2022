#!/usr/bin/env python3
"""
Advent of Code 2022 - Cathode Ray Tube
"""
import argparse

# pylint: disable=R0914
def main() -> None:
    """Main function to register the signals
    """
    parser = argparse.ArgumentParser("")
    parser.add_argument("--input_list", help="", type=str)
    parser.parse_args()
    args = parser.parse_args()

    sig_x = 1
    signal_x_strengths = [1]
    input_file = args.input_list
    with open (input_file, encoding="utf-8") as file:
        read_in = file.read()
        instructions = read_in.splitlines()

        for ins in instructions:
            if ins.startswith("noop"):
                signal_x_strengths.append(sig_x)
            if ins.startswith("addx"):
                signal_x_strengths.append(sig_x)
                sig_x += int(ins.split()[1])
                signal_x_strengths.append(sig_x)

    signal_strengths = [ (y + 1) * x for (y, x) in enumerate(signal_x_strengths) ]
    index_list = [ 20, 60, 100, 140, 180, 220 ] #20th, 60th, 100th, 140th, 180th, and 220 cycle
    chosen_cycles = [signal_strengths[i-1] for i in index_list]
    print(f"The chosen cycles: {sum(chosen_cycles)}")

    ray_pixeliser = [
    "###" if i%40 in list(range(_-1, _+2)) else "   "
    for i, _ in enumerate(signal_x_strengths)
    ]
    ray_pixeliser = [ ray_pixeliser[ i:i + 40 ] for i in range(0, len(ray_pixeliser), 40) ]
    ray_pixeliser_str = "\n".join(["".join(_) for _ in ray_pixeliser])
    print(ray_pixeliser_str)

if __name__ == main():
    main()
