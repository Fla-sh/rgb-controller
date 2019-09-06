import neopixel
from Programs.ProgramAbstract import ProgramAbstract


class ProgramOff(ProgramAbstract):
    def __init__(self, pixels: neopixel.NeoPixel, brightness):
        super().__init__(pixels, brightness)

    def run(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()
        print("Current color {}".format(color))