# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Norton & Abert\Project Rudy\Rudy\UI\MatterWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MatterWindow(object):
    def setupUi(self, MatterWindow):
        MatterWindow.setObjectName(_fromUtf8("MatterWindow"))
        MatterWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MatterWindow.resize(937, 610)
        MatterWindow.setStyleSheet(_fromUtf8("\n"
"QMainWindow#MainWindow{\n"
"    \n"
"    font: 10pt \"Microsoft Tai Le\";\n"
"    background-color:rgb(226, 226, 226);\n"
"}\n"
"QGroupBox{\n"
"    font: 75 12pt \"Microsoft Tai Le\";\n"
"}\n"
"QPushButton{\n"
"    \n"
"    font: 75 10pt \"Microsoft Tai Le\";\n"
"    color: rgb(202, 161, 56);\n"
"    background-color: rgb(11, 56, 97);\n"
"}\n"
"QToolButton{\n"
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
"}"))
        MatterWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtGui.QWidget(MatterWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setStyleSheet(_fromUtf8("font: 75 12pt \"Microsoft Tai Le\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.clientNum = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clientNum.sizePolicy().hasHeightForWidth())
        self.clientNum.setSizePolicy(sizePolicy)
        self.clientNum.setObjectName(_fromUtf8("clientNum"))
        self.horizontalLayout_5.addWidget(self.clientNum)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setStyleSheet(_fromUtf8("font: 75 12pt \"Microsoft Tai Le\";"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_5.addWidget(self.label_11)
        self.matterNum = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matterNum.sizePolicy().hasHeightForWidth())
        self.matterNum.setSizePolicy(sizePolicy)
        self.matterNum.setObjectName(_fromUtf8("matterNum"))
        self.horizontalLayout_5.addWidget(self.matterNum)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.matterGroup = QtGui.QGroupBox(self.centralwidget)
        self.matterGroup.setFlat(True)
        self.matterGroup.setObjectName(_fromUtf8("matterGroup"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.matterGroup)
        self.verticalLayout_3.setMargin(1)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame = QtGui.QFrame(self.matterGroup)
        self.frame.setStyleSheet(_fromUtf8("QFrame{ background-color: rgb(248, 233, 210); }"))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout_2 = QtGui.QFormLayout(self.frame)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.attorneyInitials = QtGui.QLineEdit(self.frame)
        self.attorneyInitials.setObjectName(_fromUtf8("attorneyInitials"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.attorneyInitials)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.matterType = QtGui.QComboBox(self.frame)
        self.matterType.setObjectName(_fromUtf8("matterType"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.matterType)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.dateOpened = QtGui.QDateEdit(self.frame)
        self.dateOpened.setProperty("showGroupSeparator", False)
        self.dateOpened.setCalendarPopup(True)
        self.dateOpened.setObjectName(_fromUtf8("dateOpened"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.dateOpened)
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtGui.QLabel(self.frame)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_10)
        self.boxNumber = QtGui.QLineEdit(self.frame)
        self.boxNumber.setObjectName(_fromUtf8("boxNumber"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.boxNumber)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.closed = QtGui.QCheckBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closed.sizePolicy().hasHeightForWidth())
        self.closed.setSizePolicy(sizePolicy)
        self.closed.setObjectName(_fromUtf8("closed"))
        self.horizontalLayout_4.addWidget(self.closed)
        self.dateClosed = QtGui.QDateEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateClosed.sizePolicy().hasHeightForWidth())
        self.dateClosed.setSizePolicy(sizePolicy)
        self.dateClosed.setProperty("showGroupSeparator", False)
        self.dateClosed.setCalendarPopup(True)
        self.dateClosed.setObjectName(_fromUtf8("dateClosed"))
        self.horizontalLayout_4.addWidget(self.dateClosed)
        self.formLayout_2.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.assets = QtGui.QDoubleSpinBox(self.frame)
        self.assets.setProperty("showGroupSeparator", True)
        self.assets.setMaximum(9999999999.99)
        self.assets.setObjectName(_fromUtf8("assets"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.assets)
        self.verticalLayout_3.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.matterGroup)
        self.billingGroup = QtGui.QGroupBox(self.centralwidget)
        self.billingGroup.setFlat(True)
        self.billingGroup.setObjectName(_fromUtf8("billingGroup"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.billingGroup)
        self.verticalLayout_4.setMargin(1)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.useClientAddress = QtGui.QToolButton(self.billingGroup)
        self.useClientAddress.setObjectName(_fromUtf8("useClientAddress"))
        self.verticalLayout_4.addWidget(self.useClientAddress)
        self.frame_2 = QtGui.QFrame(self.billingGroup)
        self.frame_2.setStyleSheet(_fromUtf8("QFrame{ background-color: rgb(248, 233, 210); }"))
        self.frame_2.setFrameShape(QtGui.QFrame.Panel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.firstName = QtGui.QLineEdit(self.frame_2)
        self.firstName.setObjectName(_fromUtf8("firstName"))
        self.gridLayout.addWidget(self.firstName, 2, 0, 1, 1)
        self.lastName = QtGui.QLineEdit(self.frame_2)
        self.lastName.setObjectName(_fromUtf8("lastName"))
        self.gridLayout.addWidget(self.lastName, 2, 2, 1, 1)
        self.middleInitial = QtGui.QLineEdit(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middleInitial.sizePolicy().hasHeightForWidth())
        self.middleInitial.setSizePolicy(sizePolicy)
        self.middleInitial.setMaximumSize(QtCore.QSize(75, 16777215))
        self.middleInitial.setObjectName(_fromUtf8("middleInitial"))
        self.gridLayout.addWidget(self.middleInitial, 2, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_27 = QtGui.QLabel(self.frame_2)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_27)
        self.addr1 = QtGui.QLineEdit(self.frame_2)
        self.addr1.setObjectName(_fromUtf8("addr1"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.addr1)
        self.label_28 = QtGui.QLabel(self.frame_2)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_28)
        self.addr2 = QtGui.QLineEdit(self.frame_2)
        self.addr2.setObjectName(_fromUtf8("addr2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.addr2)
        self.verticalLayout.addLayout(self.formLayout)
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.label_29 = QtGui.QLabel(self.frame_2)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_10.addWidget(self.label_29, 0, 0, 1, 1)
        self.label_30 = QtGui.QLabel(self.frame_2)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_10.addWidget(self.label_30, 0, 1, 1, 1)
        self.label_31 = QtGui.QLabel(self.frame_2)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_10.addWidget(self.label_31, 0, 2, 1, 1)
        self.billCity = QtGui.QLineEdit(self.frame_2)
        self.billCity.setObjectName(_fromUtf8("billCity"))
        self.gridLayout_10.addWidget(self.billCity, 1, 0, 1, 1)
        self.billState = QtGui.QComboBox(self.frame_2)
        self.billState.setObjectName(_fromUtf8("billState"))
        self.gridLayout_10.addWidget(self.billState, 1, 1, 1, 1)
        self.billZip = QtGui.QLineEdit(self.frame_2)
        self.billZip.setMaximumSize(QtCore.QSize(75, 16777215))
        self.billZip.setObjectName(_fromUtf8("billZip"))
        self.gridLayout_10.addWidget(self.billZip, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_10)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.billingGroup)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.documentGroup = QtGui.QGroupBox(self.centralwidget)
        self.documentGroup.setFlat(True)
        self.documentGroup.setObjectName(_fromUtf8("documentGroup"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.documentGroup)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.setDirectory = QtGui.QToolButton(self.documentGroup)
        self.setDirectory.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.setDirectory.setObjectName(_fromUtf8("setDirectory"))
        self.horizontalLayout_6.addWidget(self.setDirectory)
        self.currentDir = QtGui.QLineEdit(self.documentGroup)
        self.currentDir.setReadOnly(True)
        self.currentDir.setObjectName(_fromUtf8("currentDir"))
        self.horizontalLayout_6.addWidget(self.currentDir)
        self.attachDocument = QtGui.QToolButton(self.documentGroup)
        self.attachDocument.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.attachDocument.setObjectName(_fromUtf8("attachDocument"))
        self.horizontalLayout_6.addWidget(self.attachDocument)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.documentList = QtGui.QTableWidget(self.documentGroup)
        self.documentList.setObjectName(_fromUtf8("documentList"))
        self.documentList.setColumnCount(4)
        self.documentList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.documentList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.documentList.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.documentList.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.documentList.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.documentList)
        self.horizontalLayout_7.addWidget(self.documentGroup)
        self.adversePartyGroup = QtGui.QGroupBox(self.centralwidget)
        self.adversePartyGroup.setFlat(True)
        self.adversePartyGroup.setObjectName(_fromUtf8("adversePartyGroup"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.adversePartyGroup)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.frame_3 = QtGui.QFrame(self.adversePartyGroup)
        self.frame_3.setStyleSheet(_fromUtf8("QFrame{ background-color: rgb(248, 233, 210); }"))
        self.frame_3.setFrameShape(QtGui.QFrame.Panel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_14 = QtGui.QLabel(self.frame_3)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 1, 0, 1, 1)
        self.apFirst = QtGui.QLineEdit(self.frame_3)
        self.apFirst.setObjectName(_fromUtf8("apFirst"))
        self.gridLayout_3.addWidget(self.apFirst, 2, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.frame_3)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 1, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.frame_3)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 1, 1, 1, 1)
        self.apMiddle = QtGui.QLineEdit(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apMiddle.sizePolicy().hasHeightForWidth())
        self.apMiddle.setSizePolicy(sizePolicy)
        self.apMiddle.setMaximumSize(QtCore.QSize(75, 16777215))
        self.apMiddle.setObjectName(_fromUtf8("apMiddle"))
        self.gridLayout_3.addWidget(self.apMiddle, 2, 1, 1, 1)
        self.apLast = QtGui.QLineEdit(self.frame_3)
        self.apLast.setObjectName(_fromUtf8("apLast"))
        self.gridLayout_3.addWidget(self.apLast, 2, 2, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.apNew = QtGui.QToolButton(self.frame_3)
        self.apNew.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.apNew.setObjectName(_fromUtf8("apNew"))
        self.horizontalLayout_3.addWidget(self.apNew)
        self.apSave = QtGui.QToolButton(self.frame_3)
        self.apSave.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.apSave.setObjectName(_fromUtf8("apSave"))
        self.horizontalLayout_3.addWidget(self.apSave)
        self.apClear = QtGui.QToolButton(self.frame_3)
        self.apClear.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.apClear.setObjectName(_fromUtf8("apClear"))
        self.horizontalLayout_3.addWidget(self.apClear)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.apDelete = QtGui.QToolButton(self.frame_3)
        self.apDelete.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.apDelete.setObjectName(_fromUtf8("apDelete"))
        self.horizontalLayout_3.addWidget(self.apDelete)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_17 = QtGui.QLabel(self.frame_3)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_2.addWidget(self.label_17)
        self.reason = QtGui.QLineEdit(self.frame_3)
        self.reason.setObjectName(_fromUtf8("reason"))
        self.horizontalLayout_2.addWidget(self.reason)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.partyList = QtGui.QTableWidget(self.adversePartyGroup)
        self.partyList.setObjectName(_fromUtf8("partyList"))
        self.partyList.setColumnCount(4)
        self.partyList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.partyList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.partyList.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.partyList.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.partyList.setHorizontalHeaderItem(3, item)
        self.verticalLayout_6.addWidget(self.partyList)
        self.horizontalLayout_7.addWidget(self.adversePartyGroup)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        MatterWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MatterWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MatterWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave = QtGui.QAction(MatterWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/save.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionEdit = QtGui.QAction(MatterWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/note.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit.setIcon(icon1)
        self.actionEdit.setObjectName(_fromUtf8("actionEdit"))
        self.actionClose = QtGui.QAction(MatterWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/arrow-1.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon2)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionEdit)
        self.toolBar.addAction(self.actionClose)

        self.retranslateUi(MatterWindow)
        QtCore.QMetaObject.connectSlotsByName(MatterWindow)
        MatterWindow.setTabOrder(self.clientNum, self.matterNum)
        MatterWindow.setTabOrder(self.matterNum, self.attorneyInitials)
        MatterWindow.setTabOrder(self.attorneyInitials, self.matterType)
        MatterWindow.setTabOrder(self.matterType, self.dateOpened)
        MatterWindow.setTabOrder(self.dateOpened, self.boxNumber)
        MatterWindow.setTabOrder(self.boxNumber, self.closed)
        MatterWindow.setTabOrder(self.closed, self.dateClosed)
        MatterWindow.setTabOrder(self.dateClosed, self.assets)
        MatterWindow.setTabOrder(self.assets, self.useClientAddress)
        MatterWindow.setTabOrder(self.useClientAddress, self.firstName)
        MatterWindow.setTabOrder(self.firstName, self.lastName)
        MatterWindow.setTabOrder(self.lastName, self.middleInitial)
        MatterWindow.setTabOrder(self.middleInitial, self.addr1)
        MatterWindow.setTabOrder(self.addr1, self.addr2)
        MatterWindow.setTabOrder(self.addr2, self.billCity)
        MatterWindow.setTabOrder(self.billCity, self.billState)
        MatterWindow.setTabOrder(self.billState, self.billZip)
        MatterWindow.setTabOrder(self.billZip, self.setDirectory)
        MatterWindow.setTabOrder(self.setDirectory, self.currentDir)
        MatterWindow.setTabOrder(self.currentDir, self.attachDocument)
        MatterWindow.setTabOrder(self.attachDocument, self.documentList)
        MatterWindow.setTabOrder(self.documentList, self.apFirst)
        MatterWindow.setTabOrder(self.apFirst, self.apMiddle)
        MatterWindow.setTabOrder(self.apMiddle, self.apLast)
        MatterWindow.setTabOrder(self.apLast, self.reason)
        MatterWindow.setTabOrder(self.reason, self.apNew)
        MatterWindow.setTabOrder(self.apNew, self.apSave)
        MatterWindow.setTabOrder(self.apSave, self.apClear)
        MatterWindow.setTabOrder(self.apClear, self.apDelete)
        MatterWindow.setTabOrder(self.apDelete, self.partyList)

    def retranslateUi(self, MatterWindow):
        MatterWindow.setWindowTitle(_translate("MatterWindow", "Matter Details", None))
        self.label_5.setText(_translate("MatterWindow", "Matter #", None))
        self.label_11.setText(_translate("MatterWindow", ".", None))
        self.matterGroup.setTitle(_translate("MatterWindow", "Matter Info", None))
        self.label.setText(_translate("MatterWindow", "Attorney Initials", None))
        self.label_2.setText(_translate("MatterWindow", "Matter Type", None))
        self.label_3.setText(_translate("MatterWindow", "Date Opened", None))
        self.label_9.setText(_translate("MatterWindow", "Date Closed", None))
        self.label_10.setText(_translate("MatterWindow", "Box Number", None))
        self.closed.setText(_translate("MatterWindow", "Closed", None))
        self.label_4.setText(_translate("MatterWindow", "Estate Assets", None))
        self.assets.setSpecialValueText(_translate("MatterWindow", "No Assets", None))
        self.assets.setPrefix(_translate("MatterWindow", "$ ", None))
        self.billingGroup.setTitle(_translate("MatterWindow", "Billing Info", None))
        self.useClientAddress.setText(_translate("MatterWindow", "Same as Client", None))
        self.label_8.setText(_translate("MatterWindow", "LastName", None))
        self.label_6.setText(_translate("MatterWindow", "First Name", None))
        self.label_7.setText(_translate("MatterWindow", "Middle Initial", None))
        self.label_27.setText(_translate("MatterWindow", "Address 1", None))
        self.label_28.setText(_translate("MatterWindow", "Address 2", None))
        self.label_29.setText(_translate("MatterWindow", "City", None))
        self.label_30.setText(_translate("MatterWindow", "State", None))
        self.label_31.setText(_translate("MatterWindow", "Zip", None))
        self.documentGroup.setTitle(_translate("MatterWindow", "Original Documents", None))
        self.setDirectory.setText(_translate("MatterWindow", "Set Directory", None))
        self.attachDocument.setText(_translate("MatterWindow", "Add New Document(s)", None))
        item = self.documentList.horizontalHeaderItem(0)
        item.setText(_translate("MatterWindow", "Delete", None))
        item = self.documentList.horizontalHeaderItem(1)
        item.setText(_translate("MatterWindow", "Name", None))
        item = self.documentList.horizontalHeaderItem(2)
        item.setText(_translate("MatterWindow", "FileDirectory", None))
        item = self.documentList.horizontalHeaderItem(3)
        item.setText(_translate("MatterWindow", "View", None))
        self.adversePartyGroup.setTitle(_translate("MatterWindow", "Adverse Parties", None))
        self.label_14.setText(_translate("MatterWindow", "First Name", None))
        self.label_16.setText(_translate("MatterWindow", "LastName", None))
        self.label_15.setText(_translate("MatterWindow", "Middle Initial", None))
        self.apNew.setText(_translate("MatterWindow", "New", None))
        self.apSave.setText(_translate("MatterWindow", "Save", None))
        self.apClear.setText(_translate("MatterWindow", "Clear", None))
        self.apDelete.setText(_translate("MatterWindow", "Delete", None))
        self.label_17.setText(_translate("MatterWindow", "Reason", None))
        item = self.partyList.horizontalHeaderItem(0)
        item.setText(_translate("MatterWindow", "First Name", None))
        item = self.partyList.horizontalHeaderItem(1)
        item.setText(_translate("MatterWindow", "M.I.", None))
        item = self.partyList.horizontalHeaderItem(2)
        item.setText(_translate("MatterWindow", "Last Name", None))
        item = self.partyList.horizontalHeaderItem(3)
        item.setText(_translate("MatterWindow", "Reason", None))
        self.toolBar.setWindowTitle(_translate("MatterWindow", "toolBar", None))
        self.actionSave.setText(_translate("MatterWindow", "Save", None))
        self.actionEdit.setText(_translate("MatterWindow", "Edit", None))
        self.actionClose.setText(_translate("MatterWindow", "Close", None))

