from helper.utils import *
from itertools import product


DAY = 9


class Knot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.positions = [(x, y)]

    def move(self, direction):
        self.x += direction[0]
        self.y += direction[1]
        self.positions.append((self.x, self.y))

    def execute_moves(self, moves):
        for move in moves:
            self.move(move)

    def follow(self, knot):
        for position in knot.positions:
            if not self.in_range(position):
                self.move(self.get_direction(position))

    def in_range(self, position):
        x_range = range(position[0] - 1, position[0] + 2)
        y_range = range(position[1] - 1, position[1] + 2)
        return self.x in x_range and self.y in y_range

    def get_direction(self, position):
        valid_positions = {
            (position[0] + x, position[1] + y)
            for x, y in kernel(diagonals=False)
        }
        possible_positions = {
            (self.x + x, self.y + y)
            for x, y in kernel()
        }
        intersecting_positions = valid_positions.intersection(possible_positions)
        if not intersecting_positions:
            valid_positions = {
                (position[0] + x, position[1] + y)
                for x, y in kernel()
            }
            intersecting_positions = valid_positions.intersection(possible_positions)
        new_pos = intersecting_positions.pop()
        return new_pos[0] - self.x, new_pos[1] - self.y


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    moves = []
    for row in raw_data:
        match row.split(" "):
            case ["U", steps]:
                d = (0, 1)
            case ["D", steps]:
                d = (0, -1)
            case ["L", steps]:
                d = (-1, 0)
            case ["R", steps]:
                d = (1, 0)
            case _:
                raise ValueError("Unknown direction")
        for _ in range(int(steps)):
            moves.append(d)
    return moves


@time_function
def part_a(moves):
    knots = [Knot() for _ in range(2)]
    knots[0].execute_moves(moves)
    knots[1].follow(knots[0])
    return len(set(knots[1].positions))


@time_function
def part_b(moves):
    knots = [Knot() for _ in range(10)]
    knots[0].execute_moves(moves)
    for i, knot in enumerate(knots[1:]):
        knot.follow(knots[i])
    return len(set(knots[-1].positions))


def kernel(diagonals=True):
    if diagonals:
        return product([-1, 0, 1], repeat=2)
    return [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]


def main():
    part_a(prepare_data())
    part_b(prepare_data())


if __name__ == '__main__':
    main()

