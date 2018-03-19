from gallery import Gallery

__pragma__('alias', 'S', '$')

def on_scroll(percent):
    opac = 1 - 4 * percent
    S("#name").css('opacity', str(opac))

def start():
    hscroll = S.jInvertScroll(['.scroll'], {'onScroll': on_scroll})
    gallery = Gallery(S(".imgcontainer"))

    if S(window).width() <= 768:
        hscroll.destroy()
    elif S(window).width() <= 1280:
        gallery.draw(3)
    else:
        gallery.draw(2)

    def resize():
        # reinitialize() causes HUDGE performances issues by duplicating
        # jInvertScroll components, so we destroy it each time and recreate it
        # when needed
        hscroll.destroy()
        if 1280 < S(window).width():
            hscroll.reinitialize()
            gallery.draw(2)
        elif 768 < S(window).width():
            hscroll.reinitialize()
            gallery.draw(3)
        else:
            gallery.destroy()
    S(window).resize(resize)
