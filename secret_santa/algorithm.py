from enum import Enum
import itertools
from typing import Sequence, List


def check_solution(people:Sequence[str], couples: Sequence[Sequence[str]], solution: List[str]) -> bool:
    """
    Check if solution is valid.

    1. Check that every member appears only once in solution
    2. Check that two members of a couple are not consecutive in solution
    """
    check_people = {member: 0 for member in people}
    check_couple = [set(couple) for couple in couples]
    _solution = [*solution]
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


def brute_force(people: Sequence[str], couples: Sequence[Sequence[str]]) -> List[str]:
    """
    Brute force approach to find solution.

    1. Fix a first member and look at all possible permutations of people list
    2. Look for a valid solution 
    """
    _possible_solutions = itertools.permutations(people[1:])
    for _possible_solution in _possible_solutions:
        possible_solution = [people[0], *_possible_solution]
        if check_solution(people, couples, possible_solution):
            return possible_solution
    return []


class NotEnoughPeopleError(Exception):
    pass


class AlgorithmNotFoundError(Exception):
    pass


class Algorithm(Enum):
    BRUTE_FORCE = 0


ALGORITHM_MAP = {
    Algorithm.BRUTE_FORCE: brute_force
}


def solve(people: Sequence[str], couples: Sequence[Sequence[str]], algo: Algorithm) -> List[str]:
    """
    Check parameters and solve problem with given algorithm. 
    """
    if algo not in ALGORITHM_MAP:
        raise AlgorithmNotFoundError

    if len(people) < 3:
        raise NotEnoughPeopleError

    return ALGORITHM_MAP[algo](people, couples)