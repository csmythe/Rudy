# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogIn.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LogIn(object):
    def setupUi(self, LogIn):
        LogIn.setObjectName(_fromUtf8("LogIn"))
        LogIn.resize(229, 138)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/key.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LogIn.setWindowIcon(icon)
        LogIn.setStyleSheet(_fromUtf8("QLabel{ font: 10pt \"Microsoft Tai Le\";}\n"
"QLabel#softwareTitle{font: 75 14pt \"Microsoft Tai Le\"; }\n"
"\n"
"\n"
""))
        LogIn.setFrameShape(QtGui.QFrame.StyledPanel)
        LogIn.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(LogIn)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.softwareTitle = QtGui.QLabel(LogIn)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft Tai Le"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.softwareTitle.setFont(font)
        self.softwareTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.softwareTitle.setObjectName(_fromUtf8("softwareTitle"))
        self.verticalLayout.addWidget(self.softwareTitle)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(LogIn)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft Tai Le"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.username = QtGui.QLineEdit(LogIn)
        self.username.setObjectName(_fromUtf8("username"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.username)
        self.label_2 = QtGui.QLabel(LogIn)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.password = QtGui.QLineEdit(LogIn)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.password)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.login = QtGui.QPushButton(LogIn)
        self.login.setObjectName(_fromUtf8("login"))
        self.horizontalLayout.addWidget(self.login)
        self.cancel = QtGui.QPushButton(LogIn)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)

    def retranslateUi(self, LogIn):
        LogIn.setWindowTitle(_translate("LogIn", "LogIn", None))
        self.softwareTitle.setText(_translate("LogIn", "Rudy", None))
        self.label.setText(_translate("LogIn", "User Name", None))
        self.label_2.setText(_translate("LogIn", "Password", None))
        self.login.setText(_translate("LogIn", "Log In", None))
        self.cancel.setText(_translate("LogIn", "Cancel", None))

