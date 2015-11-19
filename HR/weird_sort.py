def coisa(lst):
    return reduce(lambda x, y: x + y, lst)

print coisa(['a', '1', '2'])
