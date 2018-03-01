def checkio(lines_list):
    """Return the quantity of squares"""
    #small squares
    count = 0
    for each in lines_list:
        each.sort()
    for i in range(1,12):
        if [i,i+1] in lines_list and [i,i+4] in lines_list and [i+4,i+5] in lines_list and [i+1,i+5] in lines_list:
            count += 1
        if [i,i+1] in lines_list and [i+1,i+2] in lines_list and [i+8,i+9] in lines_list and [i+9,i+10] in lines_list and [i,i+4] in lines_list and [i+4,i+8] in lines_list and [i+2,i+6] in lines_list and [i+6,i+10] in lines_list:
            count += 1
        if [i,i+1] in lines_list and [i+1,i+2] in lines_list and [i+2,i+3] in lines_list and [i+12,i+13] in lines_list and [i+13,i+14] in lines_list and [i+14,i+15] in lines_list and [i,i+4] in lines_list and [i+4,i+8] in lines_list and [i+8,i+12] in lines_list and [i+3,i+7] in lines_list and [i+7,i+11] in lines_list and [i+11,i+15] in lines_list:
            count += 1
    return count


if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"