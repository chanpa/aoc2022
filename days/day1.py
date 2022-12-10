from helper.utils import *


DAY = 1


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    gnomes = [[]]
    for row in raw_data:
        if row == "\n":
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


def chat_gpt():
    with open(f"{Path(__file__).parents[1].resolve()}/inputs/1.data") as f:
        input_data = f.read()

    inventories = []
    current_inventory = []

    for line in input_data.strip().split('\n'):
        if line:
            # Parse the Calories for each food item and add it to the current inventory
            current_inventory.append(int(line))
        else:
            # Add the current inventory to the list of inventories and reset the current inventory
            inventories.append(current_inventory)
            current_inventory = []

    # Calculate the total Calories for each inventory and find the Elf with the highest total
    max_calories = 0
    max_elf = None

    for i, inventory in enumerate(inventories):
        total_calories = sum(inventory)
        if total_calories > max_calories:
            max_calories = total_calories
            max_elf = i
    print(sum(inventories[max_elf]))


def chat_gpt2():
    input = []
    with open(f"{Path(__file__).parents[1].resolve()}/inputs/1.data") as f:
        for line in f:
            if line == "\n":
                input.append("")
            else:
                input.append(line)

    # Parse the input into a list of integers
    calories = []
    current_elf = 0
    for line in input:
        if line != '':
            calories.append((current_elf, int(line)))
        else:
            current_elf += 1

    # Calculate the total number of Calories for each Elf
    elf_calories = {}
    for elf, calorie in calories:
        if elf not in elf_calories:
            elf_calories[elf] = 0
        elf_calories[elf] += calorie

    # Find the Elf with the most Calories
    max_elf = 0
    max_calories = 0
    for elf, calorie in elf_calories.items():
        if calorie > max_calories:
            max_elf = elf
            max_calories = calorie

    # Output the result
    print(f"Elf {max_elf} has the most Calories with a total of {max_calories}")

    # Find the top three Elves with the most Calories
    sorted_elves = sorted(elf_calories, key=elf_calories.get, reverse=True)[:3]

    # Calculate the total number of Calories carried by the top three Elves
    total_calories = 0
    for elf in sorted_elves:
        total_calories += elf_calories[elf]

    # Output the result
    print(f"The top three Elves are carrying {total_calories} Calories in total")


def main():
    # data = prepare_data()
    # part_a(data)
    # part_b(data)
    chat_gpt2()


if __name__ == '__main__':
    main()

