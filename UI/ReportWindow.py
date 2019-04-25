# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReportWindow.ui'
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

class Ui_ReportFrame(object):
    def setupUi(self, ReportFrame):
        ReportFrame.setObjectName(_fromUtf8("ReportFrame"))
        ReportFrame.setWindowModality(QtCore.Qt.ApplicationModal)
        ReportFrame.resize(845, 503)
        ReportFrame.setStyleSheet(_fromUtf8("\n"
"QFrame#ReportFrame{\n"
"    \n"
"    font: 10pt \"Microsoft Tai Le\";\n"
"    background-color:rgb(226, 226, 226);\n"
"}\n"
"QGroupBox, QToolBox{\n"
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
        ReportFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        ReportFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout_4 = QtGui.QVBoxLayout(ReportFrame)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.splitter = QtGui.QSplitter(ReportFrame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.resetReport = QtGui.QToolButton(self.layoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/restart.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetReport.setIcon(icon)
        self.resetReport.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.resetReport.setObjectName(_fromUtf8("resetReport"))
        self.horizontalLayout.addWidget(self.resetReport)
        self.runReport = QtGui.QToolButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/search.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runReport.setIcon(icon1)
        self.runReport.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.runReport.setObjectName(_fromUtf8("runReport"))
        self.horizontalLayout.addWidget(self.runReport)
        self.exportReport = QtGui.QToolButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/excelExport.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportReport.setIcon(icon2)
        self.exportReport.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.exportReport.setObjectName(_fromUtf8("exportReport"))
        self.horizontalLayout.addWidget(self.exportReport)
        self.clearReport = QtGui.QToolButton(self.layoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Icons/clear.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearReport.setIcon(icon3)
        self.clearReport.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.clearReport.setObjectName(_fromUtf8("clearReport"))
        self.horizontalLayout.addWidget(self.clearReport)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.toolBox = QtGui.QToolBox(self.layoutWidget)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 535, 397))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout = QtGui.QVBoxLayout(self.page)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.displayCols = QtGui.QTreeWidget(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayCols.sizePolicy().hasHeightForWidth())
        self.displayCols.setSizePolicy(sizePolicy)
        self.displayCols.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.displayCols.setAlternatingRowColors(True)
        self.displayCols.setRootIsDecorated(True)
        self.displayCols.setUniformRowHeights(False)
        self.displayCols.setAnimated(False)
        self.displayCols.setAllColumnsShowFocus(False)
        self.displayCols.setObjectName(_fromUtf8("displayCols"))
        item_0 = QtGui.QTreeWidgetItem(self.displayCols)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.displayCols)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.displayCols)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.verticalLayout.addWidget(self.displayCols)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 535, 397))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout = QtGui.QGridLayout(self.page_2)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.page_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.page_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.availableFilters = QtGui.QTreeWidget(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.availableFilters.sizePolicy().hasHeightForWidth())
        self.availableFilters.setSizePolicy(sizePolicy)
        self.availableFilters.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.availableFilters.setAlternatingRowColors(True)
        self.availableFilters.setRootIsDecorated(True)
        self.availableFilters.setUniformRowHeights(False)
        self.availableFilters.setAnimated(False)
        self.availableFilters.setAllColumnsShowFocus(False)
        self.availableFilters.setColumnCount(1)
        self.availableFilters.setObjectName(_fromUtf8("availableFilters"))
        item_0 = QtGui.QTreeWidgetItem(self.availableFilters)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.availableFilters)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.availableFilters)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.availableFilters.header().setDefaultSectionSize(150)
        self.gridLayout.addWidget(self.availableFilters, 1, 0, 1, 1)
        self.activeFilters = QtGui.QTableWidget(self.page_2)
        self.activeFilters.setObjectName(_fromUtf8("activeFilters"))
        self.activeFilters.setColumnCount(4)
        self.activeFilters.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.activeFilters.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.activeFilters.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.activeFilters.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.activeFilters.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.activeFilters, 1, 1, 1, 1)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.toolBox)
        self.reportResults = QtGui.QTableWidget(self.splitter)
        self.reportResults.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.reportResults.setAlternatingRowColors(True)
        self.reportResults.setObjectName(_fromUtf8("reportResults"))
        self.reportResults.setColumnCount(0)
        self.reportResults.setRowCount(0)
        self.verticalLayout_4.addWidget(self.splitter)

        self.retranslateUi(ReportFrame)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ReportFrame)

    def retranslateUi(self, ReportFrame):
        ReportFrame.setWindowTitle(_translate("ReportFrame", "Rudy Reporting", None))
        self.resetReport.setText(_translate("ReportFrame", "Reset Parameters", None))
        self.runReport.setText(_translate("ReportFrame", "Run Report", None))
        self.exportReport.setText(_translate("ReportFrame", "Export Report", None))
        self.clearReport.setText(_translate("ReportFrame", "Clear Report", None))
        self.displayCols.headerItem().setText(0, _translate("ReportFrame", "Table", None))
        __sortingEnabled = self.displayCols.isSortingEnabled()
        self.displayCols.setSortingEnabled(False)
        self.displayCols.topLevelItem(0).setText(0, _translate("ReportFrame", "ClientInfo", None))
        self.displayCols.topLevelItem(0).child(0).setText(0, _translate("ReportFrame", "ClientNum", None))
        self.displayCols.topLevelItem(0).child(1).setText(0, _translate("ReportFrame", "ClientName", None))
        self.displayCols.topLevelItem(1).setText(0, _translate("ReportFrame", "ClientMatters", None))
        self.displayCols.topLevelItem(1).child(0).setText(0, _translate("ReportFrame", "MatterNum", None))
        self.displayCols.topLevelItem(1).child(1).setText(0, _translate("ReportFrame", "MatterTypeID", None))
        self.displayCols.topLevelItem(1).child(2).setText(0, _translate("ReportFrame", "Attorney", None))
        self.displayCols.topLevelItem(1).child(3).setText(0, _translate("ReportFrame", "TotalAssets", None))
        self.displayCols.topLevelItem(2).setText(0, _translate("ReportFrame", "MatterTypes", None))
        self.displayCols.topLevelItem(2).child(0).setText(0, _translate("ReportFrame", "MatterTypeID", None))
        self.displayCols.topLevelItem(2).child(1).setText(0, _translate("ReportFrame", "MatterDesc", None))
        self.displayCols.setSortingEnabled(__sortingEnabled)
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("ReportFrame", "Display Columns", None))
        self.label.setText(_translate("ReportFrame", "Choose Filter", None))
        self.label_2.setText(_translate("ReportFrame", "Active Filters", None))
        self.availableFilters.headerItem().setText(0, _translate("ReportFrame", "Table", None))
        __sortingEnabled = self.availableFilters.isSortingEnabled()
        self.availableFilters.setSortingEnabled(False)
        self.availableFilters.topLevelItem(0).setText(0, _translate("ReportFrame", "ClientInfo", None))
        self.availableFilters.topLevelItem(0).child(0).setText(0, _translate("ReportFrame", "ClientNum", None))
        self.availableFilters.topLevelItem(0).child(1).setText(0, _translate("ReportFrame", "ClientName", None))
        self.availableFilters.topLevelItem(1).setText(0, _translate("ReportFrame", "ClientMatters", None))
        self.availableFilters.topLevelItem(1).child(0).setText(0, _translate("ReportFrame", "MatterNum", None))
        self.availableFilters.topLevelItem(1).child(1).setText(0, _translate("ReportFrame", "MatterTypeID", None))
        self.availableFilters.topLevelItem(1).child(2).setText(0, _translate("ReportFrame", "Attorney", None))
        self.availableFilters.topLevelItem(1).child(3).setText(0, _translate("ReportFrame", "TotalAssets", None))
        self.availableFilters.topLevelItem(2).setText(0, _translate("ReportFrame", "MatterTypes", None))
        self.availableFilters.topLevelItem(2).child(0).setText(0, _translate("ReportFrame", "MatterTypeID", None))
        self.availableFilters.topLevelItem(2).child(1).setText(0, _translate("ReportFrame", "MatterDesc", None))
        self.availableFilters.setSortingEnabled(__sortingEnabled)
        item = self.activeFilters.horizontalHeaderItem(1)
        item.setText(_translate("ReportFrame", "Field", None))
        item = self.activeFilters.horizontalHeaderItem(2)
        item.setText(_translate("ReportFrame", "Filter", None))
        item = self.activeFilters.horizontalHeaderItem(3)
        item.setText(_translate("ReportFrame", "Value", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("ReportFrame", "Report Filters", None))

