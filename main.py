import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from vigenere_cipher import *
from extended_vigenere_cipher import *

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("main.ui", self)
        self.vigenereStandard.clicked.connect(self.Viginere)
        # self.vigenereExt.clicked.connect(self.Extended)
        # self.playfair.clicked.connect(self.Playfair)
        # self.otp.clicked.connect(self.OneTimePad)
    def Viginere(self):
        viginere = Viginere()
        widget.addWidget(viginere)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # def Extended(self):
    #     extended = Extended()
    #     widget.addWidget(extended)
    #     widget.setCurrentIndex(widget.currentIndex() + 1)

    # def Playfair(self):
    #     playfair = Playfair()
    #     widget.addWidget(playfair)
    #     widget.setCurrentIndex(widget.currentIndex() + 1)

    # def OneTimePad(self):
    #     onetimepad = OneTimePad()
    #     widget.addWidget(onetimepad)
    #     widget.setCurrentIndex(widget.currentIndex() + 1)


class Viginere(QMainWindow):
    def __init__(self):
        super(Viginere, self).__init__()
        loadUi("cipher.ui", self)
        self.label_6.setText("Viginere Cipher")
        self.woSpace.clicked.connect(self.WOSpace)
        self.go5letter.clicked.connect(self.Grouped)
        self.imp.clicked.connect(self.Import)
        self.exp.clicked.connect(self.Export)
    
    def Import(self):
        with open('text.txt', 'r') as file:
            lines = file.read().rstrip()
        self.textEdit.setPlainText(str(lines))
        
    def Export(self):
        text = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        cipher = vigenereEncode(text,key)
        txt = open('ciphertext.txt', 'w')
        cipher = txt.write(cipher)
        txt.close()

    def WOSpace(self):
        text = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        encode = vigenereEncode(text,key)
        decode = vigenereDecode(encode,key)
        self.textBrowser.setText(encode)
        self.textBrowser_2.setText(decode)

    def Grouped (self):
        output = []
        text = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        encode = vigenereEncode(text,key)
        decode = vigenereDecode(encode,key)
        for i in range(len(encode)):
            if i % 5 == 0 and i > 0:
                output.append('  ')
            output.append(encode[i])
        output = ''.join(output)
        self.textBrowser.setText(output)
        self.textBrowser_2.setText(decode)
    

# path = "D:\ITB\Sem 6\Kriptografi Koding\TuCil1_KriptografiKoding\Tugas 1_Cloud Computing_18220027_Andreana.pdf"
# bin_data = open(path, 'rb').read()
# key = "AAA"
# a = ex_vigenereEncode(str(bin_data), key)
# b = ex_vigenereDecode(a, key)
# with open('', 'wb') as f: 
#     f.write(bin_data)

app = QApplication(sys.argv)
welcome = Menu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")