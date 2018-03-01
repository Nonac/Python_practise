def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def checkio(opacity):
    fi,list =[],[]
    for i in range(0,21):fi.append(fib(i))
    for i in range(5000,-1,-1):list.append(10000)
    for i in range(0,len(list)):
        if i in fi:
            for j in range(i,len(list)):
                list[j] = list[j]-i
        else:
            for j in range(i,len(list)):
                list[j] = list[j]+1

    return list.index(opacity)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"