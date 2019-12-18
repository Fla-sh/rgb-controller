from AvailablePrograms import AvailablePrograms
import board
from neopixel import NeoPixel

from Programs.ProgramMulticolor import ProgramMulticolor
from Programs.ProgramWhite import ProgramWhite
from Programs.ProgramBlue import ProgramBlue
from Programs.ProgramRed import ProgramRed
from Programs.ProgramYellow import ProgramYellow
from Programs.ProgramGreen import ProgramGreen


class RGBController:
    """
    Controls which program ought to be executed - console case
    Color control is used in case of programatic execution
    """
    def __init__(self):
        self.program: AvailablePrograms = None
        self.color: (int,int,int) = None
        self.pixels: NeoPixel = NeoPixel(  pin=board.D18,
                                           n=300,
                                           auto_write=False,
                                           brightness=1
                                         )
        self.brightness: int = None

    def run(self):
        if self.color is not None:
            ProgramMulticolor(
                self.pixels,
                self.color.R,
                self.color.G,
                self.color.B,
                self.brightness).run()
        elif self.program is not None:
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
        else:
            print("Nor color nor program was set")

    def set_program(self, name: AvailablePrograms):
        self.program = name

    def set_color(self, R: int, G: int, B: int):
        self.color = (R, G, B)

    def set_brightness(self, value: int):
        self.brightness = value
