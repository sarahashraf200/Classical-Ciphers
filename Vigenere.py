#implementing the key and switching between the auto and repeated mode
def create_key_repeated(key , plain):
    #repeating
    rep = ""
    if len(plain) > len(key):
        for i in range(int(len(plain) / len(key))):
            rep += key
        rep += key[:len(plain) % len(key)]
    elif len(plain) < len (key):
        rep += key[:len(plain)]
    elif len(plain) == len(key):
        rep += key
    else:
        print("error")



    return rep


def create_key_auto(key, plain):
    i=0
    while (len(key) != len(plain)):
        key+= plain[i]
        i += 1


    return key

#implementing the vigenere cipher technique
def Vigenere( key , text ,  mode):
   enc = ""
   key = create_key_auto(key, text) if mode else create_key_repeated(key, text)
   for i in range(len(text)):
       if text[i].isupper():
           #adding the character
           enc += chr((ord(text[i]) - ord('A') + ord(key[i]) - ord('A')) % 26 + ord('A'))
       elif text[i].islower():
           enc += chr((ord(text[i]) - ord('a') + ord(key[i]) - ord('a')) % 26 + ord('a'))

   return enc







