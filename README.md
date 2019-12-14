# RGB Controller
## Destination
Part of IoT project. This module allow Rasberry Pi to controll RGB Strip. All needed modules are in `requirements.txt` file. Users need to keep in mind, that RGB leds have huge power consumption. Displaying white color on 300 leds takes over 100W.

## Project
- **RGBController** - interface to comunicate with module. In run function takes program to execute
- **AvailablePrograms** - contains enum with all available programs. Programs are in `programs` directory
- **Parser** - contains argparser for consol usage of module
- **ProgramController** - unused so far

## Usage
Comand line usage:
`sudo main.py program brightness`

In code usage:
```python
        controller = RGBController()
        controller.set_brightness(*brightness: int*)
        controller.set_program(*program: AvailablePrograms*)
        controller.run()
```

## Current programs
- white
- yellow
- blue
- red
- green
- off
