"""Tests on the chords module"""

import pytest
from jamulizer.analysis import Analysis

NOTE_INPUTS = [
    (98, 'D'),
    (99, 'D#/Eb'),
    (100, 'E')
]

@pytest.mark.parametrize("test_input, expected", NOTE_INPUTS)
def test_name_notes(test_input, expected):
    actual = Analysis.name_note(test_input)
    assert actual == expected


CHORD_INPUTS = [
    #([0, 7], 'C 5'),
    ([0, 4, 7], 'C maj'),
    ([0, 4, 7, 11], 'C maj7'),
    ([0, 4, 8, 10, 2, 5, 9], 'C 13'),
    ([2, 5, 9], 'D min'),
    (['a', 2, 3], None),
    (None, None),
    ([1, 2, 3], None)
]

@pytest.mark.parametrize("test_input, expected", CHORD_INPUTS)
def test_name_chords(test_input, expected):
    actual = Analysis.name_chord(test_input)
    assert actual == expected


SCALE_INPUTS = [
    ([0, 2, 4, 5, 7, 9, 11], 'C major'),
    ([0, 2, 3, 5, 7, 8, 10], 'C minor')
]

@pytest.mark.parametrize("test_input, expected", SCALE_INPUTS)
def test_name_scale(test_input, expected):
    actual = Analysis.name_scale(test_input)
    assert actual == expected
