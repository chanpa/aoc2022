from helper.utils import *


DAY = 1


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    gnomes = [[]]
    for row in raw_data:
        if not row:
            gnomes.append([])
            continue
        gnomes[-1].append(int(row))
    return gnomes


@time_function
def part_a(data):
    answer = max([sum(gnome) for gnome in data])
    return answer


@time_function
def part_b(data):
    sums = [sum(gnome) for gnome in data]
    return sum(sorted(sums)[-3:])


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

