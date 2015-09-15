def urlify(char_array, length):
    word_pointer = length - 1
    spaces = sum(1 for i in xrange(length) if char_array[i] == ' ')
    array_pointer = length + 2*spaces - 1

    for i in xrange(length - 1, -1, -1):
        if char_array[word_pointer] != " ":
            swap(char_array, word_pointer, array_pointer)
            word_pointer -= 1
            array_pointer -= 1
        else:
            char_array[array_pointer - 2: array_pointer + 1] = ["%", "2", "0"]
            array_pointer -= 3
            word_pointer -= 1
    return char_array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

print urlify(list("Hello World     "),  11)
