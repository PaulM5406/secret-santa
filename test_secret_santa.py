from typing import Sequence, List

import pytest

from secret_santa import (
    check_solution,
    brute_force,
    solve,
    AlgorithmNotFoundError, 
    NotEnoughPeopleError, 
    Algorithm
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

def test_wrong_algo():
    """Wrong algo should raise AlgorithmNotFoundError"""
    with pytest.raises(AlgorithmNotFoundError):
        solve([], [], 345)


def test_no_people():
    """People count inferior to 2 should raise NotEnoughPeopleError"""
    with pytest.raises(NotEnoughPeopleError):
        solve([], [], Algorithm.BRUTE_FORCE)
    with pytest.raises(NotEnoughPeopleError):
        solve(["Florent"], [], Algorithm.BRUTE_FORCE)