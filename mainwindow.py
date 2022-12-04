# Этот шаг нужен для пересборки файла формы
import os
from sys import platform
if platform == "linux" or platform == "linux2":
    os.system("./make_ui.sh")
elif platform == "win32":
    os.system("pyside6-uic informationDialog.ui -o informationDialog.py")
    os.system("pyside6-uic form.ui -o ui_form.py")
    os.system("pyside6-rcc resources.qrc -o rc_resource.py")
    print("No script for Win")

# This Python file uses the following encoding: utf-8
import sys
import random, string
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QWidget
from PySide6.QtCore import QFile, QIODevice, QTranslator
from Crypto.Cipher import AES
#from Crypto.PublicKey import RSA
import rsa
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from informationDialog import Ui_Dialog
import rc_resource

iv = get_random_bytes(16)
BLOCK_SIZE = 16 # Bytes

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.infoDialog = None
        self.senderPubKey = None
        self.senderPrivKey = None
        self.receiverPubKey = None
        self.receiverPrivKey = None
        self.ui.genKeysPushButton.clicked.connect(self.key_gen_clicked);
        self.ui.proceedPushButton.clicked.connect(self.proceed_clicked);
        self.ui.aesPushButton.clicked.connect(self.symmInfoClicked)
        self.ui.rsaPushButton.clicked.connect(self.assymInfoClicked)
        self.ui.hashPushButton.clicked.connect(self.hashInfoClicked)
        self.ui.ecpPushButton.clicked.connect(self.ecpInfoClicked)
        self.ui.finalPushButton.clicked.connect(self.finalInfoClicked)

    def key_gen_clicked(self):
        print("Debug: keygen")
        symmkeyLength = 16
        symmKey = ''.join(random.sample(string.ascii_letters+string.digits,symmkeyLength))
        self.ui.symmKeyLineEdit.setText(symmKey)

        (self.senderPubKey, self.senderPrivKey) = rsa.newkeys(512, poolsize=8)
        (self.receiverPubKey, self.receiverPrivKey) = rsa.newkeys(512, poolsize=8)
        self.ui.senderOpenLineEdit.setText(str(self.senderPrivKey.exp1))
        self.ui.senderPrivateLineEdit.setText(str(self.senderPrivKey.exp2))
        self.ui.receiverOpenLineEdit.setText(str(self.receiverPrivKey.exp1))
        self.ui.receiverPrivateLineEdit.setText(str(self.receiverPrivKey.exp2))
        self.ui.proceedPushButton.setEnabled(True)

    def proceed_clicked(self):
        #TODO: тут сделать условия выхода
        #   не сгенерены ключи
        #   пустое поле текста

        # Подписание текста закрытым ключом отправителя
        plainText = self.ui.plainTextEdit.toPlainText()
        hashSender = rsa.compute_hash(bytes(plainText, 'utf8'), "SHA-1")
        signature = rsa.sign_hash(hashSender, self.senderPrivKey, "SHA-1")
        self.ui.senderHashLineEdit.setText(hashSender.hex())
        self.ui.originalEcpLineEdit.setText(signature.hex())

        # Зашифровка текста симметричным шифром
        print("Debug: proceed")
        key = self.ui.symmKeyLineEdit.text()
        cipher1 = AES.new(bytes(key, 'utf-8'), AES.MODE_CBC, iv)
        cipherText = cipher1.encrypt(pad((bytes(plainText, 'utf8')),BLOCK_SIZE))
        self.ui.cipherTextEdit.setPlainText(cipherText.hex())

        # Зашифровка симметричного ключа открытым ключом получателя
        encSymmKey = rsa.encrypt(key.encode("utf-8"),self.receiverPubKey)
        self.ui.encKeyLineEdit.setText(encSymmKey.hex())

        # Расшифровка симметричного ключа закрытым ключом получателя
        decrSymmKey = rsa.decrypt(encSymmKey, self.receiverPrivKey)
        self.ui.decrKeyLineEdit.setText(decrSymmKey.decode("utf-8"))

        # Расшифровка текста симметричным шифром
        cipher2 = AES.new(decrSymmKey, AES.MODE_CBC, iv)
        decryptedText = unpad(cipher2.decrypt(cipherText),BLOCK_SIZE)
        self.ui.receivedPlainTextEdit.setPlainText(decryptedText.decode())

        # Проверка ЭЦП получателем
        hashReceiver = rsa.compute_hash(decryptedText, "SHA-1")
        self.ui.receiverHashLineEdit.setText(hashReceiver.hex())
        if rsa.verify(decryptedText, signature, self.senderPubKey):
            self.ui.decryptedEcpLineEdit.setText(self.tr("Success"))
        else:
            self.ui.decryptedEcpLineEdit.setText(self.tr("Failure"))

    def symmInfoClicked(self):
        print("AES")
        labelFile = QFile(":/symm_label")
        if not labelFile.open(QIODevice.ReadOnly):
            print("symm label file open error")
            return
        textFile = QFile(":/symm_text")
        if not textFile.open(QIODevice.ReadOnly):
            print("symm text file open error")
            return

        self.infoDialog = InfoWindow()
        self.infoDialog.ui.InfoLabel.setText(str(labelFile.readAll(),"utf-8"))
        self.infoDialog.ui.InfoTextBrowser.setText(str(textFile.readAll(),"utf-8"))

        self.infoDialog.ui.labelPic1.setPixmap (QPixmap (":/Resouces/Pictures/aes_1.JPG"))
        self.infoDialog.ui.labelPic2.setPixmap (QPixmap (":/Resouces/Pictures/aes_2.JPG"))
        self.infoDialog.ui.tabWidget.setTabVisible (2, False)


        labelFile.close()
        textFile.close()
        self.infoDialog.show()

    def assymInfoClicked(self):
        print("RSA")
        labelFile = QFile(":/ass_label")
        if not labelFile.open(QIODevice.ReadOnly):
            print("ass label file open error")
            return
        textFile = QFile(":/ass_text")
        if not textFile.open(QIODevice.ReadOnly):
            print("ass text file open error")
            return
        self.infoDialog = InfoWindow()
        self.infoDialog.ui.InfoLabel.setText(str(labelFile.readAll(),"utf-8"))
        self.infoDialog.ui.InfoTextBrowser.setText(str(textFile.readAll(),"utf-8"))

        self.infoDialog.ui.tabWidget.setVisible (False)

        labelFile.close()
        textFile.close()
        self.infoDialog.show()

    def hashInfoClicked(self):
        print("HASH")
        labelFile = QFile(":/hash_label")
        if not labelFile.open(QIODevice.ReadOnly):
            print("hash label file open error")
            return
        textFile = QFile(":/hash_text")
        if not textFile.open(QIODevice.ReadOnly):
            print("hash text file open error")
            return
        self.infoDialog = InfoWindow()
        self.infoDialog.ui.InfoLabel.setText(str(labelFile.readAll(),"utf-8"))
        self.infoDialog.ui.InfoTextBrowser.setText(str(textFile.readAll(),"utf-8"))

        self.infoDialog.ui.labelPic1.setPixmap (QPixmap (":/Resouces/Pictures/sha1_1.JPG"))
        self.infoDialog.ui.labelPic2.setPixmap (QPixmap (":/Resouces/Pictures/sha1_2.JPG"))
        self.infoDialog.ui.labelPic2.setPixmap (QPixmap (":/Resouces/Pictures/sha1_3.JPG"))

        labelFile.close()
        textFile.close()
        self.infoDialog.show()

    def ecpInfoClicked(self):
        print("ECP")
        labelFile = QFile(":/ecp_label")
        if not labelFile.open(QIODevice.ReadOnly):
            print("hash label file open error")
            return
        textFile = QFile(":/ecp_text")
        if not textFile.open(QIODevice.ReadOnly):
            print("hash text file open error")
            return
        self.infoDialog = InfoWindow()
        self.infoDialog.ui.InfoLabel.setText(str(labelFile.readAll(),"utf-8"))
        self.infoDialog.ui.InfoTextBrowser.setText(str(textFile.readAll(),"utf-8"))

        self.infoDialog.ui.labelPic1.setPixmap (QPixmap (":/Resouces/Pictures/ecp_1.JPG"))
        self.infoDialog.ui.labelPic2.setPixmap (QPixmap (":/Resouces/Pictures/ecp_2.JPG"))
        self.infoDialog.ui.tabWidget.setTabVisible (2, False)

        labelFile.close()
        textFile.close()
        self.infoDialog.show()

    def finalInfoClicked(self):
        print("ECP")
        labelFile = QFile(":/final_label")
        if not labelFile.open(QIODevice.ReadOnly):
            print("hash label file open error")
            return
        textFile = QFile(":/final_text")
        if not textFile.open(QIODevice.ReadOnly):
            print("hash text file open error")
            return
        self.infoDialog = InfoWindow()
        self.infoDialog.ui.InfoLabel.setText(str(labelFile.readAll(),"utf-8"))
        self.infoDialog.ui.InfoTextBrowser.setText(str(textFile.readAll(),"utf-8"))

        self.infoDialog.ui.tabWidget.setVisible (False)

        labelFile.close()
        textFile.close()
        self.infoDialog.show()

class InfoWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = QTranslator()
    if translator.load("translation_ru"):
        app.installTranslator(translator)
    else:
        print("Failed to load translation")
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
