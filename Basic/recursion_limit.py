def f(x):
    if x == 0:
        return 1
    return f(x - 1)

print f(998)
print f(999)
