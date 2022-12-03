from helper.utils import *


DAY = 3


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    sacks = []
    for sack in raw_data:
        middle = int(len(sack)/2)
        compartment_a = sack[:middle]
        compartment_b = sack[middle:]
        sacks.append((compartment_a, compartment_b))
    return sacks


@time_function
def part_a(data):
    duplicates = _find_duplicate_items(data)
    return _score_items(duplicates)


@time_function
def part_b(data):
    badges = _find_badges([c1 + c2 for c1, c2 in data])
    return _score_items(badges)


def _find_duplicate_items(sacks):
    duplicates = []
    for a, b in sacks:
        duplicates += set(a).intersection(b)
    return duplicates


def _find_badges(sacks):
    badges = []
    for i in range(2, len(sacks), 3):
        elf1 = sacks[i - 2]
        elf2 = sacks[i - 1]
        elf3 = sacks[i]
        badges += set(elf1).intersection(elf2).intersection(elf3)
    return badges


def _score_items(items):
    score = 0
    for item in items:
        offset = 38 if item.isupper() else 96
        score += ord(item) - offset
    return score


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

