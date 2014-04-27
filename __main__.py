import time
import sys
import os

def do_task():
    time.sleep(0.2)

def erase_line():
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)

def example_1(n):

    list = [' ._. ',' ^^ ',' ._. ',' ._. ',' ._. ',' ._. ',' ._. ',' ^^ ',' ._. ',' ._. ',' ._. ',' ._. ']

    for i in range(n):
        print list[i],
        sys.stdout.flush()
        erase_line()
        do_task()

example_1(10)