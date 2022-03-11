"""Test how to tokenize and parse."""
import re

if __name__ == '__main__':
    token_expression = '([A-Z][a-z]?|[1-9][0-9]*|[\(\)=+])'
    input_string = 'CO2+H20=Cl6H12O6+O2'

    tokens = re.findall(token_expression, input_string)
    paren_list = []
    token_tuples = []
    for token in tokens:
        if token == '(':
            paren_list.append('(')
        elif token == ')':
            paren_list.pop()
            print('apply parens')
        print(token)
        if not paren_list:
            print(token)
        else:
            token_tuples.append(token)


