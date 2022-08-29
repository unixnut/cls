"""Command-line interface"""

import re, sys

from .colorls import cols_format


LINE_REGEX = re.compile(r"\s*\S+")


def main(args):
    """Called indirectly from a `c*ls` script.  Colorise the input as required.

    Parameters: $size_column $inums $ownership_cols"""

    size_column = int(args[1]) - 1
    inums_on = args[2] == "y"
    ownership_cols = int(args[3])
    if inums_on:
        dir_column = 1
    else:
        dir_column = 0

    ## print(len(args))
    for line in sys.stdin:
        cols = LINE_REGEX.findall(line)
        if len(cols) >= size_column + 3:
            # Check for column blending, i.e. owner/group suffix blends in with size prefix
            blend = (inums_on and size_column == 3) or size_column == 2
            print(cols_format(cols, ownership_cols, size_column, dir_column, blend))
        else:
            print(line, end='')
    return 0


# *** MAINLINE ***
if __name__ == '__main__':
   sys.exit(main(sys.argv))
