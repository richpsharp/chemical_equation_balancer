import re

if __name__ == '__main__':
    token_expression = '([A-Z][a-z]?|[1-9][0-9]*|[\(\)=+])'
    input_string = 'CO2+H20=C6H12O6+O2'
    tokens = re.findall(token_expression, input_string)
    print(token_expression)
    print(tokens)
