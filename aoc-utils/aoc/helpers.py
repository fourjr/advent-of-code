import sys
from pathlib import Path


__all__ = ('get_input_as')


CURRENT_FP = Path(sys.argv[0])
CURRENT_DIR = CURRENT_FP.parent
INPUT_FP = CURRENT_DIR / 'input.txt'


def get_input(*, sep):
    with open(INPUT_FP) as f:
        contents = f.read()
        if sep is None:
            return contents.splitlines()
        else:
            return contents.split(sep)


def get_input_as(callback=str, sep=None):
    return list(map(callback, get_input(sep=sep)))


def submit():
    pass
