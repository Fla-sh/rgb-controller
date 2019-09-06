import sys
import typing
import parser
import argparse
from RGBController import RGBController


class Main:
    def __init__(self, arguments: []):
        self.arguments: str
        self.arguments = arguments

        self.namespace: argparse.Namespace
        self.namespace = parser.Parser(self.arguments).parse()

        self.controller: RGBController
        self.controller = RGBController()

    def run(self):
        # print(self.namespace)
        self.controller.set_brightness(
            self.namespace.brightness
        )
        self.controller.set_program(
            self.namespace.program
        )
        self.controller.run()


if __name__ == "__main__":
    main = Main(sys.argv)
    main.run()
