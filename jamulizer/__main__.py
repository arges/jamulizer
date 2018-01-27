#!/usr/bin/env python
"""entrypoint for the midi analysis"""

import sys
import time

from rtmidi.midiutil import open_midiinput

from jamulizer import visualizer

PORT = sys.argv[1] if len(sys.argv) > 1 else None

def main():
    """main entrypoint"""
    try:
        midi_in, port_name = open_midiinput(PORT)
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)

    midi_in.set_callback(visualizer.MidiInputAnalysisHandler(port_name))

    print("Press Control-C to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('')
    finally:
        midi_in.close_port()
        del midi_in


if __name__ == "__main__":
    main()
