def urange(*args):
    """
    Generator that works similarly to the built-in 'range' function.
    Arguments must be integer - urange(stop), urange(start, stop[, step]).
    If the start argument is omitted it is default to 0.
    If the step argument is omitted it is default to 1. Step must not be 0, ValueError is raised in that case.
    """
    if len(args) == 0 or len(args) > 3:
        raise TypeError(f"urange expected from 1 to 3 arguments, got {len(args)}")
    current = 0 if len(args) == 1 else args[0]
    end = args[0] if len(args) == 1 else args[1]
    step = 1 if len(args) < 3 else args[2]
    for parameter in [current, end, step]:
        if not isinstance(parameter, int):
            raise TypeError(f"{str(type(parameter).__name__)} object cannot be interpreted as an integer")
    if step == 0:
        raise ValueError("urange() step argument must not be zero")
    end += (current - end) % step
    if (current - end) // step < 0:
        while current != end:
            yield current
            current += step
