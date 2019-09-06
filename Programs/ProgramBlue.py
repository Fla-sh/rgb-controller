import neopixel
from Programs.ProgramAbstract import ProgramAbstract


class ProgramBlue(ProgramAbstract):
    def __init__(self, pixels: neopixel.NeoPixel, brightness):
        super().__init__(pixels, brightness)

    def run(self):
        color = self.dim((0, 0, 255))
        self.pixels.fill(color)
        self.pixels.show()
