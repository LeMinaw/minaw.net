from utils import to_px


class Scroller:
    def __init__(self, select, width=None, height=None, speed=1, callback=None):
        self.select   = select
        self.speed    = speed
        self.callback = callback  # In [0, 1]
        self.target_width  = width
        self.target_height = height

        # Listen for the actual scroll event
        window.addEventListener('scroll', self.on_scroll)

    def draw(self):
        self.elems = [el for el in document.querySelectorAll(self.select)]
        self.max_width = max([el.scrollWidth for el in self.elems])

        # Use the longest elements width if no width or height is specified
        self.width  =  self.target_width  or self.max_width
        self.height = (self.target_height or self.max_width) // self.speed

        # Set the body to the selected height
        document.body.style.height = to_px(self.height)

    def on_scroll(self):
        y_offset = window.scrollY

        doc_height = document.body.clientHeight
        win_height = window.innerHeight
        win_width  = window.innerWidth

        diff = doc_height - win_height
        scroll_percent = 0
        if diff != 0:
            scroll_percent = y_offset / diff  # Current percentual position

        if self.callback is not None:  # BUG: callback is None, WTF
            self.callback(scroll_percent)  # Call the callback

        for el in self.elems:
            # delta_w = el.offsetWidth - win_width
            delta_w = el.scrollWidth - win_width
            if delta_w <= 0:
                delta_w = el.scrollWidth
            pos = -int(delta_w * scroll_percent)
            el.style.left = to_px(pos)

    def destroy(self):
        # Remove previously added inline styles
        document.body.removeAttribute('style')

        # Remove listener
        window.removeEventListener('scroll', self.on_scroll)
