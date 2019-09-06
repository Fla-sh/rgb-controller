import neopixel


class ProgramYellow():
    def __init__(self, pixels: neopixel.NeoPixel, brightness):
        super().__init__(pixels, brightness)

    def run(self):
        color = self.dim((255, 255, 0))
        self.pixels.fill(color)
        self.pixels.show()