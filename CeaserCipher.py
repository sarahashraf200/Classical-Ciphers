

def Caesar(plain , key):
    enc = ""
    for ch in plain:
        #Handle the case if it is an upper case alphabetical
        if ch.isupper():
            index = ord(ch) - ord('A')
            shift_ch = (index+key)%26+ ord('A')
            ch_new = chr(shift_ch)
            enc += ch_new
        # Handle the case if it is an lower case alphabetical
        elif ch.islower():
            index = ord(ch) - ord('a')
            shift_ch = (index + key) % 26 + ord('a')
            ch_new = chr(shift_ch)
            enc += ch_new
        #Handle the case if it was a number
        elif ch.isdigit():
            ch_new = (int(ch) + key) % 10
            enc += str(ch_new)
        else:

        #Handle the case if it wasn't alpha or number
            enc += ch
    return enc

#s = "ATTACKATONCE"
#ciphered = ceaser(4, s)
#print(ciphered)

