#!/usr/bin/python3
# -*- coding: utf-8 -*-
# by Orik:3

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import design
from encoder import *


class MainApp(QWidget, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.encoding)

    def encoding(self):

        if self.rb_encrypt.isChecked():
            key_encoded = encode_val(key)
            value_encoded = encode_val(self.txed_input.toPlainText())
            encoded = full_encode(value_encoded, key_encoded)
            decoded = full_decode(encoded, key_encoded)
            self.txed_output.setText(''.join(decode_val(encoded)))

        elif self.rb_decrypt.isChecked():
            key_encoded = encode_val(key)
            value_encoded = encode_val(self.txed_input.toPlainText())
            encoded = full_decode(value_encoded, key_encoded)
            self.txed_output.setText(''.join(decode_val(encoded)))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
