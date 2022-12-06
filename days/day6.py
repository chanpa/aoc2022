from helper.utils import *


DAY = 6


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    return raw_data[0]


@time_function
def part_a(data):
    return _find_marker(data)


@time_function
def part_b(data):
    return _find_marker(data, window=14)


def _find_marker(signal, window=4):
    for i in range(window - 1, len(signal)):
        chars = set(signal[i - window + 1:i + 1])
        if len(chars) == window:
            return i + 1


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

