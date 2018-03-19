__pragma__('alias', 'S', '$')

def total_width(elems):
    """Cumulated width of `elems`, including margins."""
    return sum([S(el).outerWidth(True) for el in elems])

def total_blank(elems):
    """Cumulated width difference between outer and inner widths of `elems`."""
    return total_width(elems) - sum([S(el).innerWidth() for el in elems])

def empty(elem):
    """Removes all child nodes of `elem`."""
    while elem.firstChild is not None:
        elem.removeChild(elem.firstChild)

def avg(iterable):
    """Average value of `iterable` members."""
    return sum(iterable) / len(iterable)

def parse_px(val):
    """Parse px string value: '45px' -> 45"""
    return int(val[:-2])

class Gallery:
    def __init__(self, pics):
        self.pics = pics
        self.parent = pics[0].parentNode
        self.init_widths = [S(pic).css("width") for pic in pics]

    def reset_widths(self):
        for pic, w in zip(self.pics, self.init_widths):
            S(pic).css("width", w)

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
                w = parse_px(S(pic).css("width"))
                w *= ratio
                S(pic).css("width", w)

        # Display rows
        empty(self.parent)
        for row in self.rows:
            for pic in row:
                S(self.parent).append(pic)
            S(self.parent).append("<br/>")

    def destroy(self):
        self.reset_widths()

        empty(self.parent)
        for pic in self.pics:
            S(self.parent).append(pic)
