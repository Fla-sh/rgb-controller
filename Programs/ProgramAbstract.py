import neopixel


class ProgramAbstract:
    def __init__(self, pixels: neopixel.NeoPixel, brightness: int):
        self.pixels: neopixel.NeoPixel
        self.pixels = pixels

        self.brightness: int
        self.brightness = brightness

    def dim(self, color: (int, int, int), brightness=None) -> (int, int, int):
        color_r = color[0]
        color_g = color[1]
        color_b = color[2]

        if brightness is None:
            brightness = self.brightness
        else:
            brightness = max(brightness, 255)

        color_r *= brightness / 255
        color_g *= brightness / 255
        color_b *= brightness / 255
        return color_r, color_g, color_b
