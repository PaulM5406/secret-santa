from enum import Enum
import itertools
from typing import Sequence, List, Mapping


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

    1. Fix first member and look at all possible permutations of people list
    2. Look for a valid solution 
    """
    _possible_solutions = itertools.permutations(people[1:])
    for _possible_solution in _possible_solutions:
        possible_solution = [people[0], *_possible_solution]
        if check_solution(people, couples, possible_solution):
            return possible_solution
    return []


def backtracking(people: Sequence[str], couples: Sequence[Sequence[str]]) -> List[str]:
    """
    DFS/backtracking approach to find solution.
    """
    solver = BacktrackingSolver(people, couples)
    return solver.solution()

class BacktrackingSolver():  
    def __init__(self, people: Sequence[str], couples: Sequence[Sequence[str]]) -> None:
        self.people = people
        self.n_people = len(people)
        self.people_map = {member: i for i, member in enumerate(people)}
        self.graph = self.create_graph(self.people_map, couples)
        self.path = []
        self.set_path = set()
        self.n_path = 0

    def create_graph(self, people_map: Mapping[str, int], couples: Sequence[Sequence[str]]) -> List[List[str]]:
        """
        Create the graph (adjacency matrix) from inputs.
        """
        graph = [[True for i in range(self.n_people)] for j in range(self.n_people)]
        for couple in couples:
            graph[people_map[couple[0]]][people_map[couple[1]]] = False
            graph[people_map[couple[1]]][people_map[couple[0]]] = False
        return graph
    
    def is_node_checked(self, node: int) -> bool:
        """
        Has node been visited ?
        """
        if node in self.set_path:
            return False
        return True

    def neighbours(self, node: int) -> List[int]:
        """
        Find neighbours of given node.

        TODO: Neighbours could be cached or precomputed.
        """
        return [i for i, is_edge in enumerate(self.graph[node]) if i != node and is_edge is True]

    def cycle_detection(self, root: int) -> bool:
        """
        DFS and Backtracking
        """
        self.path.append(root)
        self.set_path.add(root)
        self.n_path += 1
        for neighbour in self.neighbours(root):
            if self.is_node_checked(neighbour):
                if self.cycle_detection(neighbour):
                    return True
    
        if self.n_path == self.n_people:
            if self.path[0] in self.neighbours(self.path[-1]):
                return True
            else:
                return False

        self.path.pop()
        self.set_path.remove(root)
        self.n_path -= 1

    def solution(self) -> List[str]:
        """
        Returns cycle.
        """
        if self.cycle_detection(0):
            return [self.people[i] for i in self.path]
        return [] 


class NotEnoughPeopleError(Exception):
    pass


class AlgorithmNotFoundError(Exception):
    pass


class Algorithm(Enum):
    BRUTE_FORCE = 0
    BACKTRACKING = 1


ALGORITHM_MAP = {
    Algorithm.BRUTE_FORCE: brute_force,
    Algorithm.BACKTRACKING: backtracking,
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