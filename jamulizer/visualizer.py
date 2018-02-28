"""Visualizer component"""

import time
from collections import Counter

from jamulizer.analysis import Analysis

class MidiInputAnalysisHandler(object):
    """Callback handler device for midi input"""

    def __init__(self, port, app):
        self.port = port
        self._wallclock = time.time()
        self.notes = set()
        self.notes_histogram = Counter()
        self.app = app

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime

        # only unpack messages that are 3-tuples
        try:
            event, note, _ = message
        except ValueError:
            return

        # parse midi events
        if event == 144:
            self.notes.add(note)
            self.notes_histogram[note%12] += 1
        elif event == 128:
            self.notes.remove(note)

        # get chord name
        name = Analysis.name_chord(self.notes)

        # get key name
        key_notes = set(
            [note for note, _ in self.notes_histogram.most_common(7)]
        )
        key = Analysis.name_scale(key_notes)

        # get notes and bass note
        note_names = Analysis.name_notes(self.notes)
        bass_note_name = Analysis.name_bass_note(self.notes)

        if name:
            print(
                "chord: {}, scale: {}, notes: {}, bass: {}".format(name, key, note_names, bass_note_name)
            )
            self.app.set_label(name, key, note_names, bass_note_name)
