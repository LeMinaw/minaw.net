def rgb_to_hex(rgb):
    return "{:02x}{:02x}{:02x}".format(*rgb)

def hex_to_rgb(hexcode):
    return (
        int(hexcode[0:2], 16),
        int(hexcode[2:4], 16),
        int(hexcode[4:6], 16),
    )

def alpha(color, alpha):
    r, g, b = color[:3]
    return f'rgba({r}, {g}, {b}, {alpha})'