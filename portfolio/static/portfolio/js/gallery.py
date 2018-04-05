__pragma__('alias', 'S', '$')

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

class Gallery:
    def __init__(self, pics):
        self.pics = pics
        self.parent = pics[0].parentNode
        self.init_widths = [pic.offsetWidth for pic in pics]

    def reset_widths(self):
        for pic, w in zip(self.pics, self.init_widths):
            pic.style.width = to_px(w)

    def draw(self, rows_nb):
        self.reset_widths()

        # Build rows array
        self.rows = [[] for i in range(rows_nb)]

        # Compute rows
        for pic in self.pics:
            widths = [total_width(row) for row in self.rows]
            min_index = widths.index(min(widths))
            self.rows[min_index].append(pic)

        # Compute widths
        widths = [total_width(row) for row in self.rows]
        avg_width = avg(widths)
        for row, width in zip(self.rows, widths):
            ratio = avg_width / width
            for pic in row:
                w = from_px(S(pic).css("width"))
                w *= ratio
                pic.style.width = to_px(w)

        # Display rows
        empty(self.parent)
        for row in self.rows:
            for pic in row:
                S(self.parent).append(pic)
            S(self.parent).append("<br/>")

        # Set container width
        self.parent.style.width = to_px(avg_width + 1) # Avoids rounding problems
        print(to_px(avg_width))

    def destroy(self):
        self.reset_widths()

        empty(self.parent)
        for pic in self.pics:
            S(self.parent).append(pic)
