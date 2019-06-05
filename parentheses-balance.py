'''
A common problem for compilers and text editors is determining whether the
parentheses in a string are balanced and properly nested. For example, the string
((())())() contains properly nested pairs of parentheses, which the strings )()( and
()) do not. Give an algorithm that returns true if a string contains properly nested
and balanced parentheses, and false if otherwise. For full credit, identify the position
of the first offending parenthesis if the string is not properly nested and balanced.
'''

OPEN_BRACKETS = ['(', '[', '{']
CLOSE_BRACKETS = [')', ']', '}']


def get_open_bracket(bracket):
    if bracket is ')':
        return '('
    if bracket is ']':
        return '['
    if bracket is '}':
        return '{'


def is_balanced(input):
    stack = []
    for ch in input:
        if ch in OPEN_BRACKETS:
            stack.append(ch)
        elif ch in CLOSE_BRACKETS:
            stack_length = len(stack)
            if stack_length == 0:
                return False
            elif stack[stack_length - 1] == get_open_bracket(ch):
                stack.pop()
            else:
                stack.append(ch)

    return len(stack) == 0


inputs = [
    '()()(())',
    '[([)]]',
    '[()]{}{[()()]()}',
    '[]{[{{'
]

if __name__ == '__main__':
    for input in inputs:
        print(input, is_balanced(input))
