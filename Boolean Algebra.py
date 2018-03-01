OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
def con(x,y):
    if x == 1 and y == 1:return 1
    else:return 0
def dis(x,y):
    if x == 0 and y == 0:return 0
    else:return 1
def imp(x,y):
    return dis(1-x,y)
def exc(x,y):
    co = con(x,y)
    di = dis(x,y)
    return con(di,1-co)
def equ(x,y):
    return 1-exc(x,y)


def boolean(x, y, operation):
    if operation == "conjunction":return con(x,y)
    elif operation == "disjunction":return dis(x,y)
    elif operation == "implication":return imp(x,y)
    elif operation == "exclusive":return exc(x,y)
    elif operation == "equivalence":return equ(x,y)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"