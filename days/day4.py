from helper.utils import *
import re


DAY = 4
pattern = re.compile("\d+")


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    pairs = []
    for pair in raw_data:
        matches = pattern.findall(pair)
        e1 = set(
            range(
                int(matches[0]), int(matches[1])+1, 1
            )
        )
        e2 = set(
            range(
                int(matches[2]), int(matches[3]) + 1, 1
            )
        )
        pairs.append((e1, e2))
    return pairs


@time_function
def prepare_data_new():
    raw_data = parse_file_rows_to_list(DAY)
    pairs = []
    for pair in raw_data:
        matches = pattern.findall(pair)
        e1 = int(matches[0]), int(matches[1])
        e2 = int(matches[2]), int(matches[3])
        pairs.append((e1, e2))
    return pairs


@time_function
def part_a(data):
    answer = 0
    for pair in data:
        if _is_contained_pair_new(pair):
            answer += 1
    return answer


@time_function
def part_b(data):
    answer = 0
    for pair in data:
        if _any_overlap_new(pair):
            answer += 1
    return answer


def _is_contained_pair(pair):
    if len(pair[0]) <= len(pair[1]):
        return pair[0].issubset(pair[1])
    return pair[1].issubset(pair[0])


def _is_contained_pair_new(pair):
    return (
        pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]
    ) or (
        pair[0][0] > pair[1][0] and pair[1][1] >= pair[0][1]
    )


def _any_overlap(pair):
    return len(pair[0].intersection(pair[1])) > 0


def _any_overlap_new(pair):
    return pair[0][1] <= pair[1][0] or pair[1][0] <= pair[0][0]


def main():
    data = prepare_data_new()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

