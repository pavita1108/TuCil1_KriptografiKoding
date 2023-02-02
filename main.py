import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from vigenere_cipher import *
from extended_vigenere_cipher import *
from otp import *

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("main.ui", self)
        self.vigenereStandard.clicked.connect(self.Viginere)
        self.vigenereExt.clicked.connect(self.Extended)
        # self.playfair.clicked.connect(self.Playfair)
        self.otp.clicked.connect(self.OneTimePad)
    def Viginere(self):
        viginere = Viginere()
        widget.addWidget(viginere)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Extended(self):
        extended = Extended()
        widget.addWidget(extended)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # def Playfair(self):
    #     playfair = Playfair()
    #     widget.addWidget(playfair)
    #     widget.setCurrentIndex(widget.currentIndex() + 1)

    def OneTimePad(self):
        onetimepad = OneTimePad()
        widget.addWidget(onetimepad)
        widget.setCurrentIndex(widget.currentIndex() + 1)


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

class Extended(QMainWindow):
    def __init__(self):
        super(Extended, self).__init__()
        loadUi("extended.ui", self)
        self.label_6.setText("Extended Viginere Cipher")
        self.exp.clicked.connect(self.Export)
        self.encrypt.clicked.connect(self.Encrypt)
        self.decrypt.clicked.connect(self.Decrypt)
        self.exp_2.clicked.connect(self.Export_2)

    def Encrypt (self) :
        output = []
        text = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        fileloc = self.textEdit_4.toPlainText()

        if text == '':
            bin_data = open(fileloc, 'rb').read()
            string = bin_data.decode('latin1')
            encode = ex_vigenereEncode(string, key)
        else :
            encode = ex_vigenereEncode(text,key)
        output = ''.join(encode)    
        self.textBrowser.setText(str(output))
    
    def Decrypt (self):
        output = []
        text = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        fileloc = self.textEdit_4.toPlainText()

        if text == '':
            bin_data = open(fileloc, 'rb').read()
            string = bin_data.decode('latin1')
            decode = ex_vigenereDecode(string, key)
        else :
            decode = ex_vigenereDecode(text,key)   
        self.textBrowser_2.setText(decode)

    def Export (self):
        key = self.textEdit_2.toPlainText()
        path = self.textEdit_4.toPlainText()
        bin_data = open(path, 'rb').read()
        string = bin_data.decode('latin1')
        filetype = self.textEdit_3.toPlainText()

        fileName = "hasil." + filetype
        b = ex_vigenereDecode(string, key)
        with open(fileName, 'wb') as f: 
            f.write(b.encode('latin1'))

    def Export_2 (self):
        key = self.textEdit_2.toPlainText()
        fileloc = self.textEdit_4.toPlainText()

        bin_data = open(fileloc, 'rb').read()
        string = bin_data.decode('latin1')
        encode = ex_vigenereEncode(string, key)
        en = "" . join(encode)
        with open('encrypt', 'wb') as f: 
            f.write(en.encode('latin1'))



class OneTimePad (QMainWindow):
    def __init__(self):
        super(OneTimePad, self).__init__()
        loadUi("otp.ui", self)
        self.label_6.setText("One Time Pad Cipher")
        self.woSpace.clicked.connect(self.WOSpace)
        self.go5letter.clicked.connect(self.Grouped)
        self.impKey.clicked.connect(self.GenerateKey)
        self.imp.clicked.connect(self.Import)
        self.exp.clicked.connect(self.Export)

    def WOSpace(self):
        text = self.textEdit.toPlainText()
        key = self.key.text()
        encode = otpEncode(text,key)
        decode = otpDecode(encode,key)
        self.textBrowser.setText(encode)
        self.textBrowser_2.setText(decode)

    def Grouped (self):
        output = []
        text = self.textEdit.toPlainText()
        key = self.key.text()
        encode = otpEncode(text,key)
        decode = otpDecode(encode,key)
        for i in range(len(encode)):
            if i % 5 == 0 and i > 0:
                output.append('  ')
            output.append(encode[i])
        output = ''.join(output)
        self.textBrowser.setText(output)
        self.textBrowser_2.setText(decode)

    def GenerateKey(self):
        text = str(self.textEdit.toPlainText())
        makeKey()
        key = makeRandomKey(text)
        self.key.setText(''.join(key))
        self.label_7.setText("Imported successfully")
    
    def Export(self):
        text = self.textEdit.toPlainText()
        key = self.key.text()
        cipher = otpEncode(text,key)
        txt = open('ciphertext.txt', 'w')
        cipher = txt.write(cipher)
        txt.close()
    
    def Import(self):
        with open('text.txt', 'r') as file:
            lines = file.read().rstrip()
        self.textEdit.setPlainText(str(lines))


app = QApplication(sys.argv)
welcome = Menu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(700)
widget.setFixedWidth(900)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Bye - bye")