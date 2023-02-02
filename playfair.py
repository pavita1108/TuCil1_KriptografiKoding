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

def filter(text):
    # hapus spasi n tanda baca
    remove_punctnspace = ''.join(x for x in text if x.isalnum()) 
    # hapus angka
    remove_number = ''.join(
        x for x in remove_punctnspace if not x.isdigit()
    )

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

# Proses pembagian dilakukan dengan cara mengambil dua karakter secara berurutan dari plaintext dan memasukkannya ke dalam list baru (bigram). Setelah seluruh dua karakter tersebut diproses, hasilnya disimpan dalam list baru (bigram_plaintext). Fungsi akan mengembalikan list bigram_plaintext yang berisi bigram-bigram dari teks masukan.
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
