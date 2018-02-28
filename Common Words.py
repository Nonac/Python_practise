def checkio(first, second):
    import re
    pattern = re.compile(r'[a-z]+')
    words_1 = pattern.findall(first)
    words_2 = pattern.findall(second)
    res = []
    resi = ''
    for i in range(0,len(words_2)):
        if words_2[i] in words_1:res.append(words_2[i])
    while len(res)>0:
        resi = resi + ','+min(res)
        res.remove(min(res))
    return resi[1:]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
