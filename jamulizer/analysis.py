""" midi analysis library """

class Analysis:

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
        frozenset([0, 2, 4, 5, 7, 9, 11]): 'major',
        frozenset([0, 2, 3, 5, 7, 8, 10]): 'minor'
    }

    """ chord intervals """
    chords = {
        frozenset([0, 7]): ['5', 'fifth'],
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

    @staticmethod
    def name_scale(input_notes):
        """ name scale given input notes """
        for key in Analysis.notes:
            shift_scale = frozenset([(note-key)%12 for note in input_notes])
            try:
                return Analysis.notes[key] + " " + Analysis.scales[shift_scale]
            except KeyError:
                pass


    @staticmethod
    def name_note(note):
        """ name single note """
        return Analysis.notes[note % 12]


    @staticmethod
    def name_notes(input_notes):
        """ name list of notes """
        return [Analysis.name_note(note) for note in input_notes]


    @staticmethod
    def name_bass_note(notes):
        """ name bass note in notes """
        min_note = 127
        for note in notes:
            if note < min_note:
                min_note = note
        return Analysis.name_note(min_note)


    @staticmethod
    def name_chord(input_notes):
        """ name chord given input notes """
        for key in Analysis.notes:
            try:
                note_tuple = frozenset([((note%12)-key)%12 for note in input_notes])
                print(note_tuple)
                return Analysis.notes[key] + " " + Analysis.chords[note_tuple][0]
            except KeyError:
                pass
            except TypeError:
                pass
