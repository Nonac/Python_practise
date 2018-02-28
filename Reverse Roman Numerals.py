def reverse_roman(roman_string):

    #replace this for solution
    import re
    pattern = re.compile(r'[A-Z]')
    words = pattern.findall(roman_string)
    sourve_w = ['I','V','X','L','C','D','M']
    sourve_n = [1,5,10,50,100,500,1000]
    for i in range(0,len(words)):words[i] = sourve_n[sourve_w.index(words[i])]
    for i in range(0,len(words)-1):
        if words[i] < words[i+1]: words[i] = 0-words[i]
    return sum(words)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');