# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManageMatters.ui'
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

class Ui_ManageMatters(object):
    def setupUi(self, ManageMatters):
        ManageMatters.setObjectName(_fromUtf8("ManageMatters"))
        ManageMatters.setWindowModality(QtCore.Qt.ApplicationModal)
        ManageMatters.resize(556, 338)
        ManageMatters.setStyleSheet(_fromUtf8("QLabel{ font: 10pt \"Microsoft Tai Le\";}\n"
"\n"
"\n"
""))
        ManageMatters.setFrameShape(QtGui.QFrame.StyledPanel)
        ManageMatters.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(ManageMatters)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(ManageMatters)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.showInactive = QtGui.QCheckBox(ManageMatters)
        self.showInactive.setObjectName(_fromUtf8("showInactive"))
        self.verticalLayout.addWidget(self.showInactive)
        self.matterList = QtGui.QListWidget(ManageMatters)
        self.matterList.setObjectName(_fromUtf8("matterList"))
        self.verticalLayout.addWidget(self.matterList)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.newMatter = QtGui.QToolButton(ManageMatters)
        self.newMatter.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.newMatter.setObjectName(_fromUtf8("newMatter"))
        self.horizontalLayout.addWidget(self.newMatter)
        self.save = QtGui.QToolButton(ManageMatters)
        self.save.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.save.setObjectName(_fromUtf8("save"))
        self.horizontalLayout.addWidget(self.save)
        self.clear = QtGui.QToolButton(ManageMatters)
        self.clear.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.clear.setObjectName(_fromUtf8("clear"))
        self.horizontalLayout.addWidget(self.clear)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(ManageMatters)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.matterDescr = QtGui.QLineEdit(ManageMatters)
        self.matterDescr.setObjectName(_fromUtf8("matterDescr"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.matterDescr)
        self.inactive = QtGui.QCheckBox(ManageMatters)
        self.inactive.setObjectName(_fromUtf8("inactive"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.inactive)
        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)

        self.retranslateUi(ManageMatters)
        QtCore.QMetaObject.connectSlotsByName(ManageMatters)

    def retranslateUi(self, ManageMatters):
        ManageMatters.setWindowTitle(_translate("ManageMatters", "Manage Matter Types", None))
        self.label.setText(_translate("ManageMatters", "Matter List", None))
        self.showInactive.setText(_translate("ManageMatters", "Show Inactive User Names", None))
        self.newMatter.setText(_translate("ManageMatters", "New", None))
        self.save.setText(_translate("ManageMatters", "Save", None))
        self.clear.setText(_translate("ManageMatters", "Clear", None))
        self.label_2.setText(_translate("ManageMatters", "Matter Description", None))
        self.inactive.setText(_translate("ManageMatters", "Inactive", None))

