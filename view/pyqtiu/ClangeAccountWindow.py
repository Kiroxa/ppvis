# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangeAccountScreenTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangeAccountScreenUI(object):
    def __init__(self, form) -> None:
        self.setupUi(form)
    
    def setupUi(self, ChangeAccountScreenUI):
        ChangeAccountScreenUI.setObjectName("ChangeAccountScreenUI")
        ChangeAccountScreenUI.resize(840, 620)
        self.change_account_label = QtWidgets.QLabel(ChangeAccountScreenUI)
        self.change_account_label.setGeometry(QtCore.QRect(340, 20, 161, 17))
        self.change_account_label.setObjectName("change_account_label")
        self.name_lineEdit = QtWidgets.QLineEdit(ChangeAccountScreenUI)
        self.name_lineEdit.setGeometry(QtCore.QRect(360, 50, 113, 25))
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.name_label = QtWidgets.QLabel(ChangeAccountScreenUI)
        self.name_label.setGeometry(QtCore.QRect(280, 50, 67, 17))
        self.name_label.setObjectName("name_label")
        self.back_pushButton = QtWidgets.QPushButton(ChangeAccountScreenUI)
        self.back_pushButton.setGeometry(QtCore.QRect(270, 140, 89, 25))
        self.back_pushButton.setObjectName("back_pushButton")
        self.save_pushButton = QtWidgets.QPushButton(ChangeAccountScreenUI)
        self.save_pushButton.setGeometry(QtCore.QRect(420, 140, 101, 25))
        self.save_pushButton.setObjectName("save_pushButton")

        self.retranslateUi(ChangeAccountScreenUI)
        QtCore.QMetaObject.connectSlotsByName(ChangeAccountScreenUI)

    def retranslateUi(self, ChangeAccountScreenUI):
        _translate = QtCore.QCoreApplication.translate
        ChangeAccountScreenUI.setWindowTitle(_translate("ChangeAccountScreenUI", "Form"))
        self.change_account_label.setText(_translate("ChangeAccountScreenUI", "ИЗМЕНИТЬ АККАУНТ"))
        self.name_label.setText(_translate("ChangeAccountScreenUI", "ИМЯ:"))
        self.back_pushButton.setText(_translate("ChangeAccountScreenUI", "НАЗАД"))
        self.save_pushButton.setText(_translate("ChangeAccountScreenUI", "СОХРАНИТЬ"))