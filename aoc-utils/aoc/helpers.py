import os
import sys
from pathlib import Path

import aocd


__all__ = ('get_input_as')


CURRENT_FP = Path(sys.argv[0])
CURRENT_DIR = CURRENT_FP.parent
if CURRENT_DIR.name == '':
    # Running in directory
    CURRENT_FP = Path(os.getcwd()) / CURRENT_FP
    CURRENT_DIR = CURRENT_FP.parent

INPUT_FP = CURRENT_DIR / 'input.txt'

try:
    DAY = int(CURRENT_DIR.name[3:].strip())
    YEAR = int(CURRENT_DIR.parent.name)
    PART = int(CURRENT_FP.name[4:-3])
except (ValueError, IndexError):
    raise ValueError('Invalid import file path. Ensure that you are importing this module from an advent of code problem in a filepath similar to: YEAR/DayXX/partX.py')


def get_input(*, sep, no_strip=False):
    try:
        with open(INPUT_FP, encoding='utf8') as f:
            data = f.read()
            if not data:
                raise FileNotFoundError
    except FileNotFoundError:
        data = aocd.get_data(day=DAY, year=YEAR)

        with open(INPUT_FP, 'w', encoding='utf8') as f:
            f.write(data)

    if no_strip is False:
        data = data.strip()

    if sep == -1:
        return data

    if sep is None:
        return data.splitlines()
    else:
        return data.split(sep)


def get_input_as(callback=str, sep=None, no_strip=False):
    return list(map(callback, get_input(sep=sep, no_strip=no_strip)))


def submit(answer):
    try:
        answer = int(answer)
    except ValueError:
        print(f'Warning: {answer} is not an int')

    response = input(f'Submit {answer} [y/N]: ')
    if response.lower() == 'y':
        aocd.submit(answer, part=PART, day=DAY, year=YEAR)


def sign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0
