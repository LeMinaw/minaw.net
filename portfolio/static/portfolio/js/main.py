from scroll  import Scroller
from gallery import Gallery

def desktop_width():
    return window.matchMedia("(min-width: 768px)").matches

def name_opac(percent):
    opac = 1 - 4 * percent
    document.getElementById("name").style.opacity = str(opac)

def start():
    gallery = Gallery(".imgcontainer")
    scroller = Scroller(".scroll", speed=15, callback=name_opac)

    def on_resize():
        if desktop_width():
            gallery.draw(2)
            scroller.draw()
        else:
            gallery.destroy()
            scroller.destroy()
    window.addEventListener("resize", on_resize)

    def on_load():
        if desktop_width():
            gallery.draw(2)
            scroller.draw()
    window.addEventListener("load", on_load)
