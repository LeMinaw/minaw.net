def total_width(elems):
    """Cumulated width of <elems>."""
    return sum([el.offsetWidth for el in elems])


def empty(elem):
    """Removes all child nodes of <elem>."""
    while elem.firstChild is not None:
        elem.removeChild(elem.firstChild)


def avg(iterable):
    """Average value of <iterable>."""
    return sum(iterable) / len(iterable)


def from_px(val):
    """Read int from px string value: '45px' -> 45"""
    return int(val[:-2])


def to_px(val):
    """Returns px string value from int: 45 -> '45px'"""
    return f"{val}px"
