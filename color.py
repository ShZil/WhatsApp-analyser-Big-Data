# Colors ---------------------------------------------------------------------------------------------------------------

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
WHITE = '\u001b[37m'
UNDERLINE = '\033[4m'
END = '\033[0m'


def uncolor():
    global PURPLE
    global CYAN
    global DARKCYAN
    global BLUE
    global GREEN
    global YELLOW
    global RED
    global BOLD
    global WHITE
    global UNDERLINE
    global END
    PURPLE = ''
    CYAN = ''
    DARKCYAN = ''
    BLUE = ''
    GREEN = ''
    YELLOW = ''
    RED = ''
    BOLD = ''
    WHITE = ''
    UNDERLINE = ''
    END = ''


def ize(colors, text):
    colors = list(colors)
    return "".join(colors) + text + END
