class UrangeIter:
    """
    Iterator class that works similarly to the built-in 'range' function.
    Arguments must be integer - UrangeIter(stop), UrangeIter(start, stop[, step]).
    If the start argument is omitted it is default to 0.
    If the step argument is omitted it is default to 1. Step must not be 0, ValueError is raised in that case.
    """

    def __init__(self, *args):
        if len(args) == 0 or len(args) > 3:
            raise TypeError(f"urange expected from 1 to 3 arguments, got {len(args)}")
        self.start = 0 if len(args) == 1 else args[0]
        self.end = args[0] if len(args) == 1 else args[1]
        self.step = 1 if len(args) < 3 else args[2]
        for i in [self.start, self.end, self.step]:
            if not isinstance(i, int):
                raise TypeError(f"{str(type(i).__name__)} object cannot be interpreted as an integer")
        if self.step == 0:
            raise ValueError("urange() arg 3 must not be zero")
        self.stop = self.end + (self.start - self.end) % self.step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.start - self.stop) // self.step < 0:
            while self.start != self.stop:
                self.current = self.start
                self.start += self.step
                return self.current
        raise StopIteration
