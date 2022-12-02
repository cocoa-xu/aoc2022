#!/usr/bin/env python3

import numpy as np


if __name__ == '__main__':
    elves = []
    with open('day1-input.txt') as f:
        food = []
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                elves.append(sum(food))
                food = []
            else:
                food.append(int(line))
    # question 1
    print(elves[np.argmax(elves)])
    # question 2
    print(sum(np.sort(elves)[-3:]))
