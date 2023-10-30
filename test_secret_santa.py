from typing import Sequence, List

import pytest

def check_solution(people:Sequence[str], couples: Sequence[Sequence[str]], solution: List[str]) -> bool:
    """
    Check if solution is valid.

    1. Check that every member appears only once in solution
    2. Check that two members of a couple are not consecutive in solution
    """
    check_people = {member: 0 for member in people}
    check_couple = [set(couple) for couple in couples]
    _solution = solution.copy()
    _solution.append(solution[0])
    for i, member in enumerate(solution):
        if not member in check_people:
            return False
        check_people[member] += 1
        if check_people[member] > 1:
            return False
        if set([member, _solution[i+1]]) in check_couple:
            return False
    for count in check_people.values():
        if count != 1:
            return False
    return True

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
    assert check_solution(PEOPLE, COUPLES, solution) is expected
    
    
