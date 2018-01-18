#!/usr/bin/env python

import sys
import time
from collections import Counter

from rtmidi.midiutil import open_midiinput

import chords

notes = set()
notes_histogram = Counter()

class MidiInputAnalysisHandler(object):
    def __init__(self, port):
        self.port = port
        self._wallclock = time.time()

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime

        event, note, _ = message
        if event == 144:
            notes.add(note)
            notes_histogram[note%12] += 1
        elif event == 128:
            notes.remove(note)

        name = chords.name_chord(notes)

        key_notes = set([ note for note, _ in notes_histogram.most_common(7) ])
        key = chords.name_scale(key_notes)

        note_names = chords.name_notes(notes)

        if name:
            print("chord: {}, scale: {}, notes: {}".format(name, key, note_names))


port = sys.argv[1] if len(sys.argv) > 1 else None

try:
    midiin, port_name = open_midiinput(port)
except (EOFError, KeyboardInterrupt):
    sys.exit()

midiin.set_callback(MidiInputAnalysisHandler(port_name))

print("Press Control-C to exit.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('')
finally:
    midiin.close_port()
    del midiin
