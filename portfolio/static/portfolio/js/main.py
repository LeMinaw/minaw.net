from scroll  import Scroller
from gallery import Gallery

__pragma__('alias', 'S', '$')

def name_opac(percent):
    opac = 1 - 4 * percent
    S("#name").css('opacity', str(opac))

def start():
    scroller = Scroller(".scroll", callback=name_opac)
    gallery = Gallery(S(".imgcontainer"))

    if S(window).width() > 768:
        scroller.draw()

    def on_resize():
        if S(window).width() > 768:
            scroller.draw()
            gallery.draw(2)
        else:
            scroller.destroy()
            gallery.destroy()
    window.addEventListener("resize", on_resize)

    def on_load():
        if S(window).width() > 768:
            gallery.draw(2)
    window.addEventListener("load", on_load)
