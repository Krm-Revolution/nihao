from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from string import printable
import collections
import random
import sys
import time

try:
    import curses
except ImportError:
    print("pmatrix requires curses for terminal rendering; exiting.")
    exit(1)

# Colors that the user may set as foreground/background.
COLORS = {
    "BLACK": curses.COLOR_BLACK,
    "BLUE": curses.COLOR_BLUE,
    "CYAN": curses.COLOR_CYAN,
    "GREEN": curses.COLOR_GREEN,
    "MAGENTA": curses.COLOR_MAGENTA,
    "RED": curses.COLOR_RED,
    "WHITE": curses.COLOR_WHITE,
    "YELLOW": curses.COLOR_YELLOW,
}

def rand_string(character_set, length):
    """Returns a random string.
        character_set -- the characters to choose from.
        length        -- the length of the string.
    """
    return "".join(random.choice(character_set) for _ in range(length))

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, FG, BG)
    stdscr.bkgd(curses.color_pair(1))
    size = stdscr.getmaxyx()

    # background is a matrix of the actual letters (not lit up) -- the underlay.
    # foreground is a list of [row, col] pairs representing the position of lit letters
    # dispense is where new 'streams' of lit letters appear from.
    background = [random.choice(printable.strip()) for _ in range(size[0] * size[1])]
    foreground = []
    dispense = []

    delta = 0
    bg_refresh_counter = random.randint(3, 7)
    lt = time.time()

    while True:
        stdscr.erase()

        now = time.time()
        delta += (now - lt) * UPDATES_PER_SECOND
        lt = now

        while delta >= 1:
            if stdscr.getmaxyx() != size:
                # Screen size changed, restart
                return

            # Add new dispense points
            for _ in range(LETTERS_PER_UPDATE):
                dispense.append(random.randint(0, size[1] - 1))

            # Start new streams from dispense points
            for col in dispense[:]:  # Iterate over a copy to allow modification
                foreground.append([0, col])
                if not random.randint(0, PROBABILITY):
                    dispense.remove(col)

            # Update and draw falling characters
            i = 0
            while i < len(foreground):
                row, col = foreground[i]
                if row < size[0] - 1 and col < size[1]:
                    try:
                        stdscr.addch(row, col, 
                                   background[row * size[1] + col],
                                   curses.color_pair(1))
                        foreground[i][0] += 1
                        i += 1
                    except curses.error:
                        # Ignore drawing errors at screen edges
                        del foreground[i]
                else:
                    del foreground[i]

            # Refresh background occasionally
            bg_refresh_counter -= 1
            if bg_refresh_counter <= 0:
                background = [random.choice(printable.strip()) for _ in range(size[0] * size[1])]
                bg_refresh_counter = random.randint(3, 7)

            delta -= 1
            stdscr.refresh()

def start():
    parser = ArgumentParser(description="Create the matrix falling text.",
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument("-b", "--background", default="black",
            help="The colour of the falling text.")
    parser.add_argument("-c", "--clear", action="store_true",
            help="Use stdscr.clear() instead of stdscr.erase().")
    parser.add_argument("-f", "--foreground", default="green",
            help="The colour of the falling text.")
    parser.add_argument("-l", "--letters", type=int, default=2,
            help="The number of letters produced per update.")
    parser.add_argument("-p", "--probability", type=int, default=5,
            help="1/p probability of a dispense point deactivating each tick.")
    parser.add_argument("-u", "--ups", type=int, default=15,
            help="The number of updates to perform per second.")
    args = parser.parse_args()

    global BG, CLEAR, FG, LETTERS_PER_UPDATE, PROBABILITY, UPDATES_PER_SECOND
    CLEAR = args.clear
    FG = COLORS.get(args.foreground.upper(), curses.COLOR_GREEN)
    BG = COLORS.get(args.background.upper(), curses.COLOR_BLACK)
    LETTERS_PER_UPDATE = abs(args.letters)
    PROBABILITY = max(1, args.probability) - 1  # Ensure probability is at least 1
    UPDATES_PER_SECOND = abs(args.ups)

    try:
        while True:
            curses.wrapper(main)
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)

if __name__ == "__main__":
    start()
