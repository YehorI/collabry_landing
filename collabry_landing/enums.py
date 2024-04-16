from enum import Enum, auto


class EmailStatus(Enum):
    EXISTS = auto()
    SAVED = auto()
    WRONG = auto()
