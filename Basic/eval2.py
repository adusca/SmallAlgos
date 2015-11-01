"""
Write a function called eval, which takes a string and returns a
boolean. This string is allowed 6 different characters: 0, 1, &, |, (,
and ). Eval should evaluate the string as a boolean expression, where
0 is false, 1 is true, & is an and, and | is an or. An example string
might look like '(0 | (1 | 0)) & (1 & ((1 | 0) & 0))'
"""

# expr := 0 | 1 | (expr '|' expr) | (expr '&' expr)


def eval_s(string):
    string = string.replace(' ', '')

    def eval_aux():
        nxt = consume()
        if nxt == '0':
            return False
        if nxt == '1':
            return True
        if nxt == '(':
            exp1 = eval_aux()  # Consume sub-expression 1
            op = consume()
            exp2 = eval_aux()  # Consume sub-expression 2
            tmp = consume()    # Consume ')'
            assert tmp == ")", "Unclosed parenthesis found"
            if op == '&':
                return exp1 and exp2
            if op == "|":
                return exp1 or exp2
            assert False, "There are only 2 operators"
        assert False, "We should only call eval_aux with (, 0 or 1 "

    def consume():
        eval_aux.index += 1
        return string[eval_aux.index - 1]

    eval_aux.index = 0
    result = eval_aux()
    assert eval_aux.index == len(string), "We should consume the whole string"
    return result

print eval_s('((0 | (1 | 0)) & (1 & ((1 | 0) & 0)))')
try:
    print eval_s('((0 | (1 | 0)) & (2 & ((1 | 0) & 0)))')
except Exception as e:
    print e
try:
    print eval_s('((0 | (1 | 0) & (2 & ((1 | 0) & 0)))')
except Exception as e:
    print e
