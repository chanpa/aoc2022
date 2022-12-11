from helper.utils import *
from collections import defaultdict
import re
import operator


DAY = 11
num_pattern = re.compile("\d+")
op_pattern = re.compile("old|[*+]|\d+")
operators = {"+": operator.add, "*": operator.mul}


class Monkey:
    def __init__(self):
        self.items = None
        self.operation = None
        self.test = None
        self.inspects = 0

    def __repr__(self):
        return f"\nMonkey(\n\t{self.items=}\n\t{self.operation=}\n\t{self.test=}\n)"

    def throw(self, extra_worried=False):
        self.inspects += 1
        item = self.items.pop(0)
        values = []
        for val in self.operation["vals"]:
            if val == "old":
                values.append(item)
            else:
                values.append(int(val))
        item = self.operation["op"](*values)
        if not extra_worried:
            item //= 3
        new_monkey = self.test["if_true"] if item % self.test["divisor"] == 0 else self.test["if_false"]
        return new_monkey, item


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    monkeys = defaultdict(Monkey)
    monkey = 0
    for line in raw_data:
        match [p.strip() for p in line.split(":")]:
            case [""]:
                monkey += 1
            case [attribute, vals] if attribute == "Starting items":
                worry_levels = [int(worry_level) for worry_level in num_pattern.findall(vals)]
                monkeys[monkey].items = worry_levels
            case [attribute, vals] if attribute == "Operation":
                val1, op, val2 = op_pattern.findall(vals)
                monkeys[monkey].operation = {"op": operators[op], "vals": [val1, val2]}
            case [attribute, vals] if attribute == "Test":
                divisor = num_pattern.findall(vals)[0]
                monkeys[monkey].test = {"divisor": int(divisor)}
            case [attribute, vals] if attribute == "If true":
                new_monkey = num_pattern.findall(vals)[0]
                monkeys[monkey].test["if_true"] = int(new_monkey)
            case [attribute, vals] if attribute == "If false":
                new_monkey = num_pattern.findall(vals)[0]
                monkeys[monkey].test["if_false"] = int(new_monkey)

    return monkeys


@time_function
def part_a(monkeys):
    for _ in range(20):
        for _, monkey in monkeys.items():
            for _ in range(len(monkey.items)):
                new_monkey, item = monkey.throw()
                monkeys[new_monkey].items.append(item)
    inspects = [monkey.inspects for _, monkey in monkeys.items()]
    inspects.sort()
    return inspects[-1] * inspects[-2]


@time_function
def part_b(monkeys):
    factor = 1
    for _, monkey in monkeys.items():
        factor *= monkey.test["divisor"]

    for r in range(10_000):
        for _, monkey in monkeys.items():
            for _ in range(len(monkey.items)):
                new_monkey, item = monkey.throw(extra_worried=True)
                monkeys[new_monkey].items.append(item % factor)

    inspects = [monkey.inspects for _, monkey in monkeys.items()]
    inspects.sort()
    return inspects[-1] * inspects[-2]


def main():
    part_a(prepare_data())
    part_b(prepare_data())


if __name__ == '__main__':
    main()

