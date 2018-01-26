#!/usr/bin/env python
"""Entrypoint for the midi analysis"""

import sys
import time
from collections import Counter

from rtmidi.midiutil import open_midiinput

import chords

NOTES = set()
NOTES_HISTOGRAM = Counter()
PORT = sys.argv[1] if len(sys.argv) > 1 else None

class MidiInputAnalysisHandler(object):
    """Callback handler device for midi input"""

    def __init__(self, port):
        self.port = port
        self._wallclock = time.time()

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime

        # only unpack messages that are 3-tuples
        try:
            event, note, _ = message
        except ValueError:
            return

        if event == 144:
            NOTES.add(note)
            NOTES_HISTOGRAM[note%12] += 1
        elif event == 128:
            NOTES.remove(note)

        name = chords.name_chord(NOTES)

        key_notes = set(
            [note for note, _ in NOTES_HISTOGRAM.most_common(7)]
        )
        key = chords.name_scale(key_notes)

        note_names = chords.name_notes(NOTES)

        if name:
            print(
                "chord: {}, scale: {}, notes: {}".format(name, key, note_names)
            )

try:
    MIDIIN, PORT_NAME = open_midiinput(PORT)
except (EOFError, KeyboardInterrupt):
    sys.exit()

MIDIIN.set_callback(MidiInputAnalysisHandler(PORT_NAME))

print("Press Control-C to exit.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('')
finally:
    MIDIIN.close_port()
    del MIDIIN
