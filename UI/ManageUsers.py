# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManageUsers.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManageUsers(object):
    def setupUi(self, ManageUsers):
        ManageUsers.setObjectName("ManageUsers")
        ManageUsers.setWindowModality(QtCore.Qt.ApplicationModal)
        ManageUsers.resize(562, 401)
        ManageUsers.setStyleSheet("QLabel{ font: 10pt \"Microsoft Tai Le\";}\n"
"\n"
"\n"
"")
        ManageUsers.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ManageUsers.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout = QtWidgets.QGridLayout(ManageUsers)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ManageUsers)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.showInactive = QtWidgets.QCheckBox(ManageUsers)
        self.showInactive.setObjectName("showInactive")
        self.verticalLayout.addWidget(self.showInactive)
        self.userList = QtWidgets.QListWidget(ManageUsers)
        self.userList.setObjectName("userList")
        self.verticalLayout.addWidget(self.userList)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newUser = QtWidgets.QToolButton(ManageUsers)
        self.newUser.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.newUser.setObjectName("newUser")
        self.horizontalLayout.addWidget(self.newUser)
        self.save = QtWidgets.QToolButton(ManageUsers)
        self.save.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        self.clear = QtWidgets.QToolButton(ManageUsers)
        self.clear.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(ManageUsers)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.username = QtWidgets.QLineEdit(ManageUsers)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username)
        self.label_3 = QtWidgets.QLabel(ManageUsers)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(ManageUsers)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.fullName = QtWidgets.QLineEdit(ManageUsers)
        self.fullName.setObjectName("fullName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fullName)
        self.label_5 = QtWidgets.QLabel(ManageUsers)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lastSignin = QtWidgets.QLineEdit(ManageUsers)
        self.lastSignin.setReadOnly(True)
        self.lastSignin.setObjectName("lastSignin")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lastSignin)
        self.label_6 = QtWidgets.QLabel(ManageUsers)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.admin = QtWidgets.QCheckBox(ManageUsers)
        self.admin.setObjectName("admin")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.admin)
        self.inactive = QtWidgets.QCheckBox(ManageUsers)
        self.inactive.setObjectName("inactive")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.inactive)
        self.password = QtWidgets.QPushButton(ManageUsers)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)

        self.retranslateUi(ManageUsers)
        QtCore.QMetaObject.connectSlotsByName(ManageUsers)

    def retranslateUi(self, ManageUsers):
        _translate = QtCore.QCoreApplication.translate
        ManageUsers.setWindowTitle(_translate("ManageUsers", "Manage Users"))
        self.label.setText(_translate("ManageUsers", "User List"))
        self.showInactive.setText(_translate("ManageUsers", "Show Inactive User Names"))
        self.newUser.setText(_translate("ManageUsers", "New"))
        self.save.setText(_translate("ManageUsers", "Save"))
        self.clear.setText(_translate("ManageUsers", "Clear"))
        self.label_2.setText(_translate("ManageUsers", "User Name"))
        self.label_3.setText(_translate("ManageUsers", "Password"))
        self.label_4.setText(_translate("ManageUsers", "Full Name"))
        self.label_5.setText(_translate("ManageUsers", "Last Signin"))
        self.admin.setText(_translate("ManageUsers", "Admin Account"))
        self.inactive.setText(_translate("ManageUsers", "Inactive"))
        self.password.setText(_translate("ManageUsers", "Reset Password"))


