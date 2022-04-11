chars = ['1','2','3','4','5','6','7','8','9','0',"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# affine cipher
def searchIndex(char):
    for i in range(len(chars)):
        if chars[i] == char:
            return i

def affine(text):
    cipher = ""
    a = 7
    b = 1
    m = len(chars)
    for i in range(len(text)):
        cipher += chars[(a*searchIndex(text[i])%m) + b]
    return cipher

def DeCipher(text):
    decipheredText = ""
    a = 7
    b = 1
    m = len(chars)
    a_inv = multInverse(a,m)
    print(a_inv)
    for i in range(len(text)):
        decipheredText += chars[(a_inv*searchIndex(text[i])%m) - b]
    return decipheredText

def multInverse(a,m):
    for i in range(1,m):
        if (a*i)%m == 1:
            return i

# print(len(chars))
# plaintext = "admin"
# ciphertext = affine(plaintext)
# print(ciphertext)
# decipheredtext = DeCipher(ciphertext)
# print(decipheredtext)

print(chars[61%62])