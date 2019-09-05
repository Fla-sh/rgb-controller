import argparse
from AvailablePrograms import AvailablePrograms


class Parser:
    """
    Class parse arguments from console into argparse.Namespace object
    """
    def __init__(self, arguments):
        self.arguments: str
        self.parser: argparse.ArgumentParser

        self.arguments = arguments

    def parse(self):
        self.create_parser()
        self.add_arguments()
        return self.parser.parse_args(self.arguments)

    def add_arguments(self):
        self.parser.add_argument("program",
                                 choices=[program.name for program in AvailablePrograms],
                                 type=str,
                                 required=True,
                                 help="Program to run on Stripe")

        self.parser.add_argument("brightness",
                                 type=int,
                                 required=True,
                                 default=100,
                                 help="Brightness on LEDs, default 100")

    def create_parser(self):
        description = "Utility used to controll RGB Strip"
        epilog = "Created by Piotr Tylczynski"
        self.parser = argparse.ArgumentParser(description=description, epilog=epilog)
