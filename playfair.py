from vigenere_cipher import cleanString
def make_matrix(key):
    matrix = [] # list kosong menyimpan hasil matriks
    for x in range(5): # baris
        listrow = []
        for y in range(5): # kolom
            listrow.append(key[5 * x + y])
        matrix.append(listrow) # tambahin ke matriks

    return(matrix)

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
        x for x in remove_punctnspace if not x.isdigit())
    
    return(remove_number.replace(" ", ""))


def encrypt_RowRule(matr, a, b, c, d):
    char1 = ''
    if b == 4:
        char1 = matr[a][0]
    else:
        char1 = matr[a][b+1]
 
    char2 = ''
    if d == 4:
        char2 = matr[c][0]
    else:
        char2 = matr[c][d+1]
 
    return char1, char2

def decrypt_RowRule(matr, a, b, c, d):
    char1 = ''
    if b == 4:
        char1 = matr[a][0]
    else:
        char1 = matr[a][b-1]
 
    char2 = ''
    if d == 4:
        char2 = matr[c][0]
    else:
        char2 = matr[c][d-1]
 
    return char1, char2

def encrypt_ColumnRule(matr, a, b, c, d):
    char1 = ''
    if a == 4:
        char1 = matr[0][b]
    else:
        char1 = matr[a+1][b]
 
    char2 = ''
    if c == 4:
        char2 = matr[0][d]
    else:
        char2 = matr[c+1][d]
 
    return char1, char2

def decrypt_ColumnRule(matr, a, b, c, d):
    char1 = ''
    if a == 4:
        char1 = matr[0][b]
    else:
        char1 = matr[a-1][b]
 
    char2 = ''
    if c == 4:
        char2 = matr[0][d]
    else:
        char2 = matr[c-1][d]
 
    return char1, char2

def encrypt_RectangleRule(matr, a, b, c, d):
    char1 = ''
    char1 = matr[a][d]
 
    char2 = ''
    char2 = matr[c][b]
 
    return char1, char2

def decrypt_RectangleRule(matr, a, b, c, d):
    char1 = ''
    char1 = matr[a][d]
 
    char2 = ''
    char2 = matr[c][b]
 
    return char1, char2

def search(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j
    return []

def playfairDecode(Matrix, plainList):
	CipherText = []

	for i in range(0, len(plainList)):
		c1 = 0
		c2 = 0
		x1, y1 = search(Matrix, plainList[i][0])
		x2, y2 = search(Matrix, plainList[i][1])

		if x1 == x2:
			c1, c2 = decrypt_RowRule(Matrix, x1, y1, x2, y2)
			# Get 2 letter cipherText
		elif y1 == y2:
			c1, c2 = decrypt_ColumnRule(Matrix, x1, y1, x2, y2)
		else:
			c1, c2 = decrypt_RectangleRule(
				Matrix, x1, y1, x2, y2)

		cipher = c1 + c2
		CipherText.append(cipher)
	return CipherText

def playfairEncode(Matrix, plainList):
	CipherText = []
	for i in range(0, len(plainList)):
		c1 = 0
		c2 = 0
		x1, y1 = search(Matrix, plainList[i][0])
		x2, y2 = search(Matrix, plainList[i][1])

		if x1 == x2:
			c1, c2 = encrypt_RowRule(Matrix, x1, y1, x2, y2)
			# Get 2 letter cipherText
		elif y1 == y2:
			c1, c2 = encrypt_ColumnRule(Matrix, x1, y1, x2, y2)
		else:
			c1, c2 = encrypt_RectangleRule(
				Matrix, x1, y1, x2, y2)

		cipher = c1 + c2
		CipherText.append(cipher)
	return CipherText

def bigram(text):
	bigram = []
	group = 0
	for i in range(2, len(text), 2):
		bigram.append(text[group:i])

		group = i
	bigram.append(text[group:])
	return bigram




# text = cleanString(('halo halo bandung sudah lama ti'))
# text = bigram(text)

# print(text)
# key  = 'ss'
# filtered_key = filter(key)
# full_key = make_key(filtered_key)
# matrix_key = make_matrix(full_key)
# a = playfairEncode(matrix_key,text)
# c = ''.join(a)
# print(a)
# b = playfairDecode(matrix_key,a)
# print(b)
