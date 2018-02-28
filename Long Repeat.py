def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    import re
    count = []
    pattern = re.compile(r'((\w)\2+)')
    words = pattern.findall(line)
    for each in words:count.append(len(each[0]))
    if line == '':return 0
    if len(count) > 0:return max(count)
    else:return 1


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
