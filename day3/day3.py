#!/usr/bin/env python3

import numpy as np
import functools


if __name__ == '__main__':
    with open('day3-input-sample.txt') as f:
        score_part1 = []
        score_part2 = []
        index = 0
        group_items = []
        get_priority = lambda c: ord(c) - ord('A') + 27 if ord(c) <= ord('Z') else ord(c) - ord('a') + 1
        foldl = lambda func, acc, xs: functools.reduce(func, xs, acc)
        for line in f:
            line = line.strip()
            num_items = len(line) // 2
            first_half = set(line[:num_items])
            second_half = set(line[num_items:])
            index += 1
            group_items.append(set(line))
            if index % 3 == 0:
                item = list(foldl(lambda a, b: a.intersection(b), group_items[0], group_items))[0]
                group_items = []
                score_part2.append(get_priority(item))

            common = list(first_half.intersection(second_half))[0]
            score_part1.append(get_priority(common))
            
        print(sum(score_part1))
        print(sum(score_part2))
