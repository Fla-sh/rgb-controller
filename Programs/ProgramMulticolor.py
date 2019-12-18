import neopixel
from Programs.ProgramAbstract import ProgramAbstract


class ProgramMulticolor(ProgramAbstract):
    def __init__(self, pixels: neopixel.NeoPixel, R, G, B, brightness):
        super().__init__(pixels, brightness)
        self.R: int = R
        self.G: int = G
        self.B: int = B

    def run(self):
        color = self.dim(
            (self.R,
             self.G,
             self.B))
        self.pixels.fill(color)
        self.pixels.show()
        print("Current color {}".format(color))
