def make_matrix(key):
    matrix = [] # list kosong menyimpan hasil matriks
    for x in range(5): # baris
        listrow = []
        for y in range(5): # kolom
            listrow.append(key[5 * x + y])
        matrix.append(listrow) # tambahin ke matriks

    print(matrix)
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
def search(hurufpertama, hurufkedua, key):
    hurufsatu, hurufdua = [0,0],[0,0]
    for x in range(5):
        for y in range(5):
            # Jika huruf ditemukan, posisi dari huruf tersebut akan disimpan dalam variabel
            if key[x][y] == hurufpertama:
                hurufsatu = [x, y]
            elif key[x][y] == hurufkedua:
                hurufdua = [x, y]
#  Setelah perulangan selesai, posisi dari kedua huruf akan dikembalikan sebagai tuple (hurufsatu, hurufdua).
    return(hurufsatu, hurufdua)

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

def encrypt(plaintext, key):
    result = []
    for i in range (int(len(plaintext)/2)):
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0

        for x in range(5):
            for y in range(5):
                if (plaintext[i * 2] == key[x][y]):
                    x1 = x
                    y1 = y
                if (plaintext[i * 2 + 1] == key[x][y]):
                    x2 = x
                    y2 = y
        if (x1 == x2 and y1 != y2):
            result.append(key[x1][(y1 + 4)%5])
            result.append(key[x2][(y2 + 4)%5])
        elif (x1 != x2 and y1 == y2):
            result.append(key[(x1 + 4)%5][y1])
            result.append(key[(x2 + 4)%5][y2])
        else:
            result.append(key[x1][y2])
            result.append(key[x2][y1])
    return(result)

def decrypt(ciphertext, key):
    result = []
    for i in range(int(len(ciphertext)/2)):
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0

        for x in range (5):
            for y in range(5):
                if (ciphertext[i * 2] == key[x][y]):
                    x1 = x
                    y1 = y
                if (ciphertext[i * 2 + 1] == key[x][y]):
                    x2 = x 
                    y2 = y
        if (x1 == x2 and y1 != y2):
            result.append(key[x1][(y1 + 4)%5])
            result.append(key[x2][(y2 + 4)%5])
        elif (x1 != x2 and y1 == y2):
            result.append(key[(x1 + 4)%5][y1])
            result.append(key[(x2 + 4)%5][y2])
        else:
            result.append(key[x1][y2])
            result.append(key[x2][y1])
    return(result)
 