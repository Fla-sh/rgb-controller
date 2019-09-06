from AvailablePrograms import AvailablePrograms
import board
from neopixel import NeoPixel
from Programs.ProgramWhite import ProgramWhite
from Programs.ProgramBlue import ProgramBlue
from Programs.ProgramRed import ProgramRed
from Programs.ProgramYellow import ProgramYellow
from Programs.ProgramGreen import ProgramGreen


class RGBController:
    def __init__(self):
        self.program: AvailablePrograms
        self.program = None

        self.pixels: NeoPixel
        self.pixels = NeoPixel(pin=board.D18,
                               n=300,
                               auto_write=False,
                               brightness=1)

        self.brightness: float
        self.brightness = None

    def run(self):
        if self.program == AvailablePrograms.white.name:
            ProgramWhite(self.pixels, self.brightness).run()
        elif self.program == AvailablePrograms.red.name:
            ProgramRed(self.pixels, self.brightness).run()
        elif self.program == AvailablePrograms.blue.name:
            ProgramBlue(self.pixels, self.brightness).run()
        elif self.program == AvailablePrograms.green.name:
            ProgramYellow(self.pixels, self.brightness).run()
        elif self.program == AvailablePrograms.yellow.name:
            ProgramYellow(self.pixels, self.brightness).run()
        elif self.program == AvailablePrograms.green.name:
            ProgramGreen(self.pixels, self.brightness)
        else:
            print("Program {} unknown".format(self.program))

    def set_program(self, name: AvailablePrograms):
        self.program = name

    def set_brightness(self, value: int):
        self.brightness = value
