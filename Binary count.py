def checkio(number):
    n = 0
    while number > 0:
        if number % 2 == 0:
            number = number // 2
        if number % 2 == 1:
            number = number // 2
            n += 1
    return n
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
