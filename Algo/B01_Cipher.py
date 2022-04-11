from .Functions import*

chars_arr = ['1','2','3','4','5','6','7','8','9','0',"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def searchIndex(char):
    for i in range(length_of_obj(chars_arr)):
        if chars_arr[i] == char:
            return i+1

def Cipher(text):
    cipheredText = ""
    a = 5
    b = 1
    m = length_of_obj(chars_arr)
    for i in range(length_of_obj(text)):
        cipheredText += chars_arr[(searchIndex(text[i])*a + b)%m-1]
    return cipheredText

def Decipher(text):
    decipheredText = ""
    a = 5
    b = 1
    m = length_of_obj(chars_arr)
    for i in range(length_of_obj(text)):
        decipheredText += chars_arr[(searchIndex(text[i])*a - b)%m-1]
    return decipheredText