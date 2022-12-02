from helper.utils import *
from enum import Enum


DAY = 2


class Sign(Enum):
    ROCK = 0
    PAPER = -1
    SCISSORS = 1


opp_map = {
    "A": Sign.ROCK,
    "B": Sign.PAPER,
    "C": Sign.SCISSORS
}


@time_function
def prepare_data():
    raw_data = parse_file_rows_to_list(DAY)
    rounds = [
        (opp_map[round[0]], round[2])
        for round in raw_data
    ]
    return rounds


@time_function
def part_a(data):
    me_map = {
        "X": Sign.ROCK,
        "Y": Sign.PAPER,
        "Z": Sign.SCISSORS
    }
    return sum([get_score(opp, me_map[me]) for opp, me in data])


@time_function
def part_b(data):
    strategies = {
        Sign.ROCK: {
            "X": Sign.SCISSORS,
            "Y": Sign.ROCK,
            "Z": Sign.PAPER
        },
        Sign.PAPER: {
            "X": Sign.ROCK,
            "Y": Sign.PAPER,
            "Z": Sign.SCISSORS
        },
        Sign.SCISSORS: {
            "X": Sign.PAPER,
            "Y": Sign.SCISSORS,
            "Z": Sign.ROCK
        }
    }
    return sum([get_score_new(opp, strategies[opp][strategy]) for opp, strategy in data])


def get_score(opp, me):
    ch_score = {Sign.ROCK: 1, Sign.PAPER: 2, Sign.SCISSORS: 3}
    score = ch_score[me]
    match (opp, me):
        case _ if opp == me:
            score += 3
        case (Sign.ROCK, Sign.PAPER):
            score += 6
        case (Sign.ROCK, Sign.SCISSORS):
            score += 0
        case (Sign.PAPER, Sign.ROCK):
            score += 0
        case (Sign.PAPER, Sign.SCISSORS):
            score += 6
        case (Sign.SCISSORS, Sign.ROCK):
            score += 6
        case (Sign.SCISSORS, Sign.PAPER):
            score += 0
    return score


def get_score_new(opp, me):
    ch_score = {Sign.ROCK: 1, Sign.PAPER: 2, Sign.SCISSORS: 3}
    score = ch_score[me]
    result = _get_result(opp, me)
    match result:
        case 2:
            score += 3
        case _ if result == me.value:
            score += 6
    return score


def _get_result(hand1, hand2):
    winning_hand = 2  # draw
    if hand1 != hand2:
        if abs(hand1.value) == abs(hand2.value):  # paper and scissors
            winning_hand = max(hand1.value, hand2.value)
        else:
            winning_hand = min(hand1.value, hand2.value)
    return winning_hand


def main():
    data = prepare_data()
    part_a(data)
    part_b(data)


if __name__ == '__main__':
    main()

