#!/usr/bin/env python

import sys
import datetime
import re

# times and operations
sys.argv.pop(0)

args = []

hasToBeOp = False

for arg in sys.argv:
    if hasToBeOp:
        # hasToBeOp = False
        if not (arg == '+' or arg == '-'):
            args.append('+')
        else:
            hasToBeOp = False
    else:
        hasToBeOp = True

    args.append(arg)

times = args[0::2]
ops = args[1::2]


def time_to_sec(timestr):
    ftr = [3600, 60, 1]

    return sum([a * b for a, b in zip(ftr, map(int, re.split("[,./:_-]", timestr)))])


def operate_on_time(left, op, right):
    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    else:
        raise ValueError


def sec_to_time(secs):
    return str(datetime.timedelta(seconds=secs))


seconds = map(lambda x: time_to_sec(x), times)

final_time = reduce(lambda last, current: operate_on_time(last, ops.pop(0), current), seconds, seconds.pop(0))

print sec_to_time(final_time)
