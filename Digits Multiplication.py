def checkio(number):
    text = str(number)
    import re
    patten = re.compile(r'[0-9]')
    arry = patten.findall(text)
    res = 1
    for each in arry:
        if int(each) != 0:
           res = res * int(each)

    return res

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
