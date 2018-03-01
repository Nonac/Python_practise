def div(n):
    resi,res = '',''
    if n == 0:return '0000'
    while n >0:
        res = res + str(n%2)
        n = n // 2
    if len(res) == 1:res = res+'000'
    if len(res) == 2:res = res+'00'
    if len(res) == 3:res = res+'0'
    for i in range(3,-1,-1):
        resi = resi + res[i]
    return resi
def checkio(time_string):
    #replace this for solution
    if time_string[2] != ':': time_string = '0'+time_string
    if time_string[5] != ':': time_string = time_string[:3]+'0'+time_string[3:]
    if len(time_string) != 8: time_string = time_string[:6]+'0'+time_string[6:]
    import re
    pattern = re.compile(r'[0-9]')
    num = pattern.findall(time_string)
    for i in range(0,len(num)):
        num[i] = div(int(num[i]))
    morse,time_str ='', ''
    for each in num:
        time_str = time_str+' '+each
    morse = time_str[3:11]+': '+time_str[12:21]+': '+time_str[22:]
    morse = re.sub('0','.',morse)
    morse = re.sub('1', '-', morse)
    return morse

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"