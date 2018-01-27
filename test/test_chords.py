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
