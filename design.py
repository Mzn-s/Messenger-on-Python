# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(349, 537)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 410, 331, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 380, 331, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 331, 361))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(336, 16777215))
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 460, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 440, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 440, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 490, 81, 41))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 460, 141, 20))
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My_Messenger"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p></p></body></html>"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>ар</p></body></html>"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Отправить</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Отправить"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите сообщение"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "Здесь будут сообщения..."))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Введите логин"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#55007f;\">Логин</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#55007f;\">Пароль</span></p></body></html>"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>rg</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#55007f;\">Mzn-S</span></p></body></html>"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
