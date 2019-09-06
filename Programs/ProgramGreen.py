import neopixel
from Programs.ProgramAbstract import ProgramAbstract


class ProgramGreen(ProgramAbstract):
    def __init__(self, pixels: neopixel.NeoPixel, brightness):
        super().__init__(pixels, brightness)

    def run(self):
        color = self.dim((0, 255, 0))
        self.pixels.fill(color)
        self.pixels.show()
        print("Current color {}".format(color))

