# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileMaintenance.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileMaint(object):
    def setupUi(self, FileMaint):
        FileMaint.setObjectName("FileMaint")
        FileMaint.setWindowModality(QtCore.Qt.ApplicationModal)
        FileMaint.resize(346, 78)
        FileMaint.setStyleSheet("\n"
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
"QIcon{background-color:rga(1,1,1);}")
        FileMaint.setFrameShape(QtWidgets.QFrame.StyledPanel)
        FileMaint.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(FileMaint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(FileMaint)
        self.label.setStyleSheet("\n"
"font: 75 12pt \"Microsoft Tai Le\";    ")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(FileMaint)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delDate = QtWidgets.QDateEdit(FileMaint)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delDate.sizePolicy().hasHeightForWidth())
        self.delDate.setSizePolicy(sizePolicy)
        self.delDate.setCalendarPopup(True)
        self.delDate.setObjectName("delDate")
        self.horizontalLayout.addWidget(self.delDate)
        self.run = QtWidgets.QToolButton(FileMaint)
        self.run.setObjectName("run")
        self.horizontalLayout.addWidget(self.run)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(FileMaint)
        QtCore.QMetaObject.connectSlotsByName(FileMaint)

    def retranslateUi(self, FileMaint):
        _translate = QtCore.QCoreApplication.translate
        FileMaint.setWindowTitle(_translate("FileMaint", "File Maintenance"))
        self.label.setText(_translate("FileMaint", "Clean Up Deleted Accounts"))
        self.label_2.setText(_translate("FileMaint", "Clear up to:  "))
        self.run.setText(_translate("FileMaint", "Run Clean Up"))


