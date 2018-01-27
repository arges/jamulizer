#!/usr/bin/env python
"""Visualizer component"""

import time
from collections import Counter

from jamulizer.chords import Chords

class MidiInputAnalysisHandler(object):
    """Callback handler device for midi input"""

    def __init__(self, port):
        self.port = port
        self._wallclock = time.time()
        self.notes = set()
        self.notes_histogram = Counter()
        self.chords = Chords()

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime

        # only unpack messages that are 3-tuples
        try:
            event, note, _ = message
        except ValueError:
            return

        if event == 144:
            self.notes.add(note)
            self.notes_histogram[note%12] += 1
        elif event == 128:
            self.notes.remove(note)

        name = self.chords.name_chord(self.notes)

        key_notes = set(
            [note for note, _ in self.notes_histogram.most_common(7)]
        )
        key = self.chords.name_scale(key_notes)

        note_names = self.chords.name_notes(self.notes)

        if name:
            print(
                "chord: {}, scale: {}, notes: {}".format(name, key, note_names)
            )
