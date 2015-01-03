#!/usr/bin/python3


import sys
import argparse
from itertools import islice, cycle

from pattern import *


def main(argv=None):
    argparser = argparse.ArgumentParser()
    argparser.add_argument('length', type=int)
    argparser.add_argument('sets', nargs='*', default=DEFAULT_PATTERN_SETS)
    argparser.add_argument('-a', '--alignment', type=int, default=None)
    argparser.add_argument('-f', '--allow-repeats', action='store_true')
    if argv is None:
        args = argparser.parse_args()
    else:
        args = argparser.parse_args(argv)

    try:
        print(''.join(pattern_create(args.length, args.sets, args.alignment,
                                     args.allow_repeats)))
    except NotEnoughPermutationsError as e:
        print(e, file=sys.stderr)
        print('(use -f to ignore)', file=sys.stderr)
        return 2
    except ValueError as e:
        print(e, file=sys.stderr)
        return 1

    return 0

if __name__ == '__main__':
    sys.exit(main())
