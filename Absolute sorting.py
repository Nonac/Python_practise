def checkio(numbers_array):
    array = []
    for each in numbers_array:
        array.append(each)
    for i in range(0,len(array)):
        for j in range(0,len(array)):
            if abs(array[i]) < abs(array[j]):
                bridge = array[i]
                array[i] = array[j]
                array[j] = bridge
    return array

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
