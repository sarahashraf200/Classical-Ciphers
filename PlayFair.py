
#Building a 5*5 matrix
def BuildMatrix(PlainText, Key):
    Key = Key.replace("j", "i")
    Key = Key.upper()
    Key = ''.join(Key.split())
    Alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    Text = ''.join(PlainText.split())

    for i in range(len(Key)):
        if not Key[i] in matrix:
            matrix.append(Key[i])
    for i in range(len(Alphabet)):
        if not Alphabet[i] in matrix:
            matrix.append(Alphabet[i])

    lastmatrix = [matrix[i:i + 5] for i in range(0, 25, 5)]

    return lastmatrix

#getting the position of each char in the matrix
def GetPosition(enc,char):
    x=y=0
    for i in range(5):
        for j in range(5):
             if enc[i][j] == char:
                    x=i
                    y=j
    return x,y


#play fair cipher implementation
def Playfair(PlainText, Key):
    cipher = ""
    Key = Key.replace("j", "i")
    Key = Key.upper()
    Key = ''.join(Key.split())
    Text = ''.join(PlainText.split())
    Text = Text.replace("j", "i")
    Text = Text.upper()

    msg = []

    for i in Text:
        msg.append(i)

    c = BuildMatrix(PlainText, Key)

    for i in range(0, len(msg) - 1, 2):
        if (msg[i] == msg[i + 1]):
            msg.insert(i + 1, 'X')

    if (len(msg) % 2 != 0):
        msg.append('X') 

    for i in range(0, len(msg) - 1, 2):
        x1, y1 = GetPosition(c, msg[i])
        x2, y2 = GetPosition(c, msg[i + 1])
        if (x1 == x2):
            cipher += c[x1][(y1 + 1) % 5]
            cipher += c[x2][(y2 + 1) % 5]
        elif (y1 == y2):
            cipher += c[(x1 + 1) % 5][y1]
            cipher += c[(x2 + 1) % 5][y2]
        else:
            cipher += c[x1][y2]
            cipher += c[x2][y1]

    return cipher.lower()


#s = Playfair("instruments", "Monarchy")
#print(s)




