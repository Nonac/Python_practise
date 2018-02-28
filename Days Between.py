def year_diff(year):
    if year % 4 == 0 and year % 100 != 0:
        return 366
    elif year % 400 == 0:
        return 366
    else:return 365
def mouth_diff(mouth,year):
    if mouth in [1,3,5,7,8,10,12]:
        return 31
    if mouth in [4,6,9,11]:
        return 30
    elif year_diff(year) == 366:
        return 29
    elif year_diff(year) == 365:
        return 28
def days_sum(date):
    sum_y = 0
    sum_m = 0
    for i in range(0,date[0]):
        sum_y = sum_y + year_diff(i)
    for j in range(1,date[1]):
        sum_m = sum_m + mouth_diff(j,date[0])
    sum_d = sum_y + sum_m+date[2]
    return sum_d
def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    return abs(days_sum(date2)-days_sum(date1))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
