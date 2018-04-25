from scroll  import Scroller
from gallery import Gallery

def desktop_width():
    return window.matchMedia("(min-width: 768px)").matches

def name_opac(percent):
    opac = 1 - 4 * percent
    document.getElementById("name").style.opacity = str(opac)

def start():
    scroller = Scroller(".scroll", callback=name_opac)
    gallery = Gallery(".imgcontainer")
    if desktop_width():
        scroller.draw()

    def on_resize():
        if desktop_width():
            scroller.draw()
            gallery.draw(2)
        else:
            scroller.destroy()
            gallery.destroy()
    window.addEventListener("resize", on_resize)

    def on_load():
        if desktop_width():
            gallery.draw(2)
    window.addEventListener("load", on_load)
