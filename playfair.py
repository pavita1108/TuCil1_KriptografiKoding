def make_matrix(key):
    matrix = [] # list kosong menyimpan hasil matriks
    for x in range(5): # baris
        listrow = []
        for y in range(5): # kolom
            listrow.append(key[5 * x + y])
        matrix.append(listrow) # tambahin ke matriks

    return(matrix)

#  mengambil sebuah string sebagai input dan mengubahnya menjadi string yang hanya terdiri dari huruf dan angka yang diizinkan.
def make_key(key):
    # string input diterjemahkan menjadi string baru dengan hanya menggabungkan elemen-elemen yang memenuhi kondisi (huruf atau angka) 
    text = ''.join(x for x in key if x.isalnum())
    # string baru tersebut diterjemahkan menjadi string yang hanya mengandung setiap huruf unik 
    text = ''.join(dict.fromkeys(key))

    #  mengganti huruf j jika ada
    for letter in text:
        if letter == 'j':
            text = text.replace('j','')

# membuat string baru yang berisi huruf-huruf yang belum ada dalam string text dan menambahkannya ke string text.
    key = list(set('abcdefghiklmnopqrstuvwxyz') - set(text))
    key.sort() # diurutin
    key = ''.join(key) # diterjemahkan kembali menjadi string

    return(text+key) 

# mengubah input kapital ke huruf biasa
def toLowerCase(text):
    return text.lower()

def filter(text):
    # hapus spasi n tanda baca
    remove_punctnspace = ''.join(x for x in text if x.isalnum()) 
    # hapus angka
    remove_number = ''.join(
        x for x in remove_punctnspace if not x.isdigit())

    return(remove_number)

def arrange(plaintext,key):
    # jika ada karakter 'j' dalam string plaintext, itu digantikan dengan 'i' 
    for letter in plaintext:
        if letter == 'j':
            plaintext = plaintext.replace('j', 'i')
    plaintext = list(plaintext) # string plaintext diterjemahkan menjadi list 

    a = '' # elemen saat ini
    b = '' # elemen berikutnya
    x = 0
    while x != len(plaintext)-1:
        a = plaintext[x]
        b = plaintext[x+1]

        if a == b : # jika sama elemen baru x tambah ke list
            plaintext.insert(x+1, 'x')

        x =+ 1

        if len(plaintext)%2 == 1:
            plaintext.append('x')

        return (bigram(plaintext))

# Proses pembagian dilakukan dengan cara mengambil dua karakter secara berurutan dari plaintext dan memasukkannya ke dalam list baru (bigram). Setelah seluruh dua karakter tersebut diproses, hasilnya disimpan dalam list baru
def bigram(plaintext): # bbrp kelompok 2 karakter
    plaintext_bigram = []
    for x in range (int(len(plaintext)/2)):
        bigram = []
        for y in range(2):
            bigram.append(plaintext[2 * x + y])
        plaintext_bigram.append(bigram)
    
    return(plaintext_bigram)

# mengembalikan nilai dari sebuah elemen pada matriks kunci yang berada pada posisi tertentu
def get(hurufsatu, hurufdua, key):
    for x in range(5):
        for y in range(5):
            if x == hurufsatu and y == hurufdua:
                # Variabel "hurufsatu" dan "hurufdua" merepresentasikan posisi dalam matriks kunci.
                return(key[x][y])

# mencari posisi dari dua huruf dalam matriks kunci
# def search(hurufpertama, hurufkedua, key):
#     hurufsatu, hurufdua = [0,0],[0,0]
#     for x in range(5):
#         for y in range(5):
#             # Jika huruf ditemukan, posisi dari huruf tersebut akan disimpan dalam variabel
#             if key[x][y] == hurufpertama:
#                 hurufsatu = [x, y]
#             elif key[x][y] == hurufkedua:
#                 hurufdua = [x, y]
#  Setelah perulangan selesai, posisi dari kedua huruf akan dikembalikan sebagai tuple (hurufsatu, hurufdua).
    # return(hurufsatu, hurufdua)

# mengelompokkan setiap 2 karakter dalam ciphertext dan memisahkannya dengan spasi
def group(ciphertext):
    output = []
    ciphertext = list(ciphertext)

    for x in range(len(ciphertext)):
        if x % 2 == 0 and x > 0:
            output.append(' ')
        output.append(ciphertext[x])

    output = ''.join(output)
    return(output)

# def encrypt(plaintext, key):
#     result = []
#     for i in range (int(len(plaintext)/2)):
#         a = search(plaintext[i][0], plaintext[i][1], key)
   
#         x1 = a[0][1]
#         y1 = a[0][0]
#         x2 = a[1][1]
#         y2 = a[1][0]

#         # for x in range(5):
#         #     for y in range(5):
#                 # print(plaintext[i*2], key[x][y])
#                 # if (plaintext[i * 2] == key[x][y]):
#                 #     x1 = x
#                 #     y1 = y
#                 # if (plaintext[i * 2 + 1] == key[x][y]):
#                 #     x2 = x
#                 #     y2 = y
#         if (y1 == y2):
#             x1_2 = (x1+1)%5
#             x2_2 = (x2+1)%5
#             result.append(get(y1, x1_2, key))
#             result.append(get(y2, x2_2, key))
#         elif (x1 == x2):
#             y1_2 = (y1+1)%5
#             y2_2 = (y2+1)%5
#             result.append(get(x1, y1_2, key))
#             result.append(get(x2, y2_2, key))
#         else:
#             result.append(get(x1, y2, key))
#             result.append(get(y1, x2, key))
#     return(result)

# def decrypt(ciphertext, key):
#     result = []
#     # print('a')
#     for i in range (len(ciphertext)):
#         # print(ciphertext)
#         a = search(ciphertext[i][0], ciphertext[i][1], key)
#         # print('c')
#         x1 = a[0][1]
#         y1 = a[0][0]
#         x2 = a[1][1]
#         y2 = a[1][0]

#         if (y1 == y2):
#             x1_2 = (x1-1)%5
#             x2_2 = (x2-1)%5
#             result.append(get(y1, x1_2, key))
#             result.append(get(y2, x2_2, key))
#         elif (x1 == x2):
#             y1_2 = (y1-1)%5
#             y2_2 = (y2-1)%5
#             result.append(get(x1, y1_2, key))
#             result.append(get(x2, y2_2, key))
#         else:
#             result.append(get(x1, y2, key))
#             result.append(get(y1, x2, key))
    
#     result = ''.join(result)

    for letter in result:
        if letter == 'x':
            result = result.replace('x', '')
    
    return(result)
 
def search(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j
def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 4:
        char1 = matr[e1r][0]
    else:
        char1 = matr[e1r][e1c+1]
 
    char2 = ''
    if e2c == 4:
        char2 = matr[e2r][0]
    else:
        char2 = matr[e2r][e2c+1]
 
    return char1, char2

def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 4:
        char1 = matr[0][e1c]
    else:
        char1 = matr[e1r+1][e1c]
 
    char2 = ''
    if e2r == 4:
        char2 = matr[0][e2c]
    else:
        char2 = matr[e2r+1][e2c]
 
    return char1, char2

def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]
 
    char2 = ''
    char2 = matr[e2r][e1c]
 
    return char1, char2

def encrypt(Matrix, plainList):
    CipherText = []
    ele1_y =0
    ele1_x = 0
    ele2_x =0
    ele2_y =0
    for i in range(0, len(plainList)):
        for i in range(5):
            for j in range(5):
                if(Matrix[i][j] == plainList[i][0]):
                    ele1_x = i
                    ele1_y = j
        for i in range(5):
            for j in range(5):
                if(Matrix[i][j] == plainList[i][0]):
                    ele2_x = i
                    ele2_y = j
        c1 = 0
        c2 = 0
 
        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            # Get 2 letter cipherText
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(
                Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
 
        cipher = c1 + c2
        CipherText.append(cipher)
    return CipherText



plaintext = input("Enter your plaintext: ")
while len(plaintext) == 0:
    print("Output method cannot be empty!")
    plaintext = input("Enter your plaintext: ")

key = input("Enter your key: ")
while len(key) == 0:
    print("Output method cannot be empty!")
    key = input("Enter your key: ")

output = input("Choose your output method (default/grouped): ")
while len(output) == 0:
    print("Output method cannot be empty!")
    output = input("Choose your output method (default/grouped): ")
while output != 'default' and output != 'grouped':
    print("Please choose default or grouped method!")
    output = input("Choose your output method (default/grouped): ")

filtered_plaintext = filter(plaintext)
filtered_key = filter(key)

full_key = make_key(filtered_key)
matrix_key = make_matrix(full_key)
print(matrix_key)
arranged_plaintext = arrange(filtered_plaintext, matrix_key)
print(arranged_plaintext)
print (filtered_plaintext)
encrypted_text = encrypt(matrix_key,filtered_plaintext)
print(encrypted_text)
grouped_encrypted_text = group(encrypted_text)
# decrypted_text = decrypt(encrypted_text, matrix_key)


if output == 'default':
    print("Ciphertext:", encrypted_text)
else:
    print("Ciphertext:", grouped_encrypted_text)

# print("Decrypted ciphertext:", decrypted_text)
