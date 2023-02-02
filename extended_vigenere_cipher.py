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


# path = "D:\ITB\Sem 6\Kriptografi Koding\TuCil1_KriptografiKoding\Tugas 1_Cloud Computing_18220027_Andreana.pdf"
# bin_data = open(path, 'rb').read()
# key = "AAA"
# string = bin_data.decode('latin1')
# a = ex_vigenereEncode(string, key)
# aa = "" . join(a)
# with open('encrypt', 'wb') as f: 
#     f.write(aa.encode('latin1'))

# bin_data = open('encrypt', 'rb').read()
# c = bin_data.decode('latin1')
# b = ex_vigenereDecode(c, key)
# with open('a.pdf', 'wb') as f: 
#     f.write(b.encode('latin1'))