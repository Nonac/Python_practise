def checkio(matrix):
    #replace this for solution
    width = len(matrix)
    #纵
    for i in range(0,width-3):
        for j in range(0,width):
            target = matrix[i][j]
            if matrix[i+1][j] == target and matrix[i+2][j] == target and matrix[i+3][j] == target:
                return True
    #横
    for i in range(0, width):
        for j in range(0, width-3):
            target = matrix[i][j]
            if matrix[i][j+1] == target and matrix[i][j+2] == target and matrix[i][j+3] == target:
                return True
    #斜
    for i in range(0, width-3):
        for j in range(0, width-3):
            target = matrix[i][j]
            if matrix[i+1][j+1] == target and matrix[i+2][j+2] == target and matrix[i+3][j+3] == target:
                return True
    for i in range(0, width-3):
        for j in range(3, width):
            target = matrix[i][j]
            if matrix[i+1][j-1] == target and matrix[i+2][j-2] == target and matrix[i+3][j-3] == target:
                return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
