# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileMaintenance.ui'
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

class Ui_FileMaint(object):
    def setupUi(self, FileMaint):
        FileMaint.setObjectName(_fromUtf8("FileMaint"))
        FileMaint.setWindowModality(QtCore.Qt.ApplicationModal)
        FileMaint.resize(346, 78)
        FileMaint.setStyleSheet(_fromUtf8("\n"
"QMainWindow#MainWindow{\n"
"    \n"
"    background-color:rgb(200, 200, 200);\n"
"    font: 10pt \"Microsoft Tai Le\";\n"
"}\n"
"QGroupBox{\n"
"    font: 75 12pt \"Microsoft Tai Le\";\n"
"}\n"
"QFrame#groupFrame,QFrame#groupFrame_2 {\n"
"    \n"
"    background-color:rgb(248, 233, 210);\n"
"}\n"
"QPushButton{\n"
"    \n"
"    font: 75 10pt \"Microsoft Tai Le\";\n"
"    color: rgb(202, 161, 56);\n"
"    background-color: rgb(11, 56, 97);\n"
"}\n"
"QToolButton{\n"
"    \n"
"    background-color: rgb(204, 204, 204);\n"
"    font: 75 10pt \"Microsoft Tai Le\";\n"
"}\n"
"QToolButton#prevPage{\n"
"    \n"
"    font: 75 10pt \"Microsoft Tai Le\";\n"
"    color: rgb(202, 161, 56);\n"
"    background-color: rgb(11, 56, 97);\n"
"}\n"
"QToolButton#nextPage{\n"
"    \n"
"    font: 75 10pt \"Microsoft Tai Le\";\n"
"    color: rgb(202, 161, 56);\n"
"    background-color: rgb(11, 56, 97);\n"
"}\n"
"QIcon{background-color:rga(1,1,1);}"))
        FileMaint.setFrameShape(QtGui.QFrame.StyledPanel)
        FileMaint.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(FileMaint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(FileMaint)
        self.label.setStyleSheet(_fromUtf8("\n"
"font: 75 12pt \"Microsoft Tai Le\";    "))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(FileMaint)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.delDate = QtGui.QDateEdit(FileMaint)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delDate.sizePolicy().hasHeightForWidth())
        self.delDate.setSizePolicy(sizePolicy)
        self.delDate.setCalendarPopup(True)
        self.delDate.setObjectName(_fromUtf8("delDate"))
        self.horizontalLayout.addWidget(self.delDate)
        self.run = QtGui.QToolButton(FileMaint)
        self.run.setObjectName(_fromUtf8("run"))
        self.horizontalLayout.addWidget(self.run)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(FileMaint)
        QtCore.QMetaObject.connectSlotsByName(FileMaint)

    def retranslateUi(self, FileMaint):
        FileMaint.setWindowTitle(_translate("FileMaint", "File Maintenance", None))
        self.label.setText(_translate("FileMaint", "Clean Up Deleted Accounts", None))
        self.label_2.setText(_translate("FileMaint", "Clear up to:  ", None))
        self.run.setText(_translate("FileMaint", "Run Clean Up", None))

