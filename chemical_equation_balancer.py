"""Balance a chemical equation.

Represent as
    H2O + CO2 -> CH4+O2

"""
import re
import sys

import numpy
import numpy.linalg
import scipy.optimize


def main():
    equation = ''.join(sys.argv[1:])
    if '=' not in equation:
        print(
            f'missing = from {equation}, did you accidentally put a ">" in '
            f'the equation?',  file=sys.stderr)

    left, right = equation.split('=')
    left_set, right_set = set(), set()
    left_molecule_list, right_molecule_list = [], []
    for molecule_list, atom_set, molecule_string in [
            (left_molecule_list, left_set, left.split('+')),
            (right_molecule_list, right_set, right.split('+'))]:
        for molecule in molecule_string:
            molecule_regular_expression = '([A-Z][a-z]?)([1-9]*)'
            atoms = re.findall(molecule_regular_expression, molecule)
            atom_list = []
            for atom, count in atoms:
                if count == '':
                    count = 1
                else:
                    count = int(count)
                atom_list.append((atom, count))
                atom_set.add(atom)
            molecule_list.append(atom_list)
    if left_set-right_set != set():
        print(f'ERROR: there are atoms on the left side that are not on the right side of the equation: {left_set-right_set}')
        return
    if right_set-left_set != set():
        print(f'ERROR: there are atoms on the left side that are not on the right side of the equation: {right_set-left_set}')
    n_molecules = len(left_molecule_list)+len(right_molecule_list)
    matrix = numpy.zeros((len(atom_set), n_molecules))
    # rows should be atoms, columns are molecules
    for row_index, atom in enumerate(left_set):
        for offset, sign_factor, molecule_list in [
                (0, 1, left_molecule_list),
                (len(left_molecule_list), -1, right_molecule_list)]:
            for col_index, molecule in enumerate(molecule_list):
                for mol_atom, count in molecule:
                    if mol_atom == atom:
                        matrix[row_index, col_index+offset] += count*sign_factor
    b = numpy.zeros((len(atom_set),))
    c = numpy.ones(n_molecules)

    print(matrix)
    print(b)
    print(c)
    print(right_molecule_list)
    constants = scipy.optimize.linprog(c, A_eq=matrix, b_eq=b, bounds=[(1, None) for _ in range(n_molecules)])

    print(constants)
            #matrix[row_index, col_index] =
    # chemical_regular_expression = (
    #     '[A-Z]')

    # loop while atom counts !=
    #   pick first atom count that is != and calculate least common multiple ? what if there are two molecules
    # look at all molecule factors and simplify out common multiples


def calculate_atom_counts(molecule_list):
    """Calculate the number of atoms given the molecules and their counts.

    Args:
        molecule_list (list): list of tuple of the form
            [(mol_count1, [(atom1, count1), (atom2, count2), ...]),
             (mol_count2, ....)]

    Returns:


    """
    pass


if __name__ == '__main__':
    main()
