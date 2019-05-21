# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManageMatters.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManageMatters(object):
    def setupUi(self, ManageMatters):
        ManageMatters.setObjectName("ManageMatters")
        ManageMatters.setWindowModality(QtCore.Qt.ApplicationModal)
        ManageMatters.resize(556, 338)
        ManageMatters.setStyleSheet("QLabel{ font: 10pt \"Microsoft Tai Le\";}\n"
"\n"
"\n"
"")
        ManageMatters.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ManageMatters.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout = QtWidgets.QGridLayout(ManageMatters)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ManageMatters)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.showInactive = QtWidgets.QCheckBox(ManageMatters)
        self.showInactive.setObjectName("showInactive")
        self.verticalLayout.addWidget(self.showInactive)
        self.matterList = QtWidgets.QListWidget(ManageMatters)
        self.matterList.setObjectName("matterList")
        self.verticalLayout.addWidget(self.matterList)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newMatter = QtWidgets.QToolButton(ManageMatters)
        self.newMatter.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.newMatter.setObjectName("newMatter")
        self.horizontalLayout.addWidget(self.newMatter)
        self.save = QtWidgets.QToolButton(ManageMatters)
        self.save.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        self.clear = QtWidgets.QToolButton(ManageMatters)
        self.clear.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(ManageMatters)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.matterDescr = QtWidgets.QLineEdit(ManageMatters)
        self.matterDescr.setObjectName("matterDescr")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.matterDescr)
        self.inactive = QtWidgets.QCheckBox(ManageMatters)
        self.inactive.setObjectName("inactive")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inactive)
        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)

        self.retranslateUi(ManageMatters)
        QtCore.QMetaObject.connectSlotsByName(ManageMatters)

    def retranslateUi(self, ManageMatters):
        _translate = QtCore.QCoreApplication.translate
        ManageMatters.setWindowTitle(_translate("ManageMatters", "Manage Matter Types"))
        self.label.setText(_translate("ManageMatters", "Matter List"))
        self.showInactive.setText(_translate("ManageMatters", "Show Inactive User Names"))
        self.newMatter.setText(_translate("ManageMatters", "New"))
        self.save.setText(_translate("ManageMatters", "Save"))
        self.clear.setText(_translate("ManageMatters", "Clear"))
        self.label_2.setText(_translate("ManageMatters", "Matter Description"))
        self.inactive.setText(_translate("ManageMatters", "Inactive"))


