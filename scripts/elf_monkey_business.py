#!/usr/bin/env python3
"""
Advent of Code 2022 - Monkey monkey business
"""
import argparse
import re
from math import lcm

# pylint: disable=R0903,C0301,R0913,W0123,R0914
class Monkey:
    """The actual monkey business in class form"""
    def __init__(self, stolen_items: list, operation: str, worry_num: int, divisible_num: int, next_monkeys: tuple):
        self.stolen_items = stolen_items
        self.operation = operation
        self.divisible_num = divisible_num
        self.next_monkeys = next_monkeys
        self.worry_num = worry_num
        self.item_count = 0

    def test_worry(self):
        """Check worry level with `self.divisible_num`
        """
        for i in self.stolen_items:
            morph_item = eval(f"{i} {self.operation.replace('old', str(i))}")
            morph_item = morph_item % self.worry_num
            if morph_item % self.divisible_num == 0:
                self.next_monkeys[0].stolen_items.append(morph_item)
            else:
                self.next_monkeys[1].stolen_items.append(morph_item)
            self.item_count += 1
        self.stolen_items.clear()


def make_the_monkeys(monkey_in: list, worry_num: int) -> Monkey:
    """Function to parse the raw monkey input and generate initial monkey object.
    Monkey 0:
      Starting items: 89, 74
      Operation: new = old * 5
      Test: divisible by 17
        If true: throw to monkey 4
        If false: throw to monkey 7
    """
    monkey_list = []
    for monk in monkey_in:
        monkey_data = monk.splitlines()
        start_items = re.findall(r'\d+', monkey_data[1])
        operation = ' '.join(monkey_data[2].split()[-2:])
        divisible_num = re.findall(r'\d+', monkey_data[3])[0]
        next_monkeys = [
            re.findall(r'\d+', monkey_data[4])[0], re.findall(r'\d+', monkey_data[5])[0]
        ]
        monkey_list.append(Monkey(start_items, operation, worry_num, int(divisible_num), next_monkeys))
    return monkey_list

def main() -> None:
    """Main function to generate the big worrying numbers
    """
    parser = argparse.ArgumentParser("")
    parser.add_argument("--input_list", help="Input the monkey list", type=str)
    parser.add_argument("--worry_num", help="Input the number required to worry", nargs='?', const=3, type=int)
    parser.add_argument("--reduce_worry", help="Input the number required to reduce worry", type=bool)
    parser.add_argument("--rounds", help="Number of rounds of monkey throws", nargs='?', const=20, type=int)
    parser.parse_args()
    args = parser.parse_args()

    monkey_input = []
    input_file = args.input_list
    with open (input_file, encoding="utf-8") as file:
        objects_in = file.read()
        monkey_input = objects_in.split("\n\n")
    init_monkeys = (make_the_monkeys(monkey_input, args.worry_num))

    worrying_num = int()
    if args.reduce_worry:
        lcmlistinit = [ x.divisible_num for x in init_monkeys ]
        worrying_num = lcm(*lcmlistinit)

    for ace in init_monkeys:
        true_monkey = int(ace.next_monkeys[0])
        false_monkey = int(ace.next_monkeys[1])
        true_monkey = init_monkeys[true_monkey]
        false_monkey = init_monkeys[false_monkey]
        ace.next_monkeys = [true_monkey, false_monkey]
        if args.reduce_worry:
            ace.worry_num = worrying_num

    for _ in range(args.rounds):
        for primate in init_monkeys:
            primate.test_worry()

    monkey_theft_counts = [ x.item_count for x in init_monkeys ]
    sorted_monkeys = sorted(monkey_theft_counts, reverse=True)
    total = sorted_monkeys[0] * sorted_monkeys[1]
    print(
    f"Product of inspected items with {args.rounds} rounds worry_num:{args.worry_num}: {total}"
    )

if __name__ == main():
    main()
