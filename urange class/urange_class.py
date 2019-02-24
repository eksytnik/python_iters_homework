# This code was made just to practice magic methods.
# Basically it copies with a pure Python almost all the built-in range can do but does it slower c:
# Can't handle len() for integers above sys.maxsize.

import collections.abc


class urange(collections.abc.Sequence):
    """
    Class that works similarly to the built-in 'range' function.
    Arguments must be integer (or any object that implements the __index__ special method).

    urange(stop), urange(start, stop[, step])

    If the start argument is omitted it defaults to 0.
    If the step argument is omitted it defaults to 1. If the step is 0, ValueError is raised.

    Allows indexing and slicing. Negative indexes are supported, they are interpreted as
    indexing from the end.

    Allows equality comparison (== or !=) based on the sequence. Equal objects can have
    different start, stop and step attributes, for example:
    range(0) == range(42, 1, 1)
    range(1, 3, 3) == range(1, 4, 3)
    Other comparisons can't be performed.
    """

    def __init__(self, *args):
        if len(args) == 0 or len(args) > 3:
            raise TypeError(f"urange expected from 1 to 3 arguments, got {len(args)}")
        self.start = 0 if len(args) == 1 else args[0]
        self.end = args[0] if len(args) == 1 else args[1]
        self.step = 1 if len(args) < 3 else args[2]
        for i in [self.start, self.end, self.step]:
            if not hasattr(i, '__index__'):
                raise TypeError("'%s' object cannot be interpreted as an integer" % type(i).__name__)
        if self.step == 0:
            raise ValueError("urange() arg 3 must not be zero")
        self.stop = self.end + (self.start - self.end) % self.step

    def __eq__(self, other):
        if isinstance(other, urange):
            if len(self) == len(other):
                for i, j in zip(self, other):
                    if i != j:
                        return False
                else:
                    return True
        return False

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, end, step = self._process_indexes(index)
            if not end:
                return urange(0, 0)
            return urange(start, end, step)
        else:
            index = self._process_indexes(index)
            if index:
                return self.start + self.step * index
            else:
                raise IndexError("index out of range")

    def __hash__(self):
        if (self.start - self.stop) // self.step >= 0:
            return hash(0)
        if (self.stop - self.start) // self.step <= 1:
            return hash(self.start)
        return hash((self.start, self.stop, self.step))

    def __iter__(self):
        return urangeIter(self.start, self.stop, self.step)

    def __len__(self):
        return max((self.stop - self.start) // self.step, 0)

    def __reversed__(self):
        start_sign = -1 if (self.start <= 0 or self.step > 0) else 1
        return urange(self.stop - self.step, self.start + start_sign, -self.step)

    def __repr__(self):
        step_info = f", {self.step}" if self.step != 1 else ""
        return str(f"urange({self.start}, {self.end}{step_info})")

    def __str__(self):
        step_info = f", {self.step}" if self.step != 1 else ""
        return str(f"urange({self.start}, {self.end}{step_info})")

    def _process_indexes(self, index):
        last_range_ind = (self.stop - self.start) // self.step
        if isinstance(index, slice):
            if index.start:
                index_start = index.start if index.start > 0 else index.start + last_range_ind
            else:
                index_start = 0

            if index.stop:
                index_stop = index.stop if index.stop > 0 else index.stop + last_range_ind
            else:
                index_stop = last_range_ind

            if index_start < 0 or index_stop < 0:
                return None, None, None

            index_step = index.step * self.step if index.step else self.step

            return (self.start + self.step * index_start,
                    self.start + self.step * min(index_stop, last_range_ind),
                    index_step)
        else:
            if index < 0:
                index = index + last_range_ind
            if index <= last_range_ind - 1:
                return index
            else:
                return None

    def index(self, value):
        if (value - self.start) % self.step == 0 and \
                (self.start <= value < self.end) or (self.start >= value > self.end):
            return (value - self.start) // self.step
        else:
            raise ValueError(f"{value} is not in range")

    def count(self, value):
        if (value - self.start) % self.step == 0 and \
                (self.start <= value < self.end) or (self.start >= value > self.end):
            return 1
        else:
            return 0


class urangeIter:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.start - self.stop) // self.step < 0:
            while self.start != self.stop:
                self.current = self.start
                self.start += self.step
                return self.current
        raise StopIteration
