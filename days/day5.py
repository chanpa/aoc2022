from helper.utils import *
from collections import defaultdict
import re


DAY = 5
pattern_start = re.compile("[A-Z]| {4}")
pattern_moves = re.compile("\d+")


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    rows = []
    for row in raw_data:
        if not row:
            break
        rows.append(pattern_start.findall(row))

    columns = defaultdict(list)
    for row in reversed(rows):
        for i, col in enumerate(row):
            if len(col) == 1:
                columns[i].append(col)

    moves = []
    for row in raw_data:
        if row.startswith("move"):
            moves.append([int(m) for m in pattern_moves.findall(row)])

    return columns, moves


@time_function
def part_a(data):
    columns, moves = data
    for move in moves:
        qty, frm, to = move
        frm -= 1
        to -= 1
        crates_moving = reversed(columns[frm][-qty:])
        columns[to] += crates_moving
        columns[frm] = columns[frm][:-qty]
    msg = "".join([
        col[-1]
        for _, col in columns.items()
    ])
    return msg


@time_function
def part_b(data):
    columns, moves = data
    for move in moves:
        qty, frm, to = move
        frm -= 1
        to -= 1
        crates_moving = columns[frm][-qty:]
        columns[to] += crates_moving
        columns[frm] = columns[frm][:-qty]
    msg = "".join([
        col[-1]
        for _, col in columns.items()
    ])
    return msg


def main():
    part_a(prepare_data())
    part_b(prepare_data())


if __name__ == '__main__':
    main()

