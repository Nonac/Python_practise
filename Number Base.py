def checkio(str_number, radix):
    text = str(str_number)
    import re
    patten = re.compile(r'[0-9A-Z]')
    arry = patten.findall(text)
    i = 0
    res = 0
    for each in range(len(arry)-1,-1,-1):
        if arry[i].isalpha():
            if ord(arry[i]) - 55 >= radix: return -1
            res = (ord(arry[i])-55) * (radix ** each) + res
        else:
            if int(arry[i]) >= radix: return -1
            res = int(arry[i]) * (radix ** each) + res
        i += 1
    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
