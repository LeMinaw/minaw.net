__pragma__('alias', 'S', '$')

from utils import *

class Gallery:
    def __init__(self, pics):
        self.pics = pics
        self.parent = pics[0].parentNode
        self.init_widths = None # Will be populated by first call of draw()

    def reset_widths(self):
        for pic, w in zip(self.pics, self.init_widths):
            pic.style.width = to_px(w)

    def draw(self, rows_nb):
        if self.init_widths is None: # Saves initial pics width on first call
            self.init_widths = [pic.offsetWidth for pic in self.pics]

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
        self.parent.parentNode.style.width = to_px(avg_width + 13)

    def destroy(self):
        self.reset_widths()

        empty(self.parent)
        for pic in self.pics:
            S(self.parent).append(pic)
