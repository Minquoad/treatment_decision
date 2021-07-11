import math
from time import time


class ProgressBar:
    def __init__(self, label=None, size=24, wall="", blank="░", fill="█"):
        self._size = size
        self._label = label
        self._wall = wall
        self._fill = fill
        self._blank = blank
        self._current_fill_count = -1
        self.set_progression(0.0)
        self._t0 = time()

    def set_progression(self, progression: float):
        if progression == 1.0:
            fill_count = self._size
        else:
            fill_count = round(progression * (self._size - 1) + 0.5)

        if fill_count != self._current_fill_count:
            self._current_fill_count = fill_count

            string = "\r"
            if self._label is not None:
                string += self._label + ": "
            string += self._wall
            string += self._fill * fill_count
            string += self._blank * (self._size - fill_count)
            string += self._wall
            print(string, end="")

    def end(self, end="\n"):
        execution_time = time() - self._t0
        rounded_time = round(execution_time, 3 - int(math.floor(math.log10(execution_time))) - 1)
        string = "\r"
        string += self._label if self._label is not None else "loading time"
        string += ": " + str(rounded_time) + " s"
        print(string, end=end)
