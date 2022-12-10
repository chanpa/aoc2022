from helper.utils import *
from functools import reduce
from operator import mul


DAY = 8


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    treemap = [
        [int(c) for c in row.strip()]
        for row in raw_data
    ]
    return treemap


@time_function
def part_a(treemap):
    visible_trees = (len(treemap) * 2) + ((len(treemap[0]) - 2) * 2)
    for y, row in enumerate(treemap[1:-1]):
        for x, tree in enumerate(row[1:-1]):
            if is_visible(x + 1, y + 1, treemap):
                visible_trees += 1
    return visible_trees


@time_function
def part_b(treemap):
    scenic_scores = []
    for y, row in enumerate(treemap):
        for x, tree in enumerate(row):
            scenic_scores.append(scenic_score(x, y, treemap))
    return max(scenic_scores)


def is_visible(x, y, treemap):
    tree = treemap[y][x]
    tree_in_dirs = [
        [
            treemap[t_y][x] < tree
            for t_y in range(0, y)
        ],
        [
            treemap[t_y][x] < tree
            for t_y in range(y + 1, len(treemap))
        ],
        [
            treemap[y][t_x] < tree
            for t_x in range(0, x)
        ],
        [
            treemap[y][t_x] < tree
            for t_x in range(x + 1, len(treemap[0]))
        ]
    ]
    return any([all(direction) for direction in tree_in_dirs])


def scenic_score(x, y, treemap):
    tree = treemap[y][x]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    viewing_distances = []
    for x_dir, y_dir in directions:
        d_trees = 0
        for i in range(1, 1000):
            otree_y = y + (y_dir * i)
            otree_x = x + (x_dir * i)
            if otree_x < 0 or otree_y < 0:
                break
            if otree_x >= len(treemap[0]) or otree_y >= len(treemap[0]):
                break
            otree = treemap[otree_y][otree_x]
            d_trees += 1
            if otree >= tree:
                break
        viewing_distances.append(d_trees)
    return reduce(mul, viewing_distances, 1)


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

