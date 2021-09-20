
#Implementing the 2*2 hill cipher matrix
def twobytwoMatrix(key, text, TL, enc):
    if len(text) % 2:
        text += 'x'
    for ch in text:
        TL.append(ord(ch) -65)
    for i in range(0,len(TL),2):
        enc += chr(((key[0]*TL[i] + key[2]*TL[i+1])%26)+ord('A'))
        enc += chr(((key[1]*TL[i] + key[3]*TL[i+1])%26)+ord('A'))
    return enc
#Implementing the 3*3 Hill cipher matrix
def threebythreeMatrix(key, text, TL, enc):
    if len(text) % 3: text += 'x'
    if len(text) % 3: text += 'x'
    for ch in text:
        TL.append(ord(ch) -65)
    for i in range(0,len(TL),3):
        enc += chr(((key[0]*TL[i] + key[1]*TL[i+1] + key[2]*TL[i+2])%26)+ord('A'))
        enc += chr(((key[3]*TL[i] + key[4]*TL[i+1] + key[5]*TL[i+2])%26)+ord('A'))
        enc += chr(((key[6]*TL[i] + key[7]*TL[i+1] + key[8]*TL[i+2])%26)+ord('A'))
    return enc
#Hill cipher technique
def Hill(key, text):
    TL = []
    enc = ""
    return twobytwoMatrix(key, text, TL, enc) if len(key) == 4 else threebythreeMatrix(key, text, TL, enc)
