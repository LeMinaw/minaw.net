from PIL            import Image, ImageDraw, ImageFilter, ImageEnhance
from random         import random, randint, randrange, choice, seed
from colorsys       import hsv_to_rgb
from urllib.request import urlopen
from io             import BytesIO
import xml.dom.minidom as dom
import re

def openImageUrl(url):
    """Returns an image object from the World Wide Web."""
    file = BytesIO(urlopen(url).read())
    return Image.open(file)

def pickPeople():
    """Returns a random image of a quite fancy people."""
    page = urlopen("http://www.news-people.fr/liste-people/")
    reg = re.compile(r'(\/photos\/\S+\.jpg)', re.M)
    pageCode = page.read().decode("ISO-8859-1")
    urls = reg.findall(pageCode)
    url = "http://www.news-people.fr" + choice(urls)
    return openImageUrl(url)

def linInterp(x, xMin=0, xMax=1, yMin=0, yMax=1):
    """Simple linear interpolation.
    Maps a value from one range to another."""
    return int((x - xMin) * (yMax - yMin) / (xMax - xMin) + yMin)

def randRGB():
    """Returns a random RGB color."""
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def randRGBGrey(min=0, max=255):
    """Returns a random RGB grey in the (min, max) range."""
    chanData = randint(min, max)
    return (chanData, chanData, chanData)

def randNiceRGB():
    """Returns a nice, saturated RGB color."""
    return hsv_to_rgb(randint(0, 360), randrange(.5, 1, .01), randrange(.5, 1, .01))

def randomTranspose(image):
    """Returns a randomly transposed version of an image."""
    if random() > .5:
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    if random() > .5:
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
    rot = random()
    if rot > .75:
        image = image.transpose(Image.ROTATE_90)
    elif rot > .5:
        image = image.transpose(Image.ROTATE_180)
    elif rot > .25:
        image = image.transpose(Image.ROTATE_270)
    return image

def multAplha(image, factor):
    """Multiplicates the alpha channel of image by factor."""
    channels = list(image.split())
    channels[3] = channels[3].point(lambda x: x * factor)
    return Image.merge(image.mode, channels)

def shadow(image, radius=5):
    """Adds a shadow to an image."""
    shadowImage = Image.new('RGB', image.size, (0, 0, 0))
    alphaImage = image.split()[3]
    alphaImage = alphaImage.filter(ImageFilter.GaussianBlur(radius=radius))
    shadowImage = Image.merge('RGBA', (*shadowImage.split(), alphaImage))
    return Image.alpha_composite(shadowImage, image)

def genAvatar(uid, width=128):
    """Generated a cool procedural avatar unique to uid."""
    steps = 16
    seed(uid)
    size = (width, width)
    renderSize = (width*2, width*2)
    image = Image.new('RGBA', renderSize, randRGBGrey())
    if uid == "jeanmarielepen" or uid == "6677f7953de478433b8814f0b9b4a5ff":
        image = openImageUrl("http://www.minaw.net/static/avatar/img/lepen.jpg").convert('RGBA').resize(renderSize, Image.BICUBIC)
    # else:
    #     image = pickPeople().convert('L').convert('RGBA').resize(renderSize, Image.BICUBIC)
    colorStep = randint(steps/2, steps-1)
    for step in range(steps):
        layer = Image.new('RGBA', renderSize, (0, 0, 0, 0))
        draw = ImageDraw.Draw(layer)
        if step == colorStep:
            draw.polygon([(0, 0), (renderSize[1], 0), (0, linInterp(random(), 0, 1, renderSize[0]//4, renderSize[0]//2))], randRGB())
        else:
            draw.polygon([(0, 0), (renderSize[1], 0), (0, linInterp(random(), 0, 1, renderSize[0]//16, renderSize[0]//2))], randRGBGrey())
            layer = multAplha(layer, random())
        layer = randomTranspose(layer)
        layer = shadow(layer)
        image = Image.alpha_composite(image, layer)

    return image.resize(size, Image.BICUBIC)


class Taconite(dom.Document):
    """Useful class for generating XML Taconite JQuery content.

    Usage :
    t = Taconite()
    t.append("#toto","<label>test</label>")
    t.remove("#tutu")
    t.js('alert("hello world");')
    t.toggleClass('blue','body')
    t.css("body","background-color","white")
    [...]
    print t.toprettyxml()"""

    def __init__(self):
        dom.Document.__init__(self)
        taconite = self.createElement("taconite")
        self.appendChild(taconite)

    def __str__(self):
        return self.toxml()

    def camelizeCssProperty(self, property):
        words = property.split('-')
        camelized = words[0].lower()
        for word in words[1:] :
            camelized = camelized + word[0].upper() + word[1:]
        return camelized

    def js(self, script):
        command = self.createElement("eval")
        js = self.createTextNode(script)
        command.appendChild(js)
        self.childNodes[0].appendChild(command)

    def changeContentCommand(self, method, selector, content):
        html_dom = dom.parseString(content)
        command = self.createElement(method)
        command.setAttribute("select", selector)
        command.appendChild(html_dom.childNodes[0])
        self.childNodes[0].appendChild(command)

    def changeStateCommand(self, action, selector):
        command = self.createElement(action)
        command.setAttribute("select", selector)
        self.childNodes[0].appendChild(command)

    def CssCommand(self, action, css_class, selector):
        command1 = self.createElement(action)
        command1.setAttribute("select", selector)
        command1.setAttribute("arg1", css_class)
        command2 = self.createElement(action)
        command2.setAttribute("select", selector)
        command2.setAttribute("value", css_class)
        self.childNodes[0].appendChild(command1)
        self.childNodes[0].appendChild(command2)

    def addClass(self, css_class, selector):
        self.CssCommand("addClass", css_class, selector)

    def removeClass(self, css_class, selector):
        self.CssCommand("remove", css_class, selector)

    def toggleClass(self, css_class, selector):
        self.CssCommand("toggleClass", css_class, selector)

    def append(self, selector, content):
        self.changeContentCommand("append", selector, content)

    def prepend(self, selector, content):
        self.changeContentCommand("prepend", selector, content)

    def before(self, selector, content):
        self.changeContentCommand("before", selector, content)

    def after(self,selector,content):
        self.changeContentCommand("after", selector, content)

    def wrap(self, selector, content):
        self.changeContentCommand("wrap", selector, content)

    def replace(self, selector, content):
        self.changeContentCommand("replace", selector, content)

    def replaceContent(self, selector, content):
        self.changeContentCommand("replaceContent", selector, content)

    def remove(self, selector):
        self.changeStateCommand("remove", selector)

    def show(self, selector):
        self.changeStateCommand("show", selector)

    def hide(self, selector):
        self.changeStateCommand("hide", selector)

    def removeContent(self, selector):
        self.changeStateCommand("empty", selector)

    def css(self, selector, property, value):
        command = self.createElement("css")
        command.setAttribute("select", selector)
        command.setAttribute("name", self.camelizeCssProperty(property))
        command.setAttribute("value", value)
        self.childNodes[0].appendChild(command)

    def disable(self, selector, value):
        if value:
            self.js("$('" + selector + "').prop('disabled', true);")
        else:
            self.js("$('" + selector + "').prop('disabled', false);")
