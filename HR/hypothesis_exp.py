def doit(string):
    def val_chars(c):
        return c.islower() or c.isupper() or c.isdigit()

    last_val_char = 0
    for i in xrange(len(string)):
        last_val_char = max(i*val_chars(string[i]), last_val_char)

    reverse_s = string[::-1]
    first_val_char = 0
    for i in xrange(len(string)):
        first_val_char = max(i*val_chars(reverse_s[i]), first_val_char)
    first_val_char = len(string) - 1 - first_val_char

    ans = ""
    for char in string[first_val_char:last_val_char]:
        ans = ans + char*(val_chars(char)) + " "*(not val_chars(char))

    ans = string[:first_val_char] + " ".join(ans.split()) + string[last_val_char:]
    return ans*(last_val_char != 0) + string*(last_val_char == 0)


from hypothesis import given
from hypothesis.strategies import text
import string


@given(text(string.ascii_letters + string.digits + ''' !@#$%&'''))
def test_number_groups(inp):
    assert len(inp.split()) <= len(doit(inp).split())
