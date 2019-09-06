import neopixel
from Programs.ProgramAbstract import ProgramAbstract


class ProgramRed(ProgramAbstract):
    def __init__(self, pixels: neopixel.NeoPixel, brightness):
        super().__init__(pixels, brightness)

    def run(self):
        color = self.dim((255, 0, 0))
        self.pixels.fill(color)
        self.pixels.show()
