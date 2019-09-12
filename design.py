# -*- coding: utf-8 -*-
# by Orik:3
# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 515)
        MainWindow.setMaximumSize(QtCore.QSize(685, 515))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 110, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_encrypt = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_encrypt.setFont(font)
        self.rb_encrypt.setObjectName("rb_encrypt")
        self.rb_encrypt.setChecked(True)
        self.verticalLayout.addWidget(self.rb_encrypt)
        self.rb_decrypt = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rb_decrypt.setFont(font)
        self.rb_decrypt.setObjectName("rb_decrypt")
        self.verticalLayout.addWidget(self.rb_decrypt)
        self.txed_input = QtWidgets.QTextEdit(self.centralwidget)
        self.txed_input.setGeometry(QtCore.QRect(170, 40, 490, 90))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txed_input.setFont(font)
        self.txed_input.setObjectName("txed_input")
        self.txed_output = QtWidgets.QTextEdit(self.centralwidget)
        self.txed_output.setGeometry(QtCore.QRect(170, 200, 490, 140))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txed_output.setFont(font)
        self.txed_output.setReadOnly(True)
        self.txed_output.setObjectName("txed_output")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 380, 290, 110))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encryption"))
        self.groupBox.setTitle(_translate("MainWindow", "Switch"))
        self.rb_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.rb_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.txed_input.setPlaceholderText(_translate("MainWindow", "Input your text..."))
        self.pushButton.setText(_translate("MainWindow", "RUN"))
