#!/usr/bin/env python3

import re
import copy

def parse_crate(stacks, crate_line):
    num = (len(crate_line) + 1) // 4
    for i in range(num):
        current_crate = crate_line[i*4+1]
        if current_crate != ' ':
            if stacks.get(i + 1, None) is None:
                stacks[i + 1] = []
            stacks[i + 1].append(current_crate)


if __name__ == '__main__':
    with open('day5-input-sample.txt') as f:
        stacks = {}
        stacks_part1, stacks_part2 = None, None
        parsing_operations = False
        num_stacks = 0
        op_re = re.compile(r'^move (\d+) from (\d+) to (\d+)$')
        for line in f:
            line = line.rstrip()
            if not parsing_operations:
                if line.startswith(' 1'):
                    num_stacks = len(line.split('   '))
                    for i in range(1, num_stacks + 1):
                        if stacks.get(i, None) is None:
                            stacks[i] = []
                        else:
                            stacks[i] = list(reversed(stacks[i]))
                        stacks_part1 = copy.deepcopy(stacks)
                        stacks_part2 = copy.deepcopy(stacks)
                    parsing_operations = True
                    continue
                else:
                    parse_crate(stacks, line)
            else:
                if len(line) > 0:
                    amount, src, dst = tuple(map(int, op_re.match(line).groups()))
                    crates = stacks_part1[src][-amount:]
                    stacks_part1[dst].extend(reversed(crates))
                    del stacks_part1[src][-amount:]

                    crates = stacks_part2[src][-amount:]
                    stacks_part2[dst].extend(crates)
                    del stacks_part2[src][-amount:]
        print("".join([stacks_part1[i][-1] for i in range(1, num_stacks + 1)]))
        print("".join([stacks_part2[i][-1] for i in range(1, num_stacks + 1)]))
