import math
import os


def add(a, b) -> int:
    return math.floor(a + b)


def func2(a, b, c) -> str:
    return os.getcwd()


def to_sentence(s) -> str:
    s = s.capitalize()
    if s.endswith("."):
        return s
    else:
        return s + ".."
