# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManageUsers.ui'
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

class Ui_ManageUsers(object):
    def setupUi(self, ManageUsers):
        ManageUsers.setObjectName(_fromUtf8("ManageUsers"))
        ManageUsers.setWindowModality(QtCore.Qt.ApplicationModal)
        ManageUsers.resize(562, 401)
        ManageUsers.setStyleSheet(_fromUtf8("QLabel{ font: 10pt \"Microsoft Tai Le\";}\n"
"\n"
"\n"
""))
        ManageUsers.setFrameShape(QtGui.QFrame.StyledPanel)
        ManageUsers.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(ManageUsers)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(ManageUsers)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.showInactive = QtGui.QCheckBox(ManageUsers)
        self.showInactive.setObjectName(_fromUtf8("showInactive"))
        self.verticalLayout.addWidget(self.showInactive)
        self.userList = QtGui.QListWidget(ManageUsers)
        self.userList.setObjectName(_fromUtf8("userList"))
        self.verticalLayout.addWidget(self.userList)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.newUser = QtGui.QToolButton(ManageUsers)
        self.newUser.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.newUser.setObjectName(_fromUtf8("newUser"))
        self.horizontalLayout.addWidget(self.newUser)
        self.save = QtGui.QToolButton(ManageUsers)
        self.save.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.save.setObjectName(_fromUtf8("save"))
        self.horizontalLayout.addWidget(self.save)
        self.clear = QtGui.QToolButton(ManageUsers)
        self.clear.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.clear.setObjectName(_fromUtf8("clear"))
        self.horizontalLayout.addWidget(self.clear)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(ManageUsers)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.username = QtGui.QLineEdit(ManageUsers)
        self.username.setObjectName(_fromUtf8("username"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.username)
        self.label_3 = QtGui.QLabel(ManageUsers)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(ManageUsers)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.fullName = QtGui.QLineEdit(ManageUsers)
        self.fullName.setObjectName(_fromUtf8("fullName"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.fullName)
        self.label_5 = QtGui.QLabel(ManageUsers)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lastSignin = QtGui.QLineEdit(ManageUsers)
        self.lastSignin.setReadOnly(True)
        self.lastSignin.setObjectName(_fromUtf8("lastSignin"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lastSignin)
        self.label_6 = QtGui.QLabel(ManageUsers)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.admin = QtGui.QCheckBox(ManageUsers)
        self.admin.setObjectName(_fromUtf8("admin"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.admin)
        self.inactive = QtGui.QCheckBox(ManageUsers)
        self.inactive.setObjectName(_fromUtf8("inactive"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.inactive)
        self.password = QtGui.QPushButton(ManageUsers)
        self.password.setObjectName(_fromUtf8("password"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.password)
        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)

        self.retranslateUi(ManageUsers)
        QtCore.QMetaObject.connectSlotsByName(ManageUsers)

    def retranslateUi(self, ManageUsers):
        ManageUsers.setWindowTitle(_translate("ManageUsers", "Manage Users", None))
        self.label.setText(_translate("ManageUsers", "User List", None))
        self.showInactive.setText(_translate("ManageUsers", "Show Inactive User Names", None))
        self.newUser.setText(_translate("ManageUsers", "New", None))
        self.save.setText(_translate("ManageUsers", "Save", None))
        self.clear.setText(_translate("ManageUsers", "Clear", None))
        self.label_2.setText(_translate("ManageUsers", "User Name", None))
        self.label_3.setText(_translate("ManageUsers", "Password", None))
        self.label_4.setText(_translate("ManageUsers", "Full Name", None))
        self.label_5.setText(_translate("ManageUsers", "Last Signin", None))
        self.admin.setText(_translate("ManageUsers", "Admin Account", None))
        self.inactive.setText(_translate("ManageUsers", "Inactive", None))
        self.password.setText(_translate("ManageUsers", "Reset Password", None))

