"""
Write a function called eval, which takes a string and returns a
boolean. This string is allowed 6 different characters: 0, 1, &, |, (,
and ). Eval should evaluate the string as a boolean expression, where
0 is false, 1 is true, & is an and, and | is an or. An example string
might look like '(0 | (1 | 0)) & (1 & ((1 | 0) & 0))'
"""

# expr := 0 | 1 | (expr '|' expr) | (expr '&' expr)


def eval_s(string):
    index = 0
    string = string.replace(' ', '')

    def eval_aux():
        if string[index] == '0':
            index += 1
            return False
        if string[index] == '1':
            index += 1
            return True
        if string[index] == '(':
            index += 1         # Consume '('
            exp1 = eval_aux()  # Consume sub-expression 1
            op = string[index]
            index += 1         # Consume operation
            exp2 = eval_aux()  # Consume sub-expression 2
            index += 1         # Consume ')'

            if op == '&':
                return exp1 and exp2
            return exp1 or exp2

    return eval_aux()

print eval_s('((0 | (1 | 0)) & (1 & ((1 | 0) & 0)))')
