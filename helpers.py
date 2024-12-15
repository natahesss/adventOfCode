from functools import partial

class Colors:
    OK = "\033[92m"  # green
    WARNING = "\033[93m"  # yellow
    FAIL = "\033[91m"  # red
    PINK = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[36m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
    ITALIC = "\x1B[3m"


def colored_print(color: str, *args, sep=" ", end="\n"):
    print(color, *args, Colors.END, sep=sep, end=end)


print_green = partial(colored_print, Colors.OK)
print_warning = partial(colored_print, Colors.FAIL)
print_yellow = partial(colored_print, Colors.WARNING)
print_pink = partial(colored_print, Colors.PINK+Colors.ITALIC)
print_blue = partial(colored_print, Colors.CYAN)