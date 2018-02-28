def checkio(game_result):
    a = ""
    for i in game_result:
        a = a + i
    if a[0] == a[1] and a[0] == a[2] and a[0] != ".":return a[0]
    elif a[0] == a[3] and a[0] == a[6] and a[0] != ".":return a[0]
    elif a[0] == a[4] and a[0] == a[8] and a[0] != ".":return a[0]
    elif a[1] == a[4] and a[1] == a[7] and a[1] != ".":return a[1]
    elif a[2] == a[5] and a[2] == a[8] and a[2] != ".":return a[2]
    elif a[2] == a[4] and a[2] == a[6] and a[2] != ".":
        return a[2]
    elif a[3] == a[4] and a[3] == a[5] and a[3] != ".":
        return a[3]
    elif a[6] == a[7] and a[6] == a[8] and a[6] != ".":
        return a[6]
    else:return "D"
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

