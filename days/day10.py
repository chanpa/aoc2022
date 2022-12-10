from helper.utils import *


DAY = 10


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    return raw_data


@time_function
def part_a(data):
    return sum([c * v for c, v in _signal_strengths(data)])


@time_function
def part_b(data):
    screen = _render_image(data)
    rows = [
        "".join(row)
        for row in screen
    ]
    image = "\n".join(rows)
    return f"\n{image}"


def _signal_strengths(instructions, interval=40):
    cycle = 1
    x = 1
    signals_strengths = []
    for instr in instructions:
        match [part.strip() for part in instr.split(" ")]:
            case ["noop"]:
                cycle += 1
                if cycle == 20 or (cycle - 20) % interval == 0:
                    signals_strengths.append((x, cycle))
            case ["addx", v]:
                for i in range(2):
                    cycle += 1
                    if i == 1:
                        x += int(v)
                    if cycle == 20 or (cycle - 20) % interval == 0:
                        signals_strengths.append((x, cycle))

    return signals_strengths


def _render_image(instructions):
    screen = [
        [" "] * 40,
        [" "] * 40,
        [" "] * 40,
        [" "] * 40,
        [" "] * 40,
        [" "] * 40,
    ]
    cycle = 0
    x = 1
    for instr in instructions:
        match [part.strip() for part in instr.split(" ")]:
            case ["noop"]:
                screen_x, screen_y = get_screen_pixel(cycle)
                if screen_x in range(x - 1, x + 2):
                    screen[screen_y][screen_x] = "█"
                cycle += 1

            case ["addx", v]:
                for _ in range(2):
                    screen_x, screen_y = get_screen_pixel(cycle)
                    if screen_x in range(x - 1, x + 2):
                        screen[screen_y][screen_x] = "█"
                    cycle += 1
                x += int(v)

    return screen


def get_screen_pixel(cycle):
    y = cycle // 40
    x = cycle % 40
    return x, y


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

