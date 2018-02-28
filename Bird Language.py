VOWELS = "aeiouy"

def translate(phrase):
    import re
    pattern = re.compile(r'[a-z]+')
    words = pattern.findall(phrase)
    print(words)
    res = ''
    out = ''
    for each in words:
        i = 0
        res = ''
        while i < len(each):
            if each[i] not in VOWELS:
                res = res + each[i]
                i += 2
            else:
                res = res + each[i]
                i += 3
        out = out +' '+res
    return out[1:]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
