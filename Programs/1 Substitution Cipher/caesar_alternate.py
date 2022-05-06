def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        chrc = text[i]

        if (chrc.isupper()):
            result += chr((ord(chrc) + s - 65) % 26 + 65)
        else:
            result += chr((ord(chrc) + s - 97) % 26 + 97)
    return result


def decrypt(cipher, s):
    res = ""
    for i in range(len(cipher)):
        chrc = cipher[i]
        if (chrc.isupper()):
            a = ord(chrc) - s - 65
            if a < 0:
                res += chr((a + 26) % 26 + 65)
            else:
                res += chr(a % 26 + 65)
        else:
            a = ord(chrc) - s - 97
            if a < 0:
                res += chr((a + 26) % 26 + 97)
            else:
                res += chr(a % 26 + 97)
    return res


t1 = input("Enter PlainText: ")
s1 = int(input("Enter Key: "))
cip = encrypt(t1, s1)
print("\n--------Encryption--------")
print("Text is : " + t1)
print("Key is : " + str(s1))
print("Cipher is : " + encrypt(t1, s1))
print("\n--------Decryption--------")
print("Cipher is : " + cip)
print("Key is : " + str(s1))
print("Plain text is : " + decrypt(cip, s1))
