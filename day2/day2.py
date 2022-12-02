#!/usr/bin/env python3

import numpy as np


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
        0: lambda o: (o + 2) % 3,
        1: lambda o: o + 3,
        2: lambda o: (o + 1) % 3 + 6,
    }
    score_mapping = {
        (True, False): lambda m: 3 + m,
        (False, True): lambda m: 6 + m
    }
    scores_part1 = []
    scores_part2 = []
    with open('day2-input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            choices = line.split(' ')
            opponent = mapping[choices[0]]
            me = mapping[choices[1]]
            scores_part1.append(score_mapping.get((opponent == me, (me + 2) % 3 == opponent), lambda _: me)(me) + 1)
            scores_part2.append(outcome_mapping[me](opponent) + 1)
    print(sum(scores_part1))
    print(sum(scores_part2))
