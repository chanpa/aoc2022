from helper.utils import *


DAY = 2
opp_map = {
    "A": "rock",
    "B": "paper",
    "C": "scissor"
}


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    rounds = [
        (round[0], round[2])
        for round in raw_data
    ]
    return rounds


@time_function
def part_a(data):
    me_map = {
        "X": "rock",
        "Y": "paper",
        "Z": "scissor"
    }
    return sum([get_score(opp_map[opp], me_map[me]) for opp, me in data])


@time_function
def part_b(data):
    strategies = {
        "rock": {
            "X": "scissor",
            "Y": "rock",
            "Z": "paper"
        },
        "paper": {
            "X": "rock",
            "Y": "paper",
            "Z": "scissor"
        },
        "scissor": {
            "X": "paper",
            "Y": "scissor",
            "Z": "rock"
        }
    }
    return sum([get_score(opp_map[opp], strategies[opp_map[opp]][strategy]) for opp, strategy in data])


def get_score(opp, me):
    ch_score = {"rock": 1, "paper": 2, "scissor": 3}
    score = ch_score[me]
    match (opp, me):
        case _ if opp == me:
            score += 3
        case ("rock", "paper"):
            score += 6
        case ("rock", "scissor"):
            score += 0
        case ("paper", "rock"):
            score += 0
        case ("paper", "scissor"):
            score += 6
        case ("scissor", "rock"):
            score += 6
        case ("scissor", "paper"):
            score += 0
    return score


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

