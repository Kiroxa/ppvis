# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyAccountTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyAccountScreenUI(object):
    def __init__(self, form) -> None:
        self.setupUi(form)
    
    def setupUi(self, MyAccountScreenUI):
        MyAccountScreenUI.setObjectName("MyAccountScreenUI")
        MyAccountScreenUI.resize(840, 620)
        self.my_account_label = QtWidgets.QLabel(MyAccountScreenUI)
        self.my_account_label.setGeometry(QtCore.QRect(350, 20, 111, 17))
        self.my_account_label.setObjectName("my_account_label")
        self.change_account_pushButton = QtWidgets.QPushButton(MyAccountScreenUI)
        self.change_account_pushButton.setGeometry(QtCore.QRect(320, 60, 161, 25))
        self.change_account_pushButton.setObjectName("change_account_pushButton")
        self.delete_account_pushButton = QtWidgets.QPushButton(MyAccountScreenUI)
        self.delete_account_pushButton.setGeometry(QtCore.QRect(330, 160, 151, 25))
        self.delete_account_pushButton.setObjectName("delete_account_pushButton")
        self.leave_account_pushButton = QtWidgets.QPushButton(MyAccountScreenUI)
        self.leave_account_pushButton.setGeometry(QtCore.QRect(360, 110, 89, 25))
        self.leave_account_pushButton.setObjectName("leave_account_pushButton")
        self.back_pushButton = QtWidgets.QPushButton(MyAccountScreenUI)
        self.back_pushButton.setGeometry(QtCore.QRect(220, 570, 89, 25))
        self.back_pushButton.setObjectName("back_pushButton")

        self.retranslateUi(MyAccountScreenUI)
        QtCore.QMetaObject.connectSlotsByName(MyAccountScreenUI)

    def retranslateUi(self, MyAccountScreenUI):
        _translate = QtCore.QCoreApplication.translate
        MyAccountScreenUI.setWindowTitle(_translate("MyAccountScreenUI", "Form"))
        self.my_account_label.setText(_translate("MyAccountScreenUI", "МОЙ АККАУНТ"))
        self.change_account_pushButton.setText(_translate("MyAccountScreenUI", "ИЗМЕНИТЬ АККАУНТ"))
        self.delete_account_pushButton.setText(_translate("MyAccountScreenUI", "УДАЛИТЬ АКАУНТ"))
        self.leave_account_pushButton.setText(_translate("MyAccountScreenUI", "ВЫЙТИ"))
        self.back_pushButton.setText(_translate("MyAccountScreenUI", "НАЗАД"))
