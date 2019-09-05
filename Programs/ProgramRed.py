import neopixel


class ProgramRed():
    def __init__(self, pixels: neopixel.NeoPixel):
        self.pixels: neopixel.NeoPixel

        self.pixels = pixels

    def run(self):
        self.pixels.fill((255,0,0))
        self.pixels.show()