#!/usr/bin/env python3

import numpy as np
from functools import reduce


if __name__ == '__main__':
    with open('day4-input-sample.txt') as f:
        full_contains = lambda a, b: (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1])
        overlaps = lambda a, b: (a[1] >= b[0] and b[0] >= a[0]) or (b[1] >= a[0] and a[0] >= b[0])
        num_full_contains = 0
        num_overlaps = 0
        for line in f:
            line = line.strip().split(',')
            first_half = list(map(int, line[0].split('-')))
            second_half = list(map(int, line[1].split('-')))

            if overlaps(first_half, second_half):
                num_overlaps += 1
                if full_contains(first_half, second_half):
                    num_full_contains += 1
        print(num_full_contains)
        print(num_overlaps)
