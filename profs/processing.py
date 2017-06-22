#-*- coding: utf-8 -*-

import xml.dom.minidom as dom
from random import choice

def createThanks():
    messages = ["Le monde est un peu meilleur maintenant.",
                "En récompense, prends ce cookie magic bogoss.",
                "Bisou sur la joue <3",
                "Ça nous aide à sauver les lamas du Nicaragua.",
                "C'est bien aimable de ta part."]
    return choice(messages)


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
