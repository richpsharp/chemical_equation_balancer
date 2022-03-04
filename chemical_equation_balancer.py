"""Balance a chemical equation.

Represent as
    H2O + CO2 -> CH4+O2

"""
import re
import sys


def main():
    equation = ''.join(sys.argv[1:])
    if '=' not in equation:
        print(
            f'missing = from {equation}, did you accidentally put a ">" in '
            f'the equation?',  file=sys.stderr)

    left, right = equation.split('=')
    left_set, right_set = set(), set()
    for atom_set, molecule_list in [(left_set, left.split('+')), (right_set, right.split('+'))]:
        for molecule in molecule_list:
            molecule_regular_expression = '([A-Z][a-z]?)([1-9]*)'
            atoms = re.findall(molecule_regular_expression, molecule)
            for atom, count in atoms:
                atom_set.add(atom)
        print(f'{molecule}: {atoms}')
    if left_set-right_set != set():
        print(f'ERROR: there are atoms on the left side that are not on the right side of the equation: {left_set-right_set}')
        return
    if right_set-left_set != set():
        print(f'ERROR: there are atoms on the left side that are not on the right side of the equation: {right_set-left_set}')
        return
    # chemical_regular_expression = (
    #     '[A-Z]')

    # loop while atom counts !=
    #   pick first atom count that is != and calculate least common multiple ? what if there are two molecules
    # look at all molecule factors and simplify out common multiples


def calculate_atom_counts(molecule_count):
    """Calculate the number of atoms given the molecules and their counts.

    Args:
        molecule_count (dict): mapping molecule to integer constant

    """
    pass


if __name__ == '__main__':
    main()
