def vernam( text , key):
    enc = ""
    for ch in range(len(text)):
        if text[ch].isupper():
            enc += chr((ord(text[ch])- ord('A') + ord(key[ch])- ord('A'))%26+ ord('A'))
        elif text[ch].islower():
            enc += chr((ord(text[ch]) - ord('a') + ord(key[ch]) - ord('a')) % 26 + ord('a'))
        elif text[ch].isdigit():
            ch_new = (int(text[ch]) + key[ch]) % 10
            enc += str(ch_new)
        else:

        #Handle the case if it wasn't alpha or number
            enc += text[ch]
    return enc
#s = vernam("RANCHOBABA", "RAMSWARUPK")
#print(s)