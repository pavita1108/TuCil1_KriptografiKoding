import random  
import string  
import re

def makeKey ():
    result = ''.join((random.choice(string.ascii_uppercase) for x in range(50000)))
    with open('key.txt', 'w') as f: 
            f.write(result)

def makeRandomKey (plaintext):
    with open('key.txt', 'r') as file:
            textkey = file.read().rstrip()
    totalText = len(plaintext)
    key = random.sample(textkey , totalText)
    return key

def otpEncode (plaintext,key) :
    plaintext = cleanString(plaintext)
    encrypt = []
    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - 65
        k = ord(key[i]) - 65
        letterNumber = (p + k) %26
        letter = chr(letterNumber + 65)
        encrypt.append(letter)
    encrypt = "".join(encrypt)
    return encrypt

def otpDecode(ciphertext,key) :
    ciphertext = cleanString(ciphertext)
    decrypt = []
    for i in range(len(ciphertext)):
        p = ord(ciphertext[i]) - 65
        k = ord(key[i]) - 65
        letterNumber = (p - k) %26
        letter = chr(letterNumber + 65)
        decrypt.append(letter)
    decrypt = "".join(decrypt)
    return decrypt

def cleanString (string):
    result = re.sub(r'[^\w\s]', '', string)
    result = result.replace(" ", "")
    result = ''.join(i for i in result if not i.isdigit())
    return result

