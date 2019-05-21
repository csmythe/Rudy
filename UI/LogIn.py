# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogIn.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogIn(object):
    def setupUi(self, LogIn):
        LogIn.setObjectName("LogIn")
        LogIn.resize(229, 138)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/key.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LogIn.setWindowIcon(icon)
        LogIn.setStyleSheet("QLabel{ font: 10pt \"Microsoft Tai Le\";}\n"
"QLabel#softwareTitle{font: 75 14pt \"Microsoft Tai Le\"; }\n"
"\n"
"\n"
"")
        LogIn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        LogIn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(LogIn)
        self.verticalLayout.setObjectName("verticalLayout")
        self.softwareTitle = QtWidgets.QLabel(LogIn)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.softwareTitle.setFont(font)
        self.softwareTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.softwareTitle.setObjectName("softwareTitle")
        self.verticalLayout.addWidget(self.softwareTitle)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(LogIn)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.username = QtWidgets.QLineEdit(LogIn)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username)
        self.label_2 = QtWidgets.QLabel(LogIn)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password = QtWidgets.QLineEdit(LogIn)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.login = QtWidgets.QPushButton(LogIn)
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)
        self.cancel = QtWidgets.QPushButton(LogIn)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "LogIn"))
        self.softwareTitle.setText(_translate("LogIn", "Rudy"))
        self.label.setText(_translate("LogIn", "User Name"))
        self.label_2.setText(_translate("LogIn", "Password"))
        self.login.setText(_translate("LogIn", "Log In"))
        self.cancel.setText(_translate("LogIn", "Cancel"))


