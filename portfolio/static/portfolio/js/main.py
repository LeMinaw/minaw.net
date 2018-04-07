from gallery import Gallery

__pragma__('alias', 'S', '$')

def on_scroll(percent):
    opac = 1 - 4 * percent
    S("#name").css('opacity', str(opac))

def start():
    gallery = Gallery(S(".imgcontainer"))
    hscroll = S.jInvertScroll(['.scroll'], {
        'width':  'auto',
        'height': 'auto',
        'onScroll': on_scroll
    })

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
            gallery.draw(2)
            hscroll.reinitialize()
        elif 768 < S(window).width():
            gallery.draw(3)
            hscroll.reinitialize()
        else:
            gallery.destroy()
    S(window).resize(resize)
