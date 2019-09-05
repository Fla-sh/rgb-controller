import neopixel


class ProgramWhite():
    def __init__(self, pixels: [neopixel.NeoPixel]):
        self.pixels: neopixel.NeoPixel

        self.pixels = pixels

    def run(self):
        self.pixels.fill((0,255,0))
        self.pixels.show()