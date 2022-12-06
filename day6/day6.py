#!/usr/bin/env python3


def find_marker(line: str, num_distinct: int):
    loc2char = {}
    char2loc = {}
    index = 0
    max_pos = len(line) - num_distinct
    maybe_start = 0
    while index < len(line):
        current_char = line[index]
        maybe_loc = char2loc.get(current_char)
        if maybe_loc is None:
            char2loc[current_char] = index
            loc2char[index] = current_char
            if len(char2loc) == num_distinct:
                return index + 1
        else:
            for i in range(maybe_start, maybe_loc+1):
                c = loc2char.get(i)
                if c is not None:
                    del loc2char[i]
                    del char2loc[c]
            char2loc[current_char] = index
            loc2char[index] = current_char
            maybe_start = maybe_loc
        index += 1


if __name__ == '__main__':
    with open('day6-input-sample.txt') as f:
        distinct_part1 = 4
        distinct_part2 = 14
        for line in f:
            line = line.strip()
            print(find_marker(line, distinct_part1), find_marker(line, distinct_part2))
