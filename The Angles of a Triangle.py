def cosdef(a, b, c):
    up = b ** 2 + c ** 2 - a ** 2
    down = 2 * b * c
    return (up / down)


def checkio(a, b, c):
    # replace this for solution
    import math
    res = []
    if a + b <= c or a + c <= b or b + c <= a:
        return [0, 0, 0]

    else:
        res.append(round(math.degrees(math.acos(cosdef(a, b, c)))))
        res.append(round(math.degrees(math.acos(cosdef(b, a, c)))))
        res.append(round(math.degrees(math.acos(cosdef(c, a, b)))))
    res.sort()
    return res


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"