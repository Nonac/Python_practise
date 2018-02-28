def recall_password(cipher_grille, ciphered_password):
    code,words,res = '','',''
    for a in cipher_grille:
        for b in a:
            code = code + b
    for i in range(0,4):
        for a in ciphered_password:
            for b in a:
                words = words + b
    for i in range(0,4):
        for j in range(3,-1,-1):
            code = code + cipher_grille[j][i]
    for i in range(3,-1,-1):
        for j in range(3,-1,-1):
            code = code + cipher_grille[i][j]
    for i in range(3,-1,-1):
        for j in range(0,4):
            code = code + cipher_grille[j][i]
    for i in range(len(code)):
        if code[i] == 'X':res = res + words[i]
    return res


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
