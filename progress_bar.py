import math
from time import time


class ProgressBar:
    def __init__(self, label="", size=24, wall="", blank="░", fill="█"):
        self._size = size
        self._label = label
        self._wall = wall
        self._fill = fill
        self._blank = blank
        self._current_char_count = -1
        self.set_progression(0.0)
        self._t0 = time()

    def set_progression(self, progression: float):
        if progression == 1.0:
            char_count = self._size
        else:
            char_count = round(progression * (self._size - 1) + 0.5)

        if char_count != self._current_char_count:
            self._current_char_count = char_count

            bar = self._fill * char_count + self._blank * (self._size - char_count)
            print(f"\r{self._label}: {self._wall}{bar}{self._wall}", end="")

    def end(self, end="\n"):
        execution_time = time() - self._t0
        rounded_time = round(execution_time, 3 - int(math.floor(math.log10(execution_time))) - 1)
        print(f"\r{self._label}: {rounded_time} s", end=end)
