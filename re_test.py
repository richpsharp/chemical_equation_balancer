from collections import defaultdict
import re

if __name__ == '__main__':
    token_expression = '([A-Z][a-z]?|[1-9][0-9]*|[\(\)=+])'
    input_string = 'CO2+H20=(CH2O)6+O2'
    tokens = re.findall(token_expression, input_string)
    state = 'open'  # open, molecule count
    molecule_equation = defaultdict(list)
    side = 'left'
    molecule = None
    for token in tokens:
        if state == 'open':
            molecule_id = token
            state = 'molecule_count'
        elif state == 'molecule_count':
            state = 'open'
            try:
                molecule = (molecule_id, int(token))
            except ValueError:
                if token == ')':
                    print('pop a paren and multiply all counts')
                else:
                    # molecule ended
                    molecule = (molecule_id, 1)
        if molecule is not None:
            print(molecule)
            molecule_equation[side].append(molecule)
            molecule = None
        if token == '=':
            side = 'right'
