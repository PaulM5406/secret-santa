import argparse
import time

from secret_santa import reader, algorithm 


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
    parser.add_argument(
        'pathname', 
        type=str, 
        help='Pathname of file that contains problem data. See supported formats in README.md'
        )
    parser.add_argument(
        '--runtime', 
        action='store_true', 
        help='Print runtime'
        )
    parser.add_argument(
        '--algo', 
        type=int,
        default=0,
        choices=[algo.value for algo in algorithm.Algorithm], 
        help="Algorithm to use. Default is 0 (Brute Force Search). See supported formats in README.md"
        )
    args = parser.parse_args()

    people, couples = reader.read_data(args.pathname)
    algo = algorithm.Algorithm._value2member_map_[args.algo]

    start = time.time()
    print(algorithm.solve(people, couples, algo))
    end = time.time()
    if args.runtime:
        print(f'Runtime: {(end - start) * 1e3:.3f}ms')

if __name__ == "__main__":
    main()

