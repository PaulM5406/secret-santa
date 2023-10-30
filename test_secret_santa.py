from typing import Sequence, List

import pytest

from secret_santa import (
    check_solution,
    brute_force,
    solve,
    AlgorithmNotFoundError, 
    NotEnoughPeopleError, 
    Algorithm,
    ALGORITHM_MAP,
    read_json,
    read_data,
    ExtensionNotSupportedError,
    EXTENSION_MAP
)


PEOPLE = ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien"]
COUPLES = [("Florent", "Jessica"), ("Coline", "Emilien")]
TESTDATA = [
    (["Florent"], False),
    (["Florent", "Jessica", "Coline", "Emilien", "Marie", "Bastien"], False),
    (["Florent", "Coline", "Jessica", "Emilien", "Florent", "Ambroise", "Bastien"], False),
    (["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien"], False),
    (["Florent", "Coline", "Ambroise", "Emilien", "Bastien", "Jessica"], False),
    (["Florent", "Coline", "Jessica", "Emilien", "Ambroise", "Bastien"], True),
    (["Ambroise", "Coline", "Jessica", "Emilien", "Florent", "Bastien"], True),
]


@pytest.mark.parametrize("solution,expected", TESTDATA)
def test_check_solution(solution: List[str], expected: bool):
    """Validate check_solution method to determine if a solution is valid"""
    assert check_solution(PEOPLE, COUPLES, solution) is expected


def test_brute_force():
    """
    Test that brute force algorithm works.
    """
    solution = brute_force(PEOPLE, COUPLES)
    assert solution == ['Florent', 'Coline', 'Jessica', 'Emilien', 'Ambroise', 'Bastien']


def test_algorithm_no_solution():
    """
    Empty list is returned if no solution is found.
    """
    people = ["Florent", "Jessica", "Bastien"]
    couples = [("Florent", "Jessica")]
    for algorithm in ALGORITHM_MAP.values():
        solution = algorithm(people, couples)
        assert solution == []

def test_wrong_algo():
    """Wrong algo should raise AlgorithmNotFoundError"""
    with pytest.raises(AlgorithmNotFoundError):
        solve([], [], 345)


def test_not_enough_people():
    """People count inferior to 3 should raise NotEnoughPeopleError"""
    for people in [
        [], ["Florent"], ["Florent", "Ambroise"]
    ]:
        with pytest.raises(NotEnoughPeopleError):
            solve(people, [], Algorithm.BRUTE_FORCE)

def test_read_json():
    """Test reading data from json file."""
    people, couples = read_json('data-test.json')
    couples = [tuple(couple) for couple in couples]
    assert people == PEOPLE
    assert couples == COUPLES

def test_extension_not_supported():
    """Extension not supported should raise ExtensionNotSupportedError"""
    with pytest.raises(ExtensionNotSupportedError):
        read_data('data.special')