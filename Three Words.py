def checkio(words):
    import re
    patten = re.compile(r'[A-Za-z0-9]+')
    res = patten.findall(words)
    for i in range(0,len(res)-1):
        if res[i].isalpha() and res[i+1].isalpha() and res[i+2].isalpha():
            return True
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
