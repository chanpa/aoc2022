from helper.utils import *


DAY = 2


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    rounds = [
        (round[0], round[2])
        for round in raw_data
    ]
    return rounds


def score_round(opp, me):
    vals = {"rock": 1, "paper": 2, "scissor": 3}
    return vals[me] + get_score(opp, me)


def get_score(opp, me):
    if opp == me:
        return 3

    if opp == "rock" and me == "paper":
        return 6

    if opp == "rock" and me == "scissor":
        return 0

    if opp == "paper" and me == "rock":
        return 0

    if opp == "paper" and me == "scissor":
        return 6

    if opp == "scissor" and me == "rock":
        return 6

    if opp == "scissor" and me == "paper":
        return 0


@time_function
def part_a(data):
    opp_map = {
        "A": "rock",
        "B": "paper",
        "C": "scissor"
    }
    me_map = {
        "X": "rock",
        "Y": "paper",
        "Z": "scissor"
    }
    return sum([score_round(opp_map[opp], me_map[me]) for opp, me in data])


@time_function
def part_b(data):
    opp_map = {
        "A": "rock",
        "B": "paper",
        "C": "scissor"
    }
    choices = {
        "rock": {
            "x": "scissor",
            "y": "rock",
            "z": "paper"
        },
        "paper": {
            "x": "rock",
            "y": "paper",
            "z": "scissor"
        },
        "scissor": {
            "x": "paper",
            "y": "scissor",
            "z": "rock"
        }
    }
    return sum([score_round(opp_map[opp], choices[opp_map[opp]][strat.lower()]) for opp, strat in data])


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

