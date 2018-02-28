def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    # your code here
    for l in range(len(line), 0, -1):
        for i in range(0, len(line)-l):
            sub = line[i:i + l]
            if line[i+l:].count(sub)>0:
                return len(sub)
            elif len(sub) == 1:return 0
    return 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')

