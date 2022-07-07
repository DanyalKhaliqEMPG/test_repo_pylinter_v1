import math
import os


def add(a, b) -> int:
    return math.floor(a + b)


def func2(a, b, c) -> str:
    return os.getcwd()


def subtract(a, b) -> int:
    return a - b


def pow(a, b) -> int:
    return pow(a, b)


def to_sentence(s) -> str:
    s = s.capitalize()
    if s.endswith("."):
        return s
    else:
        return s + ".."
