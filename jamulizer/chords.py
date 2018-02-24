"""
chord analysis library
"""

class Chords:

    """ names of notes """
    notes = {
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

    """ scale intervals """
    scales = {
        (0, 2, 4, 5, 7, 9, 11): 'major',
        (0, 2, 3, 5, 7, 8, 10): 'minor'
    }

    """ chord intervals """
    chords = {
        (0, 7): ['5', 'fifth'],
        (0, 2, 7): ['sus2', 'suspended second'],
        (0, 5, 7): ['sus4', 'suspended fourth'],
        (0, 4, 7): ['maj', 'major'],
        (0, 3, 7): ['min', 'minor'],
        (0, 3, 6): ['dim', 'diminished'],
        (0, 4, 8): ['aug', 'augmented'],
        (0, 3, 6, 9): ['dim7', 'diminished seventh'],
        (0, 3, 6, 10): ['m7b5', 'half-diminished seventh'],
        (0, 3, 7, 10): ['min7', 'minor seventh'],
        (0, 3, 7, 11): ['minmaj7', 'minor major seventh'],
        (0, 4, 7, 10): ['7', 'dominant seventh'],
        (0, 4, 7, 11): ['maj7', 'major seventh'],
        (0, 4, 8, 10): ['aug7', 'augmented seventh'],
        (0, 4, 8, 11): ['maj7+5', 'augmented major seventh'],
        (0, 4, 8, 10, 2): ['9', 'dominant ninth'],
        (0, 4, 8, 10, 2, 5): ['11', 'dominant eleventh'],
        (0, 4, 8, 10, 2, 5, 9): ['13', 'dominant thirteenth'],
    }


    def name_scale(self, input_notes):
        for key in self.notes:
            shift_scale = tuple(set([(note-key)%12 for note in input_notes]))
            try:
                return self.notes[key] + " " + self.scales[shift_scale]
            except KeyError:
                pass


    def name_note(self, note):
        return self.notes[note % 12]


    def name_notes(self, input_notes):
        return [self.name_note(note) for note in input_notes]


    def name_bass_note(self, notes):
        min_note = 127
        for note in notes:
            if note < min_note:
                min_note = note
        return self.name_note(min_note)


    def name_chord(self, input_notes):
        for key in self.notes:
            try:
                note_tuple = tuple(set([((note%12)-key)%12 for note in input_notes]))
                return self.notes[key] + " " + self.chords[note_tuple][0]
            except KeyError:
                pass
            except TypeError:
                pass
