def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def ex_vigenereEncode(string, keyword):
    key =  generateKey(string, keyword)
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 256
        cipher_text.append(chr(x))
    return(cipher_text)

def ex_vigenereDecode(cipher_text, keyword):
    key =  generateKey(cipher_text, keyword)
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i])) % 256
        orig_text.append(chr(x))
    return("" . join(orig_text))