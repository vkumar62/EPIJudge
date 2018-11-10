from test_framework import generic_test


def evaluate(expression):
    # TODO - you fill in here.
    OPERATOR = {
            '+' : lambda x, y: x+y,
            '-' : lambda x, y: y-x,
            '*' : lambda x, y: x*y,
            '/' : lambda x, y: y//x
            }
    operands = []
    for val in map(str.strip, expression.split(',')):
        if val not in OPERATOR:
            operands.append(int(val))
        else:
            result = OPERATOR[val](operands.pop(), operands.pop()) 
            operands.append(result)
    return operands.pop() if operands else 0

def evaluate_polish(expression):
    return evaluate(reversed(expression))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
