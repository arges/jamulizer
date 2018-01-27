"""Tests on the chords module"""

import pytest
from jamulizer.chords import Chords

NOTE_INPUTS = [
    (98, 'D'),
    (99, 'D#/Eb'),
    (100, 'E')
]

@pytest.mark.parametrize("test_input, expected", NOTE_INPUTS)
def test_name_notes(test_input, expected):
    chords = Chords()
    actual = chords.name_note(test_input)
    assert actual == expected


CHORD_INPUTS = [
    (frozenset([0, 4, 7]), 'C maj')
]

@pytest.mark.parametrize("test_input, expected", CHORD_INPUTS)
def test_name_chords(test_input, expected):
    chords = Chords()
    actual = chords.name_chord(test_input)
    assert actual == expected
