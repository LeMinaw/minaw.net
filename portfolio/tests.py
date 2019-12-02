from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from .utils import rgb_to_hex, hex_to_rgb
from .models import Work
            

class ColorConversionTestCase(TestCase):
    def setUp(self):
        pass
        
    def test_hex_to_rgb(self):
        cyan   = "00FFff"
        yellow = 'ffff00'
        self.assertEqual(hex_to_rgb(cyan), (0,   255, 255))
        self.assertEqual(hex_to_rgb(yellow), (255, 255, 0))

    def test_rgb_to_hex(self):
        magenta = (255, 0, 255)
        self.assertEqual(rgb_to_hex(magenta).lower(), "ff00ff")


class WorkColorPaletteTestCase(TestCase):
    def setUp(self):
        cover = SimpleUploadedFile('testimg.png', open('testimg.png', 'rb').read(), content_type='image/png')
        Work.objects.create(title="Work", slug="slugggy", cover=cover)

    def test_palette_decode(self):
        work = Work.objects.get(title="Work")
        work._palette = "ffff00;ffff00;00ff00"
        self.assertEqual(work.get_palette(), ((255, 255, 0), (255, 255, 0), (0, 255, 0)))



