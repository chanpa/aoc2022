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


def chat_gpt(input):
    # Parse the instructions in the program
    instructions = parse_file_rows_to_list(DAY)

    # Initialize the X register to 1
    x = 1

    # The current cycle number
    cycle = 0

    # The total signal strength
    signal_strength = 0

    # The remaining number of cycles for the current instruction
    remaining_cycles = 0

    # The next cycle where the signal strength should be checked
    next_signal_check = 20

    # Loop through each instruction in the program
    for instruction in instructions:
        # Increment the cycle number
        cycle += 1

        # Check if the instruction has finished executing
        if remaining_cycles > 0:
            # Decrement the remaining cycles for the instruction
            remaining_cycles -= 1
        else:
            # Parse the instruction
            parts = instruction.split()
            op = parts[0]

            # Check if the instruction is a noop
            if op == "noop":
                # Do nothing
                pass
            elif op == "addx":
                # Add the value to the X register
                value = int(parts[1])
                x += value

                # The addx instruction takes two cycles to execute
                remaining_cycles = 1
            else:
                # Invalid instruction
                raise ValueError("Invalid instruction: " + instruction)

        # Check if the current cycle is the next cycle where the signal strength should be checked
        if cycle == next_signal_check:
            # Calculate the signal strength for this cycle
            signal_strength += cycle * x

            # Set the next cycle where the signal strength should be checked to 40 cycles after the current cycle
            next_signal_check += 40

    # Print the final signal strength
    print("Signal strength:", signal_strength)


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)
    chat_gpt(data)


if __name__ == '__main__':
    main()

