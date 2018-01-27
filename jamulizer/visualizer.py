#!/usr/bin/env python
"""Visualizer component"""

import time
from collections import Counter

from jamulizer import chords

NOTES = set()
NOTES_HISTOGRAM = Counter()

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
