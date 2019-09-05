import neopixel


class ProgramBlue():
    def __init__(self, pixels: neopixel.NeoPixel):
        self.pixels: neopixel.NeoPixel

        self.pixels = pixels

    def run(self):
        self.pixels.fill((0,0,255))
        self.pixels.show()