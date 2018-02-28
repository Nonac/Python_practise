def repeat_inside(line):
    import re
    x = [i for i, k in re.findall(r"((.{2,})\2+)", line) + re.findall(r"((.)\2+)", line)]
    return sorted(x, key=len, reverse=True)[0] if x else ""

"""
        first the longest repeating substring

    # your code here

    words = []
    words_n = []
    res = ''
    target = ''
    max = 0
    for l in range(len(line)//2, 0, -1):
        for i in range(0, len(line)-l+1,1):
            words.append(line[i:i+l])
    print(words)
    for i in range(0,len(words)):
        if words.count(words[i]) != 1:
            words_n.append(words[i])
    print(words_n)
    for i in range(0,len(words_n)-1):
        if i < len(words_n):
            target = words_n[i]
            while i+1<len(words_n) and target == words_n[i+1]:
                words_n[i] = words_n[i]+words_n[i+1]
                words_n.remove(target)
    print(words_n)
    for each in words_n:
        if max < len(each):
            max = len(each)
            res = each
    return res
    
"""



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')