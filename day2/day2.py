#!/usr/bin/env python3

import numpy as np


def score(opponent, me):
    if opponent == me:
        return 3 + me + 1
    elif (me + 2) % 3 == opponent:
        return 6 + me + 1
    else:
        return me + 1


if __name__ == '__main__':
    mapping = {
        'X': 0,
        'Y': 1,
        'Z': 2,
        
        'A': 0,
        'B': 1,
        'C': 2,
    }
    outcome_mapping = {
        'X': lambda o: (o + 2) % 3,
        'Y': lambda o: o + 3,
        'Z': lambda o: (o + 1) % 3 + 6,
    }
    scores_part1 = []
    scores_part2 = []
    with open('day2-input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            choices = line.split(' ')
            opponent = mapping[choices[0]]
            me = choices[1]
            scores_part1.append(score(opponent, mapping[me]))
            scores_part2.append(outcome_mapping[me](opponent) + 1)
    print(sum(scores_part1))
    print(sum(scores_part2))
