def non_repeat(s):
    for l in range(len(s), 0, -1):
        for i in range(0, len(s) - l + 1):
            sub = s[i:i + l]
            if all(sub.count(c) == 1 for c in sub):
                return sub
    return ""

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')
