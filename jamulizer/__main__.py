#!/usr/bin/env python
"""entrypoint for the midi analysis"""

import sys
import tkinter
from rtmidi.midiutil import open_midiinput
from jamulizer import visualizer, gui

PORT = sys.argv[1] if len(sys.argv) > 1 else None


def main():
    """main entrypoint"""

    # open midi port
    try:
        midi_in, port_name = open_midiinput(PORT)
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)

    # setup gui
    root = tkinter.Tk()
    app = gui.Application(root)

    # setup callback
    midi_in.set_callback(visualizer.MidiInputAnalysisHandler(port_name, app))

    # main loop
    try:
        app.mainloop()
    except KeyboardInterrupt:
        print('')
    finally:
        midi_in.close_port()
        del midi_in
        root.quit()


if __name__ == "__main__":
    main()
