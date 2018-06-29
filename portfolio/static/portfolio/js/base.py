def go_back(fallback_url=None, timeout=200):
    window.history.back()

    if fallback_url is not None:
        def load_fallback():
            window.location.href = fallback_url
        setTimeout(load_fallback, timeout)


def start():
    def on_click(event):
        if not document.getElementById("work").contains(event.target):
            go_back("/")
    window.addEventListener('click', on_click)

    def on_keypress(event):
        if event.key == 'Escape':
            go_back("/")
    window.addEventListener('keypress', on_keypress)
