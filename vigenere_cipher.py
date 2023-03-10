import re

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def cleanString (string):
    result = re.sub(r'[^\w\s]', '', string)
    result = result.replace(" ", "")
    result = ''.join(i for i in result if not i.isdigit())
    return result

def vigenereEncode(str, keyword):
    string = cleanString(str)
    key =  generateKey(string, keyword)
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

def vigenereDecode(str, keyword):
    cipher_text = cleanString(str)
    key =  generateKey(cipher_text, keyword)
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))