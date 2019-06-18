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
    for index, char in enumerate(input):
        if char in OPEN_BRACKETS:
            stack.append(char)
        elif char in CLOSE_BRACKETS:
            stack_length = len(stack)
            if stack_length == 0:
                return False, index
            elif stack[stack_length - 1] == get_open_bracket(char):
                stack.pop()
            else:
                return False, index

    return len(stack) == 0, len(stack)


inputs = [
    '()()(())',
    '[([)]]',
    '[()]{}{[()()]()}',
    '[]{[{{'
]

if __name__ == '__main__':
    for input in inputs:
        balanced, offending = is_balanced(input)
        print(input, 'balanced' if balanced else 'imbalanced at %s' % offending)
