from helper.utils import *
import re


DAY = 5
pattern_start = re.compile("[A-Z]| {4}")
pattern_moves = re.compile("\d+")


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    moves = []
    columns = [[] for _ in range(9)]
    for row in reversed(raw_data):
        if row.startswith("move"):
            move = [int(n) for n in pattern_moves.findall(row)]
            move[1] -= 1
            move[2] -= 1
            moves.append(move)
        elif row := pattern_start.findall(row):
            for i, crate_tag in enumerate(row):
                if len(crate_tag) == 1:
                    columns[i].append(crate_tag)

    return columns, reversed(moves)


@time_function
def part_a(data):
    columns, moves = data
    _execute_moves(columns, moves)
    return _get_top_crates(columns)


@time_function
def part_b(data):
    columns, moves = data
    _execute_moves(columns, moves, move_all=True)
    return _get_top_crates(columns)


def _execute_moves(columns, moves, move_all=False):
    for move in moves:
        qty, frm, to = move

        if move_all:
            crates_moving = columns[frm][-qty:]
        else:
            crates_moving = reversed(columns[frm][-qty:])

        columns[to] += crates_moving
        columns[frm] = columns[frm][:-qty]


def _get_top_crates(arrangement):
    return "".join([
        col[-1]
        for col in arrangement
    ])


def main():
    part_a(prepare_data())
    part_b(prepare_data())


if __name__ == '__main__':
    main()

