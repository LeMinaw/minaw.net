from utils import *

class Gallery:
    """A row-oriented gallery for showcasing nice pics."""

    def __init__(self, selector):
        """<selector> must be a css selector that matches each pic of the
        Gallery."""

        self.pics = [pic for pic in document.querySelectorAll(selector)]
        self.parent = self.pics[0].parentNode
        self.init_widths = None # Will be populated by first call of draw()


    def reset_widths(self):
        """Resets all widths to initial values."""

        for pic, w in zip(self.pics, self.init_widths):
            pic.style.width = to_px(w)


    def rows_widths(self):
        """Computes the total width for each row of the Gallery."""

        return [sum([max(pic.offsetWidth, 200) for pic in row])
                for row in self.rows]


    def draw(self, rows_nb):
        """Draws the gallery by setting pics widths."""

        if self.init_widths is None: # Saves initial pics width on first call
            self.init_widths = [pic.offsetWidth for pic in self.pics]

        self.reset_widths()

        # Build rows array
        self.rows = [[] for i in range(rows_nb)]

        # Compute rows
        for pic in self.pics:
            widths = self.rows_widths()
            min_index = widths.index(min(widths))
            self.rows[min_index].append(pic)

        # Compute widths
        widths = self.rows_widths()
        avg_width = avg(widths)
        for row, width in zip(self.rows, widths):
            ratio = avg_width / width
            for pic in row:
                w = max(pic.offsetWidth, 200)
                w *= ratio
                pic.style.width = to_px(w)

        # Display rows
        empty(self.parent)
        for row in self.rows:
            for pic in row:
                self.parent.appendChild(pic)
            br = document.createElement("br")
            self.parent.appendChild(br)

        # Set container width
        self.parent.style.width = to_px(avg_width + 1) # Avoids rounding problems
        self.parent.parentNode.style.width = to_px(avg_width + 12 + 1)

    def destroy(self):
        self.reset_widths()

        empty(self.parent)
        for pic in self.pics:
            self.parent.appendChild(pic)
