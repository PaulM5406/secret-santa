from typing import Sequence, List

import pytest

from ..reader import (
    read_json,
    read_data,
    ExtensionNotSupportedError,
    EXTENSION_MAP
)


PEOPLE = ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien"]
COUPLES = [("Florent", "Jessica"), ("Coline", "Emilien")]

def test_read_json():
    """Test reading data from json file."""
    people, couples = read_json('data/data-test.json')
    couples = [tuple(couple) for couple in couples]
    assert people == PEOPLE
    assert couples == COUPLES

def test_extension_not_supported():
    """Extension not supported should raise ExtensionNotSupportedError"""
    with pytest.raises(ExtensionNotSupportedError):
        read_data('data.special')