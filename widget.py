# This Python file uses the following encoding: utf-8
import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QLineEdit
from PySide6.QtCore import QObject, Signal, QThread


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class EncryptionWorker(QObject):
    finished = Signal()
    progress = Signal(int)
    message = Signal(str)

    def __init__(self, encrypting, **kwargs):
        super().__init__()
        self.encrypting = encrypting
        self.params = kwargs
        self.password = self.params["password"]
        self.salt = self.params["salt"]
    def run(self):
        self.message.emit("Deriving key...")
        kdf = Argon2id(
            salt=self.salt,
            length=64,
            iterations=2,
            lanes=4,
            memory_cost=2*1024*1024,
            ad=None,
            secret=None,
        )

        self.derivedkey = kdf.derive(self.password.encode())
        self.key = self.derivedkey[:32]
        self.hmackey = self.derivedkey[32:64]
        try:
            if self.encrypting:
                self.encrypt_file()
            else:
                self.decrypt_file()
            self.finished.emit()
        except Exception as e:
            self.message.emit(str(e))
            self.finished.emit()

    def encrypt_file(self):
        input_path = self.params['input_path']
        output_path = self.params['output_path']
        filesize = os.path.getsize(input_path)
        iv = os.urandom(16)

        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()

        self.message.emit("Encrypting...")

        with open(input_path, 'rb') as inputfile:
            with open(output_path, 'wb') as outputfile:
                outputfile.write(iv)
                outputfile.write(self.salt)
                totalread = 0
                while True:
                    plaintext = inputfile.read(1048576)
                    totalread += len(plaintext)
                    if totalread == filesize:
                        padded = padder.update(plaintext)
                        padded += padder.finalize()
                        ciphertext = encryptor.update(padded) + encryptor.finalize()
                        outputfile.write(ciphertext)
                        break
                    else:
                        ciphertext = encryptor.update(plaintext)
                        outputfile.write(ciphertext)
                        self.progress.emit(int((totalread / filesize)*100))

        self.message.emit("Computing authentication tag...")
        with open(output_path, 'rb+') as encryptedfile:
            filesize = os.path.getsize(output_path)
            totalread = 0
            h = hmac.HMAC(self.hmackey, hashes.SHA256())
            while True:
                filecontent = encryptedfile.read(1048576)
                totalread += len(filecontent)
                if(totalread == filesize):
                    h.update(filecontent)
                    signature = h.finalize()
                    encryptedfile.write(signature)
                    break
                else:
                    h.update(filecontent)
                    self.progress.emit(int((totalread / filesize)*100))

        self.message.emit("Encryption finished.")
        self.progress.emit(100)

    def decrypt_file(self):
        input_path = self.params['input_path']
        output_path = self.params['output_path']
        unpadder = padding.PKCS7(128).unpadder()
        filesignature = bytes(0)

        self.message.emit("Authenticating file...")
        with open(input_path, 'rb') as encryptedfile:
            h = hmac.HMAC(self.hmackey, hashes.SHA256())
            filesize = os.path.getsize(input_path) - 32
            totalread = 0
            while True:
                filecontent = encryptedfile.read(1048576)
                totalread += len(filecontent)
                if(totalread >= filesize):
                    if(totalread > filesize):
                        excess = totalread - filesize
                        filecontent = filecontent[:-excess]
                    h.update(filecontent)
                    signature = h.finalize()
                    encryptedfile.seek(-32, 2)
                    filehash = encryptedfile.read(32)
                    if(filehash == signature):
                        self.message.emit("Authentication successful.")
                    else:
                        self.message.emit("Authentication failed. File corrupted or tampered, or incorrect password.")
                    break
                else:
                    h.update(filecontent)
                    self.progress.emit(int((totalread / filesize)*100))

        self.message.emit("Decrypting...")
        filesize = os.path.getsize(input_path) - 32 - 16 - 16
        with open(input_path, 'rb') as inputfile:
            iv = inputfile.read(16)
            inputfile.seek(32)
            with open(output_path, 'wb') as outputfile:
                cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
                decryptor = cipher.decryptor()
                totalread = 0
                while True:
                    ciphertext = inputfile.read(1048576)
                    totalread += len(ciphertext)
                    if totalread >= filesize:
                        if(totalread > filesize):
                            excess = totalread - filesize
                            ciphertext = ciphertext[:-excess]
                        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
                        unpadded = unpadder.update(plaintext)
                        unpadded += unpadder.finalize()
                        outputfile.write(unpadded)
                        break
                    else:
                        plaintext = decryptor.update(ciphertext)
                        outputfile.write(plaintext)
                        self.progress.emit(int((totalread / filesize)*100))
        self.message.emit("Decryption finished")
        self.progress.emit(100)

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.pushButton_encrypt.setEnabled(False)
        self.ui.pushButton_decrypt.setEnabled(False)

        self.ui.pushButton_encrypt.clicked.connect(lambda: self.run(True))
        self.ui.pushButton_decrypt.clicked.connect(lambda: self.run(False))
        self.ui.pushButton_selectInputFile.clicked.connect(self.on_pushButton_selectInputFile_clicked)
        self.ui.pushButton_selectOutputFile.clicked.connect(self.on_pushButton_selectOutputFile_clicked)
        self.ui.lineEdit_password.textChanged.connect(self.updateButtons)
        self.ui.lineEdit_passwordConfirm.textChanged.connect(self.updateButtons)
        self.ui.lineEdit_inputFile.textChanged.connect(self.updateButtons)
        self.ui.lineEdit_outputFile.textChanged.connect(self.updateButtons)
        self.ui.checkBox_showPassword.checkStateChanged.connect(self.showPassword)

    def showPassword(self):
        if self.ui.checkBox_showPassword.isChecked():
            self.ui.lineEdit_password.setEchoMode(QLineEdit.Normal)
            self.ui.lineEdit_passwordConfirm.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.lineEdit_password.setEchoMode(QLineEdit.Password)
            self.ui.lineEdit_passwordConfirm.setEchoMode(QLineEdit.Password)


    def updateButtons(self):
        if len(self.ui.lineEdit_inputFile.text()) > 0 and len(self.ui.lineEdit_outputFile.text()) > 0:
            match = self.ui.lineEdit_password.text() == self.ui.lineEdit_passwordConfirm.text()
            self.ui.pushButton_encrypt.setEnabled(match)
            self.ui.pushButton_decrypt.setEnabled(True)
        else:
            self.ui.pushButton_encrypt.setEnabled(False)
            self.ui.pushButton_decrypt.setEnabled(False)

    def on_pushButton_selectInputFile_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select file",
            "",
            "All Files (*)"
            )

        if file_path:
            self.ui.lineEdit_inputFile.setText(file_path)

    def on_pushButton_selectOutputFile_clicked(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Choose output file",
            "",
            "All Files (*)"
        )

        if file_path:
            self.ui.lineEdit_outputFile.setText(file_path)

    def run(self, encrypting):
        input_path = self.ui.lineEdit_inputFile.text()
        output_path = self.ui.lineEdit_outputFile.text()
        password = self.ui.lineEdit_password.text()
        salt = bytes(16)
        self.ui.textBrowser.clear()

        if(encrypting):
            salt = os.urandom(16)
        else:
            f = open(input_path, "rb")
            f.seek(16)
            salt = f.read(16)

        self.worker = EncryptionWorker(
            encrypting=encrypting,
            input_path=input_path,
            output_path=output_path,
            salt=salt,
            password=password
        )
        self.thread = QThread()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.ui.progressBar.setValue)
        self.worker.message.connect(self.ui.textBrowser.append)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
