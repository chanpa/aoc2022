from helper.utils import *
from pathlib import Path


DAY = 7


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    return raw_data


@time_function
def part_a(data):
    dir_sizes = _calc_sizes(data)
    total = sum(size for size in dir_sizes.values() if size <= 100000)
    return total


@time_function
def part_b(data):
    dir_sizes = _calc_sizes(data)
    free_space = 70_000_000 - dir_sizes["/"]
    required_deletion = 30_000_000 - free_space

    for size in sorted(dir_sizes.values()):
        if size >= required_deletion:
            return size


def _calc_sizes(commands):
    dir_stack = [""]
    dir_sizes = defaultdict(int)
    for command in [c.strip() for c in commands[1:]]:
        match command.split(" "):
            case ["$", "cd", ".."]:
                dir_stack.pop()
            case ["$", "cd", new_dir]:
                dir_stack.append(new_dir)
            case [size, file_name] if size.isnumeric():
                for d in Path("/".join(dir_stack + [file_name])).parents:
                    dir_sizes[str(d)] += int(size)
    return dir_sizes


def main():
    part_a(prepare_data())
    part_b(prepare_data())


if __name__ == '__main__':
    main()

