"""
chord analysis library
"""

NOTES = {
    0: 'C',
    1: 'C#/Db',
    2: 'D',
    3: 'D#/Eb',
    4: 'E',
    5: 'F',
    6: 'F#/Gb',
    7: 'G',
    8: 'G#/Ab',
    9: 'A',
    10: 'A#/Bb',
    11: 'B'
}

SCALES = {
    frozenset([0, 2, 4, 5, 7, 9, 11]): 'major',
    frozenset([0, 2, 4, 3, 7, 9, 11]): 'minor',
}

CHORDS = {
    frozenset([0, 2, 7]): ['sus2', 'suspended second'],
    frozenset([0, 5, 7]): ['sus4', 'suspended fourth'],
    frozenset([0, 4, 7]): ['maj', 'major'],
    frozenset([0, 3, 7]): ['min', 'minor'],
    frozenset([0, 3, 6]): ['dim', 'diminished'],
    frozenset([0, 4, 8]): ['aug', 'augmented'],
    frozenset([0, 3, 6, 9]): ['dim7', 'diminished seventh'],
    frozenset([0, 3, 6, 10]): ['m7b5', 'half-diminished seventh'],
    frozenset([0, 3, 7, 10]): ['min7', 'minor seventh'],
    frozenset([0, 3, 7, 11]): ['minmaj7', 'minor major seventh'],
    frozenset([0, 4, 7, 10]): ['7', 'dominant seventh'],
    frozenset([0, 4, 7, 11]): ['maj7', 'major seventh'],
    frozenset([0, 4, 8, 10]): ['aug7', 'augmented seventh'],
    frozenset([0, 4, 8, 11]): ['maj7+5', 'augmented major seventh'],
    frozenset([0, 4, 8, 10, 2]): ['9', 'dominant ninth'],
    frozenset([0, 4, 8, 10, 2, 5]): ['11', 'dominant eleventh'],
    frozenset([0, 4, 8, 10, 2, 5, 9]): ['13', 'dominant thirteenth'],
}


def name_scale(input_notes):
    for key in NOTES:
        shift_scale = frozenset([(note-key)%12 for note in input_notes])
        try:
            return NOTES[key] + " " + SCALES[shift_scale]
        except KeyError:
            pass


def name_note(note):
    return NOTES[note % 12]


def name_notes(input_notes):
    return [name_note(note) for note in input_notes]


def name_chord(input_notes):
    for key in NOTES:
        note_set = frozenset([((note%12)-key)%12 for note in input_notes])
        try:
            return NOTES[key] + " " + CHORDS[note_set][0]
        except KeyError:
            pass
