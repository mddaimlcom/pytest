from enum import unique, Enum


@unique
class TermColors(Enum):
   PURPLE = '\033[95m{}\033[0m'
   CYAN = '\033[96m{}\033[0m'
   DARKCYAN = '\033[36m{}\033[0m'
   BLUE = '\033[94m{}\033[0m'
   GREEN = '\033[92m{}\033[0m'
   YELLOW = '\033[93m{}\033[0m'
   RED = '\033[91m{}\033[0m'
   BOLD = '\033[1m{}\033[0m'
   UNDERLINE = '\033[4m{}\033[0m'
