import argparse
from enum import Enum
import itertools
import time
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
    BRUTE_FORCE = 1

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


def main() -> None:
    """
    Print solution to the secret santa problem defined in README.

    A solution is a list of members and needs to be read like this:
        - the first member of the list offers a gift to the second member of the list
        - the second member offers a gift to the third member of the list
        - ...
        - the last member of the list offers a gift to the first member of the list

    If no solution is found, an empty list is printed.
    """
    parser = argparse.ArgumentParser(
        prog='secret-santa',
        description='Find a solution if at least one exists to the secret santa problem'
        )
    parser.add_argument('--runtime', action='store_true', help='Print runtime')
    args = parser.parse_args()

    PEOPLE = ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien"]
    COUPLES = [("Florent", "Jessica"), ("Coline", "Emilien")]
    start = time.time()
    print(solve(PEOPLE, COUPLES, Algorithm.BRUTE_FORCE))
    end = time.time()
    if args.runtime:
        print(f'Runtime: {(end - start) * 1e3:.3f}ms')

if __name__ == "__main__":
    main()

