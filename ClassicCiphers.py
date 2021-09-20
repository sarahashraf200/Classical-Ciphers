
from CeaserCipher import *
from HillCipher import Hill
from PlayFair import Playfair
from vernamCipher import vernam
from Vigenere import Vigenere


def inoutfiles():
    # Caesar
    file1 = open("Input Files/Caesar/caesar_plain.txt", "r")
    file2 = open("Output Files/caesar_cipher.txt", "w")


    Lines = file1.readlines()

    for line in Lines:
        file2.write(
            line.strip()
            + "      "
            + "encryption by 3 ="
            + Caesar(line.strip(), 3)
            + "        "
            + "\n"
        )
    file2.write("\n")
    for line in Lines:
        file2.write(
            line.strip()
            + "      "
            + "encryption by 6 ="
            + Caesar(line.strip(), 6)
            + "        "
            + "\n"
        )
    file2.write("\n")
    for line in Lines:
        file2.write(
            line.strip()
            + "      "
            + "encryption by 12 ="
            + Caesar(line.strip(), 12)
            + "        "
            + "\n"
        )

    file1.close()
    file2.close()

    # HILL 2X2
    file1 = open("Input Files/Hill/hill_plain_2x2.txt", "r")
    file2 = open("Output Files/hill_cipher_2x2.txt", "w+")
    Lines = file1.readlines()

    for line in Lines:
        file2.write(line.strip() + "              " +
                    "encryption with key [[5,17],[8,3]] = " + Hill([5, 17, 8, 3], line) + "\n")

    file1.close()
    file2.close()

    # HILL 3X3
    file1 = open("Input Files/Hill/hill_plain_3x3.txt", "r")
    file2 = open("Output Files/hill_cipher_3x3.txt", "w+")
    Lines = file1.readlines()
    for line in Lines:
        file2.write(line.strip() + "              " +
                    "encryption with key [[2,4,12],[9,1,6],[7,5,3]] = " + Hill( [2, 4, 12, 9, 1, 6, 7, 5, 3], line) + "\n")

    file1.close()
    file2.close()

    # playfair

    file1 = open("Input Files/PlayFair/playfair_plain.txt", "r")
    file2 = open("Output Files/playfair_cipher.txt", "w")

    Lines = file1.readlines()

    for line in Lines:
        file2.write(
            line.strip()
            + "      "
            + "encryption by rats = "
            + Playfair(line.strip(), "rats")
            + "\n"
        )
    file2.write("\n")
    for line in Lines:
        file2.write(
            line.strip()
            + "      "
            + "encryption by archangel = "
            + Playfair(line.strip(), "archangel")
            + "\n"
        )

    file1.close()
    file2.close()

    # vernam
    file1 = open("Input Files/vernam/vernam_plain.txt", "r")
    file2 = open("Output Files/vernam_cipher.txt", "w")
    Lines = file1.readlines()
    for line in Lines:
        file2.write(
            line.strip()
            + "      "
            + "encryption by key SPARTANS = "
            + vernam(line.strip(), "SPARTANS")
            + "\n"
        )

    file1.close()
    file2.close()

    # Vigenere
    file1 = open("Input Files/Vigenere/vigenere_plain.txt", "r")
    file2 = open("Output Files/vigenere_cipher.txt", "w")
    Lines = file1.readlines()

    for line in Lines:
        file2.write(line.strip()+"          " +
                    "encryption by pie = "+Vigenere( "pie" ,line, False)+"\n")

    file2.write("\n")

    for line in Lines:
        file2.write(line.strip()+"          " +
                    "encryption by aether = "+Vigenere( "aether", line, True)+"\n")

    file1.close()
    file2.close()


def main():

    inoutfiles()
    while(1):
        print("YOU WILL FIND THE ENCRYPTION OF GIVEN SAMPLES IN THE OUTPUT FOLDER")
        x = input(
            "chose an encryption\n1)Caesar Cipher\n2)Play Fair\n3)Hill Cipher\n4)Vigenere Ciphen\n5)vernam Cipher\nany key to exit\n").strip()

        if((x) == '1'):
            txt = input("plaintext  for Caesar ")
            key = input("key for Caesar Cipher must be an integer ")
            try:
                print("cipher = "+Caesar(txt.strip(), int(key)))
            except ValueError:
                print("Please input integer only as key")
            except:
                print("error")
        elif(x == '2'):
            txt = input("plaintext for Play Fair Cipher ")
            key = input("key for 1Play Fair Cipher (a word) ")
            try:
                print("cipher = "+Playfair(txt.strip(), key))
            except:
                print("error")
        elif(x == '3'):
            try:
                txt = input("plaintext for Hill Cipher ")
                m = int(input(
                    "inter a number for hill mode (2 for 2*2 or for 3*3 matrix) "))
                key = []
                for i in range(m):
                    a = []
                    for j in range(m):
                        a.append(
                            int(input("inter the " + str(j+1) + " column " + "in the " + str(i+1) + " row ")))
                    key.append(a)
                print("cipher = "+Hill(txt, key))
            except ValueError:
                print("Please input integer only ")
            except:
                print("error")

        elif(x == '4'):
            try:
                txt = input("plaintext for Vigenere Cipher ")
                key = input("key for Vigenere Cipher (a word) ")
                m = input(
                    "the mode of the  cipher 1) repeating 2) auto \nyou can type 1 or 2 or the word like auto\n")

                print("cipher = "+Vigenere(txt, key, m))

            except:
                print("error")
        elif(x == '5'):
            try:
                txt = input("plaintext for vernam Cipher ")
                key = input("key for vernam Cipher (a word) ")
                print("cipher = "+vernam(txt.strip(), key))

            except:
                print("error")
        else:
            e = input("exit [y/n]\n")
            if(e == 'y'):
                exit()
            else:
                continue

        e = input("exit [y/n]\n")
        if(e == 'y'):
            exit()


if __name__ == "__main__":
    main()
